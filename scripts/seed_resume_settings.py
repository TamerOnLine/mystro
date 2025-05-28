import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from config.database import SessionLocal
from models.resume_section import ResumeSetting

# إعدادات افتراضية
default_settings = [
    {
        "key": "section_title_css",
        "value": "font-size: 22px; font-weight: bold; color: #333;",
        "description": "تنسيق عنوان القسم"
    },
    {
        "key": "paragraph_css",
        "value": "margin-bottom: 10px; line-height: 1.6;",
        "description": "تنسيق فقرات القسم"
    },
    {
        "key": "body_font",
        "value": "'Segoe UI', sans-serif;",
        "description": "الخط العام للنص"
    }
]

# إدخال البيانات
db = SessionLocal()
for setting in default_settings:
    exists = db.query(ResumeSetting).filter_by(key=setting["key"]).first()
    if not exists:
        db.add(ResumeSetting(**setting))

db.commit()
db.close()

print("✅ تم إدخال الإعدادات بنجاح.")
