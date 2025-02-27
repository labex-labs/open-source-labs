# Tracer l'importance des fonctionnalités

Pour cet exemple, nous utiliserons les importances des fonctionnalités basées sur l'impureté pour identifier les fonctionnalités les plus prédictives.

```python
feature_importance = reg.feature_importances_
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + 0.5
fig = plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.barh(pos, feature_importance[sorted_idx], align="center")
plt.yticks(pos, np.array(diabetes.feature_names)[sorted_idx])
plt.title("Feature Importance (MDI)")
```
