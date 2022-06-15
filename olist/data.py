import os
import pandas as pd

def get_data():
    """ Reads in all csv files from the folder "data" and
    returns them in a dictionary with the keys being
    the names of the dataframes
    """

    # Note: Check if this runs in terminal as well
    root_dir = os.path.dirname(os.path.abspath(""))
    data_path = os.path.join(root_dir, "data")

    # get file names of all files in data folder
    file_names = []
    # and the key_names for the dictionary
    key_names = []

    # loop over
    for file in os.listdir(data_path):
        if file.endswith("csv"):
            file_names.append(file)
            key_names.append(file.replace("_dataset.csv", "").replace("olist_", ""))
    data = dict()

    for key, file in zip(key_names, file_names):
        data[key] = pd.read_csv(os.path.join(data_path, file))

    return data


if __name__=="__main__":
    data= get_data()
    print(data.keys())
