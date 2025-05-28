import os
from flask import Flask, redirect
from routes.resume import resume_bp
from config.database import Base, engine, SessionLocal
from models.resume_section import ResumeSection
from scripts.seed_resume_sections import seed_resume_sections
from dotenv import load_dotenv

load_dotenv()

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.register_blueprint(resume_bp)

    @app.route("/")
    def index():
        """
        Redirect to the resume route.

        Returns:
            Response: A redirect response to /resume.
        """
        return redirect("/resume")

    # Initialize the database if it does not exist
    if not os.path.exists("db.sqlite3"):
        print("Database not found. Creating it now...")
        Base.metadata.create_all(bind=engine)
        seed_resume_sections()
        seed_data_if_empty()
        print("Initial setup completed successfully.")
    else:
        print("Database already exists. Skipping initialization.")

    return app

def seed_data_if_empty():
    """
    Seed the resume section data if the database table is empty.

    This ensures that the application has default sections to work with.
    """
    db = SessionLocal()
    try:
        count = db.query(ResumeSection).count()
        if count == 0:
            print("Seeding initial resume data...")
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
            print("Initial resume sections inserted.")
        else:
            print(f"Resume table already has {count} sections.")
    finally:
        db.close()

if __name__ == "__main__":
    app = create_app()
    app.run(
        host=os.getenv("FLASK_RUN_HOST", "0.0.0.0"),
        port=int(os.getenv("FLASK_RUN_PORT", 7777)),
        debug=os.getenv("FLASK_DEBUG", "true").lower() == "true"
    )
