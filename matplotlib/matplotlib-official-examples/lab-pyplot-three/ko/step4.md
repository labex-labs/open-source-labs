# 레이블 및 제목 추가

이 단계에서는 플롯에 제목을 추가하고 x 축과 y 축에 레이블을 지정합니다.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.title("Multiple Datasets")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()
```
