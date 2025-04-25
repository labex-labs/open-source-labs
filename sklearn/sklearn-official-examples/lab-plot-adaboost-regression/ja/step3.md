# 結果のプロット

最後に、単一の決定木回帰器と AdaBoost 回帰器の 2 つの回帰器がデータにどの程度適合するかをプロットします。Matplotlib の`scatter()`関数を使って、学習サンプルと両方の回帰器からの予測値をプロットします。Matplotlib の`plot()`関数を使って、両方の回帰器に対して予測値とデータを対応させてプロットします。2 つの回帰器を区別するために、プロットに凡例を追加します。

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()
```
