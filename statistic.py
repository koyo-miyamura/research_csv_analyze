# coding:utf-8
import numpy as np
import sys
from collections import OrderedDict

def print_statistics(dir_name, errors, d_num, r_num):
    print("-----" + dir_name + " all_xy" + "-----")
    print("Average error")
    print(np.mean(errors))
    print("Variance")
    print(np.var(errors))
    print("Max error")
    print(np.max(errors))
    print("Min error")
    print(np.min(errors))
    errors_sorted = np.sort(errors)
    percent90 = (d_num*r_num//10)*9 - 1
    print("90% error")
    print(errors_sorted[percent90])

# @Output
# {PNUM100: [
#   [x0,y0],
#   [x1,y1],
#   ...
# ],
# PMUM500: [
# ...
# ],
# ...
# }
def load_all_csvs(args):
    all_xy_s = OrderedDict() # note: 辞書順のループは入力した順番を必ずしも保持しないのでOrderedDictを使う
    for i in range(len(args)):
        if i==0:
            continue # args[0]は自分のファイル名
        all_xy_s[args[i]]  = np.loadtxt(args[i] + "/all.csv", delimiter = ",")
    return all_xy_s

all_xy_s = load_all_csvs(args=sys.argv)
true_xy = np.loadtxt("true.csv", delimiter = ",")

d_num = 10 # データ数
r_num = 11 # 行数
true_xy = [true_xy[i%r_num] for i in range(len(true_xy)*d_num)] # change len(true_xy) into 110 for all.csv
for dir_name, all_xy in all_xy_s.items():
    errors = [np.linalg.norm(true_xy[i] - all_xy[i]) for i in range(len(all_xy))]
    print_statistics(dir_name=dir_name, errors=errors, d_num=d_num, r_num=r_num)
