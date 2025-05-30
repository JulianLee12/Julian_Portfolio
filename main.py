import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import smtplib
from email.message import EmailMessage
st.set_page_config(page_title="My App", layout="wide")

EMAIL_ADDRESS=st.secrets["EMAIL_USER"]
EMAIL_PASSWORD=st.secrets["EMAIL_PASS"]

def send_email(name,user_email,user_message):
    msg = EmailMessage()
    msg["Subject"] ="Streamlit Message"
    msg["From"] = EMAIL_ADDRESS
    msg["Reply-To"] = user_email
    msg["To"] = EMAIL_ADDRESS



    msg.set_content(f"{name} has sent {user_message}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Header
st.title(" Julian Portfolio")

tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "💻 Projects", "🙋 About", "📬 Contact"])

with tab1:
    st.header("Welcome to my portfolio")
    st.write("Welcome to my portfolio")

with tab2:
    tab01,tab02,tab03 = st.tabs(["English Projects","STEM Projects","Coding Projects"])
    with tab01:
        st.title("🏅 Sci Fi Short Story")
        st.markdown("Description")

        col1, col2 = st.columns([3, 2])  # Two-column Layout (3:2 ratio)

        with col1:
            st.markdown("### 📖 Sci Fi Short Story Live Preview")
            pdf_viewer("Story.pdf", width=700, height=500)  # Adjust width/height as needed

        with col2:
            st.markdown("### 📥 Download Story")
            with open("Story.pdf", "rb") as file:
                st.download_button(
                    label="⬇️ Download PDF",
                    data=file,
                    file_name="STEMcraft_Certificate.pdf",
                    mime="application/pdf"
                )

            st.markdown("---")

        st.markdown("---")

with tab02:
    st.write("s")
with tab03:
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("### 🐍 Python Pet Simulator")
        st.markdown(
            "An educational Unity-based game that teaches kids Python by interacting with a virtual pet. Players feed their pet by writing real Python code that determines how happy it becomes!")

        st.markdown("#### 🧩 Sample Code:")
        EXAMPLECODE = """def feed(pet, food):
        if food in ["apple", "banana", "carrot"]:
            pet.happiness += 10
        else:
            pet.happiness -= 5"""
    st.code(EXAMPLECODE, language='python')

    with col2:
        st.image(""
                 "Stjl.png", caption="Screenshot of Python Pet Simulator", use_container_width=True)

        st.markdown("### 🔗 Project Repository")
    if st.button("🐱 See Project on GitHub"):
        st.markdown("[View on GitHub](https://github.com/JulianLee12)", unsafe_allow_html=True)

    # Optional divider
    st.markdown("---")
with tab3:
    st.header("About Me")
    st.write("Hi! My name is Julian Lee, and I am 11 years old. I am passionate about a variety of activities that help me learn and have fun. One of my favorite subjects is math because I enjoy solving problems and exploring new concepts. I also love coding, which allows me to create my own programs and understand how computers work—it’s like solving puzzles in a different way! Besides academics, I am a big fan of sports. I enjoy playing basketball because I like teamwork and trying to improve my skills on the court. Golf is another sport I enjoy, as it helps me stay focused and disciplined while having a relaxing time outdoors. In my free time, I like to challenge myself with new projects, whether it’s a coding project or practicing my basketball shots. I believe that trying new things and staying curious helps me grow and have fun every day. I’m excited to keep learning, playing, and exploring new interests in the future!")

with tab4:
    st.header("Get in Touch")
    st.write("Email, social links, etc.")
    with st.form('Contact Me'):
        a = st.text_input('Name')
        b = st.text_input('Email Address')
        c = st.text_area('#Optional# Message')
        submit = st.form_submit_button('Send')



    if submit:
        st.success("Sent")
        send_email(a,b,c)
        st.write("I will get back to you as soon as I can.")
        # col2.title(f'{a + b+c:.2f}')

