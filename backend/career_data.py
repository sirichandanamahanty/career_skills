from typing import Dict, List, Any

FIELDS: Dict[str, str] = {
    "Computer Science / IT": "You have the technical base. Focus on depth, projects and interview skills.",
    "Engineering (any branch)": "Your problem-solving and maths training transfers to almost any role. Show it with a project in your target area.",
    "Science (Physics, Chem, Bio, Maths, Stats)": "You are used to evidence and experiments. That helps in research, data, teaching and policy work.",
    "Commerce / Business / Economics": "You understand money, markets and decisions, which suits finance, sales, marketing and management.",
    "Arts / Humanities / Social Science": "Your writing, research and people skills are in demand in media, HR, teaching, civil services and marketing.",
    "Law": "Your reasoning and drafting skills fit legal, compliance, policy and civil services paths.",
    "Medical / Pharmacy / Life Sciences": "Your domain knowledge is rare. It helps in research, healthcare administration and health data roles.",
    "Education / Teaching": "You can explain and organise. That helps in training, HR, content and public service roles.",
    "Design / Media": "You think visually and communicate well, which suits design, marketing and content roles.",
    "Other / Self-taught": "Start from the basics and track each step. Consistency matters more than where you begin."
}

TAG: Dict[str, str] = {
    "ias": "PI", "bnk": "PVI", "def": "PI", "pol": "PI", "rly": "PI",
    "ifs": "PIA", "jud": "PI", "ifo": "PI", "tax": "PI", "isr": "PI",
    "jea": "PI", "grc": "PI", "atc": "PIA", "ca": "PVIA", "act": "PVIA",
    "den": "PVIA", "bsa": "PVIA", "erp": "PVIA", "cre": "VIA", "rea": "VIA",
    "ins": "PVI", "cra": "VIA", "bio": "PVIA", "lab": "PVIA", "hca": "PVIA",
    "trn": "PVIA", "cvl": "PVIA", "usm": "PVA", "nab": "PVA", "itr": "VA",
    "sfr": "VA", "crw": "VIA", "skl": "PVIA"
}

BK: Dict[str, str] = {
    "dev": "Cracking the Coding Interview|Clean Code|The Pragmatic Programmer",
    "an": "Storytelling with Data|Naked Statistics",
    "ds": "Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow|Python for Data Analysis",
    "mkt": "This Is Marketing|Building a StoryBrand",
    "hrx": "First, Break All the Rules|Work Rules!",
    "sal": "SPIN Selling|To Sell Is Human",
    "fin": "Financial Intelligence|Financial Shenanigans",
    "ias": "Indian Polity by M. Laxmikanth|India’s Struggle for Independence by Bipan Chandra|Indian Economy by Ramesh Singh",
    "bnk": "Quantitative Aptitude by R.S. Aggarwal|A Modern Approach to Verbal and Non-Verbal Reasoning",
    "res": "The Craft of Research|How to Write a Lot",
    "tch": "Make It Stick|Teach Like a Champion",
    "des": "The Design of Everyday Things|Don’t Make Me Think",
    "wrt": "On Writing Well|Everybody Writes",
    "law": "Constitutional Law of India by J.N. Pandey|Law of Contract by Avtar Singh",
    "eng": "Advanced Engineering Mathematics by Erwin Kreyszig|Shigley’s Mechanical Engineering Design",
    "doc": "Harrison’s Principles of Internal Medicine|Gray’s Anatomy for Students",
    "nur": "Fundamentals of Nursing by Potter and Perry|Brunner and Suddarth’s Medical-Surgical Nursing",
    "pha": "Rang and Dale’s Pharmacology|Goodman and Gilman’s Pharmacological Basis of Therapeutics",
    "phy": "Therapeutic Exercise by Kisner and Colby|Kinesiology of the Musculoskeletal System",
    "psy": "Psychology by David Myers|Man’s Search for Meaning",
    "vet": "Merck Veterinary Manual|Textbook of Veterinary Anatomy by Dyce",
    "cyb": "The Web Application Hacker’s Handbook|Hacking: The Art of Exploitation",
    "cld": "The Phoenix Project|Site Reliability Engineering",
    "aim": "Deep Learning by Ian Goodfellow|Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow",
    "mob": "Head First Android Development|Flutter in Action",
    "gam": "The Art of Game Design by Jesse Schell|Game Programming Patterns",
    "qat": "Lessons Learned in Software Testing|Agile Testing",
    "pdm": "Inspired by Marty Cagan|Cracking the PM Interview",
    "net": "Computer Networking: A Top-Down Approach|The Art of Electronics",
    "ops": "The Goal by Eliyahu Goldratt|Operations Management by Heizer and Render",
    "ent": "The Lean Startup|Zero to One",
    "pjm": "PMBOK Guide|Scrum by Jeff Sutherland",
    "con": "Case in Point|The McKinsey Way",
    "inb": "The Intelligent Investor|Investment Valuation by Aswath Damodaran",
    "cus": "Delivering Happiness|The Effortless Experience",
    "cs": "Company Law by Avtar Singh",
    "evt": "Special Events by Joe Goldblatt|Event Planning by Judy Allen",
    "def": "Lucent’s General Knowledge|NDA/NA Exam Guide (Arihant)",
    "pol": "Lucent’s General Knowledge|Quantitative Aptitude by R.S. Aggarwal",
    "rly": "Lucent’s General Knowledge|Quantitative Aptitude by R.S. Aggarwal",
    "arc": "Architecture: Form, Space, and Order by Francis D.K. Ching|A Pattern Language",
    "int": "Interior Design Illustrated by Francis D.K. Ching",
    "fas": "Fashion Design Course by Steven Faerm|Fashion Sketchbook by Bina Abling",
    "pho": "Understanding Exposure by Bryan Peterson|In the Blink of an Eye by Walter Murch",
    "ani": "The Animator’s Survival Kit by Richard Williams",
    "chf": "On Cooking by Labensky|The Professional Chef",
    "hot": "Introduction to Hospitality by John R. Walker",
    "pil": "Pilot’s Handbook of Aeronautical Knowledge|Stick and Rudder",
    "elt": "A Textbook of Electrical Technology by B.L. Theraja",
    "agr": "Principles of Agronomy by S.R. Reddy",
    "fit": "Essentials of Strength Training and Conditioning|Becoming a Supple Leopard",
    "swk": "Development as Freedom by Amartya Sen|Poor Economics",
    "eco": "Principles of Economics by N. Gregory Mankiw|Poor Economics",
    "env": "Environmental Science by Botkin and Keller|Silent Spring by Rachel Carson"
}

