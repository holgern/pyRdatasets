# pyRdatasets
pyRdatasets is a collection of 2264 datasets taken from https://github.com/vincentarelbundock/Rdatasets.
The datasets were extracted from various R packages and stored as gzip packed pickle files in pandas DataFrame structure.
A description to each dataset can be found here: http://vincentarelbundock.github.io/Rdatasets/datasets.html


All 2264 data records are already included in the package (no internet connection necessary), which has a size around 25 Mb.

## Installation
```
pip install rdatasets
```

## Usage

```
>>> from rdatasets import data
>>> dataset = data("iris")
>>> dataset
     Sepal.Length  Sepal.Width  Petal.Length  Petal.Width    Species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
3             4.6          3.1           1.5          0.2     setosa
4             5.0          3.6           1.4          0.2     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

[150 rows x 5 columns]
>>> data("forecast", "co2")
Could not read forecast/co2
Which item did you mean: ['gas', 'gold', 'taylor', 'wineind', 'woolyrnq']?
>>> data("forecast", "gas")
            time  value
0    1956.000000   1709
1    1956.083333   1646
2    1956.166667   1794
3    1956.250000   1878
4    1956.333333   2173
..           ...    ...
471  1995.250000  49013
472  1995.333333  56624
473  1995.416667  61739
474  1995.500000  66600
475  1995.583333  60054

[476 rows x 2 columns]
```

The dataset description can be printed by:
```
from rdatasets import data, descr
print(descr("iris"))
```
A summary of all datasets is available as DataFrame object:
```
from rdatasets import summary
summary()
```

## Thanks to
The archive of datasets distributed with R: of https://github.com/vincentarelbundock/Rdatasets


## Pre-commit-config

### Installation

```
$ pip install pre-commit
```

### Using homebrew:
```
$ brew install pre-commit
```

```
$ pre-commit --version
pre-commit 2.10.0
```

### Install the git hook scripts

```
$ pre-commit install
```

### Run against all the files
```
pre-commit run --all-files
pre-commit run --show-diff-on-failure --color=always --all-files
```

### Update package rev in pre-commit yaml
```bash
pre-commit autoupdate
pre-commit run --show-diff-on-failure --color=always --all-files
```
