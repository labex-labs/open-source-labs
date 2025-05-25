# 수직 컬러바가 있는 플롯 생성

수직 컬러바가 있는 플롯을 생성하는 것으로 시작합니다. `numpy`의 `randn`을 사용하여 일부 임의 데이터를 생성하고 값을 -1 에서 1 범위로 클리핑합니다. 그런 다음 `imshow`와 `coolwarm` 컬러맵을 사용하여 `AxesImage` 객체를 생성합니다. 마지막으로 플롯에 제목을 추가합니다.

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
