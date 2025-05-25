# 이상치 점수 확인

이상치 예측 외에도 각 관측치에 대한 이상치 점수를 `negative_outlier_factor_` 속성을 통해 확인할 수 있습니다. 점수가 낮을수록 이상치일 가능성이 높습니다.

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```