NEED: Dict[str, str] = {
    "dev": "Entry: any degree plus proven coding skills|Tools: laptop, VS Code, Git and a GitHub account|Also: internet and a portfolio of 3 projects",
    "an": "Entry: any degree with maths or business sense|Tools: Excel, an SQL database, Power BI or Tableau (free versions), Python|Also: portfolio of 3 case studies",
    "ds": "Entry: degree in maths, stats or CS helps, strong self-study also works|Tools: laptop with 8 GB RAM, Python, Jupyter, free Kaggle or Colab account|Also: GitHub with 3 projects",
    "mkt": "Entry: any degree|Tools: Canva, Google Analytics, a practice social media account|Also: portfolio of campaigns",
    "hrx": "Entry: any degree, MBA in HR helps|Tools: Excel, a job portal account, an applicant tracking tool demo|Also: knowledge of labour laws",
    "sal": "Entry: any degree|Tools: LinkedIn profile, phone, CRM basics|Also: strong communication and a product to practise pitching",
    "fin": "Entry: B.Com or related, CA or CMA for senior roles|Tools: Excel, Tally or QuickBooks|Also: GST and income tax knowledge",
    "ias": "Entry: a degree from a recognised university, with age and attempt limits|Tools: NCERT books, a daily newspaper, a test series|Also: check the current UPSC notification for eligibility",
    "bnk": "Entry: graduation, check each exam notice|Tools: mock-test platform, previous year papers|Also: age limit and category rules in the official notice",
    "res": "Entry: master's degree, often PhD|Tools: journal access, a reference manager such as Zotero, lab or data tools|Also: a supervisor and a research proposal",
    "tch": "Entry: degree plus B.Ed and TET or NET as required|Tools: slides, whiteboard or tablet, quiz tools|Also: a recorded demo lesson",
    "des": "Entry: any background, a design degree helps|Tools: Figma (free plan), Adobe or Canva, a laptop|Also: portfolio website",
    "wrt": "Entry: any degree|Tools: laptop, Google Docs, a blog or portfolio|Also: published writing samples",
    "law": "Entry: LL.B (3 or 5 years) and Bar Council enrolment|Tools: Indian Kanoon, India Code, law reports|Also: internships with advocates",
    "eng": "Entry: B.E. or B.Tech in the branch, GATE for higher studies|Tools: CAD and simulation software with student licences|Also: internships and safety gear for site work",
    "doc": "Entry: MBBS through NEET UG, then NEET PG to specialise|Tools: stethoscope, textbooks, anatomy resources|Also: registration with the National Medical Commission",
    "nur": "Entry: B.Sc Nursing or GNM|Tools: uniform, stethoscope, BP apparatus|Also: state nursing council registration",
    "pha": "Entry: D.Pharm or B.Pharm|Tools: reference books, lab coat|Also: pharmacy council registration",
    "phy": "Entry: BPT degree|Tools: goniometer and exercise equipment for practice|Also: council registration where required",
    "psy": "Entry: BA or MA in Psychology, M.Phil for clinical work|Tools: standard test manuals, a private space for practice|Also: supervised hours and RCI registration for clinical roles",
    "vet": "Entry: BVSc and AH through an entrance exam|Tools: clinical kit, textbooks|Also: Veterinary Council registration",
    "cyb": "Entry: IT or CS degree, or any degree with strong IT skills|Tools: laptop, VirtualBox, Kali Linux, Wireshark|Also: practise only on systems you own or are allowed to test",
    "cld": "Entry: CS or IT degree, or equivalent skills|Tools: free tiers of AWS, Azure or GCP, Docker, Linux|Also: cloud signup may need a card, so set billing alerts",
    "aim": "Entry: degree in CS, maths or stats helps|Tools: Python, Jupyter or Colab, free GPU on Colab or Kaggle|Also: GitHub projects",
    "mob": "Entry: any degree plus coding skills|Tools: Android Studio or Xcode (a Mac for iOS), a phone for testing|Also: a developer account to publish, store fees apply",
    "gam": "Entry: any degree, the portfolio matters most|Tools: Unity or Unreal (free for learning), Blender|Also: game jam entries",
    "qat": "Entry: any degree, basic coding helps|Tools: Postman, Selenium or Playwright, Jira|Also: sample bug reports",
    "pdm": "Entry: any degree, MBA or tech experience helps|Tools: Figma, Jira, Notion, an analytics tool|Also: product teardown samples",
    "net": "Entry: B.E. or B.Tech in ECE or CS, or a diploma|Tools: Arduino or STM32 board, multimeter, Cisco Packet Tracer (free)|Also: lab projects",
    "ops": "Entry: any degree, MBA in operations helps|Tools: Excel, ERP basics|Also: internship in logistics or manufacturing",
    "ent": "Entry: no fixed degree|Tools: a business idea, basic accounts, a bank account, registrations such as GST or Udyam|Also: savings or a funding plan, and mentors",
    "pjm": "Entry: any degree plus work experience|Tools: Jira, Trello, MS Project, Excel|Also: PMP has experience-hour requirements",
    "con": "Entry: a strong degree or MBA is typical|Tools: Excel, PowerPoint|Also: a case practice partner",
    "inb": "Entry: B.Com, BBA, MBA or CFA|Tools: Excel, market data sites, annual reports|Also: NISM certification for some roles",
    "cus": "Entry: 12th pass or degree|Tools: headset, ticketing or chat tool, good typing speed|Also: language skills",
    "cs": "Entry: CSEET, then the ICSI course|Tools: Companies Act text, MCA portal access|Also: ICSI registration",
    "evt": "Entry: any degree or diploma|Tools: planning sheets, vendor contacts, a phone|Also: first-aid awareness",
    "def": "Entry: 12th pass for NDA, graduation for CDS and AFCAT, with age and medical standards|Tools: running shoes, mock tests|Also: check each official notification",
    "pol": "Entry: 12th or graduation depending on the post, with age, physical and medical standards|Tools: running shoes, study material|Also: state police recruitment notices",
    "rly": "Entry: 10th, 12th, diploma or degree depending on the post|Tools: mock tests, previous papers|Also: check the RRB or PSU notice",
    "arc": "Entry: B.Arch through NATA or JEE Paper 2|Tools: AutoCAD, Revit, SketchUp, a drawing kit|Also: Council of Architecture registration",
    "int": "Entry: diploma or degree in interior design|Tools: SketchUp, AutoCAD, Photoshop, measuring tools|Also: portfolio and sample boards",
    "fas": "Entry: degree or diploma in fashion design|Tools: sewing machine, sketchbook, Illustrator|Also: a mini collection for the portfolio",
    "pho": "Entry: no fixed degree|Tools: camera, lenses, editing software, a computer|Also: portfolio and social presence",
    "ani": "Entry: degree or diploma, portfolio-led|Tools: Blender (free), Maya or After Effects, a drawing tablet|Also: a showreel",
    "chf": "Entry: diploma or degree in culinary arts or hotel management|Tools: knife set, chef whites, kitchen access|Also: food safety certificate",
    "hot": "Entry: BHM or a diploma|Tools: uniform and grooming|Also: hotel internships and language skills",
    "pil": "Entry: 12th with physics and maths, and a DGCA Class 1 medical|Tools: headset, flight simulator software for practice|Also: training fees are high, so plan the funding",
    "elt": "Entry: ITI or diploma|Tools: multimeter, tester, wire cutters, safety gear|Also: licence as required by the state",
    "agr": "Entry: B.Sc Agriculture or practical experience|Tools: soil testing kit, farm tools or access to land|Also: government scheme registrations",
    "fit": "Entry: certification or a sports science degree|Tools: basic equipment and a gym or open space|Also: first-aid and CPR certificate",
    "swk": "Entry: BSW or MSW|Tools: survey tools, MS Office|Also: field placements and NGO volunteering",
    "eco": "Entry: BA or B.Sc Economics, then MA|Tools: Excel, R or Stata, public datasets|Also: policy writing samples",
    "env": "Entry: B.Sc or M.Sc in environmental science, ecology or related|Tools: QGIS (free), a field sampling kit|Also: field experience",
    "ifs": "Entry: a degree plus the UPSC Civil Services Exam, with age and attempt limits|Tools: NCERT and standard books, a test series|Also: check the current UPSC notification",
    "jud": "Entry: LL.B and enrolment as the state notice requires|Tools: bare acts, law reports, past papers|Also: age and experience rules differ by state",
    "ifo": "Entry: degree in science, agriculture, forestry or engineering for IFoS|Tools: maps, field kit, fitness training|Also: check UPSC and state forest notices",
    "tax": "Entry: graduation for SSC CGL, or UPSC for IRS|Tools: mock tests, past papers|Also: SSC and UPSC notices",
    "isr": "Entry: B.E., B.Tech or M.Sc as per the notice|Tools: project work, GATE preparation|Also: read each official recruitment notice",
    "jea": "Entry: diploma or B.E./B.Tech depending on the post|Tools: CAD software, past papers|Also: official notices",
    "grc": "Entry: 10th, 12th or graduation depending on the post|Tools: typing practice, mock tests|Also: state notifications",
    "atc": "Entry: B.Sc with physics and maths, or B.E./B.Tech, for AAI|Tools: mock tests|Also: medical fitness and training",
    "ca": "Entry: ICAI Foundation, Intermediate, Final and articleship|Tools: Excel, Tally, ICAI material|Also: ICAI membership",
    "act": "Entry: strong maths, then actuarial exams|Tools: Excel, R or Python|Also: professional body membership",
    "den": "Entry: CS or IT degree or equivalent skills|Tools: free cloud tiers, Docker, Spark|Also: GitHub projects",
    "bsa": "Entry: any degree, domain knowledge helps|Tools: Excel, SQL, Visio or Lucidchart, Jira|Also: sample documents",
    "erp": "Entry: B.E., B.Com, MBA or MCA|Tools: a practice system or free learning access|Also: module certification",
    "cre": "Entry: no fixed degree|Tools: phone or camera, editing app, a channel or profile|Also: consistency and a clear niche",
    "rea": "Entry: any degree, RERA registration for agents in India|Tools: CRM, listing portals|Also: a local network",
    "ins": "Entry: 12th pass or degree, the IRDAI exam for agents|Tools: product brochures, CRM|Also: licence",
    "cra": "Entry: B.Pharm, M.Pharm, life science or medical degree|Tools: GCP training, MS Office|Also: certification",
    "bio": "Entry: M.Sc, M.Pharm or PhD|Tools: lab access, Excel or R|Also: publications",
    "lab": "Entry: DMLT, BMLT, B.Sc MLT or a radiology diploma|Tools: lab practice, safety gear|Also: council registration",
    "hca": "Entry: a degree plus MHA or MBA in hospital management|Tools: Excel, hospital software|Also: internships",
    "trn": "Entry: language degree or proof of fluency|Tools: translation tools, glossaries|Also: language certificates",
    "cvl": "Entry: B.E. or B.Tech in Civil|Tools: AutoCAD, STAAD, Revit|Also: licences where required",
    "usm": "Entry: MBBS plus the licensing exams of the target country|Tools: question banks, official guides|Also: licensing and visa rules differ by country",
    "nab": "Entry: nursing degree plus the target country’s licence exam|Tools: practice question banks, English test preparation|Also: registration and visa steps",
    "itr": "Entry: degree plus a teaching qualification|Tools: lesson plans and a teaching portfolio|Also: visa and background checks",
    "sfr": "Entry: DNS, B.Sc Nautical Science or B.Tech Marine, via IMU-CET or company selection|Tools: STCW courses|Also: medical fitness and CDC",
    "crw": "Entry: 12th pass, airline height and fitness standards|Tools: grooming, fluent English|Also: check each airline’s notice",
    "skl": "Entry: ITI or a trade course|Tools: trade tools, safety gear|Also: trade tests and certificates, which jobs abroad often require"
}

