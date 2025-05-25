# 분류기 정의

데이터셋에 대한 여러 분류기를 정의합니다.

```python
C = 10
kernel = 1.0 * RBF([1.0, 1.0])  # GPC 를 위한 커널

# 서로 다른 분류기를 만듭니다.
classifiers = {
    "L1 로지스틱 회귀": LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 로지스틱 회귀 (다항 분류)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 로지스틱 회귀 (OvR)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="ovr", max_iter=10000
    ),
    "선형 SVC": SVC(kernel="linear", C=C, probability=True, random_state=0),
    "GPC": GaussianProcessClassifier(kernel),
}
```
