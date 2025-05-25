# PCA 수행

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

입력 데이터에서 특징을 추출하기 위해 주성분 분석 (PCA) 을 수행합니다. 주성분의 개수를 150 으로 설정하고 학습 데이터에 PCA 모델을 적합시킵니다. 그런 다음 고유 얼굴 (eigenfaces) 을 얻고 입력 데이터를 주성분으로 변환합니다.