FREE: Dict[str, List[List[str]]] = {
    "all": [
        ["Khan Academy", "https://www.khanacademy.org", "free lessons in maths, science, economics and more"],
        ["NPTEL", "https://nptel.ac.in", "free IIT and IISc course videos"],
        ["SWAYAM", "https://swayam.gov.in", "free Government of India courses"],
        ["MIT OpenCourseWare", "https://ocw.mit.edu", "free university course material"],
        ["Coursera", "https://www.coursera.org", "most courses can be audited for free"],
        ["Alison", "https://alison.com", "free short courses with certificates"]
    ],
    "Technology and data": [
        ["freeCodeCamp", "https://www.freecodecamp.org", "web, data and Python curriculum"],
        ["The Odin Project", "https://www.theodinproject.com", "full web development path"],
        ["CS50", "https://cs50.harvard.edu/x", "Harvard’s intro to computer science"],
        ["Kaggle Learn", "https://www.kaggle.com/learn", "short data and ML courses"],
        ["roadmap.sh", "https://roadmap.sh", "step-by-step role roadmaps"],
        ["W3Schools", "https://www.w3schools.com", "quick web and SQL references"]
    ],
    "Business and management": [
        ["HubSpot Academy", "https://academy.hubspot.com", "marketing, sales and service courses"],
        ["Google Skillshop", "https://skillshop.withgoogle.com", "Google Ads and Analytics training"]
    ],
    "Government and public service": [
        ["NCERT textbooks", "https://ncert.nic.in/textbook.php", "free school books, the base for most exams"],
        ["PIB", "https://pib.gov.in", "official government press releases for current affairs"],
        ["UPSC", "https://upsc.gov.in", "official notices and past papers"]
    ],
    "Healthcare": [
        ["OpenWHO", "https://openwho.org", "free health courses from WHO"],
        ["MedlinePlus", "https://medlineplus.gov", "reliable health information"],
        ["Khan Academy Health", "https://www.khanacademy.org/science/health-and-medicine", "medicine and physiology basics"]
    ],
    "Creative and media": [
        ["Canva Design School", "https://www.canva.com/learn/design/", "design basics"],
        ["Blender tutorials", "https://www.blender.org/support/tutorials/", "3D and animation"],
        ["Figma Help", "https://help.figma.com", "UI design tool guides"],
        ["Google Fonts Knowledge", "https://fonts.google.com/knowledge", "typography lessons"],
        ["DaVinci Resolve training", "https://www.blackmagicdesign.com/products/davinciresolve/training", "free video editing training"]
    ],
    "Law": [
        ["India Code", "https://www.indiacode.nic.in", "all central laws, free"],
        ["Indian Kanoon", "https://indiankanoon.org", "free case law search"],
        ["Supreme Court of India", "https://www.sci.gov.in", "judgments and notices"]
    ],
    "Trades, hospitality and services": [
        ["Skill India Digital", "https://skillindiadigital.gov.in", "free skill courses"],
        ["NSDC", "https://www.nsdcindia.org", "skill training and certification"]
    ],
    "Science, health and education": [
        ["DIKSHA", "https://diksha.gov.in", "free teaching resources"],
        ["NCERT textbooks", "https://ncert.nic.in/textbook.php", "free school books"],
        ["OpenLearn", "https://www.open.edu/openlearn/", "free courses from the Open University"]
    ]
}

ROLES_CATALOG: Dict[str, Dict[str, Any]] = {}

def _parse_skills(raw_str: str) -> List[List[Any]]:
    skills = []
    items = raw_str.split("|")
    for i, item in enumerate(items):
        parts = item.split(":")
        name = parts[0]
        note = parts[1] if len(parts) > 1 else ""
        hours = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 30
        weight = 12 - min(i, 4)
        skills.append([name, weight, hours, note])
    return skills

def _p(id_key: str, name: str, desc: str, cat: str, skills: List[List[Any]], pr: List[str], ce: List[str], tag: str = "PVIA", nd: str = ""):
    t = TAG.get(id_key, tag)
    s = "Public + Private" if ("P" in t and "V" in t) else ("Public" if "P" in t else "Private")
    r = "India + Abroad" if ("I" in t and "A" in t) else ("India" if "I" in t else "Abroad")
    books = BK.get(id_key, "").split("|") if BK.get(id_key) else []
    needs = nd.split("|") if nd else (NEED.get(id_key, "").split("|") if NEED.get(id_key) else [])
    
    ROLES_CATALOG[id_key] = {
        "id": id_key,
        "name": name,
        "description": desc,
        "category": cat,
        "skills": skills,
        "projects": pr,
        "certificates": ce,
        "books": [b for b in books if b],
        "needs": [n for n in needs if n],
        "sector": s,
        "region": r,
        "tag": t
    }

def _q(id_key: str, name: str, cat: str, s_str: str, pr_str: str, ce_str: str, tag: str = "PVIA", nd_str: str = ""):
    skills = _parse_skills(s_str)
    pr = pr_str.split("|")
    ce = ce_str.split("|")
    _p(id_key, name, "", cat, skills, pr, ce, tag, nd_str)

# 1. Base Technology Roles
_p("dev", "Software Developer", "Build apps, websites and systems", "Technology and data", [
    ["Programming basics (Python, Java or JS)", 10, 40, "Variables, loops, functions, problem solving"],
    ["Git and GitHub", 6, 8, "Commit, branch, pull request, a public profile"],
    ["Data structures and algorithms", 14, 70, "Arrays, strings, hashing, trees, sorting, complexity"],
    ["SQL and databases", 9, 25, "Joins, indexes, design of tables"],
    ["Web basics (HTML, CSS, JavaScript)", 10, 40, "Build and host a responsive page"],
    ["Backend and APIs", 12, 40, "REST APIs with Node, Flask or Spring"],
    ["OOP and clean code", 8, 20, "Classes, design principles, readable code"],
    ["Testing and debugging", 6, 15, "Unit tests, reading errors, logging"],
    ["System design basics", 8, 25, "Scaling, caching, queues, trade-offs"],
    ["Cloud and deployment", 7, 20, "Deploy an app, basic Docker, CI"]
], [
    "Personal portfolio site, hosted live",
    "Task manager app with login and a database",
    "REST API with tests and documentation",
    "A full-stack project that solves a problem from your own field"
], [
    "Meta Back-End or Front-End Developer (Coursera)",
    "freeCodeCamp Responsive Web Design / JS Algorithms",
    "AWS Cloud Practitioner",
    "CS50 (Harvard, free)"
])

