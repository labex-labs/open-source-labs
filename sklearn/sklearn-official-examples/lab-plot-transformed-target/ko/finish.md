# 요약

이 실습에서는 scikit-learn 라이브러리의 TransformedTargetRegressor 를 사용하는 방법을 배웠습니다. 선형 회귀 모델을 학습하기 전에 타겟 값을 변환하는 것이 가져오는 이점을 관찰하기 위해 두 개의 다른 데이터 세트에 적용했습니다. 합성 데이터와 Ames 주택 데이터 세트를 사용하여 타겟 값을 변환하는 영향을 보여주었습니다. 로그 함수가 타겟을 선형화하여 중앙 절대 오차 (MedAE) 와 같은 유사한 선형 모델로도 더 나은 예측을 가능하게 한다는 것을 관찰했습니다. 또한, Ames 주택 데이터 세트의 경우 변환기의 효과가 약했지만, R2 가 증가하고 MedAE 가 크게 감소하는 결과를 얻었습니다.
