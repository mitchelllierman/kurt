# Kurt: A Document Scraping Tool for Investigative Journalism
Kurt is a scraping project developed as part of my Master's studies at the Arnolt Center for Investigative Journalism. The tool is designed to streamline the process of gathering documents related to polluted sites across the state of Indiana.

By providing Kurt with the name of a community, the tool will search the Indiana Department of Environmental Management's (IDEM) virtual file cabinet for any associated sites and gather PDF documents detailing attempts to manage and clean brownfields. Once gathered, Kurt downloads the files as a zip file, which can be unzipped and used for further analysis with tools like Google's Pinpoint Journalist Studio.

### Getting Started
The easiest way to use Kurt is to load kurt.ipynb in Google Colab. This approach handles the installation of necessary dependencies and ensures that the data from IDEM's brownfields program is available, saving you the trouble of dealing with package managers and Java updates. Earlier versions of Kurt required Anaconda, tabula-py, and Java to function properly.

### Important Note for Journalists
If you are a journalist new to Colab, we encourage you to learn more about Jupyter Notebooks. However, rest assured that you can use Kurt effectively without a background in computer science or data journalism. Simply follow these steps:

1. Open Google Colab: Go to [Google Colab](colab.google) and select "New Notebook."
2. Load Kurt Notebook: Open the file drop-down menu and select "Open notebook" (or press Ctrl + O). Click on "GitHub," paste the following URL into the search bar, and hit enter:
```
https://github.com/mitchelllierman/kurt/blob/master/kurt.ipynb
```
3. Run Kurt: In kurt.ipynb, click "Runtime" in the ribbon to open the runtime context menu. Select "Run all" and input your city when prompted.

### Letting Kurt Run and Next Steps
After inputting your city, please be patient while Kurt searches for and gathers the necessary files. This process may take several minutes, but barring any issues, you should soon see the files you need downloaded as a .zip file. This zip file contains a folder named yourcity_folder, which contains subfolders full of PDFs for each site in your city.

Once you have reached this step, Kurt's job is done, and you are free to proceed with your analysis. Best of luck in your reporting!