_p("an", "Data Analyst", "Turn data into decisions and dashboards", "Technology and data", [
    ["Excel / Google Sheets", 10, 20, "Formulas, pivot tables, lookups"],
    ["SQL", 14, 35, "Select, joins, group by, window functions"],
    ["Statistics basics", 11, 30, "Mean, spread, distributions, hypothesis tests"],
    ["Data cleaning", 8, 20, "Missing values, duplicates, formats"],
    ["Python with pandas", 10, 40, "Load, filter, group, merge, plot"],
    ["Data visualization (Power BI or Tableau)", 12, 30, "Charts that answer a question, interactive dashboards"],
    ["Business thinking", 9, 15, "KPIs, funnels, asking the right question"],
    ["Storytelling and communication", 8, 12, "Present findings to non-technical people"],
    ["Documentation and Git", 4, 8, "Keep your work reproducible"]
], [
    "Sales dashboard in Power BI or Tableau",
    "SQL analysis of a public dataset, written as a case study",
    "Cleaning and analysing a messy real dataset with pandas",
    "Analysis from your own field, such as marks, surveys or finance"
], [
    "Google Data Analytics Certificate",
    "Microsoft PL-300 (Power BI)",
    "IBM Data Analyst (Coursera)",
    "Kaggle micro-courses (free)"
])

_p("ds", "Data Scientist", "Build models that predict and explain", "Technology and data", [
    ["Python programming", 12, 40, "Functions, data types, libraries, notebooks"],
    ["Statistics and probability", 13, 45, "Distributions, inference, A/B testing"],
    ["Linear algebra and calculus basics", 7, 25, "Vectors, matrices, gradients"],
    ["SQL", 9, 25, "Querying and joining large tables"],
    ["Data wrangling (pandas, NumPy)", 10, 35, "Clean and shape messy data"],
    ["Machine learning algorithms", 14, 60, "Regression, trees, clustering, scikit-learn"],
    ["Model evaluation", 9, 20, "Cross-validation, metrics, overfitting"],
    ["Data visualization", 6, 15, "Matplotlib, Seaborn, clear charts"],
    ["Deep learning basics", 7, 45, "Neural networks with PyTorch or TensorFlow"],
    ["Deployment and MLOps basics", 5, 25, "Serve a model, track experiments"]
], [
    "Prediction project end to end, such as house prices or churn",
    "Kaggle competition entry with a write-up",
    "NLP or image classifier with a simple web demo",
    "Model built on data from your own field"
], [
    "Machine Learning Specialization (Andrew Ng)",
    "IBM Data Science Professional Certificate",
    "Google Advanced Data Analytics",
    "Kaggle Learn (free)"
])

# 2. Business & Management
_p("mkt", "Digital Marketing Executive", "Grow brands with content, ads and analytics", "Business and management", [
    ["Marketing fundamentals", 10, 20, "Segments, positioning, the 4 Ps"],
    ["Content and copywriting", 10, 30, "Posts, emails, landing pages"],
    ["Social media and SEO", 12, 35, "Organic reach, keywords, platforms"],
    ["Paid ads (Google, Meta)", 10, 25, "Budgets, targeting, A/B tests"],
    ["Analytics and reporting", 10, 25, "GA4, funnels, campaign reports"],
    ["Design basics (Canva)", 5, 10, "Clean creatives and presentations"]
], ["Run a 4-week social campaign for a local business", "Rank a blog for one keyword", "Campaign report with results"],
["Google Digital Garage", "Google Ads and Analytics certificates", "HubSpot Inbound Marketing"])

_p("hrx", "HR Executive", "Hire, onboard and support people", "Business and management", [
    ["HR fundamentals and labour law basics", 11, 25, "Hiring cycle, payroll basics, compliance"],
    ["Recruitment and interviewing", 12, 25, "Job posts, screening, structured interviews"],
    ["Communication and empathy", 10, 15, "Listening, feedback, conflict handling"],
    ["HR tools and Excel", 8, 20, "ATS, attendance, simple HR reports"],
    ["Training and engagement", 7, 15, "Onboarding plans, surveys"]
], ["Write a full job description and interview plan", "Design an onboarding checklist", "Mock interview panel with feedback forms"],
["SHRM or HRCI entry courses", "LinkedIn Learning HR basics"])

_p("sal", "Sales and Business Development", "Win customers and grow revenue", "Business and management", [
    ["Product and market knowledge", 9, 15, "Know customer problems and competitors"],
    ["Prospecting and lead generation", 11, 20, "Cold outreach, LinkedIn, referrals"],
    ["Pitching and negotiation", 12, 25, "Discovery calls, objections, closing"],
    ["CRM and tracking", 7, 10, "Pipeline stages, follow-ups"],
    ["Communication and resilience", 10, 15, "Clear speaking, handling rejection"]
], ["Role-play 10 sales calls and review them", "Build a 30-lead outreach list and track replies", "Create a one-page pitch for any product"],
["HubSpot Sales Software", "Salesforce Trailhead basics"])

_p("fin", "Accountant / Finance Analyst", "Manage books, budgets and financial reports", "Business and management", [
    ["Accounting principles", 12, 40, "Ledgers, balance sheet, P&L"],
    ["Excel and financial modelling", 12, 35, "Formulas, budgets, forecasts"],
    ["Taxation and compliance basics", 9, 25, "GST, income tax, filing rules"],
    ["Accounting software (Tally, QuickBooks)", 9, 20, "Entries, invoices, reconciliation"],
    ["Financial statement analysis", 9, 25, "Ratios, cash flow, trends"],
    ["Reporting and ethics", 5, 10, "Clear summaries, accuracy"]
], ["Maintain books for a small shop for one month", "Ratio analysis of two listed companies", "Build a 12-month budget model"],
["Tally Prime", "CA / CMA / CFA foundation levels", "Excel for finance courses"])

# 3. Government & Public Service
_p("ias", "Civil Services (IAS / State PSC)", "Serve in public administration", "Government and public service", [
    ["Polity and governance", 11, 80, "Constitution, institutions, schemes"],
    ["History, geography and environment", 11, 120, "NCERT first, then standard books"],
    ["Economy and current affairs", 11, 100, "Budget, survey, daily newspaper"],
    ["Optional subject", 10, 150, "Syllabus, past papers, notes"],
    ["Answer writing and essay", 12, 60, "Structure, examples, time limits"],
    ["Mock tests and revision", 10, 80, "Prelims series, error log"]
], ["Weekly answer writing with feedback", "Monthly current-affairs notes", "Full prelims mock every 2 weeks"],
["UPSC official syllabus and past papers", "NCERT books (6–12)"])

_p("bnk", "Bank / SSC Exams", "Clear competitive exams for banking and government jobs", "Government and public service", [
    ["Quantitative aptitude", 12, 60, "Arithmetic, data interpretation"],
    ["Reasoning", 12, 50, "Puzzles, seating, logic"],
    ["English language", 10, 40, "Grammar, reading comprehension"],
    ["General and financial awareness", 9, 40, "Banking terms, current affairs"],
    ["Speed and mock tests", 11, 50, "Timed tests, accuracy tracking"]
], ["One sectional test daily", "Full mock every weekend", "Error notebook"],
["IBPS, SBI and SSC official notifications and past papers"])

# 4. Science, Health & Education
_p("res", "Research Scientist", "Run experiments and publish findings", "Science, health and education", [
    ["Subject depth in your discipline", 12, 80, "Core theory and recent papers"],
    ["Research methods and statistics", 12, 40, "Design, sampling, tests"],
    ["Lab or field techniques", 10, 50, "Safe, repeatable procedures"],
    ["Scientific writing", 9, 25, "Papers, abstracts, citations"],
    ["Data tools (Excel, R or Python)", 8, 30, "Analyse and plot your data"]
], ["Literature review on one topic", "Small experiment with a written report", "Poster or paper submission"],
["NPTEL courses", "GATE / NET / CSIR as relevant"])

