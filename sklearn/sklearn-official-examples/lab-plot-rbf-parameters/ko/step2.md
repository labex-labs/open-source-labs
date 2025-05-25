# 분류기 학습

- `np.logspace`를 사용하여 `gamma`와 `C` 매개변수의 로그 스케일 그리드를 생성합니다.
- `StratifiedShuffleSplit`를 사용하여 데이터를 학습 및 테스트 세트로 분할합니다.
- `GridSearchCV`를 사용하여 SVM 모델에 대한 최적의 매개변수를 찾습니다.
- 2 차원 버전의 모든 매개변수에 대해 분류기를 학습합니다.
