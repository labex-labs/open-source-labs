# 막대 그래프 생성

0 에서 5 까지의 X 축 값과 해당 Y 축 값을 사용하여 막대 그래프를 생성합니다. `pyplot` 모듈에서 제공하는 `bar` 함수를 사용하여 막대 그래프를 생성합니다.

```python
# X 축 값 생성
x = np.arange(0, 5, 0.1)

# Y 축 값 생성
y = np.sin(x)

# 막대 그래프 생성
plt.bar(x, y)

# 그래프에 제목과 레이블 추가
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 표시
plt.show()
```
