from bs4 import BeautifulSoup
from datetime import timedelta, date
from datetime import datetime as dt
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def pickle_file(output_file_name, object_to_pickle):
    """
    Accepts output file name and the object to pickle
    Returns a pickled file with the desired output file name
    """
    with open(output_file_name, "wb") as out_file:
        pickle.dump(object_to_pickle, out_file)


def unpickle_file(file_name):
    """
    Accepts the pickle file name 
    Returns an object from the pickled file 
    """
    with open(file_name, "rb") as in_file:
        return pickle.load(in_file)


def extract_data(extract="dataframe"):
    """
    function extracts the date and the respective winning poll numbers 
    input extract: specifies the data to be extracted

    either: 'numbers' : returns a list of arrays for all the numbers
    
    or: 'dataframe': returns a dataframe containing the date and the
    respective winning numbers for that date, the dataframe is formatted as:
    date,num_1,num_2,num_3,num_4,num_5,num_6,num_extra

    """

    soup = BeautifulSoup(open("HistoryDetail.html"), "html.parser")

    # return all the tags that have an image attribute
    images = soup.find_all("img")

    # return all the tags containing the class DrawNumber
    data_table = soup.findAll("td", attrs={"class": "DrawNumber"})

    # perform list comprehension on the text values contained within the tags
    # only return the date text by verifying that the length of the text is >7
    # convert extracted string values into date values using datetime
    dates = [
        dt.strptime(tag.text, "%m/%d/%Y").date()
        for tag in data_table
        if len(tag.text) > 7
    ]

    numbers = []

    # return the ball number via the url and stripping the uneeded text
    # convert number to an int value
    for i, image in enumerate(images):
        link = image.attrs["src"]
        number = link.replace("./HistoryDetail_files/", "")
        number = number.replace(".jpg", "")
        numbers.append(int(number))

    if extract == "numbers":
        return numbers

    numbers = np.array(numbers)
    # split the array into the winning lottos
    len_array = (numbers.size) / 7
    numbers_array = np.split(numbers, len_array)
    # eliminate the extra lotto ball and add them to a list of their own
    extra_numbers = []
    for i, array in enumerate(numbers_array):
        extra_numbers.append(array[-1])
        numbers_array[i] = array[:-1]

    df = pd.DataFrame(numbers_array)
    df.insert(loc=0, column="dates", value=dates)
    df.insert(loc=7, column="num_extra", value=extra_numbers)

    index = ["dates", "num_1", "num_2", "num_3", "num_4", "num_5", "num_6", "num_extra"]

    df.columns = index

    return df


def plot_bar(dataframe, column):

    # plotting the frequency of the lottery numbers in a histogram
    plt.style.use("fivethirtyeight")

    data_counts = dataframe[column].value_counts()

    data_counts.plot("bar")

    plt.title("frequency ditrubution of lotto numbers")
    plt.xlabel("lotto numbers")
    plt.ylabel("frequency")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    dataframe = extract_data(extract="dataframe")
    numbers_array = extract_data(extract="numbers")

    pickle_file("dataframe", dataframe)
    pickle_file("numbers", numbers_array)

    dataframe.to_csv("lotto_data.csv")

