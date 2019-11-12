import os
from os.path import expanduser
import pandas as pd

if __name__ == '__main__':
    home = expanduser("~")
    data_dir = os.path.join(home, "documents")
    data_out_dir = os.path.join(data_dir, "git//pyRdatasets//Rdatasets//_data//")
    datasets = pd.read_csv(os.path.join(data_dir, "datasets.csv"))
    datasets.to_pickle(os.path.join(data_out_dir, "datasets.pkl.compress"), compression="gzip")
    for i in range(len(datasets)):
        row = datasets.iloc[i]
        print("%s - %s" % (row["Package"], row["Item"]))
        try:
            dataset = pd.read_csv(os.path.join(data_dir, "csv//%s//%s.csv" % (row["Package"], row["Item"])))
        except:
            dataset = pd.read_csv(os.path.join(data_dir, "csv//%s//%s.csv" % (row["Package"], row["Item"])), encoding="ISO-8859-1")
        directory = os.path.join(data_out_dir, "%s" % (row["Package"]))
        if not os.path.exists(directory):
            os.makedirs(directory)
        dataset.to_pickle(os.path.join(directory, "%s.pkl.compress" % (row["Item"])), compression="gzip")