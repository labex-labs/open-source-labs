# 縦型のカラーバーの目盛りラベルをカスタマイズする

次に、縦型のカラーバーの目盛りラベルをカスタマイズします。`colorbar` を使ってカラーバーを作成し、`ticks` パラメータを使って目盛りの位置を指定します。その後、カラーバーオブジェクトの `ax` 属性に対して `set_yticklabels` を使って目盛りラベルを設定します。

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
