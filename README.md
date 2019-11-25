# PlayLebanon-Lotto-Data-Extractor
Allows the user to extract the most up to date data for the playlebanon lottery on playlebanon.com

# How to use:
Navigate to https://www.playlebanon.com/webservices/website/lotto/PopUps/HistoryDetail.aspx?t=1410910536000&FromDraw=1&ToDraw=44&Draw=0

Change the to FromDraw and the ToDraw values in the URL to the desired range that you would like to extract. In the case above we are extracting for draw 1 up to draw 44.

Note that the page may take time to load depending on how large the range is.
After the page has loaded, right click the page and save it as an HTML file, and place it in the same directory as the python script.

Note that this is done because the website is currently not accepting any requests.

Run the script to extract the data.

2 Files will be created:
  The dataframe pickle file
  The numbers pickle file

The dataframe file contains a data frame that is formatted as follows:

Dates | num_1 | num_2 | num_3 | num_4 | num_5 | num_6 | num_extra 
--- | --- | --- | --- |--- |--- |--- |--- 

The numbers file simply contains an array of all the numbers that have appeard in lottory.
