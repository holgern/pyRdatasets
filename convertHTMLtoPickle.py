import os
from os.path import expanduser
import pandas as pd
import html2text
import pickle

if __name__ == '__main__':
    home = expanduser("~")
    data_dir = os.path.join(home, "documents")
    data_out_dir = os.path.join(data_dir, "git//pyRdatasets//Rdatasets//_data//")
    datasets = pd.read_csv(os.path.join(data_dir, "datasets.csv"))
    descr = {}
    
    
    for i in range(len(datasets)):
        row = datasets.iloc[i]
        print("%s - %s" % (row["Package"], row["Item"]))
        if row["Package"] not in descr:
            descr[row["Package"]] = {}
        
        html_file = os.path.join(data_dir, "doc//%s//%s.html" % (row["Package"], row["Item"]))
        with open(html_file) as f:
            content = f.read().splitlines()      
        descr[row["Package"]][row["Item"]] = html2text.html2text('\n'.join(content))
        # print('\n'.join(content))

    with open(os.path.join(data_out_dir, 'descr.pickle'), 'wb') as handle:
        pickle.dump(descr, handle, protocol=pickle.HIGHEST_PROTOCOL)    