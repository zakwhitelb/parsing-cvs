from groq import Groq

class LLMAccessor:
    def __init__(self):
        # Initialize the Groq client with your API key
        self.client = Groq(api_key="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")

    def generate_text(self, text):
        try:
            # Generate text using the Groq API
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": """
                        ### Enhanced Instructions for Error Handling and Data Extraction:

Error Handling Before Processing Data:

Fix Merged Words:

Correct any merged words to restore proper spacing (e.g., "atThe" → "at The", "builtlongstanding" → "built longstanding").

Correct Typos:

Fix spelling and grammatical errors to ensure accuracy (e.g., "ashleygill2023@gotmail.com" → "ashleygill2023@gmail.com").

Remove Artifacts:

Eliminate irrelevant artifacts, headers, footers, and page markers (e.g., "Skills_based_CV.qxd 5/8/11 3:55 pm Page 1").

Ensure Proper Formatting:

Standardize spacing and formatting for better readability (e.g., "AudigestS.A." → "Audigest S.A.").

Preserve Context:

Ensure the original structure and meaning of the CV remain intact while cleaning the text.

Fix Date Formatting Issues:

Convert all date formats to YYYY-MM-DD. If only a year is available, use YYYY-01-01 as a placeholder.

Extract Additional Information:

Include missing details such as addresses, referees, voluntary experiences, and interests when present.

Data Extraction Instructions:

Extract the following information from the CV and return it in JSON format.

Use the exact wording from the CV unless correcting errors based on the instructions above.

If a field is missing or unclear in the CV, leave it as null or provide a reasonable default.

Ensure all sections are populated where relevant, including education, work experience, skills, languages, and additional details.

Enhanced JSON Structure:

{
    "name": "Full name of the candidate",
    "email": "Email address of the candidate",
    "phone": "Phone number of the candidate",
    "address": "Full mailing address if available",
    "education": [
        {
            "institution": "Name of the educational institution",
            "degree": "Degree obtained",
            "field_of_study": "Field of study",
            "start_date": "Start date of the education (YYYY-MM-DD)",
            "end_date": "End date of the education (YYYY-MM-DD)",
            "study_abroad": "Details of study abroad experience if applicable",
            "modules": ["Relevant module 1", "Relevant module 2"]
        }
    ],
    "work_experience": [
        {
            "company": "Name of the company",
            "position": "Job title or position held",
            "start_date": "Start date of the job (YYYY-MM-DD)",
            "end_date": "End date of the job (YYYY-MM-DD)",
            "description": "Description of the role and responsibilities"
        }
    ],
    "skills": [
        {
            "skill_name": "Name of the skill",
            "proficiency": "Proficiency level (e.g., Beginner, Intermediate, Expert)",
            "examples": "Examples of how the skill was demonstrated"
        }
    ],
    "languages": [
        {
            "language": "Name of the language",
            "proficiency": "Proficiency level (e.g., Basic, Intermediate, Fluent, Native)"
        }
    ],
    "voluntary_experience": [
        {
            "organization": "Organization name",
            "role": "Role performed",
            "start_date": "YYYY-MM-DD",
            "end_date": "YYYY-MM-DD",
            "description": "Description of experience"
        }
    ],
    "interests": [
        "Interest 1", "Interest 2"
    ],
    "referees": [
        {
            "name": "Referee's name",
            "position": "Referee's position",
            "company": "Company/Institution",
            "contact_email": "Email address",
            "contact_phone": "Phone number"
        }
    ]
}

Additional Enhancements:

Ensure all relevant work experience details are captured, including responsibilities and promotions.

Include voluntary experience and interests, as these provide additional insight into the candidate's profile.

Extract referees' details where available.

Provide structured proficiency levels for skills, along with relevant examples.




### Enhanced Instructions for Error Handling and Data Extraction:

Error Handling Before Processing Data:

Fix Merged Words:

Correct any merged words to restore proper spacing (e.g., "atThe" → "at The", "builtlongstanding" → "built longstanding").

Correct Typos:

Fix spelling and grammatical errors to ensure accuracy (e.g., "ashleygill2023@gotmail.com" → "ashleygill2023@gmail.com").

Remove Artifacts:

Eliminate irrelevant artifacts, headers, footers, and page markers (e.g., "Skills_based_CV.qxd 5/8/11 3:55 pm Page 1").

Ensure Proper Formatting:

