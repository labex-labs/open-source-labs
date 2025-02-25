# 不等しい軸のアスペクト比で円を描画する

まず、等しい軸のアスペクト比を設定する重要性を示すために、不等しい軸のアスペクト比で円を描画します。

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

結果のグラフは、不等しい軸のアスペクト比のために楕円のように見える円を表示します。
