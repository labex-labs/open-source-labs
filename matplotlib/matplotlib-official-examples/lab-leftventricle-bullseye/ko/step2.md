# 간단한 꺾은선 그래프 생성

0 에서 5 까지의 X 축 값과 해당 Y 축 값을 사용하여 간단한 꺾은선 그래프를 생성합니다. `pyplot` 모듈에서 제공하는 `plot` 함수를 사용하여 꺾은선 그래프를 생성합니다.

```python
# X 축 값 생성
x = np.arange(0, 5, 0.1)

# Y 축 값 생성
y = np.sin(x)

# 꺾은선 그래프 생성
plt.plot(x, y)

# 그래프에 제목과 레이블 추가
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 표시
plt.show()
```
