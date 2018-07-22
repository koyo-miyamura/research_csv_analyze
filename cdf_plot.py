from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import sys

def load_all_csvs(args):
    all_xy_s = OrderedDict() # note: 辞書順のループは入力した順番を必ずしも保持しないのでOrderedDictを使う
    for i in range(len(args)):
        if i==0:
            continue # args[0]は自分のファイル名
        all_xy_s[args[i]]  = np.loadtxt(args[i] + "/all.csv", delimiter = ",")
    return all_xy_s

args = sys.argv

# データと真の値を読み込み
all_xy_s = load_all_csvs(args=sys.argv)
true_xy = np.loadtxt("true.csv", delimiter = ",")

d_num = 10 # データ数
r_num = 11 # 行数
true_xy = [true_xy[i%r_num] for i in range(len(true_xy)*d_num)] # change len(true_xy) into 110 for all.csv

for dir_name, all_xy in all_xy_s.items():
    errors = [np.linalg.norm(true_xy[i] - all_xy[i]) for i in range(len(all_xy))] # ユークリッド距離の計算

    errors_sorted = np.sort(errors)
    percent90 = (d_num*r_num//10)*9 - 1 
    print("-----" + dir_name + "-----")
    print("90%以内誤差")
    print(errors_sorted[percent90])

    #0から8まで80個にすれば0.1刻みになる
    hist_fig, hist_ax = plt.subplots()
    y, bins, patches = hist_ax.hist(errors, bins=80, range=(0,8), density=True, cumulative=True, histtype="step", label="hist")
    plt.close(hist_fig) # y, bins があればヒストグラム自体は必要ないのでここで消す(もう少しいいやり方がありそう)

    # 散布図の描画
    plt.plot(bins[:-1], y)
    plt.scatter(bins[:-1], y, s=10, label=dir_name)
# plt.title("title")
plt.xlabel("Error [m]")
plt.ylabel("Cumulative frequency [%]")
plt.legend()
plt.show()
