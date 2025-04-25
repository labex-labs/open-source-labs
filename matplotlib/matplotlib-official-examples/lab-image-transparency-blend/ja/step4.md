# 透明度を使って値を強調する

最後に、同じプロットを再作成しますが、今回は透明度を使ってデータの極端な値を強調します。これは、小さな p 値を持つデータポイントを強調するためによく使われます。また、画像の値を強調するために等高線も追加します。

```python
# 重み値に基づいてアルファチャンネルを作成する
alphas = Normalize(0,.3, clip=True)(np.abs(weights))
alphas = np.clip(alphas,.4, 1)  # アルファ値は下側で.4 でクリップされる

# 画像とグラフを作成する
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# さまざまなレベルをさらに強調するために等高線を追加する
ax.contour(weights[::-1], levels=[-.1,.1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001,.0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```

# 透明度を使って値を強調する

最後に、同じプロットを再作成しますが、今回は透明度を使ってデータの極端な値を強調します。これは、小さな p 値を持つデータポイントを強調するためによく使われます。また、画像の値を強調するために等高線も追加します。

```python
# 重み値に基づいてアルファチャンネルを作成する
alphas = Normalize(0,.3, clip=True)(np.abs(weights))
alphas = np.clip(alphas,.4, 1)  # アルファ値は下側で.4 でクリップされる

# 画像とグラフを作成する
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# さまざまなレベルをさらに強調するために等高線を追加する
ax.contour(weights[::-1], levels=[-.1,.1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001,.0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
