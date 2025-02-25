# サブプロットの作成

異なるスパインのカスタマイズを示すために 3 つのサブプロットを作成します。ラベルが軸と重ならないようにするために制約付きレイアウトを使用します。

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```
