# research_csv_analyze

## Requirement

* python3
* matplotlib==1.5.1
* numpy==1.11.0

## Quick Start

### Create "all.csv"

`./all_csv_generate.sh data`

もしデータの入ったディレクトリが `sample1, sample2 ...`のような形式であれば以下のように実行してください

`./all_csv_generate.sh sample`

### Output statistic
`./statistic.sh data`

個別で出力したい場合は以下

`python statistic.py data1`

`python statistic.py data2`

### Output CDF
`./cdf_plot.sh data`

個別で出力したい場合は以下

`python cdf_plot.py data1`

`python cdf_plot.py data2`

### Article(How to use)
