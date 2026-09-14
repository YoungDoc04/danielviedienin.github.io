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
from reportlab.lib.utils import ImageReader

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
role_style = ParagraphStyle("role", fontName="Sans", fontSize=10, leading=13, textColor=MUTED, spaceAfter=6)
cta_style = ParagraphStyle("cta", fontName="Sans-Bold", fontSize=10.5, leading=13, textColor=LINK, spaceAfter=8)
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
               colWidths=[100*mm, 33*mm])
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

BG_IMAGE = "pdf-bg-faded.jpg"
BG_IMG_W, BG_IMG_H = 1700, 786
PHOTO_IMAGE = "pdf-photo.jpg"
PAGE_W, PAGE_H = A4
BG_DRAW_W = PAGE_W
BG_DRAW_H = BG_DRAW_W * (BG_IMG_H / BG_IMG_W)
PHOTO_W = 30*mm
PHOTO_H = PHOTO_W / (520/680)
PHOTO_X = PAGE_W - 18*mm - PHOTO_W
PHOTO_Y = PAGE_H - 14*mm - PHOTO_H

def draw_bg(canvas, doc):
    canvas.saveState()
    canvas.drawImage(BG_IMAGE, 0, 0, width=BG_DRAW_W, height=BG_DRAW_H)
    canvas.restoreState()

def draw_first_page(canvas, doc):
    draw_bg(canvas, doc)
    canvas.saveState()
    canvas.drawImage(PHOTO_IMAGE, PHOTO_X, PHOTO_Y, width=PHOTO_W, height=PHOTO_H)
    canvas.restoreState()

doc = SimpleDocTemplate(
    "../assets/files/CV-Daniel-Viedienin-UA.pdf",
    pagesize=A4,
    topMargin=14*mm, bottomMargin=13*mm, leftMargin=18*mm, rightMargin=55*mm,
    title="Daniel Viedienin - Resume (CV)", author="Daniel Viedienin",
)

story = []
story.append(Paragraph("Данило Вєдєнін", name_style))
story.append(Paragraph("Парамедик &middot; Студент-медик &middot; ШІ в екстреній медицині", role_style))
story.append(Paragraph('Бажаєш дізнатись більше? Мій сайт-візитівка: <a href="https://danielviedienin.com" color="#1f6f5c">DanielViedienin.com</a>', cta_style))
story.append(hr())

story.append(Paragraph(
    'Email: youngdoc@ukr.net &nbsp;&nbsp;|&nbsp;&nbsp; '
    'LinkedIn: linkedin.com/in/daniel-viedienin &nbsp;&nbsp;|&nbsp;&nbsp; '
    'Telegram: t.me/spittinfax<br/>Локація: місто Кривий Ріг, Дніпропетровська область, Україна',
    contact_style))

story.append(Paragraph("Професійний профіль", section_style))
story.append(hr())
story.append(Paragraph(
    "Парамедик із 3+ роками та 4000+ викликів у медицині катастроф. Досвід B2B-продажів. "
    "Впроваджую ШІ в практику. Переходжу в HealthTech, щоб поєднати клінічну реальність із "
    "розробкою продуктів.", body_style))

story.append(Paragraph("Досвід роботи", section_style))
story.append(hr())
story.append(section_row("Парамедик (екстрена медична допомога)", "08.2023 &ndash; дотепер"))
story.append(Paragraph("КНП «Обласний центр екстреної медичної допомоги та медицини катастроф» ДОР", entry_org))
story.append(bullets([
    "Власна система промптів для екстреної документації &ndash; розробив і підтримую бібліотеку "
    "з 50+ структурованих запитів для швидкої диференційної діагностики, автоматизованого "
    "документування (скорочення часу на паперову роботу на ~30%) та сценарних протоколів для "
    "травми, зупинки серця, інсульту, передозування та психіатричних станів.",
    "Використовував електронні медичні записи (ЕМЗ) та мобільні інструменти документування для "
    "забезпечення точності даних за кожним викликом, підтримуючи 100% відповідність стандартам "
    "звітності.",
    "Вів складні переговори з пацієнтами та родичами в критичних ситуаціях, зберігаючи спокій і "
    "чіткість під час передачі життєво важливої інформації.",
    "Приймав самостійні клінічні рішення в умовах високого тиску та обмеженої інформації, "
    "досягаючи позитивних результатів для пацієнтів.",
    "Оптимізував протоколи долікарської допомоги, аналізуючи дані викликів та зворотний зв'язок "
    "від персоналу лікарень, скорочуючи середній час від реагування до передачі пацієнта.",
]))

story.append(section_row("Менеджер з B2B-продажів &ndash; Ветеринарна фармацевтика", "4 місяці, 2026"))
story.append(Paragraph("Приватний дистриб'ютор ветеринарної фармації", entry_org))
story.append(bullets([
    "Вибудовував довірливі стосунки з лікарями через клінічну аргументацію, а не стандартні продажі.",
    "Вів CRM-звітність та аналізував показники продажів.",
    "Показував стабільні результати в конкурентному середовищі.",
]))
story.append(Paragraph(
    "Пішов після того, як компанія змістила фокус із реальної цінності продукту на формальну "
    "звітність &ndash; це не відповідало моїм професійним принципам.", body_style))

