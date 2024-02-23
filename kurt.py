# Import Needed Libraries
import re
import pandas as pd
import os


# Read in the spreadsheet listing sites
bf_data = pd.read_excel("Temp Excel File.xlsx",)

# Read in Brownfield sites by their ID number
bf_id = bf_data['BFD#']
bf_name = bf_data['Name']


def search_Id(id):
    cabinet_base = "https://ecm.idem.in.gov/cs/"
    oracle_pls = "idcplg?IdcService=GET_SEARCH_RESULTS&QueryText="
    query = f"%3cftx%3e{id}%3c%2fftx%3e"
    sort = "&SortField=xProgram"
    order = "&SortOrder=Desc"
    results = "&ResultCount=100"
    id_search = cabinet_base + oracle_pls + query + sort + order + results
    search_result = ""  # Use requests here to get resulting file from IDEM
    return search_result


def extract_Data(search_result):
    # Page Handling
    # A lot of XPATH/CSS Selectors
    # Builds PD frame

    extracted = {'link': [],
                 # Ex https://ecm.idem.in.gov/cs/idcplg?IdcService=GET_FILE&dID=4080205&dDocName=63984694&Rendition=web&allowInterrupt=1&noSaveAs=1
                 'date': [],
                 # YYYY_MM_DD -- requires PARSING
                 'program': [],
                 # Ex Brownfield
                 'doctype': []}
    # Ex Brownfield Completion Document
    return extracted


def save_PDF(page, site_name, extracted):
    # Open Link
    # Download or Save as PDF
    fn = extracted.keys()
    filename = f'{site_name}/{fn[2]}_{site_name}_{fn[3]}_{fn[4]}.pdf'
    # Implement saving pdf with this filename here:
    # curl -o downloaded_file.pdf "{fn[1]}"
    # While making PDF make a txt too?
    # PDF miner


for ind, id in enumerate(bf_id):
    # Requests the data from IDEM digital file cabinet using requests
    search_result = search_Id(id)

    extracted = extract_Data()  # Scrape the results pages.
    # Get a PD frame with: # Link to PDF, Date of Doc, Program, Doc Type

    site_name = bf_name[ind]  # Needs to be processed with regex
    os.mkdir(site_name)

    for link in extracted:
        save_PDF(site_name, extracted)


'''
==================================================================
TODO:
    Implement requests things
    Implement saving PDF
    Implement PDF2txt
    Bonus functions for analysis?
    Create GitHub repo for Kurt
==================================================================
Error detected while processing function <SNR>43_NetrwBrowseChgDir[194]..<SNR>43_NetrwEditFile:
line    7:
E325: ATTENTION
Found a swap file by the name "~/.local/state/nvim/swap//%home%mitch%Projects%Python%Kurt%kurt.py.swp"

          owned by: mitch   dated: Thu Feb 22 00:19:18 2024
         file name: ~mitch/Projects/Python/Kurt/kurt.py
          modified: YES
         user name: mitch   host name: Lux
        process ID: 7016
While opening file "/home/mitch/Projects/Python/Kurt/kurt.py"
             dated: Thu Feb 22 02:22:35 2024
      NEWER than swap file!

(1) Another program may be editing the same file.  If this is the case,
    be careful not to end up with two different instances of the same
    file when making changes.  Quit, or continue with caution.
(2) An edit session for this file crashed.
    If this is the case, use ":recover" or "vim -r /home/mitch/Projects/Python/Kurt/kurt.py"
    to recover the changes (see ":help recovery").
    If you did this already, delete the swap file "/home/mitch/.local/state/nvim/swap//%home%mitch%Pro
jects%Python%Kurt%kurt.py.swp"
    to avoid this message.

Swap file "~/.local/state/nvim/swap//%home%mitch%Projects%Python%Kurt%kurt.py.swp" already exists!'''