_p("tch", "Teacher / Lecturer", "Teach and mentor students", "Science, health and education", [
    ["Subject mastery", 12, 60, "Know it deeply and simply"],
    ["Lesson planning", 10, 20, "Objectives, activities, assessment"],
    ["Classroom communication", 11, 20, "Explaining, questioning, engagement"],
    ["Educational technology", 6, 15, "Slides, quizzes, online tools"],
    ["Eligibility exams (TET, NET, B.Ed)", 10, 60, "Syllabus and previous papers"]
], ["Record a 15-minute demo lesson", "Prepare a 4-week unit plan", "Tutor a small group and collect feedback"],
["B.Ed", "TET / CTET / NET", "Teaching courses on Coursera or SWAYAM"])

# 5. Creative & Media
_p("des", "Graphic / UI-UX Designer", "Design visuals and digital experiences", "Creative and media", [
    ["Design principles", 11, 25, "Layout, colour, type, hierarchy"],
    ["Design tools (Figma, Adobe)", 12, 40, "Frames, components, export"],
    ["User research and UX basics", 10, 25, "Interviews, flows, wireframes"],
    ["Prototyping", 9, 20, "Clickable flows and testing"],
    ["Portfolio and storytelling", 10, 25, "Case studies with process"]
], ["Redesign a poorly designed app screen", "Brand kit for a local business", "Three case studies in a portfolio site"],
["Google UX Design Certificate", "Figma tutorials"])

_p("wrt", "Content Writer / Journalist", "Research and write for audiences", "Creative and media", [
    ["Writing and editing", 12, 40, "Clarity, structure, grammar"],
    ["Research and fact-checking", 10, 25, "Sources, interviews, accuracy"],
    ["Storytelling and tone", 10, 25, "Hooks, angles, voice"],
    ["SEO and digital publishing", 8, 20, "Headlines, keywords, CMS"],
    ["Portfolio", 10, 20, "Published samples"]
], ["Publish 6 articles on a blog or Medium", "Interview a local professional and write the story", "Pitch an article to a publication"],
["Poynter or Coursera journalism courses", "HubSpot Content Marketing"])

# 6. Law
_p("law", "Lawyer / Legal Professional", "Advise, draft and argue legal matters", "Law", [
    ["Core legal subjects", 12, 100, "Constitutional, contract, criminal, civil law"],
    ["Legal research", 11, 30, "Case law databases and statutes"],
    ["Drafting", 11, 35, "Notices, contracts, petitions"],
    ["Advocacy and moot court", 10, 30, "Arguments, cross-examination"],
    ["Entrance and bar exams (CLAT, AIBE)", 9, 60, "Syllabus and past papers"]
], ["Moot court participation", "Draft five different agreements", "Case brief summaries every week"],
["CLAT / AILET", "AIBE", "Internship with an advocate"])

# 7. Core Engineering
_p("eng", "Core Engineer (Mech, Civil, Elec)", "Design, build and maintain physical systems", "Technology and data", [
    ["Core subject fundamentals", 12, 80, "Mechanics, materials, circuits, structures"],
    ["CAD and design tools", 11, 40, "AutoCAD, SolidWorks or similar"],
    ["Simulation and analysis", 9, 30, "ANSYS, MATLAB or equivalent"],
    ["Standards and safety", 8, 20, "Codes, quality, safe practice"],
    ["Hands-on projects and internship", 11, 60, "Build, test, document"]
], ["Design and model one component or structure", "Capstone with a test report", "Site or plant visit report"],
["GATE", "NPTEL core courses", "AutoCAD or SolidWorks certificate"])

# 8. Healthcare (H)
_q("doc", "Doctor (MBBS)", "Healthcare", "Pre-clinical subjects:Anatomy, physiology, biochemistry:90|Clinical subjects:Medicine, surgery, paediatrics, OB-GYN:120|Clinical skills and patient care:History, examination, procedures:60|Entrance and PG exams:NEET UG, then NEET PG:100|Communication and ethics:Consent, breaking news, empathy:20", "Shadow doctors in a hospital|Write up one case every week|Daily timed mock tests", "NEET UG|NEET PG|NMC guidelines")
_q("nur", "Nurse", "Healthcare", "Nursing fundamentals:Vitals, hygiene, medication safety:60|Clinical practice:Ward rotations, wound care, emergencies:80|Anatomy and pharmacology:Core science for care:50|Patient communication:Empathy, documentation, handover:20|Licensing exams:State nursing council, NCLEX or similar:60", "Practise skills in a simulation lab|Care plan for one patient case|Mock licensing test", "B.Sc Nursing or GNM|State nursing council registration|NCLEX-RN")
_q("pha", "Pharmacist", "Healthcare", "Pharmacology:Drug action, dosage, interactions:70|Dispensing and prescriptions:Reading, checking, labelling:30|Pharmaceutics and chemistry:Formulations and quality:60|Regulation and ethics:Drug laws, records:25|Patient counselling:Explain medicines clearly:20", "Mock dispensing practice|Medicine information leaflet for patients|Internship at a pharmacy", "D.Pharm or B.Pharm|State pharmacy council registration|GPAT")
_q("phy", "Physiotherapist", "Healthcare", "Anatomy and biomechanics:Muscles, joints, movement:60|Assessment skills:Posture, range, strength testing:40|Treatment techniques:Exercise therapy, manual therapy:60|Rehabilitation planning:Goals, progress tracking:30|Patient motivation:Communication and follow-up:15", "Design a 6-week rehab plan for a sample case|Clinical internship log|Community posture camp", "BPT|State council registration|Sports physiotherapy courses")
_q("psy", "Psychologist / Counsellor", "Healthcare", "Psychology theory:Development, cognition, abnormal psychology:80|Counselling skills:Active listening, rapport, boundaries:40|Assessment and testing:Standard tools and ethics:40|Research and statistics:Studies and reading data:35|Supervised practice:Internship with a licensed professional:80", "Role-play counselling sessions with feedback|Small survey study|Supervised internship", "BA/MA Psychology|M.Phil Clinical Psychology (RCI)|Counselling certificates")
_q("vet", "Veterinarian", "Healthcare", "Animal anatomy and physiology:All major species:90|Veterinary medicine and surgery:Diagnosis and treatment:100|Animal husbandry:Nutrition, breeding, welfare:40|Entrance exams:NEET or state tests, then licensing:80|Client communication:Owners and farmers:15", "Volunteer at an animal clinic|Case notes on common diseases|Vaccination awareness drive", "BVSc and AH|Veterinary Council registration")

