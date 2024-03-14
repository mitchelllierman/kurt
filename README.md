# kurt
A scraping project developed for my Master's studies in the Arnolt Center for Investigative Journalism

Kurt aims to streamline the process of gathering documents related to polluted sites across the state of Indiana. By providing Kurt with the name of a community, the tool will search IDEM's virtual file cabinet for any associated sites and gather PDF documents which detail attempts to manage and clean brownfields. Once gathered, Kurt downloads the files it gathered as a zip file which can be unzipped and used for further analysis with tools like Google's Pinpoint Journalist Studio.

# Instructions
The easiest approach to using Kurt is to load kurt.ipynb in [Google Colab](colab.google). If you are a journalist using this tool and are new to Colab, I encourage you to learn more about Jupyter Notebooks, but rest assured that you will be in good shape without a background in computer science or data journalism: simply follow the link to Google Colab and select "New Notebook." From there, open the file drop down menu and select open notebook. Click on GitHub, then paste the URL to this repository followed by 'kurt.ipynb.' 

This will handle the installation of tabula on Colab's virtual system and ensure that the necessary data from IDEM's brownfields program is available, which saves you the trouble of wrestling with package managers and Java updates. Earlier versions of kurt existed as a Python script that required Anaconda, tabula-py, and Java to function properly. 

Once kurt.ipynb is loaded, simply run all cells. You will be prompted for a city to search for until your search query matches a city with sites listed in IDEM's database. 
