from sqlalchemy import Column, Integer, String, Text, Boolean
from config.database import Base
from sqlalchemy.orm import Session

class ResumeSection(Base):
    __tablename__ = "resume_sections"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    order = Column(Integer, default=0)
    is_visible = Column(Boolean, default=True)


class ResumeSetting(Base):
    __tablename__ = "resume_settings"

    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(String(500), nullable=False)
    description = Column(String(255), nullable=True)



def get_settings_dict(db: Session):
    settings = db.query(ResumeSetting).all()
    return {setting.key: setting.value for setting in settings}