Standardize spacing and formatting for better readability (e.g., "AudigestS.A." → "Audigest S.A.").

Preserve Context:

Ensure the original structure and meaning of the CV remain intact while cleaning the text.

Fix Date Formatting Issues:

Convert all date formats to YYYY-MM-DD. If only a year is available, use YYYY-01-01 as a placeholder.

Extract Additional Information:

Include missing details such as addresses, referees, voluntary experiences, and interests when present.

Data Extraction Instructions:

Extract the following information from the CV and return it in JSON format.

Use the exact wording from the CV unless correcting errors based on the instructions above.

If a field is missing or unclear in the CV, leave it as null or provide a reasonable default.

If something have 2 values or more add it on this format:
"XXXX":
        {
            "XXXX_1": "XXXX",
            "XXXX_2": "XXXX",
        }
if there is just one value :
"XXXX": "..."

Ensure all sections are populated where relevant, including education, work experience, skills, languages, and additional details.

Enhanced JSON Structure:

{
    "name": "Full name of the candidate",
    "email": "Email address of the candidate",
    "phone": "Phone number of the candidate",
    "address": "Full mailing address if available",
    "education": [
        {
            "institution": "Name of the educational institution",
            "degree": "Degree obtained",
            "field_of_study": "Field of study",
            "start_date": "Start date of the education (YYYY-MM-DD)",
            "end_date": "End date of the education (YYYY-MM-DD)",
            "study_abroad": "Details of study abroad experience if applicable",
            "modules": ["Relevant module 1", "Relevant module 2"]
        }
    ],
    "work_experience": [
        {
            "company": "Name of the company",
            "position": "Job title or position held",
            "start_date": "Start date of the job (YYYY-MM-DD)",
            "end_date": "End date of the job (YYYY-MM-DD)",
            "description": "Description of the role and responsibilities"
        }
    ],
    "skills": [
        {
            "skill_name": "Name of the skill",
            "proficiency": "Proficiency level (e.g., Beginner, Intermediate, Expert)",
            "examples": "Examples of how the skill was demonstrated"
        }
    ],
    "languages": [
        {
            "language": "Name of the language",
            "proficiency": "Proficiency level (e.g., Basic, Intermediate, Fluent, Native)"
        }
    ],
    "voluntary_experience": [
        {
            "organization": "Organization name",
            "role": "Role performed",
            "start_date": "YYYY-MM-DD",
            "end_date": "YYYY-MM-DD",
            "description": "Description of experience"
        }
    ],
    "interests": [
        "Interest 1", "Interest 2"
    ],
    "referees": [
        {
            "name": "Referee's name",
            "position": "Referee's position",
            "company": "Company/Institution",
            "contact_email": "Email address",
            "contact_phone": "Phone number"
        }
    ]
}

Additional Enhancements:

Ensure all relevant work experience details are captured, including responsibilities and promotions.

Include voluntary experience and interests, as these provide additional insight into the candidate's profile.

Extract referees' details where available.

Provide structured proficiency levels for skills, along with relevant examples.

Ensure multiple values are stored in sub-keys (e.g., phone numbers, modules, etc.).

