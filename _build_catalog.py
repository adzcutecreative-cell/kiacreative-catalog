#!/usr/bin/env python3
"""Bangun products.js + resize gambar untuk landing page katalog."""
from pathlib import Path
from PIL import Image, ImageOps
import json

SRC = Path(r"C:\Users\USER\Downloads")
KP = SRC / "KIACreative_Products"
EM = SRC / "Etsy_Mockups"
HERE = Path(r"C:\Users\USER\Downloads\KIACreative_Products\Landing_Page")
OUT = HERE / "assets" / "products"
OUT.mkdir(parents=True, exist_ok=True)

CANVA = EM / "CanvaMediaKit" / "01_canvamedia.jpg"

RAW = [
 ("4624519583","24 Currency VAT Tracker Web App, Invoice & Exchange Rate Manager, 7 Languages, Bonus Excel","9.99","Web App", KP/"MultiCurrency_VAT_App/01_Listing_Assets/Hero_2000x2000.jpg"),
 ("4624014953","10 KDP Storybook Templates, Watercolor Covers, 8.5x8.5 Print Ready (PLR License)","3.99","Kids & KDP", KP/"KDP_Kids_Storybook_Bundle/01_Listing_Assets/Hero_10_Covers_1Frame/Hero_10_Covers_1Frame_2000x2000.jpg"),
 ("4622722009","Freelancer Template Bundle, Notion Client Tracker + Canva Media Kit Resume Rate Card","14.99","Templates", EM/"FreelancerBundle/01_bundle.jpg"),
 ("4622696713","Freelancer Client Tracker Notion Template, Project & Invoice Dashboard","8.99","Notion", EM/"NotionFreelancer/01_notionfreelancer.jpg"),
 ("4616359420","Budget Spreadsheet Google Sheets and Excel, Monthly Bills Tracker with Dashboard","0.99","Spreadsheet", KP/"Budget_Starter_Free/Cover_Budget_Starter.png"),
 ("4621079101","Client Tracker for Freelancers, Invoice & Project Manager, No Coding","9.99","Web App", EM/"ClientNest/01_clientnest.jpg"),
 ("4620465835","200 Question Bank, Editable Quiz Questions With Answer Key, Multi Select","3.99","Education", EM/"QBank/01_qbank.jpg"),
 ("4620453749","Gradebook Google Sheets, Teacher Grade Tracker, Auto Average & Letter Grades","5.99","Spreadsheet", EM/"Gradebook/01_gradebook.jpg"),
 ("4620421833","Custom Quiz Web App Made to Order, Branded Online Assessment, No Coding","79.00","Web App", EM/"CustomApp/01_custom-app.jpg"),
 ("4620411670","Quiz Maker Web App, Offline Quiz With Student Login & Teacher Dashboard","9.99","Web App", EM/"QuizNest/01_quiznest.jpg"),
 ("4617879412","Art Deco Clipart Bundle, 30 Gold Vector Designs, SVG PNG EPS","4.99","Design & SVG", EM/"ArtDeco/01_artdeco.jpg"),
 ("4616169439","Secret Santa Gift Exchange Organizer Spreadsheet, Wishlist + Budget","5.99","Spreadsheet", EM/"GiftExchange/01_giftexchange.jpg"),
 ("4613447793","Wedding Budget + Timeline Spreadsheet, Guest RSVP Tracker","9.99","Spreadsheet", EM/"Wedding/01_wedding.jpg"),
 ("4613456792","Savings Challenge Spreadsheet, 52-Week Budget Goal Tracker","5.99","Spreadsheet", EM/"Savings/01_savings.jpg"),
 ("4615662559","Daily Life Bundle Spreadsheet, 3 Excel Trackers for Meals Fitness and Study","5.49","Spreadsheet", KP/"Daily_Balance_Product/Daily_Tutorial_Input75_Highlight_chk1.png"),
 ("4615664341","Spreadsheet Bundle, 7 Finance and Life Trackers for Excel and Google Sheets","9.99","Spreadsheet", EM/"DailyBalance/01_dailybalance.jpg"),
 ("4615672362","Budget Spreadsheet Bundle, 3 Excel and Google Sheets Templates for Bills and Debt","5.49","Spreadsheet", EM/"BillsDue/01_billsdue.jpg"),
 ("4614224828","Christmas Glow SVG Bundle, 36 Neon Files, PNG EPS, Commercial Use","9.99","Design & SVG", KP/"Christmas_Glowing_Bundle_Product/designs_neon/01_christmas_tree.png"),
 ("4614114097","Christmas SVG Cut Files, 18 Files, PNG EPS, Commercial Use","2.99","Design & SVG", KP/"Christmas_Vector_Bundle_Product/designs/01_christmas_tree.png"),
 ("4613379404","New Year 2027 Card Set, 6 Printable Designs in 5x7 PDF and PNG","5.49","Greeting Cards", KP/"NewYear2027_Cards_Product/Listing_Images/01_minimal_hero.png"),
 ("4613381810","Christmas Cards PDF, Set of 6 Printable 5x7 Folded Holiday Greetings","5.49","Greeting Cards", KP/"Christmas_Cards_Product/Listing_Images/01_minimal_hero.png"),
 ("4613384918","Printable Valentine Cards, 6 Designs, 5x7 Folded Greeting Card Set","5.49","Greeting Cards", KP/"Valentines_Cards_Product/Listing_Images/01_minimal_hero.png"),
 ("4613155926","Freelancer Income Tracker Spreadsheet, Client Invoice and Payment Log","2.49","Spreadsheet", KP/"Freelancer_Product/Listing_Images/01_hero_laptop.png"),
 ("4613138145","Study Planner Spreadsheet, Exam Countdown Pomodoro and Revision","2.49","Spreadsheet", KP/"Study_Product/Listing_Images/01_hero_laptop.png"),
 ("4613151762","Fitness and Weight Tracker Spreadsheet, Workout Log Gym Planner","2.49","Spreadsheet", KP/"Fitness_Product/Listing_Images/01_hero_laptop.png"),
 ("4612774265","Weekly Meal Planner Spreadsheet, Grocery Budget List","2.49","Spreadsheet", KP/"Meal_Planner_Product/Listing_Images/01_hero_laptop.png"),
 ("4612762774","Greeting Card Bundle, 18 Printable Cards 5x7, Christmas New Year Valentine","9.99","Greeting Cards", KP/"Etsy_Holiday_Love_Bundle/Etsy_Holiday_Love_Bundle/02_Listing_Photos/01_cover.png"),
 ("4612672320","Debt Payoff Tracker Spreadsheet, Snowball and Avalanche","2.49","Spreadsheet", KP/"Debt_Payoff_Product/Listing_Images/01_hero_laptop.png"),
 ("4612743626","Bills Due Tracker and Budget Calendar, Monthly Bill Payment Checklist","2.49","Spreadsheet", KP/"Bills_Due_Product/Listing_Images/01_hero_laptop.png"),
 ("4612620030","Budget Planner and Habit Tracker Spreadsheet, Monthly Dashboard","2.49","Spreadsheet", KP/"Daily_Balance_Product/Daily_Tutorial_Input75_Highlight_chk1.png"),
 ("4612114699","Instagram Templates for Boutiques, 10 Neutral Gold Canva Feed Posts","5.49","Canva Templates", CANVA),
 ("4611873958","Instagram Post Kit, 35 Canva Templates for Feed Stories and Carousels","9.99","Canva Templates", CANVA),
]

products = []
for pid, title, price, cat, src in RAW:
    p = Path(src)
    if not p.exists():
        print("MISSING", p)
        continue
    out = OUT / f"{pid}.jpg"
    im = Image.open(p).convert("RGB")
    im = ImageOps.fit(im, (800,800), Image.LANCZOS, centering=(0.5,0.35))
    im.save(out, quality=85, optimize=True)
    products.append({
        "id": pid, "title": title, "price": price, "category": cat,
        "image": f"assets/products/{pid}.jpg",
        "url": f"https://www.etsy.com/listing/{pid}"
    })

(HERE/"products.js").write_text(
    "const PRODUCTS = " + json.dumps(products, ensure_ascii=False, indent=2) + ";\n",
    encoding="utf-8")
print("products", len(products))
