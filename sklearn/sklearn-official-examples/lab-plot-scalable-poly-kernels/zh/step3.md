# 建立核近似模型

现在，我们将在由PolynomialCountSketch生成的具有不同n_components值的特征上训练线性支持向量机（SVM）。我们将使用一个循环来遍历不同的n_components值，并打印每个模型的准确率。

```python
from sklearn.kernel_approximation import PolynomialCountSketch

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # 在由PolynomialCountSketch生成的特征上训练一个线性SVM
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # 打印模型的准确率
    print(f"Linear SVM score on {n_components} PolynomialCountSketch features: {ps_lsvm_score:.2f}%")
```