By following these enhanced instructions, we ensure the extracted JSON is as complete and accurate as possible, covering all relevant details from the CV.
                        """
                    },
                    {
                        "role": "user",
                        "content": text,
                    }
                ],
                model="llama-3.3-70b-versatile",  # Use a valid Groq model name
                temperature=0.5,
                max_tokens=2048,
                top_p=1,
                stop=None,
                stream=False,
            )

            # Return the generated text
            return chat_completion.choices[0].message.content

        except Exception as e:
            # Handle any errors that occur during the API call
            return f"An error occurred: {str(e)}"

# Test block
if __name__ == "__main__":
    llm_accessor = LLMAccessor()
    text = """
    File id : 1
    CV name : CVToTest.pdf
    Skills_based_CV.qxd 5/8/11 3:55 pm Page 1
    Example of a skills-based CV
    ASHLEY GILL
    3 Lappage Court Telephone: 01882 652349
    Tyler Green, Bucks. Mobile: 07717 121824
    HP8 4JD Email: ashleygill2023@gotmail.com
    Personal Details
    Summary
    • Business studies with Spanish undergraduate.
    • Ability to speak French and Spanish.
    • Extensive business experience including an internship with Top Choice Holidays.
    Education And Qualifications
    2008 – present Buckinghamshire Edge University
    BA International Business Studies with Spanish (expected 2:1)
    Relate your degree to • Study semester atThe University of Valloid (Spain).
    the job by listing your • Six-month work placementin Madrid.
    relevantmodules/ • Relevantmodules included: Business Planning; Sales Promotion and
    dissertation. Marketing; and Business Operations Management.
    2000 – 2007 Freebridge School
    A-Levels: Business Studies (B), French (C)
    8 GCSEs including Maths, English, Spanish and French
    Work History
    2008 – 2011 Buckinghamshire Edge University - Librarian/tour guide
    • General administrative and customer service roles. Briefly list
    your relevant
    2011 (Feb–Aug) AudigestS.A. (Madrid) – AuditAssistant duties.
    • Six months’work experience in an international bank.
    • Liaising with colleagues and clients in English and Spanish.
    2010 (June–Dec) Finsbury’s supermarket(Hazelbridge) – Supervisor
    • Managing a small team.
    • Customer service in a busy competitive environment.
    2010 (Jan–Aug) Top Choice Holidays and Flights Ltd (Low Wycombe)
    Financial Assistant/Supervisor
    • Working in a range of teams to manage complex financial processes.
    2007 (Jul–Aug) Dogs Protection League – General Assistant
    • Dealing with enquiries and selling packages to a range of clients.
    2006 (Jan–Dec) McHenry’s Restaurant(Low Wycombe) – Supervisor
    Voluntary Experience
    2007/2011 Teaching English in Mexico/Spain
    Interests
    Active member of University Business Club– Winner of the ‘Bucks BestBusiness Pitch’award in 2010 Enterprise
    week, judged by Michael Eavis.Skills_based_CV.qxd 5/8/11 3:55 pm Page 2
    Make sure you carefully assess
    Skills And Achievements the job advert/job description
    and address all the skills they
    Effective communication require.
    • Able to communicate effectively with a wide range of clients and colleagues, by showing interest, carefully
    listening to needs and appropriately adjusting my message, as demonstrated during my time atFinsbury’s
    Supermarket.
    • Strong presentation skills and confidence demonstrated by experience of delivering presentations in different
    languages to groups of five to fifty.
    Customer service
    • Ability to quickly build rapportwith customers and calmly deal with any problems as shown during my retail
    experience in high pressure environments.
    • Capacity to maintain professional relationships through email and other written correspondence, for example,
    atAudigestin Madrid, where I builtlongstanding business relationships with customers and colleagues across
    the globe.
    Teamwork
    • AtTop Choice Holidays demonstrated excellentteamwork skills in a busy financial environment, such as an
    ability to listen to clients and managers, perform my role to a high level and supportcolleagues, resulting in
    promotion.
    Administration Prove you have each of the
    • Excellentability to plan ahead and manage time effectively, for example, skills required by outlining
    where you performed them
    managing complex roles during my internship atTop Choice Holidays.
    and how you performed
    • Gathered data from a wide range of sources during my dissertation
    them well.
    whilstbalancing my other studies and two jobs, resulting in a 73% grade.
    Experience of travellers’needs
    • Recenttravel consultancy experience gives me an in-depth understanding of the expectations of holiday
    customers and the competitive nature of the industry.
    • International travel experience and language ability give me an empathy with travellers and a passion for
    helping them find a unique holiday experience.
    Initiative
    • Self-funding an evening course in bookkeeping during my firstaccountancy role demonstrated my ability to
    plan ahead and take control of my career.
    • Successful study and work in Spain and Mexico show thatI can creatively develop my skills and experience and
    adaptto new and differentenvironments.
    Sales knowledge
    • Wide experience of financial roles gives me an awareness of the tightmonetary pressures which drive UK
    service industries.
    • Raised sales atThe Dogs Protection League by 12% by up selling add-on packages to new and existing
    customers.
    Language ability
    • Spanish fluency obtained working overseas, French - semi-fluent.
    Include all your referee details including their email and
    Referees
    phone number (butask for their permission first).
    Professional:Mr. Jose Andreas, ManagementAccountant, Audigest, Avenida de Concha Espina 2, Madrid, ES-
    28036, +34 91 398 5476, j.andreas@audigest.es
    Academic:Dr. Jane Luffle, Personal Tutor, Buckinghamshire Edge University, Due Road, Low Wycombe, Bucks,
    HD15 3DL, 01628 435 6784, j.luffle@bedge.ac.uk
    """
    response = llm_accessor.generate_text(text)
    print(response)