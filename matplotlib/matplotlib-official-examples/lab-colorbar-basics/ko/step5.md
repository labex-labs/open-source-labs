# 양수 및 음수 데이터가 있는 플롯 생성

양수 및 음수 데이터가 모두 있는 플롯을 생성하고, `colorbar` 함수를 사용하여 플롯에 컬러바를 추가합니다. 이번에는 `vmin` 및 `vmax` 매개변수를 사용하여 컬러바의 최소 및 최대 값을 지정합니다.

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
