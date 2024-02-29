import os
from os.path import expanduser

import pandas as pd

if __name__ == '__main__':
    data_dir = "./rdatasets_orig"
    data_out_dir = os.path.join('./', "rdatasets//_data//")
    datasets = pd.read_csv(os.path.join(data_dir, "datasets.csv"))
    datasets.to_pickle(
        os.path.join(data_out_dir, "datasets.pkl.compress"), compression="gzip"
    )
    for i in range(len(datasets)):
        row = datasets.iloc[i]
        package = row["Package"]
        item = row["Item"].split(" ")[0]
        print("{} - {}".format(package, item))
        try:
            dataset = pd.read_csv(
                os.path.join(
                    data_dir, "csv//{}//{}.csv".format(package, item)
                )
            )
        except:
            dataset = pd.read_csv(
                os.path.join(
                    data_dir, "csv//{}//{}.csv".format(package, item)
                ),
                encoding="ISO-8859-1",
            )
        directory = os.path.join(data_out_dir, "%s" % (package))
        if not os.path.exists(directory):
            os.makedirs(directory)
        if "Unnamed:" in dataset.columns[0]:
            dataset = dataset.drop(dataset.columns[0], axis=1)
        dataset.to_pickle(
            os.path.join(directory, "%s.pkl.compress" % (item)),
            compression="gzip",
        )
