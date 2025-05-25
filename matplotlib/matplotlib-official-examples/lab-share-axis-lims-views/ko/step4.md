# 두 번째 플롯 생성

다음으로, 두 번째 플롯을 생성합니다. 다시 `subplot`을 사용하지만, 이번에는 `sharex` 속성을 첫 번째 플롯 (`ax1`) 으로 설정합니다. 이렇게 하면 두 번째 플롯이 첫 번째 플롯과 동일한 x 축을 공유하게 됩니다.

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
