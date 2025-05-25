# 채워진 다각형 생성

이제 `fill()` 함수를 사용하여 채워진 다각형을 생성할 수 있습니다. Koch 설화 함수를 사용하여 다각형의 좌표를 생성합니다.

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
