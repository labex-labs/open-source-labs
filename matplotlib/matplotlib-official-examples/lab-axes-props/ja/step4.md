# 軸目盛りとグリッドのプロパティのカスタマイズ

`grid()` 関数と `tick_params()` 関数を使って、軸目盛りとグリッドのプロパティをカスタマイズすることができます。この例では、目盛りラベルの色とサイズ、およびグリッド線の太さとスタイルを変更します。

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
