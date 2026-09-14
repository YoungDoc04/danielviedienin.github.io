# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, ListFlowable, ListItem)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SERIF = "fonts/IBMPlexSerif-Regular.ttf"
SERIF_B = "fonts/IBMPlexSerif-Bold.ttf"
SANS = "fonts/DejaVuSans.ttf"
SANS_B = "fonts/DejaVuSans-Bold.ttf"

pdfmetrics.registerFont(TTFont("PlexSerif", SERIF))
pdfmetrics.registerFont(TTFont("PlexSerif-Bold", SERIF_B))
pdfmetrics.registerFont(TTFont("Sans", SANS))
pdfmetrics.registerFont(TTFont("Sans-Bold", SANS_B))

TEXT = colors.HexColor("#14191c")
BODY = colors.HexColor("#2a3033")
MUTED = colors.HexColor("#5b6265")
LINE = colors.HexColor("#d9d6cd")
ACCENT = colors.HexColor("#c8371f")
LINK = colors.HexColor("#1f6f5c")

styles = getSampleStyleSheet()

name_style = ParagraphStyle("name", fontName="PlexSerif-Bold", fontSize=20, leading=23, textColor=TEXT, spaceAfter=2)
role_style = ParagraphStyle("role", fontName="Sans", fontSize=10, leading=13, textColor=MUTED, spaceAfter=8)
section_style = ParagraphStyle("section", fontName="PlexSerif", fontSize=12.5, leading=15, textColor=TEXT, spaceBefore=8, spaceAfter=4)
contact_style = ParagraphStyle("contact", fontName="Sans", fontSize=9.2, textColor=BODY, leading=13)
body_style = ParagraphStyle("body", fontName="Sans", fontSize=9.2, textColor=BODY, leading=12.8, spaceAfter=3)
entry_title = ParagraphStyle("entrytitle", fontName="Sans-Bold", fontSize=9.6, leading=12, textColor=TEXT)
entry_date = ParagraphStyle("entrydate", fontName="Sans", fontSize=8.5, leading=12, textColor=MUTED, alignment=TA_RIGHT)
entry_org = ParagraphStyle("entryorg", fontName="Sans", fontSize=9, textColor=BODY, leading=11.5, spaceAfter=2)
bullet_style = ParagraphStyle("bullet", fontName="Sans", fontSize=8.6, textColor=BODY, leading=11.8, spaceAfter=2)
tag_style = ParagraphStyle("tag", fontName="Sans", fontSize=8.4, textColor=BODY, leading=11.5)
small_muted = ParagraphStyle("smallmuted", fontName="Sans", fontSize=8.4, textColor=MUTED, leading=11, spaceBefore=3)
cert_group_title = ParagraphStyle("certgroup", fontName="Sans-Bold", fontSize=9.1, leading=11.5, textColor=TEXT, spaceBefore=4, spaceAfter=1.5)
cert_line = ParagraphStyle("certline", fontName="Sans", fontSize=8.6, textColor=BODY, leading=11.5, spaceAfter=1)

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=1, spaceAfter=6)

def section_row(title_text, date_text):
    t = Table([[Paragraph(title_text, entry_title), Paragraph(date_text, entry_date)]],
               colWidths=[130*mm, 40*mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, bullet_style), leftIndent=10, bulletColor=ACCENT) for i in items],
        bulletType="bullet", bulletFontName="Sans", bulletFontSize=8, start="\u2013",
        leftIndent=12, spaceBefore=1, spaceAfter=5,
    )

doc = SimpleDocTemplate(
    "../assets/files/CV-Daniel-Viedienin-EN.pdf",
    pagesize=A4,
    topMargin=14*mm, bottomMargin=13*mm, leftMargin=18*mm, rightMargin=18*mm,
    title="Daniel Viedienin - Resume (CV)", author="Daniel Viedienin",
)

story = []
story.append(Paragraph("Daniel Viedienin", name_style))
story.append(Paragraph("Paramedic &middot; Medical Student &middot; AI in Emergency Medicine", role_style))
story.append(hr())

story.append(Paragraph(
    'Email: youngdoc@ukr.net &nbsp;&nbsp;|&nbsp;&nbsp; '
    'LinkedIn: linkedin.com/in/daniel-viedienin &nbsp;&nbsp;|&nbsp;&nbsp; '
    'Telegram: t.me/spittinfax<br/>Location: Kriviy Rih city, Dnipropetrovsk region, Ukraine',
    contact_style))

story.append(Paragraph("Professional Profile", section_style))
story.append(hr())
story.append(Paragraph(
    "Paramedic with 3+ years and 4,000+ emergency calls in disaster medicine. B2B sales background. "
    "Integrate AI into daily practice. Now moving into HealthTech to bridge clinical reality and "
    "product development.", body_style))

story.append(Paragraph("Experience", section_style))
story.append(hr())
story.append(section_row("Paramedic (EMS, ambulance)", "08.2023 &ndash; Present"))
story.append(Paragraph("Regional Center for Emergency Medical Care and Disaster Medicine of Dnipropetrovsk Regional Council, Ukraine", entry_org))
story.append(bullets([
    "Custom AI prompting framework for emergency documentation &ndash; developed and maintained a personal "
    "library of 50+ structured prompts for rapid differential diagnosis, automated documentation "
    "(reducing paperwork time by ~30%), and scenario-based protocols for trauma, cardiac arrest, "
    "stroke, overdose, and psychiatric emergencies.",
    "Used electronic health records (EHR) and mobile documentation tools to ensure accurate and timely "
    "data entry for every call, maintaining 100% compliance with reporting standards.",
    "Managed high-stress conversations with patients and families in life-threatening situations, "
    "maintaining calm and clarity while delivering critical information.",
    "Made independent clinical decisions in high-pressure environments with limited information, "
    "consistently achieving positive patient outcomes.",
    "Optimized pre-hospital care protocols by analyzing call data and feedback from hospital staff, "
    "reducing average response-to-handover time.",
]))

