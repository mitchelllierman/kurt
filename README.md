# kurt
A scraping project developed for my Master's studies in the Arnolt Center for Investigative Journalism

Kurt aims to streamline the process of gathering documents related to polluted sites across the state of Indiana. By providing Kurt with the name of a community, the tool will search IDEM's virtual file cabinet for any associated sites and gather PDF documents which detail attempts to manage and clean brownfields. Once gathered, Kurt downloads the files it gathered as a zip file which can be unzipped and used for further analysis with tools like Google's Pinpoint Journalist Studio.

# Instructions
The easiest approach to using Kurt is to load kurt.ipynb in [Google Colab](colab.google). This will handle the installation of tabula on Colab's virtual system and ensure that the necessary data from IDEM's brownfields program is available, which saves you the trouble of wrestling with package managers and Java updates. Earlier versions of kurt existed as a Python script that required Anaconda, tabula-py, and Java to function properly. 

### Important Note to Journalists Using This Tool
If you are a journalist using this tool and are new to Colab, I encourage you to learn more about Jupyter Notebooks, but rest assured that you will be in good shape without a background in computer science or data journalism: simply follow the link to Google Colab and select "New Notebook." From there, open the file drop down menu and select open notebook (this can also be done by pressing Ctrl + O). Click on GitHub, then paste the following URL in the search bar and hit enter:

```
https://github.com/mitchelllierman/kurt/blob/master/kurt.ipynb
```
### In kurt.ipynb
The above step will open kurt.ipynb. From here, click "Runtime" in the ribbon to open the runtime context menu. Select run all and input your city when prompted. 

### Letting kurt Run and Next Steps
After inputting your city, hold tight and wait for the program to run: it may take several minutes for Kurt to search for and gather the files you need, but without anything going horribly wrong you should soon see the files you need downloaded as a .zip file. This zip file contains a folder named yourcity_folder, which contains subfolders full of PDFs for each of the sites in your city. Once you have reached this step, kurt's job is done and you are free to proceed as needed. Best of luck in your reporting! 



