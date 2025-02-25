# 個々のコンポーネントを削除する

`boxplot()` 関数に用意されているさまざまなキーワード引数を使って、ボックスプロットの個々のコンポーネントを削除することができます。たとえば、`showmeans` を False に設定することで平均値を削除できます。また、`showbox` と `showcaps` をそれぞれ False に設定することで、ボックスとひげを削除できます。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

axs[0, 1].boxplot(data, labels=labels, showmeans=False)
axs[0, 1].set_title('No Means')

axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axs[1, 0].set_title('No Box or Whiskers')

axs[1, 1].boxplot(data, labels=labels, showfliers=False)
axs[1, 1].set_title('No Outliers')

plt.show()
```
