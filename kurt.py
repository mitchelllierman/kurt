# Import Needed Libraries

from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os


# Read in the spreadsheet listing sites
bf_data = pd.read_excel('Site_assignments.xlsx')

# Read in Brownfield sites by their ID number
bf_id = bf_data['BFD#']
bf_name = bf_data['Name']


def search_Id(id, count=100):  # Completed
    cabinet_base = "https://ecm.idem.in.gov/cs/"
    oracle_pls = "idcplg?IdcService=GET_SEARCH_RESULTS&QueryText="
    query = f"%3cftx%3e{id}%3c%2fftx%3e"
    sort = "&SortField=xProgram"
    order = "&SortOrder=Desc"
    results = "&ResultCount=100"
    id_search = cabinet_base + oracle_pls + query + sort + order + results
    search_result = requests.get(id_search)

    return search_result


def extract_Data(search_result):

    extracted = {'link': [],
                 'date': [],
                 # YYYY_MM_DD -- requires PARSING
                 'program': [],
                 # Ex Brownfield
                 'doctype': []}
    # Ex Brownfield Completion Document

    # Load the HTML content
    soup = BeautifulSoup(search_result.text, 'html.parser')

    # Find the table
    table = soup.find('table', {'class': 'xuiListTable'})

    if table is None:
        return 1
    header_check = 0
    # Extract data from each row
    for row in table.find_all('tr'):
        cells = row.find_all('td')

        if header_check == 0:
            header_check += 1
            continue

        if len(cells) > 0:
            # Assuming the first column contains links
            loc = cells[0].find('a')['href']
            extracted['link'].append(loc)
            # Assuming the second column contains dates

            date_object = datetime.strptime(cells[2].text.strip(), "%m/%d/%Y")
            formatted_date = date_object.strftime("%Y_%m_%d")

            extracted['date'].append(formatted_date)
            # Assuming the third column contains programs
            extracted['program'].append(cells[4].text)
            # Assuming the fourth column contains document types
            extracted['doctype'].append(cells[6].text)
    # Page Handling
    return extracted


def save_PDFs(site_name, extracted):
    # Open Link
    # Download or Save as PDF

    for i, link in enumerate(extracted['link']):
        print(link)
        pdf = requests.get(link)
        if pdf.status_code == 200:
            date = extracted['date'][i]
            program = extracted['program'][i]
            doc = extracted['doctype'][i]

            # Save the PDF
            fname = f'bf_sites/{site_name}/{date}_{site_name}_{program}_{doc}.pdf'

            with open(fname, 'wb') as file:
                file.write(pdf.content)
        else:
            print(f"Failed to download PDF from {link}")

    # Implement saving pdf with this filename here:
    # curl -o downloaded_file.pdf "{fn[1]}"
    # While making PDF make a txt too?
    # PDF miner


def kurt_Loop(bf_id):
    os.mkdir('bf_sites')

    extraction_errors = []
    try:
        for ind, id in enumerate(bf_id):
            # Requests the data from IDEM digital file cabinet using requests
            search_result = search_Id(id)

            # Scrape the results pages.:with expression as target:
            extracted = extract_Data(search_result)
            if extracted == 1:
                extraction_errors.append(id)
                continue
            # Get PD frame with: # Link to PDF, Date of Doc, Program, Doc Type

            # Needs to be processed with regex
            site_name = re.sub(r"[()<>:\"/\\|?&#*. ]",  "_", bf_name[ind],)
            site_name = re.sub(r"\n*", "", site_name)

            os.mkdir(f'bf_sites/{site_name}')

            save_PDFs(site_name, extracted)
    finally:
        print("The following IDs returned no results:")
        print(extraction_errors)


kurt_Loop(bf_id)

'''
==================================================================
TODO:
    Implement PDF2txt
    Bonus functions for analysis?
    Error handling
        -Search results with no entries
        -Wait Time
        Test against known results w/ limited sample

DONE:
    Implement requests things ( X )
    Create GitHub repo for Kurt ( X )
    Implement PDF saving ( X )
================================================================== '''
