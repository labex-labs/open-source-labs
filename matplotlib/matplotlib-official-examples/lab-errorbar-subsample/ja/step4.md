# 2 番目の系列を 3 だけシフトする

場合によっては、データの異なる部分に誤差棒サブサンプリングを適用したい場合があります。これは、`errorevery`パラメータにタプルを指定することで行うことができます。たとえば、2 番目の系列に誤差棒サブサンプリングを適用し、3 つのデータポイントだけシフトさせましょう。

```python
fig, ax = plt.subplots()

ax.set_title('Second Series Shifted by 3')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```
