import streamlit as st
import docx2txt
import json
import nltk
from PIL import Image
import spacy
nltk.download('stopwords')
spacy.load('en_core_web_sm')

import pandas as pd
import base64, random
import time, datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from streamlit_lottie import st_lottie
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io, random
from streamlit_tags import st_tags
from PIL import Image
import pymysql
from Courses import ds_course, web_course, android_course, ios_course, uiux_course
import pafy
import plotly.express as px

def get_table_download_link(df, filename, text):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()
    return text

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def course_recommender(course_list):
    st.subheader("**Courses & Certificates🎓 Recommendations**")
    c = 0
    rec_course = []
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 4)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course

connection = pymysql.connect(host='localhost', user='root', password='')
cursor = connection.cursor()

def insert_data(name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills,
                courses):
    DB_table_name = 'user_data'
    insert_sql = "insert into " + DB_table_name + """
    values (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    rec_values = (
    name, email, str(res_score), timestamp, str(no_of_pages), reco_field, cand_level, skills, recommended_skills,
    courses)
    cursor.execute(insert_sql, rec_values)
    connection.commit()

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon='./Logo/logo.jpg',
    layout="wide"
)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_hello = load_lottiefile("lottiefiles/hello.json")
lottie_analyze = load_lottiefile("lottiefiles/analyze.json")
lottie_upload = load_lottiefile("lottiefiles/upload.json")

c1, c2= st.columns((1, 2), gap="large")
st.write("")

with c1:

    st.title("Interview Questions for FRESHERS")
    st.markdown("Stay updated with the latest answers!")
    
    with st.expander("Tell me about yourself?" , expanded=True):
        st.markdown("Hello, my name is Rajesh, and I graduated from Xyz University. I majored in B.Tech Computer Science. I’ve always had a fascination with computers since I was a child, and my fascination with computers led me to want to learn new programming languages. I am well-versed in C programming, Java, data structures, and SQL. Along with these technical skills, I have strong communication skills that I believe are essential for this position. Our final year major project is a Surveillance Robot built with a Raspberry Pi microcontroller. We were a group of four, and we used our coding skills to make the project a success. I was a member of ISTE, or the Indian Society for Technical Education, a college club that organizes technical and non-technical events for all branches, where I discovered that I have excellent leadership skills. I’ve learned how to work well with others. I also have internship experience in this field and would like to use my skills to help your company grow while also improving my own.")
    
    with st.expander("Why are you interested in this position", expanded=True):
        st.markdown("I am interested in this position because it aligns with my career goals and aspirations. As a recent graduate in computer science, I have been looking for an opportunity to apply my skills and knowledge in a practical setting. I am impressed by the projects and achievements of your company, especially in the field of artificial intelligence and machine learning. I believe that working for your company would provide me with valuable experience and exposure to the latest technologies and innovations in the industry.Additionally, I am interested in this position because it matches my skills and qualifications. I have a strong background in programming languages such as Python, Java, and C++, as well as frameworks such as TensorFlow, PyTorch, and Keras. I have also completed several projects and courses related to artificial intelligence and machine learning, such as building a chatbot, a face recognition system, and a sentiment analysis model. I have a keen interest in learning new things and solving challenging problems. I think that I can bring a fresh perspective and a creative approach to your team.")
    
    with st.expander("What are your biggest strenghts and weakness", expanded=True):
        st.markdown("Strengths: One of my biggest strengths is my communication skills. I can express myself clearly and confidently, both verbally and in writing. I have experience in giving presentations, writing reports, and collaborating with different teams. I also have strong analytical skills. I enjoy solving problems, finding patterns, and making data-driven decisions. I have used various tools and methods to analyze data, such as Excel, Python, and statistics. I have applied these skills in various projects and internships, such as [briefly describe an example]. Weaknesses: One of my weaknesses is that I sometimes struggle with delegating tasks. I tend to take on too much responsibility and try to do everything myself, which can lead to stress and burnout. I am working on improving this by learning to trust others and communicating my expectations clearly. I have also started to use time management tools to prioritize and organize my tasks better. I have noticed that this has helped me to be more efficient and productive, as well as more collaborative and supportive of my teammates.")
        
    with st.expander("What are your salary expectations?", expanded=True):
        st.markdown("Thank you for asking me this question. I understand that salary is an important factor to consider when hiring a new employee. Based on my research and my experience as a fresher in the field of computer science, I would expect a salary range of Rs. 4 to 6 lakhs per annum for this role. However, I am flexible and willing to negotiate depending on the overall compensation package, the scope of the role, and the opportunities for learning and growth within the company. I am very interested in working for your company and I believe that I have the skills and qualifications to excel in this position. Could you please tell me what is the salary range that you have in mind for this role?")
        
    with st.expander("Why do you want to work for this company?", expanded=True):
        st.markdown("Hello, my name is Aisha Sharma, and I appreciate the opportunity to discuss my interest in joining Google. As a recent graduate in Computer Science from the University of California, Berkeley, I have been meticulously exploring potential employers, and Google stands out for several compelling reasons. Presently, I am equipped with a strong foundation in Computer Science and a passion for machine learning. In my academic journey, I have developed a keen interest in natural language processing (NLP) and computer vision, which align with Google’s innovative approach in these fields. Looking into the past, I’ve been particularly impressed by Google’s commitment to artificial intelligence research and its development of groundbreaking technologies like TensorFlow. Your emphasis on empowering people with information resonates with my professional aspirations, and I am eager to contribute to and grow with a company that shares these principles. Considering the future, I am excited about the prospect of contributing my skills and fresh perspectives to Google’s AI for Social Good initiatives. I am drawn to the potential for learning and development that Google offers, and I believe that my enthusiasm for machine learning development aligns seamlessly with the goals and values of your organization.")
        
    with st.expander("Why should we hire you?", expanded=True):
        st.markdown("I believe that you should hire me because I have the skills, qualifications, and experience that you are looking for in this role. I have a bachelor’s degree in computer science . I have also completed several online courses and projects related to HTML, CSS, JavaScript, and React. I have learned a lot from these courses and projects, and I have applied my skills and knowledge in a real-world setting as a web developer intern at ABC Tech Solutions. During my internship, I was responsible for designing, developing, and maintaining various web applications for different clients and industries. I used my coding skills and creativity to create user-friendly, responsive, and functional websites that met the clients’ specifications and expectations. I also used my communication and collaboration skills to work effectively with my team members and supervisors. I received positive feedback from both my clients and my mentors on my performance and deliverables.")
    
    with st.expander("What are your technical skills and how do you stay updated?", expanded=True):
        st.markdown("Sure, I have a solid foundation in programming languages like HTML, CSS, JavaScript, along with knowledge in front-end frameworks like React and Angular, and experience with tools like Git, GitHub, and WordPress. During my academic journey in Computer Science, I’ve gained a strong understanding of core technical principles like web development methodologies, database management, and security best practices. To stay updated, I regularly engage in online learning through platforms like Coursera and Udemy, exploring tutorials and participating in forums like Stack Overflow. I stay hands-on by working on personal projects like building responsive single-page applications and applying the latest technologies like TypeScript and progressive web apps (PWAs). Networking on LinkedIn and attending webinars help me learn from industry experts like frontendmasters.com.")
        
    with st.expander("How do you handle criticism or feedback?", expanded=True):
        st.markdown("I see feedback as a chance to grow. When I get criticism, I listen, stay open-minded, and focus on learning from it. I take proactive steps to improve, whether through more research or seeking guidance. I actively ask for feedback, considering it a valuable tool for my development.")
        
    with st.expander("Are you comfortable working independently and taking initiative?", expanded=True):
        st.markdown("Yes, I am comfortable working independently and taking initiative. Throughout my academic journey and personal projects, I’ve developed a proactive approach to tasks. I enjoy taking ownership of my work, setting goals, and ensuring deadlines are met. I believe that being self-motivated and taking initiative are essential qualities that contribute to both personal and team success.")

    with st.expander("Will you be able to work overtime and even relocate if we ask you to?", expanded=True):
        st.markdown("Yes. For the right opportunity, I am definitely willing to relocate. I believe that this position and company is an opportunity to improve myself. I’m also willing to work overtime whenever such circumstances will arrive as good things do not come easily in life, and I know I will have to sacrifice something for my professional success. Staying overtime, or even working on Saturday at times, does not seem like a big sacrifice to me, considering everything I can gain in your company.")

    with st.expander("How would you prioritize your workload if you were faced with multiple deadlines?", expanded=True):
        st.markdown("When faced with multiple deadlines, I prioritize by urgency and impact. First, I tackle urgent and critical tasks that directly affect overall goals. Next, I schedule important but less urgent tasks with room for flexibility. Clear communication with my team helps adjust priorities as needed, ensuring quality work on time.")
    
    with st.expander("How would you approach a task that required you to learn a new skill quickly?", expanded=True):
        st.markdown("During my web dev internship, I had to learn a new framework React for a project on a tight deadline. I started by breaking down the learning into smaller steps, focusing on core functionalities first. I used online tutorials, documentation, and even reached out to more experienced developers for help. I practiced by building small test projects before integrating it into the main one. This helped me learn quickly and apply it effectively, delivering the project on time. This experience showed me the importance of being a fast learner, resourceful, and not afraid to ask for help when needed.")

st.markdown(
    """
    <style>
    .c1-container {
        background-color: #f0f0f0; /* Light gray background */
        padding: 20px; /* Add some padding for spacing */
        border: 2px solid #e0e0e0; /* Light gray border */
        height: 100vh; /* Set height to 100% of viewport height */
        overflow-y: auto; /* Add vertical scrollbar if content exceeds viewport height */
    }
    .stExpander > .stExpanderSummary > .stExpanderIcon > div > svg {
        fill: #000; /* Change the expander icon color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def calculate_similarity(text1, text2):
    content = [text1, text2]
    cv = CountVectorizer()
    matrix = cv.fit_transform(content)
    similarity_matrix = cosine_similarity(matrix)
    return similarity_matrix[1][0]



with c2:
    def run():
        
        st.title("Welcome to our Resume Analyzer!!")
        st_lottie(
            lottie_hello,
            speed = 1,
            reverse = False,
            quality = "medium",
            height = None,
            width = None,
            key = None,
        )
        st.text("Unlock the secrets of your resume's tech prowess with our cutting-edge app!")
        st.text(" Discover where you stand in industry-level tech skills and rankings. ")
        st.text("Ready to level up?")
        st.text("Upload your resume now and kickstart your journey!")

        activities = ["🤵Candidate", "📋Administrator"]
        choice = st.selectbox("Choose among the given  options:", activities)

        db_sql = """CREATE DATABASE IF NOT EXISTS RESUME;"""
        cursor.execute(db_sql)
        connection.select_db("resume")

        DB_table_name = 'user_data'
        table_sql = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                        (ID INT NOT NULL AUTO_INCREMENT,
                         Name varchar(100) NOT NULL,
                         Email_ID VARCHAR(50) NOT NULL,
                         resume_score VARCHAR(8) NOT NULL,
                         Timestamp VARCHAR(50) NOT NULL,
                         Page_no VARCHAR(5) NOT NULL,
                         Predicted_Field VARCHAR(25) NOT NULL,
                         User_level VARCHAR(30) NOT NULL,
                         Actual_skills VARCHAR(300) NOT NULL,
                         Recommended_skills VARCHAR(300) NOT NULL,
                         Recommended_courses VARCHAR(600) NOT NULL,
                         PRIMARY KEY (ID));
                        """
        cursor.execute(table_sql)
        if choice == '🤵Candidate':

            pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
            job_description = st.text_area("Enter Job Description", height=200)
            st_lottie(
                    lottie_upload,
                    speed = 1,
                    reverse = False,
                    quality = "medium",
                    height = None,
                    width = None,
                    key = None,
                    )
            if pdf_file is not None and job_description:
                
                save_image_path = './Uploaded_Resumes/' + pdf_file.name
                with open(save_image_path, "wb") as f:
                    f.write(pdf_file.getbuffer())
                show_pdf(save_image_path)
                resume_data = ResumeParser(save_image_path).get_extracted_data()
                if resume_data:
                    
                    resume_text = pdf_reader(save_image_path)

                    st.header("**Resume Analysis**")
                    st_lottie(
                        lottie_analyze,
                        speed = 1,
                        reverse = False,
                        quality = "medium",
                        height = None,
                        width = None,
                        key = None,
                    )

                    st.subheader("**Basic Personal Detalils📃:**")
                    try:
                        st.text('Name: ' + resume_data['name'])
                        st.text('Email: ' + resume_data['email'])
                        st.text('Contact: ' + resume_data['mobile_number'])
                        st.text('Resume pages: ' + str(resume_data['no_of_pages']))
                    except:
                        pass
                    cand_level = ''
                    
                    similarity = calculate_similarity(job_description, resume_text)
                    st.write("Similarity between job description and resume:", str(similarity * 100) + '%')


                    if resume_data['no_of_pages'] == 1:
                        cand_level = "Fresher"
                        st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>You are looking Fresher.</h4>''',
                                    unsafe_allow_html=True)
                    elif resume_data['no_of_pages'] == 2:
                        cand_level = "Intermediate"
                        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>You are at intermediate level!</h4>''',
                                    unsafe_allow_html=True)
                    elif resume_data['no_of_pages'] >= 3:
                        cand_level = "Experienced"
                        st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at experience level!''',
                                    unsafe_allow_html=True)

                    st.subheader("**Recommending skills based upon your resume📚✏️:**")
                    
                    keywords = st_tags(label='### Skills that you have',
                                       text='See our skills recommendation',
                                       value=resume_data['skills'], key='1')

                    
                    ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep Learning', 'flask',
                                  'streamlit']
                    web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                                   'javascript', 'angular js', 'c#', 'flask']
                    android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy']
                    ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
                    uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes',
                                    'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator',
                                    'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro',
                                    'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp',
                                    'user research', 'user experience']

                    recommended_skills = []
                    reco_field = ''
                    rec_course = ''
                    
                    for i in resume_data['skills']:
                        
                        if i.lower() in ds_keyword:
                            print(i.lower())
                            reco_field = 'Data Science'
                            st.success("Based on our analysis, it appears you're interested in opportunities related to Data Science Jobs.")
                            recommended_skills = ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling',
                                                  'Data Mining', 'Clustering & Classification', 'Data Analytics',
                                                  'Quantitative Analysis', 'Web Scraping', 'ML Algorithms', 'Keras',
                                                  'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', "Flask",
                                                  'Streamlit']
                            recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                           text='Recommended skills generated from System',
                                                           value=recommended_skills, key='2')
                            
                            rec_course = course_recommender(ds_course)
                            break

                        ## Web development recommendation
                        elif i.lower() in web_keyword:
                            print(i.lower())
                            reco_field = 'Web Development'
                            st.success("Based on our analysis, it appears you're interested in opportunities related to Web Development Jobs")
                            recommended_skills = ['React', 'Django', 'Node JS', 'React JS', 'php', 'laravel', 'Magento',
                                                  'wordpress', 'Javascript', 'Angular JS', 'c#', 'Flask', 'SDK']
                            recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                           text='Recommended skills generated from System',
                                                           value=recommended_skills, key='3')
                            st.markdown(
                                '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                                unsafe_allow_html=True)
                            rec_course = course_recommender(web_course)
                            break

                        ## Android App Development
                        elif i.lower() in android_keyword:
                            print(i.lower())
                            reco_field = 'Android Development'
                            st.success("Based on our analysis, it appears you're interested in opportunities related to Android app development.")
                            recommended_skills = ['Android', 'Android development', 'Flutter', 'Kotlin', 'XML', 'Java',
                                                  'Kivy', 'GIT', 'SDK', 'SQLite']
                            recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                           text='Recommended skills generated from System',
                                                           value=recommended_skills, key='4')
                            st.markdown(
                                '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                                unsafe_allow_html=True)
                            rec_course = course_recommender(android_course)
                            break

                        ## IOS App Development
                        elif i.lower() in ios_keyword:
                            print(i.lower())
                            reco_field = 'IOS Development'
                            st.success("Based on our analysis, it appears you're interested in opportunities related toIOS App Development Jobs")
                            recommended_skills = ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode',
                                                  'Objective-C', 'SQLite', 'Plist', 'StoreKit', "UI-Kit", 'AV Foundation',
                                                  'Auto-Layout']
                            recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                           text='Recommended skills generated from System',
                                                           value=recommended_skills, key='5')
                            st.markdown(
                                '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                                unsafe_allow_html=True)
                            rec_course = course_recommender(ios_course)
                            break

                        ## Ui-UX Recommendation
                        elif i.lower() in uiux_keyword:
                            print(i.lower())
                            reco_field = 'UI-UX Development'
                            st.success("Based on our analysis, it appears you're interested in opportunities related to UI-UX Development Jobs ")
                            recommended_skills = ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq',
                                                  'Prototyping', 'Wireframes', 'Storyframes', 'Adobe Photoshop', 'Editing',
                                                  'Illustrator', 'After Effects', 'Premier Pro', 'Indesign', 'Wireframe',
                                                  'Solid', 'Grasp', 'User Research']
                            recommended_keywords = st_tags(label='### Recommended skills for you.',
                                                           text='Recommended skills generated from System',
                                                           value=recommended_skills, key='6')
                            st.markdown(
                                '''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',
                                unsafe_allow_html=True)
                            rec_course = course_recommender(uiux_course)
                            break

                    
                    
                    ts = time.time()
                    cur_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    cur_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    timestamp = str(cur_date + '_' + cur_time)

                    
                    st.subheader("**Resume Tips & Ideas💡**")
                    resume_score = str(similarity * 100)
                    

                    st.subheader("**Resume Score📝**")
                    st.markdown(
                        """
                        <style>
                            .stProgress > div > div > div > div {
                                background-color: #d73b5c;
                            }
                        </style>""",
                        unsafe_allow_html=True,
                    )
                    resume_score_float = float(resume_score)
                    my_bar = st.progress(0)
                    score = 0
                    for percent_complete in range(round(resume_score_float)):
                        score += 1
                        time.sleep(0.1)
                        my_bar.progress(percent_complete + 1)
                    st.write(
                        "Your resume score is determined by comparing the information you've included in your resume with the requirements outlined in the job description. The closer the match between your qualifications and the job requirements, the higher your resume score will be.")
                    st.success('Your Resume Writing Score: ' + str(score))
                    st.balloons()

                    insert_data(resume_data['name'], resume_data['email'], str(resume_score), timestamp,
                                str(resume_data['no_of_pages']), reco_field, cand_level, str(resume_data['skills']),
                                str(recommended_skills), str(rec_course))

                    connection.commit()
                else:
                    st.error('Something went wrong..')
        else:
            ## Admin Side
            
            ad_user = st.text_input("Username")
            ad_password = st.text_input("Password", type='password')
            if st.button('Login'):
                if ad_user == 'Sushma0204' and ad_password == 'Sushma0204':
                    st.success("Analyze the user's data with our Application - @Admin!")
                    
                    cursor.execute('''SELECT*FROM user_data''')
                    data = cursor.fetchall()
                   
                    df = pd.DataFrame(data, columns=['ID', 'Name', 'Email', 'resume_score_float', 'Timestamp', 'Total Page',
                                                     'Predicted Field', 'User Level', 'Actual Skills', 'Recommended_skills', 'Recommended_courses'])
                    
                    df_sorted = df.sort_values(by='resume_score_float', ascending=False)
        
                    st.header("**Sorted User's👨‍💻 Data by Resume Score**")
                    st.dataframe(df_sorted)
                    st.markdown(get_table_download_link(df_sorted, 'Sorted_User_Data.csv', 'Download Sorted Report'), unsafe_allow_html=True)
                
                    query = 'select * from user_data;'
                    plot_data = pd.read_sql(query, connection)

                    
                    fig2 = px.histogram(plot_data, x='resume_score', title='Resume Score Distribution')
                    st.plotly_chart(fig2, use_container_width=True)

                else:
                    st.error('Invalid Username or Password')
    run()
