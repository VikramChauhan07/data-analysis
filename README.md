# data-analysis
1. Download and the files
2. After downloading all the files save them in a folder
3. Open extract.py file in VS code and download all the necessary packages
4. This Python script is designed to extract and save the titles and text content of web pages listed in an Excel file. Here's a shorter overview of how to use it:

    1. Make sure you have the required libraries installed:
   - `os`: Standard library for operating system-related operations.
   - `pandas`: Library for data manipulation and analysis.
   - `requests`: Library for sending HTTP GET requests.
   - `BeautifulSoup` from `bs4`: Library for parsing HTML content.
    2. Specify the input Excel file path (`input_file`) and the output folder where you want to save the extracted data (`output_folder`).
    3. Ensure that the output folder exists; if not, the script will create it.
    4. Load the Excel file into a DataFrame, assuming it contains at least two columns: 'URL_ID' and 'URL'.
    5. Loop through each row in the DataFrame:
   - Extract the 'URL_ID' and 'URL' from the current row.
   - Send an HTTP GET request to the 'URL'.
   - If the request is successful (status code 200):
     - Parse the HTML content of the page.
     - Extract the title and text content.
     - Create a text file in the output folder with the 'URL_ID' as the filename and write the title and text content.
     - Print a message indicating that the article was saved.
     - If the request fails (status code other than 200), print a failure message.
   6. After processing all rows in the Excel file, the script will print "Extraction and saving complete."

   Here's a step-by-step breakdown:
   - Ensure you have the necessary libraries installed.
   - Specify input and output paths.
   - Run the script, and it will process the URLs listed in the Excel file, saving the extracted content in the specified output folder.
   Make sure you have installed the required libraries using `pip install pandas requests beautifulsoup4` before running the script. 
5. All the text file will get saved in the folder name output
6. After this open analysis.py file in VS code and download all the necessary packages
7. This Python script performs text analysis on a set of text files located in a specified folder and saves the analysis results to an Excel file. Here's a shorter overview of how to use it:
   1. Make sure you have the required libraries installed:
   - `nltk`: Natural Language Toolkit for text processing.
   - `pandas`: Library for data manipulation and analysis.
   2. Define the functions for text analysis, including functions for cleaning text, calculating scores, readability metrics, and more.
   3. Specify the directory containing the text files you want to analyze (`folder_path`).
   4. Initialize an empty list (`results_list`) to store the analysis results.
   5. Specify the folder containing stopwords (`stop_words_folder`) and load stopwords from the files in that folder.
   6. Load positive and negative words from the specified files (`positive-words.txt` and `negative-words.txt`).
   7. Loop through each text file in the specified folder:
   - Read the content of the text file.
   - Calculate various text analysis metrics using the defined functions.
   - Store the results in a dictionary (`result_dict`).
   8. Append each `result_dict` to the `results_list` for each text file.
   9. Create a DataFrame (`output_data`) to store all the results.
   10. Save the output DataFrame to an Excel file (`Output Data Structure.xlsx`).
    Make sure you have installed the required libraries using `pip install nltk pandas` before running the script. Additionally, ensure that you have the necessary text files for stopwords, positive words, and negative words in the specified folders.
    To use the script, you can simply modify the `folder_path`, `stop_words_folder`, and filenames for positive and negative words as needed. Then, execute the script, and it will analyze the text files in the specified folder and generate an Excel file with the analysis results. 
8.The data will be analysis according to the parameters in the readme file , the data will get saved in  a excel file named output data structure
