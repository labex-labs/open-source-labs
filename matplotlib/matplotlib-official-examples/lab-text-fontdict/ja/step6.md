# 軸ラベルをカスタマイズする

同じくフォント辞書を使って、プロットの軸ラベルをカスタマイズできます。xlabel() 関数と ylabel() 関数の fontdict パラメータを、私たちのフォント辞書に設定します。

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
