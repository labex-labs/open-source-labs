# 플롯 생성

이 단계에서는 이전 단계에서 생성된 마스크 배열을 사용하여 플롯을 생성합니다. 각 마스크 배열을 개별적으로 플롯하고 각 배열에 대해 다른 색상을 사용합니다.

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