# 9. Additional Tech Roles
_q("cyb", "Cybersecurity Analyst", "Technology and data", "Networking basics:TCP/IP, DNS, firewalls:40|Operating systems:Linux and Windows internals:40|Security fundamentals:Threats, encryption, access control:40|Ethical hacking and tools:Nmap, Wireshark, Burp:50|Incident response and logs:Detect and report issues:30", "Set up a home lab and scan it|Write a vulnerability report for a practice site|Capture-the-flag challenges", "CompTIA Security+|CEH|Google Cybersecurity Certificate")
_q("cld", "Cloud / DevOps Engineer", "Technology and data", "Linux and scripting:Shell, Python basics:40|Cloud platforms:AWS, Azure or GCP core services:50|Containers and Kubernetes:Docker, orchestration:40|CI/CD and Git:Automated build and deploy:30|Monitoring and infrastructure as code:Terraform, logs, alerts:35", "Deploy a web app on the cloud with CI/CD|Dockerise an existing project|Infrastructure as code for a small stack", "AWS Solutions Architect Associate|Azure Fundamentals|CKA")
_q("aim", "AI / ML Engineer", "Technology and data", "Python and maths:Linear algebra, probability, code:60|Machine learning:Models, training, evaluation:60|Deep learning:PyTorch or TensorFlow:50|Data pipelines:Clean, store, serve data:35|Deploying models:APIs, monitoring:30", "Image or text classifier with a web demo|Reproduce a published paper|Deploy a model behind an API", "Deep Learning Specialization|Google ML Engineer|Hugging Face courses")
_q("mob", "Mobile App Developer", "Technology and data", "Programming language:Kotlin, Swift or Dart:50|UI and layouts:Screens, navigation, design guidelines:35|Data and APIs:Networking, local storage:35|Publishing:Store listing and testing:15|Version control:Git workflows:10", "Habit tracker app|App using a public API|Publish one app to a store", "Meta Android Developer|Flutter tutorials|Apple Developer tutorials")
_q("gam", "Game Developer", "Technology and data", "Programming:C# or C++:50|Game engine (Unity or Unreal):Scenes, physics, UI:50|Game design:Loops, balance, feedback:30|Maths and physics for games:Vectors, collisions:30|Art and sound basics:Assets and tools:20", "2D platformer|Small multiplayer prototype|Game jam entry", "Unity Learn|Unreal Online Learning|GDC talks")
_q("qat", "QA / Test Engineer", "Technology and data", "Testing fundamentals:Test cases, bugs, severity:25|Manual and exploratory testing:Find real defects:30|Test automation:Selenium or Playwright:45|API testing:Postman, REST:25|Agile and tools:Jira, reporting:15", "Write a full test plan for a public website|Automate five user flows|Bug report portfolio", "ISTQB Foundation|Selenium courses")
_q("pdm", "Product Manager", "Technology and data", "User research:Interviews, problems, personas:30|Product strategy:Roadmaps, priorities, metrics:35|Working with teams:Requirements, stand-ups:20|Data and experiments:Funnels, A/B tests:30|Communication:Specs and stakeholder updates:20", "Write a product spec for an app you use|Teardown of a popular product|Prioritise a backlog using a framework", "Product School|Google or Reforge PM courses")
_q("net", "Network / Embedded Engineer", "Technology and data", "Electronics and circuits:Analog and digital:60|Embedded C and microcontrollers:Arduino, STM32:50|Protocols:I2C, SPI, TCP/IP:35|Debugging with instruments:Scope, logic analyser:25|Networking:Routing, switching:40", "Sensor data logger|Home automation with microcontrollers|Network lab with routing", "Cisco CCNA|Embedded systems courses")

# 10. Additional Business Roles
_q("ops", "Operations / Supply Chain Manager", "Business and management", "Process management:Workflows, bottlenecks:30|Inventory and procurement:Stock, suppliers, costs:35|Logistics and planning:Transport, scheduling:30|Data and Excel:Reports and forecasts:25|Leadership:Coordinate teams:20", "Map and improve one process|Inventory plan with Excel|Case study of a supply chain failure", "APICS CSCP|Six Sigma Green Belt|Supply chain courses")
_q("ent", "Entrepreneur / Startup Founder", "Business and management", "Problem and customer discovery:Talk to 20 users:30|Business model and finance:Costs, pricing, runway:35|Building the first product:Minimum version:50|Marketing and sales:First 10 customers:35|Resilience and networking:Mentors, peers:15", "Launch a minimum product in 6 weeks|Business plan with numbers|Pitch to a mentor panel", "Startup India resources|NPTEL entrepreneurship|Incubator programmes")
_q("pjm", "Project Manager", "Business and management", "Planning and scheduling:Scope, timeline, budget:30|Risk and quality:Plans for what can go wrong:25|Tools:Jira, MS Project, Excel:20|Stakeholder communication:Updates, meetings:20|Agile and Scrum:Sprints, retros:20", "Plan a real event or project end to end|Project charter and risk log|Run a sprint with a small team", "PMP or CAPM|Scrum Master|Google Project Management Certificate")
_q("con", "Management Consultant", "Business and management", "Structured problem solving:Issue trees, hypotheses:40|Case interviews:Market sizing, profitability:50|Excel and presentations:Models and slides:35|Industry knowledge:Read business news:30|Communication:Crisp, confident:20", "Practise 30 cases with a partner|Slide deck on a company problem|Market-sizing practice daily", "Case in Point book|Consulting club prep|CAT or GMAT for MBA")
_q("inb", "Investment / Equity Analyst", "Business and management", "Financial statements:Read and analyse:40|Valuation:DCF, multiples:45|Markets and economics:Rates, sectors, news:30|Excel modelling:Build models from scratch:40|Reports and ethics:Clear write-ups:20", "Valuation report on one listed company|Build a DCF model|Weekly market note", "CFA Level 1|NISM certifications|Financial modelling courses")
_q("cus", "Customer Support / Service", "Business and management", "Product knowledge:Know the product well:20|Communication:Clear, calm writing and speaking:25|Problem solving:Find root causes:20|Support tools:Ticketing, chat, CRM:15|Handling difficult customers:De-escalation:15", "Write 20 help-centre replies|Role-play angry customer calls|Build a FAQ", "Customer service courses|HubSpot Service Software")
_q("cs", "Company Secretary", "Business and management", "Company law:Companies Act, governance:70|Corporate compliance:Filings, meetings, records:50|Securities law:SEBI rules:40|Drafting:Minutes, resolutions:30|Exam preparation:CSEET, Executive, Professional:100", "Draft board resolutions and minutes|Compliance calendar for a company", "CSEET|ICSI CS course")
_q("evt", "Event Manager", "Business and management", "Planning and budgeting:Timeline, costs:30|Vendor and venue management:Negotiation, contracts:25|On-site coordination:Run the day smoothly:30|Marketing and promotion:Ticketing, social media:20|Teamwork and stress handling:Volunteers, backup plans:15", "Organise a college fest segment|Budget and run-of-show for a mock event", "Event management diplomas|Internship with an agency")

# 11. Government, Defense & Police
_q("def", "Defence Officer (NDA / CDS / AFCAT)", "Government and public service", "Written exam subjects:Maths, English, GK, reasoning:100|SSB interview preparation:Psychology tests, GD, interview:60|Physical fitness:Running, strength, endurance:80|Leadership and teamwork:Initiative and responsibility:30|Current affairs and awareness:Defence and world news:40", "Daily fitness log|Weekly mock SSB tasks|Timed written mock tests", "NDA|CDS|AFCAT official notifications")
_q("pol", "Police Officer", "Government and public service", "General knowledge and law basics:IPC or BNS, CrPC or BNSS:70|Reasoning and aptitude:Written test:50|Physical standards:Running, jumps, strength:80|Interview and communication:Clear and confident:30|Integrity and awareness:Ethics, current affairs:30", "Physical training schedule|Mock written tests|Interview practice", "State police recruitment notifications|UPSC CAPF")
_q("rly", "Railway / PSU Jobs", "Government and public service", "Maths and reasoning:RRB and PSU exams:80|General science and awareness:Basics:50|Technical subject (for engineers):GATE-style revision:100|Speed and accuracy:Mocks:50|Document and interview prep:Final stage:20", "Previous-year paper practice|Weekly full mocks", "RRB NTPC / JE|GATE for PSUs")

# 12. Creative, Arts & Design
_q("arc", "Architect", "Creative and media", "Design and drawing:Sketching, plans, elevations:60|CAD and 3D tools:AutoCAD, Revit, SketchUp:60|Structures and materials:How buildings stand:50|Building codes and sustainability:Rules and green design:30|Portfolio and presentation:Studio work:40", "Design a small house with full drawings|Site analysis and model|Portfolio of 4 projects", "NATA|Council of Architecture registration")
_q("int", "Interior Designer", "Creative and media", "Space planning:Layouts and flow:35|Colour, materials, lighting:Mood and function:30|Design software:SketchUp, AutoCAD, Photoshop:50|Client briefing and budgeting:Needs and cost control:25|Portfolio:Before and after projects:30", "Redesign a room with mood board and layout|3D render of a living space", "Interior design diploma|SketchUp and V-Ray courses")
_q("fas", "Fashion Designer", "Creative and media", "Sketching and design:Illustration, silhouettes:40|Fabric and garment construction:Pattern making, sewing:60|Trends and branding:Research and collections:30|Design software:Illustrator, CLO3D:30|Portfolio and styling:Mini collection:40", "Design and make a 5-piece mini collection|Trend board for one season", "NIFT / NID entrance|Fashion design diplomas")
_q("pho", "Photographer / Video Editor", "Creative and media", "Camera and lighting:Exposure, composition:40|Editing software:Lightroom, Premiere, DaVinci:50|Storytelling:Shots and sequence:30|Client work and business:Pricing, contracts:20|Portfolio and social presence:Show your best 12:25", "Photo series or short film|Edit a 2-minute story video|Shoot for a local business", "Adobe Certified Professional|Film school short courses")
_q("ani", "Animator / VFX Artist", "Creative and media", "Drawing and animation principles:Timing, weight, spacing:60|Software (Blender, Maya, After Effects):Core tools:60|Storyboarding and storytelling:Plan scenes:30|Modelling or compositing:Depending on path:50|Showreel:60-second best work:40", "30-second animated short|Character walk cycle|VFX shot breakdown", "Animation school courses|Blender Foundation tutorials")

