# プロットの作成

データが用意できたので、プロットを作成しましょう。異なる `symlog` 軸スケーリングを持つ3つのサブプロットを作成します。

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
```
