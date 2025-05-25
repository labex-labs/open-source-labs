# 플롯 사용자 정의

x 및 y 축에 레이블을 추가하고, 플롯에 제목을 추가하고, 범례를 추가하여 플롯을 사용자 정의할 수 있습니다. 또한 선 스타일과 색상을 변경할 수도 있습니다.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
