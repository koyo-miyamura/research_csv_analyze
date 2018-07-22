# !bin/sh
set -eu
for name in $@
do
  ls $name/EXP*.csv | xargs cat | cut -d "," -f 2,3 > $name/all.csv
done