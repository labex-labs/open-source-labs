# 파이 차트 생성

다섯 개의 슬라이스로 구성된 파이 차트를 생성하여 서로 다른 데이터 포인트를 나타냅니다. `pyplot` 모듈에서 제공하는 `pie` 함수를 사용하여 파이 차트를 생성합니다.

```python
# 파이 차트 데이터 생성
data = [10, 20, 30, 25, 15]

# 파이 차트 레이블 생성
labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5']

# 파이 차트 생성
plt.pie(data, labels=labels)

# 그래프에 제목 추가
plt.title('Pie Chart')

# 그래프 표시
plt.show()
```
