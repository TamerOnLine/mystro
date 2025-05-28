# scripts/seed_resume_sections.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.resume_section import ResumeSection
from config.database import SessionLocal

def seed_resume_sections():
    db = SessionLocal()
    if db.query(ResumeSection).count() > 0:
        db.close()
        return

    print("🚀 Seeding real resume sections...")

    def ul(*items):
        return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

    def link(text, url):
        return f'<a href="{url}" target="_blank">{text}</a>'

    sections = [

        ResumeSection(
            title="Personal Info",
            order=0,
            content="""
                <h1>Tamer Hamad Faour</h1>
                <p class="info">Werneuchener Str. 19, 13055 Berlin | info@tameronline.com</p>
            """
        ),

        ResumeSection(title="Profile Summary", order=1, content="""
            <p>Experienced Python and AI developer with expertise in Generative AI, LLMs, and data analysis. Passionate about innovative projects and emerging technologies.</p>
        """),

        ResumeSection(title="Career Objective", order=2, content="""
            <p>Motivated software developer with specialization in Python, AI, data processing, and automation. Eager to contribute to forward-looking projects in AI/ML and intelligent applications.</p>
        """),

        ResumeSection(title="Preferred Fields", order=3, content=ul(
            "Python Developer",
            "AI/ML Engineer",
            "Generative AI Specialist",
            "Data Analyst (including Clinical Data)"
        )),

        ResumeSection(title="Professional Experience", order=4, content=ul(
            "<strong>AI Internship – YOLO GmbH (Feb. 2025 – Mar. 2025):</strong> Developed AI-powered health assistant with LLMs and agent architecture.",
            "<strong>Administrative Internship – TRAINICO GmbH (Nov. 2017):</strong> Supported organizational tasks and assisted with events.",
            "<strong>Freelance Developer & Accountant (2002 – 2015):</strong> Built accounting systems and handled financial operations for SMEs."
        )),

        ResumeSection(title="Education & Certifications", order=5, content=ul(
            "AI Development – Mystro GmbH (Jun. 2024 – Dec. 2024, 1000 hrs)",
            "Commercial Office Administration – AMVG gGmbH (Aug. 2017 – Nov. 2017, 420 hrs)"
        )),

        ResumeSection(title="Technical Skills", order=6, content=ul(
            "Languages: Python, SQL, Visual Basic",
            "Frameworks: FastAPI, LangChain, Streamlit",
            "AI/ML: NLP, LLMs, Computer Vision, HuggingFace, FAISS",
            "DevOps: Docker, GitHub Actions, CI/CD",
            "Cloud & Tools: GitHub, Kaggle, Ollama, n8n, Pi Node, Oracle Cloud, Cloudflare, Microsoft Access"
        )),

        ResumeSection(title="Language Skills", order=7, content=ul(
            "German: A2 (telc, 2018)",
            "English: A2",
            "Arabic: Native"
        )),

        ResumeSection(title="Online Profiles & Certificates", order=8, content=ul(
            link("Microsoft Sway – AI Development Certificate", "https://sway.cloud.microsoft/BVRyxoeaThCBbIsR"),
            link("LinkedIn", "https://linkedin.com/in/tameronline"),
            link("HackerRank", "https://hackerrank.com/profile/tameronline"),
            link("LeetCode", "https://leetcode.com/u/TamerOnLine")
        )),

        ResumeSection(title="Projects (GitHub)", order=9, content=ul(
            link("AI Financial Analyst", "https://github.com/TamerOnLine/AI-Financial-Analyst"),
            link("Sentence Embeddings Search", "https://github.com/TamerOnLine/sentence-embeddings-similarity-search"),
            link("FastAPI + CI/CD", "https://github.com/TamerOnLine/MystroTamer-FastAPI-Docker"),
            link("Liebemama", "https://www.liebemama.com")
        )),

        ResumeSection(title="Additional Information & Interests", order=10, content=ul(
            "Active interest in open-source projects and modern technologies",
            "Highly motivated to grow within the startup ecosystem and AI innovation landscape"
        )),
    ]

    db.add_all(sections)
    db.commit()
    db.close()
    print("✅ Resume sections added.")
