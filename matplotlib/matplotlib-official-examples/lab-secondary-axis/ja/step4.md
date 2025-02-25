# 別の例をプロットする

ここでは、対数対数スケールで波数から波長への変換の別の例をプロットします。この例では、ランダムなスペクトルを使用します。

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```
