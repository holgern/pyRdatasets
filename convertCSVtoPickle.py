import os

import pandas as pd

if __name__ == '__main__':
    data_dir = "./rdatasets_orig"
    data_out_dir = os.path.join('./', "rdatasets//_data//")
    datasets = pd.read_csv(os.path.join(data_dir, "datasets.csv"))
    datasets.to_pickle(
        os.path.join(data_out_dir, "datasets.pkl.compress"), compression="xz"
    )
    for i in range(len(datasets)):
        row = datasets.iloc[i]
        package = row["Package"]
        item = row["Item"].split(" ")[0]
        print(f"{package} - {item}")
        try:
            dataset = pd.read_csv(os.path.join(data_dir, f"csv//{package}//{item}.csv"))
        except Exception as e:
            print(e)
            dataset = pd.read_csv(
                os.path.join(data_dir, f"csv//{package}//{item}.csv"),
                encoding="ISO-8859-1",
            )
        directory = os.path.join(data_out_dir, "%s" % (package))
        if not os.path.exists(directory):
            os.makedirs(directory)
        if "Unnamed:" in dataset.columns[0]:
            dataset = dataset.drop(dataset.columns[0], axis=1)
        dataset.to_pickle(
            os.path.join(directory, "%s.pkl.compress" % (item)),
            compression="xz",
        )
