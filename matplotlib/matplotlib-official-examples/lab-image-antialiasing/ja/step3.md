# 「アンチエイリアス」補間を使った画像のサブサンプリング

次に、「アンチエイリアス」補間を使って画像を 450 データピクセルから 125 ピクセルまたは 250 ピクセルにサブサンプリングします。これにより、高周波データのサブサンプリングによって引き起こされるモアレパターンを軽減するためにアンチエイリアシングをどのように使用できるかを示します。

```python
fig, axs = plt.subplots(2, 2, figsize=(5, 6), layout='constrained')
axs[0, 0].imshow(a, interpolation='nearest', cmap='RdBu_r')
axs[0, 0].set_xlim(100, 200)
axs[0, 0].set_ylim(275, 175)
axs[0, 0].set_title('Zoom')

for ax, interp, space in zip(axs.flat[1:],
                             ['nearest', 'antialiased', 'antialiased'],
                             ['data', 'data', 'rgba']):
    ax.imshow(a, interpolation=interp, interpolation_stage=space,
              cmap='RdBu_r')
    ax.set_title(f"interpolation='{interp}'\nspace='{space}'")
plt.show()
```
