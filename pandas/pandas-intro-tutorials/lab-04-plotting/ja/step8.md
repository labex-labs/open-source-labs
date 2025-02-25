# グラフをカスタマイズして保存する

Matplotlib のカスタマイズオプションを使用して、さらにグラフをカスタマイズすることができます。また、グラフをファイルに保存することもできます。

```python
# Customizing and saving the plot
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```
