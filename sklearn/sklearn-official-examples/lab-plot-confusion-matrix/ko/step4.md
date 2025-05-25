# 모델 학습

선형 커널을 사용하여 서포트 벡터 머신 (SVM) 분류기를 학습할 것입니다. 결과에 미치는 영향을 보기 위해 너무 낮은 정규화 매개변수 C 를 사용할 것입니다.

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
