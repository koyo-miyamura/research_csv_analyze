# !bin/bash
set -eu
: $1 # 引数が渡されていなければスクリプト実行中止
prefix=$1
ls -d $prefix* | xargs ./csv_generate.sh