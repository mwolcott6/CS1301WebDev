import streamlit as st
import info
import pandas as pd

#About Me
def aboutMeSection():
    st.header("About Me")
    st.image(info.profile_picture, width = 200) #change link on info page
    st.write(info.about_me) #change on info page
    st.write('---')
aboutMeSection()

#Sidebar Links
def linksSection():
    st.sidebar.header("Links")
    st.sidebar.tex("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height = "75"></a>
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.tex("Check out my work")
    linkedin_link = f'<a href="{info.my_github_url}><img src="{info.github_image_url}" alt="Github" width="75" height = "75"></a>
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.tex("Or email me!")
    linkedin_link = f'<a href="mailto:{info.my_email_address}><img src="{info.email_image_url}" alt="Email" width="75" height = "75"></a>
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

linksSection()

#Education
def educationSection(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:**{education_data['Degree'}}")
    st.write(f"**Gradutation Date:**{education_data['Graduation Date'}}")
    st.write(f"**GPA:**{education_data['GPA'}}")
    st.write("**Relevant COursework:**")
    coursework= pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True
        )
    st.write("---")

educationSection(info.education_data, info.course_data)

#Profesional Experience

def experienceSection(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experienceSection(info.experience_data)


#Project

def projectSection(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander= st.expander(f"{project_name}")
        expander.write(project_description)
    st.write(---)
projectSection(info.projects_data)

#Skills

def skillsSection(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,"")}")
        st.progress(percentage)
    
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken, ""): {proficiency}}")
    st.write("---")
    
skillsSection(info.programming_data, info.spoken_data)

#Activities

def activitiesSection(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activty_data.items():
            expander = st.expander(f"{title}")
            for bullets in details:
                expander.write(bullet)
                
    st.write("---")

activitesSection(info.leadership_data, info.activity_data)

#add some fun icons later
