# 특성 중요도 시각화

이 예제에서는 불순도 기반 특성 중요도를 사용하여 가장 예측력이 높은 특성을 식별합니다.

```python
feature_importance = reg.feature_importances_
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + 0.5
fig = plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.barh(pos, feature_importance[sorted_idx], align="center")
plt.yticks(pos, np.array(diabetes.feature_names)[sorted_idx])
plt.title("특성 중요도 (MDI)")
```
