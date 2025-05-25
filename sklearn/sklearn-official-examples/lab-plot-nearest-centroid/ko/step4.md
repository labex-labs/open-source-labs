# 분류기 생성 및 학습

0.2 의 축소 (shrinkage) 값을 가진 최근접 중심 분류기 (Nearest Centroid Classifier) 의 인스턴스를 생성하고 데이터를 학습합니다.

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```
