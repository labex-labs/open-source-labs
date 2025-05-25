# 소개

이 실습에서는 환자의 당뇨병 진행 상황을 예측하기 위해 투표 회귀 분석 (Voting Regressor) 을 사용합니다. 데이터 예측을 위해 그래디언트 부스팅 회귀 분석 (Gradient Boosting Regressor), 랜덤 포레스트 회귀 분석 (Random Forest Regressor), 선형 회귀 분석 (Linear Regression) 세 가지 회귀 분석 모델을 사용합니다. 그 후, 위 세 가지 회귀 분석 모델을 투표 회귀 분석에 사용합니다. 마지막으로, 모든 모델의 예측 결과를 비교하기 위해 플롯을 그립니다.

당뇨병 환자 코호트에서 수집된 10 개의 특징으로 구성된 당뇨병 데이터 세트를 사용합니다. 목표는 기준 시점으로부터 1 년 후 질병 진행 정도의 정량적 측정값입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
