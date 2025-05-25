# LabelPropagation 을 이용한 레이블 학습

알 수 없는 샘플의 레이블을 학습하기 위해 `LabelSpreading`을 사용합니다.

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
