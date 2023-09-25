import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the Excel file
input_file = "C:/Users/vikra/OneDrive/Desktop/New folder/Input.xlsx"
output_folder = "C:/Users/vikra/OneDrive/Desktop/New folder/output"


# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Load the Excel file into a DataFrame
df = pd.read_excel(input_file)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the article title and text
        article_title = soup.find('title').text
        article_text = ' '.join([p.text for p in soup.find_all('p')])

        # Create a text file with the URL_ID as the filename and write the title and text
        filename = os.path.join(output_folder, f'{url_id}.txt')
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'Title: {article_title}\n\n')
            file.write(f'{article_text}')

        print(f'Saved article with URL_ID {url_id} to {filename}')
    else:
        print(f'Failed to retrieve article with URL_ID {url_id} from {url}')

print('Extraction and saving complete.')
