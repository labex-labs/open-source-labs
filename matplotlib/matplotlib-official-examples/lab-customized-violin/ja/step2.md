# デフォルトのバイオリンプロットを作成する

次に、Matplotlib の`violinplot`関数を使用してデフォルトのバイオリンプロットを作成します。後の手順でプロットをカスタマイズする際の比較の基準となります。

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
