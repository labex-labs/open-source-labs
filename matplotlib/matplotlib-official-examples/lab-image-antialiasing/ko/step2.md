# 'nearest' 보간법 (Interpolation) 으로 이미지 서브샘플링

이제 'nearest' 보간법을 사용하여 이미지를 450 데이터 픽셀에서 125 픽셀 또는 250 픽셀로 서브샘플링합니다. 이는 서브샘플링되는 고주파 데이터가 어떻게 모아레 패턴을 유발할 수 있는지 보여줍니다.

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
