# 산점도 생성

무작위 데이터 포인트를 사용하여 산점도를 생성합니다.

```python
# 재현성을 위해 무작위 상태 고정
np.random.seed(19680801)

# 무작위 데이터 포인트 생성
x, y = np.random.normal(size=(2, 200))

# 산점도 생성
plt.plot(x, y, 'o')
plt.show()
```
