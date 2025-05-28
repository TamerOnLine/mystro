from flask import Blueprint, render_template, request, redirect, url_for
from models.resume_section import ResumeSection, ResumeSetting, get_settings_dict
from config.database import SessionLocal
from logic.formatter import format_text_to_html
from flask import render_template



resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/")
def index():
    return render_template("index.html")



@resume_bp.route("/resume")
def resume_page():
    db = SessionLocal()
    sections = db.query(ResumeSection).filter_by(is_visible=True).order_by(ResumeSection.order).all()
    settings = get_settings_dict(db)
    return render_template("resume.html", sections=sections, settings=settings)


@resume_bp.route("/admin", methods=["GET", "POST"])
def admin():
    db = SessionLocal()
    edit_id = request.args.get("edit_id", type=int)
    editing = None

    if request.method == "POST":
        section_id = request.form.get("section_id")
        title = request.form["title"].strip()
        order = int(request.form["order"])
        raw_content = request.form["content"].strip()
        format_type = request.form.get("format", "paragraph")

        # التحويل إلى HTML بناءً على النوع المختار
        if format_type == "list":
            lines = [line.strip() for line in raw_content.splitlines() if line.strip()]
            content = "<ul>" + "".join(f"<li>{line}</li>" for line in lines) + "</ul>"
        else:  # paragraph
            content = "<p>" + raw_content.replace("\n", "<br>") + "</p>"
                



        is_visible = 'is_visible' in request.form

        if section_id:  # تعديل قسم
            section = db.query(ResumeSection).get(int(section_id))
            if section:
                section.title = title
                section.order = order
                section.content = content
                section.is_visible = is_visible
        else:  # إضافة قسم جديد
            section = ResumeSection(
                title=title,
                order=order,
                content=content,
                is_visible=is_visible
            )
            db.add(section)

        db.commit()
        return redirect(url_for("resume.admin"))

    if edit_id:
        editing = db.query(ResumeSection).get(edit_id)

    sections = db.query(ResumeSection).order_by(ResumeSection.order).all()
    db.close()
    return render_template("admin.html", sections=sections, editing=editing)





@resume_bp.route("/admin/edit/<int:section_id>", methods=["GET", "POST"])
def edit_section(section_id):
    db = SessionLocal()
    section = db.query(ResumeSection).get(section_id)

    if not section:
        db.close()
        return "Section not found", 404

    if request.method == "POST":
        section.title = request.form.get("title", section.title).strip()
        section.content = request.form.get("content", section.content).strip()
        section.order = int(request.form.get("order", section.order))
        section.is_visible = 'is_visible' in request.form
        db.commit()
        db.close()
        return redirect(url_for("resume.admin"))

    db.close()
    return render_template("edit_section.html", section=section)

@resume_bp.route("/admin/delete/<int:section_id>")
def delete_section(section_id):
    db = SessionLocal()
    section = db.query(ResumeSection).get(section_id)
    if section:
        db.delete(section)
        db.commit()
    db.close()
    return redirect(url_for("resume.admin"))


@resume_bp.route("/admin/settings", methods=["GET", "POST"])
def admin_settings():
    db = SessionLocal()

    if request.method == "POST":
        for key in request.form:
            setting = db.query(ResumeSetting).filter_by(key=key).first()
            if setting:
                setting.value = request.form[key].strip()
        db.commit()
        return redirect(url_for("resume.admin_settings"))

    # ✅ استعلام واحد فقط + تحويل النتائج إلى قاموس
    settings = db.query(ResumeSetting).order_by(ResumeSetting.key).all()
    settings_dict = {s.key: s.value for s in settings}
    db.close()

    return render_template("settings.html", settings=settings, settings_dict=settings_dict)


@resume_bp.route("/resume")
def show_resume():
    db = SessionLocal()
    sections = db.query(ResumeSection).filter_by(is_visible=True).order_by(ResumeSection.order).all()
    settings = {s.key: s.value for s in db.query(ResumeSetting).all()}
    db.close()
    return render_template("resume.html", sections=sections, settings=settings)