# 13. Trades, Services & Hospitality
_q("chf", "Chef / Culinary Professional", "Trades, hospitality and services", "Cooking techniques:Knife skills, heat, sauces:80|Food safety and hygiene:HACCP basics:25|Menu planning and costing:Portions, margins:30|Kitchen operations:Station work, speed:60|Creativity and presentation:Plating, flavours:30", "Plan a 3-course menu with costing|Cook for 20 people|Kitchen internship", "Culinary diploma or hotel management|FSSAI food safety certificate")
_q("hot", "Hotel / Hospitality Manager", "Trades, hospitality and services", "Front office and guest service:Check-in, complaints:40|Food and beverage service:Restaurant operations:40|Housekeeping and facilities:Standards:30|Revenue and cost control:Rates and occupancy:30|Communication and grooming:Professional presence:20", "Hotel internship rotation|Guest-handling role-plays|Revenue report for a sample hotel", "BHM / IHM entrance (NCHMCT JEE)|Hospitality diplomas")
_q("pil", "Pilot / Aviation Professional", "Trades, hospitality and services", "Ground school theory:Aerodynamics, navigation, meteorology:150|Flight hours:Training and simulation:200|Regulations and safety:DGCA rules:40|Medical fitness:Class 1 medical:10|English and communication:Radio telephony:30", "Simulator practice|Weekly theory tests", "DGCA CPL|Class 1 medical|Flying school entrance")
_q("elt", "Electrician / Technician", "Trades, hospitality and services", "Electrical basics:Circuits, wiring, safety:50|Tools and installation:Panels, motors, appliances:60|Troubleshooting:Find and fix faults:40|Codes and safety:Earthing, standards:25|Customer handling:Quotes and trust:15", "Wire a practice board|Repair five faulty appliances", "ITI Electrician|NSDC skill certification|Wireman licence")
_q("agr", "Agriculture / Agri-entrepreneur", "Trades, hospitality and services", "Crop science:Soil, water, nutrition:60|Modern farming methods:Drip, protected cultivation:40|Marketing and pricing:Mandi, direct sales:30|Farm business and finance:Schemes, loans:30|Agri-tech tools:Sensors, drones, apps:20", "Plan one crop cycle with a budget|Farm visit report", "B.Sc Agriculture|ICAR AIEEA|Krishi Vigyan Kendra training")
_q("fit", "Fitness Coach / Sports Professional", "Trades, hospitality and services", "Exercise science:Muscles, energy, recovery:50|Programming:Training plans for goals:40|Nutrition basics:Food and performance:30|Coaching and motivation:Teach form, keep clients:25|Business and safety:Injury prevention, first aid:20", "Create 8-week plans for three clients|Coach a small group", "ACE or NASM|First aid and CPR|NIS Patiala courses")

# 14. Science, Policy & Environment
_q("swk", "Social Worker / NGO Professional", "Science, health and education", "Social issues and policy:Poverty, health, rights:50|Fieldwork and community engagement:Surveys, outreach:60|Programme planning and funding:Budgets, proposals:40|Counselling and communication:Listen, support:30|Monitoring and reporting:Impact measurement:30", "Community survey and report|Write a grant proposal|NGO internship", "MSW|TISS entrance|NGO fellowship programmes")
_q("eco", "Economist / Policy Analyst", "Science, health and education", "Micro and macro economics:Theory and policy:80|Statistics and econometrics:Regression, causality:60|Data tools:Excel, R or Stata:40|Policy reading and writing:Briefs, reports:40|Current economy tracking:Budget, RBI, trade data:30", "Policy brief on a current issue|Analyse a public economic dataset", "Economics MA entrance (DSE, JNU)|Indian Economic Service (UPSC)")
_q("env", "Environmental Scientist", "Science, health and education", "Ecology and environmental science:Systems, pollution, climate:70|Field and lab methods:Sampling, testing:50|GIS and data analysis:QGIS, Excel, R:50|Environmental law and impact assessment:EIA, regulations:40|Reports and communication:Findings for decision makers:30", "Local water or air quality study|GIS map of a local issue", "M.Sc Environmental Science|Indian Forest Service (UPSC)|GIS certificates")

