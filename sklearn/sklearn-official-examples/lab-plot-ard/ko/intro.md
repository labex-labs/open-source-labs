# 소개

이 실습에서는 합성 데이터셋을 사용하여 두 가지 다른 베이지안 회귀 모델인 자동 관련성 결정 (ARD) 과 베이지안 릿지 회귀를 비교합니다. 첫 번째 부분에서는 기준 모델로서 최소자승법 (OLS) 모델을 사용하여 모델의 계수를 실제 계수와 비교합니다. 마지막 섹션에서는 다항식 특징 확장을 사용하여 `X`와 `y` 사이의 비선형 관계를 적합시킨 후 ARD 와 베이지안 릿지 회귀에 대한 예측값과 불확실성을 플롯합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