story.append(Paragraph("Освіта", section_style))
story.append(hr())
story.append(section_row("Криворізький фаховий медичний коледж", "2019&ndash;2023"))
story.append(Paragraph("Лікувальна справа, молодший спеціаліст", entry_org))
story.append(section_row("Харківський національний медичний університет", "1 курс"))
story.append(Paragraph("Медицина, 1 курс (бюджет)", entry_org))

story.append(Paragraph("Курси та сертифікати", section_style))
story.append(hr())
cert_groups = [
    ("Психічне здоров'я", [
        "mhGAP (рівень 1) &ndash; Ведення поширених психічних розладів на первинному рівні медичної допомоги (2023)",
        "mhGAP (рівень 2) &ndash; Ведення поширених психічних розладів на первинному рівні медичної допомоги (2024)",
    ]),
    ("Підвищення кваліфікації", [
        "Екстрена медицина (420 год, 2025) &ndash; повторення навчального матеріалу для підвищення кваліфікації",
    ]),
    ("Критична допомога", [
        "Менеджмент критичного дорослого пацієнта та розширені реанімаційні заходи у дорослих (27 год, 2025)",
        "Менеджмент критичного травмованого пацієнта (15 год, 2025)",
        "Менеджмент критичного педіатричного пацієнта (10 год, 2025)",
        "Менеджмент критичного травмованого пацієнта (16 год, 2026) &ndash; поглиблений рівень",
    ]),
    ("Медицина катастроф", [
        "Хімічна, біологічна, радіологічна, ядерна та вибухова загроза (CBRNE) &ndash; Harvard "
        "Humanitarian Initiative (2024) &ndash; загальні поняття, координація бригад у надзвичайних ситуаціях",
        "Медицина катастроф (6 год, 2025)",
    ]),
]
for title, lines_ in cert_groups:
    story.append(Paragraph(title, cert_group_title))
    for l in lines_:
        story.append(Paragraph(l, cert_line))

story.append(Paragraph("Навички", section_style))
story.append(hr())
hard_skills = ("Долікарська екстрена допомога &middot; Медицина катастроф та координація при масових "
    "надходженнях &middot; Сортування (triage) та швидка оцінка пацієнта &middot; Розширена реанімація "
    "(ACLS, ATLS) &middot; Диференційна діагностика в умовах дефіциту часу &middot; Інтеграція ШІ в "
    "клінічну практику &middot; Розробка промптів для діагностики та документування &middot; ЕМЗ та "
    "мобільні інструменти &middot; CRM-системи та відстеження продажів &middot; B2B-продажі та "
    "переговори &middot; Демонстрація клінічних продуктів &middot; Публічні виступи та навчання команд "
    "&middot; Медичне документування")
soft_skills = ("Швидке прийняття рішень у критичних умовах &middot; Емоційна стійкість та управління "
    "стресом &middot; Емпатія та активне слухання &middot; Кризова комунікація та деескалація "
    "конфліктів &middot; Адаптивність у хаотичному середовищі &middot; Лідерство та координація "
    "команди &middot; Системне мислення та оптимізація процесів &middot; Самодисципліна та постійне "
    "навчання &middot; Чесність, порядність та повага до кордонів")
story.append(Paragraph("Hard Skills", cert_group_title))
story.append(Paragraph(hard_skills, tag_style))
story.append(Paragraph("Англійська (B2, рухаюсь до C1; + медична термінологія) &middot; Українська (рідна) &middot; Російська (вільно)", small_muted))
story.append(Paragraph("Soft Skills", cert_group_title))
story.append(Paragraph(soft_skills, tag_style))

story.append(Paragraph("Досягнення", section_style))
story.append(hr())
story.append(bullets([
    "4000+ екстрених викликів &ndash; надання долікарської допомоги у випадках найвищого пріоритету: "
    "інфаркти, політравми, інсульти, інші всеможливі невідкладні стани.",
    "Скорочення часу на документацію на 30% &ndash; впровадження ШІ-асистованого документування, що "
    "дозволило більше часу приділяти пацієнтам.",
    "50+ авторських клінічних промптів &ndash; створена структурована бібліотека запитів для "
    "диференційної діагностики, status localis та сценарних протоколів, що використовується як "
    "персональний інструмент підтримки рішень.",
    "100% відповідність ЕМЗ &ndash; системне дотримання стандартів електронних записів та звітності "
    "у всіх змінах.",
    "Самостійне ведення складних випадків &ndash; прийняття критичних клінічних рішень в умовах "
    "екстремальної невизначеності (обмежена інформація, масові інциденти, політравма) з позитивними "
    "результатами для пацієнтів.",
    "Інтеграція ШІ в щоденну клінічну практику &ndash; один із перших парамедиків регіону, який "
    "системно впровадив генеративний ШІ в екстрені робочі процеси, створивши прецедент для "
    "впровадження технологій у долікарській допомозі.",
]))

doc.build(story, onFirstPage=draw_first_page, onLaterPages=draw_bg)
