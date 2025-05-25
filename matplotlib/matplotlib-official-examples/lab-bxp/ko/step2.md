# 상자 그림 통계 계산

`matplotlib.cbook` 모듈의 `boxplot_stats()` 함수는 상자 그림에 필요한 통계를 계산합니다. 데이터와 레이블을 매개변수로 전달합니다.

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
