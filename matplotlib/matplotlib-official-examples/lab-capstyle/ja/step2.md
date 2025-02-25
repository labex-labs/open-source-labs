# グラフを作成する

次に、異なる `CapStyle` オプションを示すための簡単なグラフを作成します。

```python
fig, ax = plt.subplots()

# Plotting the line with different CapStyle options
for i, cap_style in enumerate(CapStyle):
    ax.plot([0, 1], [i, i], label=str(cap_style), linewidth=10, solid_capstyle=cap_style)

# Adding legend and title
ax.legend(title='CapStyle')
ax.set_title('CapStyle Demo')
```
