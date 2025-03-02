import asyncio
from app.services.helpers.MultiFileAccessor import MultiFileAccessor
from app.services.helpers.LLMAccessor import LLMAccessor

from app.utils.StringToJson import StringToJson
from app.services.helpers.SetDataDB import SetDataDB

class AllAccessor:
    async def get_cv_data_json_format(self, files):
        """
        Process multiple CV files and return their data in JSON format.
        """
        # Extract text from the PDF files
        multi_file_accessor = MultiFileAccessor(files)
        cv_text = await multi_file_accessor.convert_to_text()  # Await the async method

        # Prepare the prompt for the LLM
        llm_accessor = LLMAccessor()

        # Generate JSON data using the LLM
        response = llm_accessor.generate_text(cv_text)  # Await the async method
        
        # self.set_data_db(response)

        return response

    def set_data_db(self, data):
        # Convert the input string to JSON
        string_to_json = StringToJson(data)
        json_data = string_to_json.to_json()

        # Insert the data into the database
        set_data_db = SetDataDB()
        set_data_db.process_json_data(json_data)

# Example usage
if __name__ == '__main__':
    async def main():
        all_accessor = AllAccessor()
        files_path = [
            'D:\\carrier\\project\\parsing-cvs\\backend\\app\\resources\\CVToTest.pdf', 
            'D:\\carrier\\project\\parsing-cvs\\backend\\app\\resources\\ZAKARIA_LABIAD_CV.pdf'
        ]
        result = await all_accessor.get_cv_data_json_format(files_path)  # Await the coroutine
        print(result)

    asyncio.run(main())