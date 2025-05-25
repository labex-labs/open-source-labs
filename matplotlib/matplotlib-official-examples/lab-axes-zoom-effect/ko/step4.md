# 축 연결

이 단계에서는 축을 연결하고 확대 효과를 생성합니다. 네 개의 축이 있는 그림 (figure) 을 생성하고 `zoom_effect01` 및 `zoom_effect02` 함수를 사용하여 연결합니다.

```python
axs = plt.figure().subplot_mosaic([
    ["zoom1", "zoom2"],
    ["main", "main"],
])

axs["main"].set(xlim=(0, 5))
zoom_effect01(axs["zoom1"], axs["main"], 0.2, 0.8)
axs["zoom2"].set(xlim=(2, 3))
zoom_effect02(axs["zoom2"], axs["main"])

plt.show()
```
