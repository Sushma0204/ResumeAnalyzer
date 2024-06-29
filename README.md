# RESUME ANALYZER APPLICATION

Demo of the project:
1. The Resume Analyser application's opening page
 ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/d693d021-cbfb-4579-a488-318015051c15)

CANDIDATE:
2. There are two options available in the illustration below. 
  (a) Candidate (b) Administrator
  We can now drag & drop files here in PDF format after choosing the Candidate option. I'm choosing Sample.pdf here.
  ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/7913b30b-463d-4107-ad06-0ea30623d43b)

3.We may now input the job description provided on any Job portal.
  ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/26ef2f48-c6c6-43c1-ae32-76b440639f0b)

4. The resume is now shown on the website for better understanding.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/9c8ea64b-28b0-4c65-b283-7e4dce11b1bf)

5. The analysis of resumes is currently in progress
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/029dcb71-da30-47e3-9d79-81c895af155b)

6. Name, email, and contact details are now all displayed for basic personal information. I have also extracted resume pages with this.
   We can determine whether this resume writer is experienced (3 pages), intermediate (2 pages), or fresher (1 page) based on its contents. 
  After parsing the resume and extracting the text using Pyresparser and PDFminer3, I was able to calculate the resume score using cosine similarity between the job description and the resume.
  ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/fabff800-9fca-4250-a108-ddb9537f8469)

7. I have now suggested a few abilities that are in line with industry trends based on the resume. 
  Additionally, if the candidate is interested in honing their abilities from home, they can complete certification programmes from reputable websites like Coursera, Udemy, and many more.
  ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/d9264159-7e8a-432c-9712-423a43751b19)

8. In order to provide a clear idea of a candidate's talents to both recruiters and job seekers, the resume score is now displayed at the end by rounding to the nearest interest.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/f4c054f3-58a1-4e65-8528-3fe8aa0d155a)


ADMINISTRATOR:
9. We can now see what Recruiter can see if we choose the Administrator option. In this area, I've included login and password information. On the ADMINSTRATOR side, only the @Admin can log in.
  ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/e794c353-414a-4f18-8611-e891377b4130)

10. The administrator may see how the user's data has been organised according to the candidate's resume score. He has the ability to edit and download the report in Excel format.
    ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/76ba2f7d-15c2-43c7-9f9a-42167d8e16e5)

11. Recruiter can see the score in a histogram after receiving the resume score.
    ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/9fa454be-8271-4674-a42c-d6deef0d5f70)

12. A recruiter has access to the MySQL database's data. Name, email address, resume score, number of pages, predicted field, user experience,
    skills listed in resume, and timestamp (the time the resume was uploaded) are all visible to him. The system-recommended courses and skills (scale up to 0–10)
    ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/f6a4ad3c-5f11-4dcd-8ea5-0451d1a31564)

13. The recruiter can view the data that was downloaded in Excel format.
    ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/50c22ebc-e481-49a9-9afc-bea896d1abdc)













