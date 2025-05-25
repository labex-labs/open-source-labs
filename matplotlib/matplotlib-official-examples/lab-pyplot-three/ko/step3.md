# 데이터 플롯

이 단계에서는 Matplotlib 의 `plot` 함수를 사용하여 세 개의 모든 데이터 세트를 단일 호출로 플롯합니다. 첫 번째 데이터 세트에는 빨간색 대시 (dashes), 두 번째 데이터 세트에는 파란색 사각형 (squares), 세 번째 데이터 세트에는 녹색 삼각형 (triangles) 을 사용합니다.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
