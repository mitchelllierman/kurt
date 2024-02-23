# Import Needed Libraries

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os


# Read in the spreadsheet listing sites
bf_data = pd.read_excel("Site_assignments.xlsx",)

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
                 # Ex https://ecm.idem.in.gov/cs/idcplg?IdcService=GET_FILE&dID=4080205&dDocName=63984694&Rendition=web&allowInterrupt=1&noSaveAs=1
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

    # Extract data from each row
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 0:
            # Assuming the first column contains links
            extracted['link'].append(cells[0].find('a')['href'])
            # Assuming the second column contains dates
            extracted['date'].append(cells[1].text)
            # Assuming the third column contains programs
            extracted['program'].append(cells[2].text)
            # Assuming the fourth column contains document types
            extracted['doc_type'].append(cells[3].text)

    # Page Handling
    return extracted


def save_PDFs(site_name, extracted):
    # Open Link
    # Download or Save as PDF

    for i, link in enumerate(extracted['link']):
        pdf = requests.get(link)

        fn = extracted.keys()
        filename = f'{site_name}/{fn[2][i]}_{site_name}_{fn[3][i]}_{fn[4][i]}.pdf'

        with open(filename, 'wb') as file:
            file.write(pdf.content)

    # Implement saving pdf with this filename here:
    # curl -o downloaded_file.pdf "{fn[1]}"
    # While making PDF make a txt too?
    # PDF miner


for ind, id in enumerate(bf_id):
    # Requests the data from IDEM digital file cabinet using requests
    search_result = search_Id(id)

    extracted = extract_Data()  # Scrape the results pages.:with expression as target:
        pass
    # Get a PD frame with: # Link to PDF, Date of Doc, Program, Doc Type

    # Needs to be processed with regex
    site_name = re.sub(r"[<>:\"/\\|?&#*. ]", bf_name[ind], "_")
    os.mkdir(site_name)

    save_PDFs(site_name, extracted)

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
