# 等しい軸のアスペクト比を維持しながらグラフの範囲を調整する

等しい軸のアスペクト比を維持しながら、グラフの範囲を調整することもできます。

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

結果のグラフは、範囲を変更した後も依然として比例した円を表示します。
