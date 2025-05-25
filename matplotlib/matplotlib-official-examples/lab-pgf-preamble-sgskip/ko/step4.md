# 그래프 사용자 정의

색상, 선 스타일 (line style), 마커 (marker) 를 변경하여 그래프를 사용자 정의할 수 있습니다. 다음은 예시입니다.

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
