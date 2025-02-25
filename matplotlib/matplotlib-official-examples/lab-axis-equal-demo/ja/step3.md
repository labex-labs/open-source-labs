# 等しい軸のアスペクト比で円を描画する

等しい軸のアスペクト比を設定するには、`axis('equal')` 関数を使用できます。

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

結果のグラフは、比例しており視覚的に魅力的な円を表示します。
