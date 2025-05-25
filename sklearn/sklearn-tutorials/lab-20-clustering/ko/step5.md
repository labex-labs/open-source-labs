# 군집 시각화

k-평균 알고리즘으로 생성된 군집을 시각화해 보겠습니다.

```python
# 각 데이터 포인트의 군집 레이블 가져오기
labels = kmeans.labels_

# 색상으로 군집을 구분하여 데이터 포인트 플롯
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('특징 1')
plt.ylabel('특징 2')
plt.show()
```
