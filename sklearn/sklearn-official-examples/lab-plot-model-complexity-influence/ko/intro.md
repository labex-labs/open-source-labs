# 소개

이 실험에서는 모델 복잡성이 예측 정확성과 계산 성능에 미치는 영향을 살펴봅니다. 회귀를 위한 Diabetes 데이터셋과 분류를 위한 20newsgroups 데이터셋을 사용합니다. 선택된 세 가지 추정기 (estimator) 에서 모델 복잡성의 영향을 분석합니다.

- SGDClassifier (분류 데이터용): 확률적 경사 하강법 학습을 구현합니다.
- NuSVR (회귀 데이터용): Nu 서포트 벡터 회귀를 구현합니다.
- GradientBoostingRegressor: 순차적 단계별 방식으로 가산 모델을 구축합니다.

선택된 모델의 관련 모델 매개변수를 변경하여 모델 복잡성을 조절합니다. 이어서 계산 성능 (지연 시간) 과 예측력 (MSE 또는 해밍 손실) 에 미치는 영향을 측정합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제약으로 인해 작업 검증을 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
