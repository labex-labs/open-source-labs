# 軸ラベルをカスタマイズする

同じくフォント辞書を使って、プロットの軸ラベルをカスタマイズできます。xlabel()関数とylabel()関数のfontdictパラメータを、私たちのフォント辞書に設定します。

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
