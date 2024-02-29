import os
import pickle

import html2text
import pandas as pd

if __name__ == '__main__':
    data_dir = "./rdatasets_orig"
    data_out_dir = os.path.join('./', "rdatasets//_data//")
    datasets = pd.read_csv(os.path.join(data_dir, "datasets.csv"))
    descr = {}

    for i in range(len(datasets)):
        row = datasets.iloc[i]
        package = row["Package"]
        item = row["Item"].split(" ")[0]
        print(f"{package} - {item}")
        if package not in descr:
            descr[package] = {}

        html_file = os.path.join(data_dir, f"doc//{package}//{item}.html")
        with open(html_file, encoding="utf8") as f:
            content = f.read().splitlines()
        descr[package][item] = html2text.html2text('\n'.join(content))
        # print('\n'.join(content))

    with open(os.path.join(data_out_dir, 'descr.pickle'), 'wb') as handle:
        pickle.dump(descr, handle, protocol=pickle.HIGHEST_PROTOCOL)
