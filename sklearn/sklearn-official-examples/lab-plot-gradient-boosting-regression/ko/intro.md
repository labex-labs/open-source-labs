# 소개

이 실습에서는 경사 부스팅 (Gradient Boosting) 을 사용하여 당뇨병 회귀 예측 모델을 구축합니다. diabetes 데이터셋으로 모델을 학습하고 `sklearn.ensemble.GradientBoostingRegressor`를 사용하여 최소 제곱 손실 (least squares loss) 과 깊이 4 의 500 개 회귀 트리로 결과를 얻습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습용 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