# 15. Q2 Roles (Global & Specialized)
_q("ifs", "Diplomat (Indian Foreign Service)", "Government and public service", "International relations and history|Polity, economy and current affairs|A foreign language|Answer writing and interview", "Weekly current-affairs notes|Mock interview with a panel", "UPSC Civil Services Exam (IFS is chosen as a service)|Foreign language courses", "PIA", "Entry: a degree plus the UPSC Civil Services Exam, with age and attempt limits|Tools: NCERT and standard books, a test series|Also: check the current UPSC notification")
_q("jud", "Judge (Judicial Services)", "Government and public service", "Core laws (civil, criminal, evidence, contract)|Judgment writing|State judicial exam syllabus|Ethics and temperament", "Draft practice judgments|Timed mock papers", "State Judicial Services Exam|Judicial academy resources", "PI", "Entry: LL.B and enrolment as the state notice requires|Tools: bare acts, law reports, past papers|Also: age and experience rules differ by state")
_q("ifo", "Forest Officer", "Government and public service", "Ecology and forestry|Forest and wildlife law|Fitness and field skills|Exam preparation (UPSC IFoS or state)", "Field visit report|Weekly fitness log", "UPSC Indian Forest Service Exam|State forest service exams", "PI", "Entry: degree in science, agriculture, forestry or engineering for IFoS|Tools: maps, field kit, fitness training|Also: check UPSC and state forest notices")
_q("tax", "Income Tax / Revenue Officer", "Government and public service", "Tax law and accounts basics|Quantitative aptitude and reasoning|English and general awareness|Exam practice (SSC CGL or UPSC)", "Daily timed mocks|Notes on tax rules", "SSC CGL|UPSC Civil Services (IRS)", "PI", "Entry: graduation for SSC CGL, or UPSC for IRS|Tools: mock tests, past papers|Also: SSC and UPSC notices")
_q("isr", "Scientist (ISRO / DRDO / PSU labs)", "Government and public service", "Core engineering or science subject|Maths and problem solving|Research projects|Entrance exams (ICRB, GATE, CEPTAM)", "A research or design project|GATE mock tests", "GATE|ISRO and DRDO official recruitment pages", "PI", "Entry: B.E., B.Tech or M.Sc as per the notice|Tools: project work, GATE preparation|Also: read each official recruitment notice")
_q("jea", "Government Engineer (JE / AE)", "Government and public service", "Core branch subjects|Maths and reasoning|Drawings and codes|Exam practice (SSC JE, state PSC, GATE)", "Previous-year papers|One design project", "SSC JE|State PSC engineering exams", "PI", "Entry: diploma or B.E./B.Tech depending on the post|Tools: CAD software, past papers|Also: official notices")
_q("grc", "State Government Clerk / Group C", "Government and public service", "Quantitative aptitude and reasoning|English and the regional language|General awareness|Typing and computer skills", "Daily typing practice|Weekly mocks", "State Staff Selection exams|SSC CHSL", "PI", "Entry: 10th, 12th or graduation depending on the post|Tools: typing practice, mock tests|Also: state notifications")
_q("atc", "Air Traffic Controller", "Government and public service", "Maths and physics|English communication|Aviation basics|Recruitment exam and training", "Radio phraseology practice|Mock tests", "AAI recruitment exam|Aviation basics courses", "PIA", "Entry: B.Sc with physics and maths, or B.E./B.Tech, for AAI|Tools: mock tests|Also: medical fitness and training")
_q("ca", "Chartered Accountant (CA)", "Business and management", "Accounting and auditing|Taxation and law|Financial reporting and costing|ICAI exams and articleship", "Complete full mock papers|Audit a small firm’s books during articleship", "ICAI Foundation, Intermediate and Final|ICAI study material", "PVIA", "Entry: ICAI Foundation, Intermediate, Final and articleship|Tools: Excel, Tally, ICAI material|Also: ICAI membership")
_q("act", "Actuary", "Business and management", "Probability and statistics|Financial maths|Insurance and risk|Actuarial exams", "Pricing model in Excel|Mortality table analysis", "Institute and Faculty of Actuaries or IAI exams|Actuarial science courses", "PVIA", "Entry: strong maths, then actuarial exams|Tools: Excel, R or Python|Also: professional body membership")
_q("den", "Data Engineer", "Technology and data", "SQL and Python|Data pipelines (Airflow, Spark)|Cloud data tools|Data modelling", "Build an ETL pipeline|Data warehouse on a free cloud tier", "Google Cloud or AWS data certificates|Data Engineering Zoomcamp (free)", "PVIA", "Entry: CS or IT degree or equivalent skills|Tools: free cloud tiers, Docker, Spark|Also: GitHub projects")
_q("bsa", "Business Analyst (IT / Consulting)", "Business and management", "Requirements gathering|SQL and Excel|Process modelling|Documentation and communication", "Write a requirements document|Map a business process", "IIBA ECBA|Business analysis courses", "PVIA", "Entry: any degree, domain knowledge helps|Tools: Excel, SQL, Visio or Lucidchart, Jira|Also: sample documents")
_q("erp", "ERP / SAP Consultant", "Technology and data", "Business processes (finance, supply chain)|SAP or Oracle modules|Configuration and testing|Client communication", "Configure a sample process|Document a support case", "SAP Learning Hub free tier|SAP or Oracle certifications", "PVIA", "Entry: B.E., B.Com, MBA or MCA|Tools: a practice system or free learning access|Also: module certification")
_q("cre", "Content Creator", "Creative and media", "Niche and audience research|Video, audio and editing|Platform growth and analytics|Brand deals and income planning", "Publish 30 pieces in 30 days|Analyse your best three posts", "YouTube Creator Academy|Meta Blueprint", "VIA", "Entry: no fixed degree|Tools: phone or camera, editing app, a channel or profile|Also: consistency and a clear niche")
_q("rea", "Real Estate Professional", "Business and management", "Market knowledge and RERA basics|Sales and negotiation|Valuation basics|Customer relationships", "Market study of one locality|Mock property pitch", "RERA agent registration|Real estate courses", "VIA", "Entry: any degree, RERA registration for agents in India|Tools: CRM, listing portals|Also: a local network")
_q("ins", "Insurance Advisor", "Business and management", "Insurance products|Needs analysis and selling|Regulations|Customer trust", "Mock advisory meeting|Product comparison sheet", "IRDAI agent exam|Insurance Institute of India courses", "PVI", "Entry: 12th pass or degree, the IRDAI exam for agents|Tools: product brochures, CRM|Also: licence")
_q("cra", "Clinical Research Associate", "Healthcare", "Clinical trial basics (GCP)|Regulation and ethics|Documentation and monitoring|Life science knowledge", "Summarise a published trial|GCP practice quiz", "ICH-GCP training|Clinical research diplomas", "VIA", "Entry: B.Pharm, M.Pharm, life science or medical degree|Tools: GCP training, MS Office|Also: certification")
_q("bio", "Biotech / Pharma R&D Scientist", "Science, health and education", "Molecular biology and chemistry|Lab techniques|Data and statistics|Scientific writing", "Lab project with a report|Literature review", "GATE Life Sciences|CSIR NET", "PVIA", "Entry: M.Sc, M.Pharm or PhD|Tools: lab access, Excel or R|Also: publications")
_q("lab", "Medical Lab / Radiology Technologist", "Healthcare", "Lab techniques|Imaging basics|Quality and safety|Patient handling", "Practice sample handling|Safety checklist", "DMLT, BMLT or radiology diploma|State paramedical council registration", "PVIA", "Entry: DMLT, BMLT, B.Sc MLT or a radiology diploma|Tools: lab practice, safety gear|Also: council registration")
_q("hca", "Hospital Administrator", "Healthcare", "Healthcare systems|Finance and operations|Quality and accreditation (NABH)|People management", "Study one hospital’s workflow|Draft a quality checklist", "MHA or MBA Hospital Management|NABH awareness courses", "PVIA", "Entry: a degree plus MHA or MBA in hospital management|Tools: Excel, hospital software|Also: internships")
_q("trn", "Translator / Interpreter", "Creative and media", "Two or more languages|Subject expertise|Translation tools|Ethics and quality", "Translate a 1,000-word document|Interpret a mock meeting", "DELF, Goethe or JLPT certificates|Translation diplomas", "PVIA", "Entry: language degree or proof of fluency|Tools: translation tools, glossaries|Also: language certificates")
_q("cvl", "Civil Engineer", "Technology and data", "Structures and geotechnics|Surveying and CAD|Estimation and costing|Site management", "Design a small structure|Estimate a building’s cost", "GATE Civil|STAAD or Revit courses", "PVIA", "Entry: B.E. or B.Tech in Civil|Tools: AutoCAD, STAAD, Revit|Also: licences where required")
_q("usm", "Doctor Abroad (USMLE / PLAB)", "Healthcare", "Licensing exam preparation|Clinical knowledge|Language and communication|Visa and registration process", "Daily question-bank practice|Clinical electives abroad", "USMLE|PLAB (UK)", "PVA", "Entry: MBBS plus the licensing exams of the target country|Tools: question banks, official guides|Also: licensing and visa rules differ by country")
_q("nab", "Nurse Abroad (NCLEX / OET)", "Healthcare", "Licensing exam preparation|English test (OET or IELTS)|Clinical experience|Registration and visa process", "Practice exam questions daily|Document your clinical hours", "NCLEX-RN|OET or IELTS", "PVA", "Entry: nursing degree plus the target country’s licence exam|Tools: practice question banks, English test preparation|Also: registration and visa steps")
_q("itr", "International School Teacher", "Science, health and education", "Subject mastery|IB or Cambridge curriculum|Classroom management|Teaching qualification (PGCE or similar)", "Record a demo lesson|Plan a unit in the IB format", "PGCE or equivalent|IB teacher training", "VA", "Entry: degree plus a teaching qualification|Tools: lesson plans and a teaching portfolio|Also: visa and background checks")
_q("sfr", "Merchant Navy Officer", "Trades, hospitality and services", "Maritime subjects|Seamanship and safety (STCW)|Physical and medical fitness|Entrance exam and sponsorship", "STCW basic training|Fitness plan", "IMU-CET|STCW courses", "VA", "Entry: DNS, B.Sc Nautical Science or B.Tech Marine, via IMU-CET or company selection|Tools: STCW courses|Also: medical fitness and CDC")
_q("crw", "Cabin Crew", "Trades, hospitality and services", "Customer service and grooming|Safety and first aid|Language skills|Interview preparation", "Mock airline interview|First-aid course", "First-aid and CPR|Airline cabin crew training", "VIA", "Entry: 12th pass, airline height and fitness standards|Tools: grooming, fluent English|Also: check each airline’s notice")
_q("skl", "Skilled Trades (Welder, Plumber, Mechanic)", "Trades, hospitality and services", "Trade skills|Safety and tools|Reading drawings|Certification and trade tests", "Complete a practice project|Safety checklist", "ITI trade certificate|NSDC skill certification", "PVIA", "Entry: ITI or a trade course|Tools: trade tools, safety gear|Also: trade tests and certificates, which jobs abroad often require")
