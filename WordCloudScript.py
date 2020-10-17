from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np
import pandas as pd
import re

# Storing the current directory path to a variable. Will be using it to store the wordcloud file in the same directory.
current_dir = os.path.dirname(__file__)

fulltext = []

# Saving the file name to a variable. Helps in future if we have to change the file type
file_loc = "sheet.xls"

# Using pandas we are loading the columns we need into a variable called db
df = pd.read_excel(
    file_loc, index_col=None, index_row=0, na_values=["NA"], usecols="D,E,F,G,J,K,M"
)

# Converting into string type
df = df.astype(str)

# Iterating through all the rows and columns.
for i, row in df.iterrows():
    for j, column in row.iteritems():
        fulltext.append(column)

# This helps us to store only character and avoid the special characters and numbers.
letters_only = [re.sub("[^a-zA-Z]", " ", str(fulltext))]

stringwords = [i for item in letters_only for i in item.split()]

text = " "

for word in stringwords:
    text = text + " " + word

# print(text)


# A function to create the wordcloud
def create_cloud(text):
    # This helps us to shape the wordcloud according to our need
    mask = np.array(Image.open(os.path.join(current_dir, "logo.png")))

    # Stopwords has the list of common english words which will not be considered during the analysis
    stopwords = set(STOPWORDS)
    # We can add any additional words that we may want to be ignored from the analysis
    stopwords.add("Meh")
    stopwords.add("average")
    stopwords.add("wwYBowKkoK")
    stopwords.add("nan")

    wc = WordCloud(
        background_color="white",
        mask=mask,
        # The number of words you want to be displayed in the image
        max_words=100,
        stopwords=stopwords,
        # If you dont want any word to repeat in the image
        collocations=False,
        # To color the words in the image
        colormap="Reds",
    )

    wc.generate(text)

    # Here we use the current directory to save the image or wordcloud
    wc.to_file(os.path.join(current_dir, "WordCloudPic.png"))


create_cloud(text)
