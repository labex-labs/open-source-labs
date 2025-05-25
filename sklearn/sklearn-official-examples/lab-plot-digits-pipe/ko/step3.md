# 데이터셋 로드 및 GridSearchCV 매개변수 정의

숫자 데이터셋을 로드하고 GridSearchCV 를 위한 매개변수를 정의합니다. PCA 절단 및 분류기 정규화에 대한 매개변수를 설정합니다.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```
