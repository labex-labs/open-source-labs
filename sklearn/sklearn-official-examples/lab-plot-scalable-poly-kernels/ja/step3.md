# カーネル近似モデルの構築

ここでは、異なる `n_components` の値を持つ `PolynomialCountSketch` によって生成された特徴で線形 SVM を訓練します。`n_components` の異なる値をループして各モデルの精度を表示します。

```python
from sklearn.kernel_approximation import PolynomialCountSketch

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # PolynomialCountSketch によって生成された特徴で線形 SVM を訓練
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # モデルの精度を表示
    print(f"Linear SVM score on {n_components} PolynomialCountSketch features: {ps_lsvm_score:.2f}%")
```
