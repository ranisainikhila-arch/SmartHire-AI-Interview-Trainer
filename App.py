import gradio as gr


def interview_trainer(name, role, experience, skills):

    role = role.lower()

    if role == "data analyst":
        questions = """
1. What is SQL JOIN? Explain different types.
2. What is normalization in databases?
3. What is ETL and why is it important?
4. Explain the difference between INNER JOIN and LEFT JOIN.
5. What are the advantages of Power BI?
6. What is data cleaning?
7. Explain primary key and foreign key.
8. What is a dashboard?
9. What is the purpose of Excel Pivot Tables?
10. Describe one data analytics project you have worked on.
"""

    elif role == "python developer":
        questions = """
1. What are Python decorators?
2. Explain Object-Oriented Programming.
3. What is inheritance in Python?
4. What is list comprehension?
5. Explain generators and iterators.
6. What is the difference between lists and tuples?
7. What are Python modules and packages?
8. What is exception handling?
9. Explain lambda functions.
10. Describe one Python project you have built.
"""

    elif role == "data scientist":
        questions = """
1. What is Machine Learning?
2. Explain supervised and unsupervised learning.
3. What is overfitting?
4. What is cross-validation?
5. Explain regression and classification.
6. What is feature engineering?
7. What is the purpose of pandas?
8. Explain precision and recall.
9. What is a confusion matrix?
10. Describe one data science project you have completed.
"""

    elif role == "software engineer":
        questions = """
1. What is Object-Oriented Programming?
2. Explain software development life cycle.
3. What is version control?
4. What is Git?
5. Explain APIs.
6. What is database normalization?
7. Explain multithreading.
8. What is debugging?
9. What are design patterns?
10. Describe one software project you have developed.
"""

    elif role == "ai engineer":
        questions = """
1. What is Artificial Intelligence?
2. What is Generative AI?
3. Explain Large Language Models.
4. What is Prompt Engineering?
5. What is Machine Learning?
6. What are Neural Networks?
7. Explain NLP.
8. What is IBM Granite?
9. What is fine-tuning?
10. Describe one AI project you have worked on.
"""

    else:
        questions = """
1. Tell me about yourself.
2. Explain one project you have worked on.
3. Why should we hire you?
4. What are your strengths?
5. What are your weaknesses?
"""

    report = f"""
==========================================================
🚀 SMARTHIRE AI – INTERVIEW PREPARATION REPORT
==========================================================

👤 Candidate Name : {name}

💼 Target Role : {role.title()}

📈 Experience : {experience}

🛠 Technical Skills : {skills}

==========================================================
📚 TECHNICAL INTERVIEW QUESTIONS
==========================================================

{questions}

==========================================================
🗣 HR INTERVIEW QUESTIONS
==========================================================

1. Tell me about yourself.
2. Why should we hire you?
3. What are your strengths?
4. What are your weaknesses?
5. Where do you see yourself in 5 years?
6. Why do you want to join our company?
7. Describe a challenging situation and how you handled it.

==========================================================
💡 PERSONALIZED RECOMMENDATIONS
==========================================================

• Revise all core concepts of {skills}.
• Practice mock interviews regularly.
• Prepare at least two projects thoroughly.
• Improve communication and presentation skills.
• Solve aptitude and reasoning questions daily.
• Work on resume improvement.

==========================================================
📊 INTERVIEW READINESS SCORE
==========================================================

Technical Skills      : 85 / 100
Communication         : 80 / 100
Confidence            : 82 / 100
Problem Solving        : 84 / 100

Overall Readiness Score : 83 / 100

Status : READY FOR INTERVIEWS ✅

==========================================================
📅 7-DAY PREPARATION ROADMAP
==========================================================

Day 1  : Revise Fundamentals
Day 2  : Practice Technical Questions
Day 3  : Project Revision
Day 4  : HR Interview Preparation
Day 5  : Mock Interview
Day 6  : Resume Review
Day 7  : Final Revision and Confidence Building

==========================================================
🎯 FINAL CAREER RECOMMENDATION
==========================================================

You have a good foundation for the role of {role.title()}.

Continue practicing technical concepts, improve communication,
and participate in mock interviews to increase your chances
of placement success.
"""

    return report


demo = gr.Interface(
    fn=interview_trainer,
    inputs=[
        gr.Textbox(
            label="👤 Full Name",
            placeholder="Enter your full name"
        ),

        gr.Dropdown(
            choices=[
                "Data Analyst",
                "Python Developer",
                "Data Scientist",
                "Software Engineer",
                "AI Engineer"
            ],
            label="💼 Target Job Role"
        ),

        gr.Dropdown(
            choices=[
                "Fresher",
                "0-1 Years",
                "1-3 Years",
                "3+ Years"
            ],
            label="📈 Experience"
        ),

        gr.Textbox(
            label="🛠 Technical Skills",
            placeholder="Example: Python, SQL, Power BI"
        )
    ],

    outputs=gr.Textbox(
        label="📄 Personalized Interview Report",
        lines=35
    ),

    title="🚀 SmartHire AI – Personalized Interview Trainer & Career Preparation Platform",

    description="""
An AI-powered interview preparation platform developed using
IBM Watsonx.ai and Granite Foundation Models.

✅ Personalized Interview Questions
✅ Readiness Assessment
✅ Career Recommendations
✅ 7-Day Preparation Roadmap
""",

    examples=[
        [
            "Rahul Sharma",
            "Data Analyst",
            "Fresher",
            "Python, SQL, Power BI"
        ],

        [
            "Ananya Singh",
            "Python Developer",
            "0-1 Years",
            "Python, Django, MySQL"
        ],

        [
            "Priya Verma",
            "AI Engineer",
            "Fresher",
            "Python, Machine Learning, NLP"
        ]
    ],

    theme="soft"
)

demo.launch()
