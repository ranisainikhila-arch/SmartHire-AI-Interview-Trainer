import gradio as gr

def interview_trainer(name, role, experience, skills):

    if role.lower() == "data analyst":
        questions = """
1. What is SQL JOIN?
2. Explain normalization.
3. What is Power BI?
4. What is ETL?
"""
    elif role.lower() == "python developer":
        questions = """
1. What are decorators?
2. Explain OOP.
3. What is list comprehension?
4. What are generators?
"""
    else:
        questions = """
1. Tell me about yourself.
2. Explain one of your projects.
3. Why should we hire you?
"""

    report = f"""
SMARTHIRE AI - INTERVIEW REPORT

Candidate Name: {name}
Target Role: {role}
Experience: {experience}
Skills: {skills}

TECHNICAL QUESTIONS
{questions}

HR QUESTIONS
1. Tell me about yourself.
2. Why should we hire you?
3. What are your strengths?
4. Where do you see yourself in 5 years?

RECOMMENDATIONS
• Revise fundamentals.
• Practice mock interviews.
• Improve communication skills.
• Build projects.

INTERVIEW READINESS SCORE
85%

7-DAY PREPARATION PLAN
Day 1 - Fundamentals
Day 2 - Projects
Day 3 - Coding
Day 4 - HR Preparation
Day 5 - Mock Interview
Day 6 - Resume Review
Day 7 - Final Revision
"""

    return report


demo = gr.Interface(
    fn=interview_trainer,
    inputs=[
        gr.Textbox(label="Candidate Name"),
        gr.Textbox(label="Target Job Role"),
        gr.Textbox(label="Experience"),
        gr.Textbox(label="Skills")
    ],
    outputs=gr.Textbox(label="Interview Report", lines=25),
    title="SmartHire AI - Personalized Interview Trainer",
    description="AI-powered Interview Preparation Platform using IBM Watsonx.ai and Granite Models."
)

demo.launch(share=True)
