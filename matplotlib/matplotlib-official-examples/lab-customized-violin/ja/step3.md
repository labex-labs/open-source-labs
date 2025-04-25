# バイオリンプロットの外観をカスタマイズする

ここでは、バイオリンプロットの外観をカスタマイズします。まず、`showmeans`、`showmedians`、`showextrema`の各引数を`False`に設定することで、Matplotlib が描画する内容を制限します。次に、`set_facecolor`と`set_alpha`メソッドを使って、バイオリンの本体の色と不透明度を変更します。最後に、NumPy の`percentile`関数を使って四分位数、中央値、ひげを計算し、バイオリンプロットの上に箱ひげ図の簡略化された表現を追加します。

```python
# customize violin plot appearance
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# create violin plot
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# customize violin bodies
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# add box plot
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```
