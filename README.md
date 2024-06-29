# Resume Analyzer Application

## Demo of the Project

### Opening Page
![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/d693d021-cbfb-4579-a488-318015051c15)

### Candidate Workflow

1. **Options for Candidate and Administrator**
   - Choose either the **Candidate** or **Administrator** option.
   - Example: Selecting the **Candidate** option.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/7913b30b-463d-4107-ad06-0ea30623d43b)

2. **Upload Resume**
   - Drag and drop PDF files for resume upload.
   - Example: Uploading `Sample.pdf`.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/7913b30b-463d-4107-ad06-0ea30623d43b)

3. **Input Job Description**
   - Enter the job description from any job portal.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/26ef2f48-c6c6-43c1-ae32-76b440639f0b)

4. **Resume Display**
   - The resume is displayed on the website for better understanding.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/9c8ea64b-28b0-4c65-b283-7e4dce11b1bf)

5. **Resume Analysis in Progress**
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/029dcb71-da30-47e3-9d79-81c895af155b)

6. **Display Basic Information and Resume Details**
   - Name, email, and contact details are displayed.
   - Resume pages are extracted, categorizing the writer as experienced (3 pages), intermediate (2 pages), or fresher (1 page).
   - Resume score is calculated using cosine similarity between the job description and the resume, using Pyresparser and PDFminer3 for text extraction.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/fabff800-9fca-4250-a108-ddb9537f8469)

7. **Skills and Recommendations**
   - Suggests industry-relevant skills.
   - Recommends certification programs from reputable websites like Coursera and Udemy for skill enhancement.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/d9264159-7e8a-432c-9712-423a43751b19)

8. **Display Resume Score**
   - Resume score is displayed, rounded to the nearest integer for clarity.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/f4c054f3-58a1-4e65-8528-3fe8aa0d155a)

### Administrator Workflow

1. **Administrator Login**
   - Provides login and password information.
   - Only @Admin can log in.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/e794c353-414a-4f18-8611-e891377b4130)

2. **View Organized Data**
   - Administrator can see the data organized by candidate resume scores.
   - Can edit and download reports in Excel format.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/76ba2f7d-15c2-43c7-9f9a-42167d8e16e5)

3. **Histogram of Resume Scores**
   - Displays resume scores in a histogram.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/9fa454be-8271-4674-a42c-d6deef0d5f70)

4. **Access to MySQL Database**
   - Shows data from the MySQL database including name, email, resume score, number of pages, predicted field, user experience, skills, timestamp, and recommended courses.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/f6a4ad3c-5f11-4dcd-8ea5-0451d1a31564)

5. **Download Data in Excel Format**
   - Recruiter can view and download the organized data in Excel format.
   ![image](https://github.com/Sushma0204/ResumeAnalyzer/assets/98072240/50c22ebc-e481-49a9-9afc-bea896d1abdc)
