import aiohttp  # For asynchronous HTTP requests
import asyncio

class LLMAccessor:
    def __init__(self):
        self.API_KEY = "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"
        self.API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
        self.headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }

    def truncate_text(self, text, max_tokens=512):
        """
        Truncate the input text to ensure it does not exceed the model's token limit.
        This is a simple approximation and may not be as accurate as using a tokenizer.
        1 token ~ 4 characters
        """
        max_chars = max_tokens * 4
        if len(text) > max_chars:
            truncated_text = text[:max_chars]
            print(f"Input truncated to {max_tokens} tokens (approx {max_chars} characters).")
            return truncated_text
        return text

    async def generate_text(self, text):
        """
        Generate text using the Hugging Face API asynchronously.
        """
        # Truncate the input text to avoid exceeding the token limit
        truncated_text = self.truncate_text(text)

        # Send the query to the Hugging Face API
        payload = {
            "inputs": text,
            "parameters": {
                "max_length": 512  # Adjust max_length as needed
            }
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.API_URL, headers=self.headers, json=payload) as response:
                    if response.status == 200:
                        return await response.json()  # Return the JSON response
                    else:
                        print(f"HTTP error occurred: {response.status} - {response.reason}")
                        print(f"Response content: {await response.text()}")
                        return {"error": f"HTTP error {response.status}", "response": await response.text()}
            except Exception as e:
                print(f"An error occurred: {e}")
                return {"error": str(e)}


# Test block
if __name__ == "__main__":
    async def main():
        llm_accessor = LLMAccessor()
        llm_accessor.text = """
        Before processing the data, handle any errors in the text, such as merged words, typos, or formatting issues, to ensure accurate extraction.

        ### Instructions for Handling Errors:
        1. Fix merged words (e.g., "atThe" → "at The", "builtlongstanding" → "built longstanding").
        2. Correct typos (e.g., "ashleygill2023@gotmail.com" → "ashleygill2023@gmail.com").
        3. Remove artifacts (e.g., "Skills_based_CV.qxd 5/8/11 3:55 pm Page 1").
        4. Ensure proper spacing and formatting (e.g., "AudigestS.A." → "Audigest S.A.").
        5. Preserve the structure and context of the CV while cleaning the text.

        Extract the following information from the CV below and return the data in JSON format:
        {
            "name": "Full name of the candidate",
            "email": "Email address of the candidate",
            "phone": "Phone number of the candidate",
            "education": [
                {
                    "institution": "Name of the educational institution",
                    "degree": "Degree obtained",
                    "field_of_study": "Field of study",
                    "start_date": "Start date of the education (YYYY-MM-DD)",
                    "end_date": "End date of the education (YYYY-MM-DD)"
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
                    "proficiency": "Proficiency level (e.g., Beginner, Intermediate, Expert)"
                }
            ],
            "languages": [
                {
                    "language": "Name of the language",
                    "proficiency": "Proficiency level (e.g., Basic, Intermediate, Fluent, Native)"
                }
            ]
        }

        Here is the CV text:
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
        response = await llm_accessor.generate_text(llm_accessor.text)
        print(response)

    asyncio.run(main())