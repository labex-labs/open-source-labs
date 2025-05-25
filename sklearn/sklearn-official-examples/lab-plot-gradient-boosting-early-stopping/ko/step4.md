# 조기 종료를 사용한 모델 구축 및 학습

이제 조기 종료를 사용하여 경사 부스팅 모델을 구축하고 학습합니다. 유효성 검사* 비율을 지정하여 모델의 유효성 검사 손실을 평가하기 위해 학습에서 제외될 전체 데이터 세트의 비율을 나타냅니다. 경사 부스팅 모델은 학습 집합을 사용하여 학습되고 유효성 검사 집합을 사용하여 평가됩니다. 회귀 트리의 각 추가 단계가 추가될 때마다 유효성 검사 집합을 사용하여 모델을 평가합니다. 이는 마지막 n_iter_no_change 단계의 모델 점수가 적어도 tol 만큼 개선되지 않을 때까지 계속됩니다. 그 후, 모델이 수렴한 것으로 간주되고 추가 단계의 추가는 "조기에 중단"됩니다. 최종 모델의 단계 수는 속성 n_estimators*에서 확인할 수 있습니다.

```python
gbes = ensemble.GradientBoostingClassifier(
        n_estimators=n_estimators,
        validation_fraction=0.2,
        n_iter_no_change=5,
        tol=0.01,
        random_state=0,
    )
start = time.time()
gbes.fit(X_train, y_train)
time_gbes.append(time.time() - start)
```
