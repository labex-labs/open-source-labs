# 소개

이 실습에서는 정보 이론 기준을 사용하여 가우시안 혼합 모델 (GMM) 을 이용한 모델 선택 방법을 배웁니다. 모델 선택은 모델의 공분산 유형과 구성 요소 수 모두를 고려합니다. 적절한 모델을 선택하기 위해 아카이케 정보 기준 (AIC) 과 베이즈 정보 기준 (BIC) 을 사용합니다. 표준 정규 분포에서 무작위로 샘플링하여 두 개의 구성 요소를 생성합니다. 한 구성 요소는 구형이지만 이동 및 재조정됩니다. 다른 구성 요소는 더 일반적인 공분산 행렬을 갖도록 변형됩니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
