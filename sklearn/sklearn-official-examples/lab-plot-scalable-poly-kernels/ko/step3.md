# 커널 근사 모델 설정

이제 PolynomialCountSketch 를 사용하여 생성된 특징에 대해 서로 다른 n_components 값으로 선형 SVM 을 학습합니다. n_components 의 다양한 값을 반복하는 루프를 사용하여 각 모델의 정확도를 출력합니다.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

n_runs = 1
N_COMPONENTS = [250, 500, 1000, 2000]

for n_components in N_COMPONENTS:
    ps_lsvm_score = 0
    for _ in range(n_runs):
        # PolynomialCountSketch 로 생성된 특징에 대한 선형 SVM 학습
        pipeline = make_pipeline(
            PolynomialCountSketch(n_components=n_components, degree=4),
            LinearSVC(dual="auto"),
        )
        pipeline.fit(X_train, y_train)
        ps_lsvm_score += 100 * pipeline.score(X_test, y_test)

    ps_lsvm_score /= n_runs

    # 모델의 정확도 출력
    print(f"{n_components} PolynomialCountSketch 특징에 대한 선형 SVM 점수: {ps_lsvm_score:.2f}%")
```
