# サブプロットの作成

Matplotlibの`subplots`関数を使って3つのサブプロットを作成します。サブプロットが共通のx軸を共有するようにするために、`sharex`パラメータを`True`に設定します。また、`subplots_adjust`関数を使ってサブプロット間の垂直方向の余白を削除します。

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```
