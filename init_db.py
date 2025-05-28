from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# إعداد قاعدة البيانات
engine = create_engine("sqlite:///db.sqlite3", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# نموذج الإعدادات
class ResumeSetting(Base):
    __tablename__ = "resume_settings"
    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(String(500), nullable=False)
    description = Column(String(255), nullable=True)

# إنشاء الجداول
Base.metadata.create_all(bind=engine)

# إضافة البيانات الافتراضية
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

# تنفيذ الحفظ
db = SessionLocal()
for setting in default_settings:
    exists = db.query(ResumeSetting).filter_by(key=setting["key"]).first()
    if not exists:
        db.add(ResumeSetting(**setting))
db.commit()
db.close()

print("✅ تم إنشاء قاعدة البيانات db.sqlite3 وإدخال الإعدادات بنجاح.")
