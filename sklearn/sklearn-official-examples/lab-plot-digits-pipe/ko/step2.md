# 파이프라인 구성 요소 정의

PCA, 표준화 스케일러, 로지스틱 회귀를 포함한 파이프라인 구성 요소를 정의합니다. 예시를 빠르게 하기 위해 허용 오차를 큰 값으로 설정합니다.

```python
# PCA 절단과 분류기 정규화의 최적 조합을 검색하기 위한 파이프라인을 정의합니다.
pca = PCA()
# 입력을 정규화하기 위한 표준화 스케일러를 정의합니다.
scaler = StandardScaler()

logistic = LogisticRegression(max_iter=10000, tol=0.1)

pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])
```
