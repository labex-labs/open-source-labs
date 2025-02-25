# サブプロットを作成する

補間方法を使って画像を表示するためのサブプロットを作成します。

```python
fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9, 6),
                        subplot_kw={'xticks': [], 'yticks': []})
```