story.append(section_row("B2B Sales Representative &ndash; Veterinary Pharmaceuticals", "4 months, 2026"))
story.append(Paragraph("Private veterinary pharma distributor", entry_org))
story.append(bullets([
    "Built trust-based relationships with veterinarians by offering clinical insights, not just product pitches.",
    "Managed CRM records and tracked sales performance.",
    "Delivered consistent results in a competitive market.",
]))
story.append(Paragraph(
    "Left the position after the company shifted its focus from product value to formal reporting &ndash; "
    "a direction that no longer aligned with my professional standards.", body_style))

story.append(Paragraph("Education", section_style))
story.append(hr())
story.append(section_row("Kryvyi Rih Professional Medical College", "2019&ndash;2023"))
story.append(Paragraph("General Medicine, Junior Specialist", entry_org))
story.append(section_row("Kharkiv National Medical University", "1st year"))
story.append(Paragraph("Medicine, 1st year student (state-funded)", entry_org))

story.append(Paragraph("Certifications", section_style))
story.append(hr())
cert_groups = [
    ("Mental Health", [
        "mhGAP (Level 1) &ndash; Management of Common Mental Disorders in Primary Care (2023)",
        "mhGAP (Level 2) &ndash; Management of Common Mental Disorders in Primary Care (2024)",
    ]),
    ("Professional Development", [
        "Emergency Medicine Refresher Course (420 hrs, 2025) &ndash; comprehensive clinical competency review",
    ]),
    ("Critical Care", [
        "Critical Adult Patient Management &amp; Advanced Resuscitation (27 hrs, 2025)",
        "Critical Trauma Patient Management &ndash; Foundation (15 hrs, 2025)",
        "Critical Pediatric Patient Management (10 hrs, 2025)",
        "Critical Trauma Patient Management &ndash; Advanced (16 hrs, 2026)",
    ]),
    ("Disaster Medicine", [
        "CBRNE Training &ndash; Harvard Humanitarian Initiative (2024) &ndash; Chemical, Biological, "
        "Radiological, Nuclear, and Explosive threats; mass casualty coordination",
        "Disaster Medicine (6 hrs, 2025)",
    ]),
]
for title, lines in cert_groups:
    story.append(Paragraph(title, cert_group_title))
    for l in lines:
        story.append(Paragraph(l, cert_line))

story.append(Paragraph("Skills", section_style))
story.append(hr())
hard_skills = ("Pre-hospital emergency care &middot; Disaster medicine &amp; mass casualty coordination &middot; "
    "Triage &amp; rapid patient assessment &middot; Advanced resuscitation (ACLS, ATLS) &middot; "
    "Differential diagnosis under pressure &middot; AI integration in clinical practice &middot; "
    "Prompt engineering for diagnostics &amp; documentation &middot; EHR &amp; mobile documentation tools &middot; "
    "CRM systems &amp; sales tracking &middot; B2B sales &amp; negotiations &middot; "
    "Clinical product demonstration &middot; Public speaking &amp; team training &middot; "
    "Medical writing &amp; documentation")
soft_skills = ("Rapid decision-making under pressure &middot; Emotional resilience &amp; stress management &middot; "
    "Empathy &amp; active listening &middot; Crisis communication &amp; de-escalation &middot; "
    "Adaptability in chaotic environments &middot; Leadership &amp; team coordination &middot; "
    "Systematic thinking &amp; process optimization &middot; Self-discipline &amp; continuous learning &middot; "
    "Integrity &amp; professional boundaries")
story.append(Paragraph("Hard Skills", cert_group_title))
story.append(Paragraph(hard_skills, tag_style))
story.append(Paragraph("English (B2, progressing to C1; + medical terminology) &middot; Ukrainian (native) &middot; Russian (fluent)", small_muted))
story.append(Paragraph("Soft Skills", cert_group_title))
story.append(Paragraph(soft_skills, tag_style))

story.append(Paragraph("Key Achievements", section_style))
story.append(hr())
story.append(bullets([
    "4000+ emergency calls &ndash; provided pre-hospital care in highest-priority cases: heart attacks, "
    "polytrauma, strokes, and various other emergency conditions.",
    "30% reduction in documentation time &ndash; implemented AI-assisted documentation, allowing more "
    "time for direct patient care.",
    "Developed 50+ custom clinical prompts &ndash; built a structured prompt library for differential "
    "diagnostics, status localis, and scenario-based protocols, now used as a personal decision-support tool.",
    "Maintained 100% EHR compliance &ndash; consistently met all electronic health record and reporting "
    "standards across shifts.",
    "Managed high-complexity cases independently &ndash; made critical clinical decisions in conditions "
    "of extreme uncertainty, consistently achieving positive patient outcomes.",
    "Integrated AI into daily clinical routine &ndash; one of the first paramedics in the region to "
    "systematically apply generative AI in emergency workflows, setting a precedent for technology "
    "adoption in pre-hospital care.",
]))

doc.build(story)
print("PDF written")
