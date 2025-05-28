# myapp.py

from flask import Flask, redirect
from routes.resume import resume_bp
from config.database import Base, engine, SessionLocal
from models.resume_section import ResumeSection
from scripts.seed_resume_sections import seed_resume_sections




def create_app():
    app = Flask(__name__)


    app.register_blueprint(resume_bp)


    @app.route("/")
    def index():
        return redirect("/resume")


    Base.metadata.create_all(bind=engine)
    seed_resume_sections()



    seed_data_if_empty()

    return app

def seed_data_if_empty():
    db = SessionLocal()
    count = db.query(ResumeSection).count()
    if count == 0:
        print("🚀 Seeding initial resume data...")
        sections = [
            ResumeSection(
                title="Profile Summary",
                content="<p>Your summary goes here</p>",
                order=1
            ),
            ResumeSection(
                title="Career Objective",
                content="<p>Your objective goes here</p>",
                order=2
            ),
            ResumeSection(
                title="Technical Skills",
                content="<ul><li>Python</li><li>Flask</li><li>Git</li></ul>",
                order=3
            )
        ]
        db.add_all(sections)
        db.commit()
        print("✅ Initial resume sections inserted.")
    else:
        print(f"ℹ️ Resume table already has {count} sections.")
    db.close()

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5777, debug=True)
