# 等しい軸のアスペクト比に対してデータ範囲を自動調整する

等しい軸のアスペクト比に対してデータ範囲を自動調整するには、`set_aspect('equal', 'box')` 関数を使用することもできます。

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

結果のグラフは、依然として比例しており視覚的に魅力的な円を表示します。
