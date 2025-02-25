# 透明度をブレンドする

`imshow`を使ってデータをプロットする際に透明度を含める最も簡単な方法は、データの形状に合う配列を`alpha`引数に渡すことです。

```python
# 右に向かって線形に増加する値のアルファチャンネルを作成する。
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# 画像とグラフを作成する
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```

# 透明度をブレンドする

`imshow`を使ってデータをプロットする際に透明度を含める最も簡単な方法は、データの形状に合う配列を`alpha`引数に渡すことです。

```python
# 右に向かって線形に増加する値のアルファチャンネルを作成する。
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# 画像とグラフを作成する
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```
