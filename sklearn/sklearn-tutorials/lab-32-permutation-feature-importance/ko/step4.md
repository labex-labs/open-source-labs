# 변수 중요도 측정 (Permutation Feature Importance)

이제 scikit-learn 의 `permutation_importance` 함수를 사용하여 변수 중요도를 계산하겠습니다. 이 함수는 학습된 모델, 검증 세트, 변수를 셔플할 횟수를 입력으로 받습니다.

```python
from sklearn.inspection import permutation_importance

# 변수 중요도 계산
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# 변수 중요도 출력
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
