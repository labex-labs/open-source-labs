# 正則化パスをプロットする

学習済みモデルの係数を使用して正則化パスをプロットします。係数は、正則化強度の対数に対してプロットされます。グラフの左側（強い正則化項）では、すべての係数が正確に0になります。正則化が徐々に緩くなると、係数が順に非ゼロの値をとるようになります。

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Coefficients")
plt.title("Logistic Regression Path")
plt.axis("tight")
plt.show()
```
