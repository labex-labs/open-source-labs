# 소개

이 실습에서는 scikit-learn 의 `cross_val_predict` 및 `PredictionErrorDisplay` 함수를 사용하여 교차 검증을 통해 모델 예측값과 오차를 시각화하는 방법을 배웁니다. 당뇨병 데이터셋을 로드하고 선형 회귀 모델 인스턴스를 생성한 후 교차 검증을 사용하여 예측값 배열을 얻습니다. 그런 다음 `PredictionErrorDisplay`를 사용하여 실제 값 대 예측 값, 그리고 잔차 대 예측 값을 플롯합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
