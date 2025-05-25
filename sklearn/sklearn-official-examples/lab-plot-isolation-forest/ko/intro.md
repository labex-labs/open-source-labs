# 소개

이 실습에서는 이상 탐지에 Isolation Forest 를 사용하는 과정을 살펴봅니다. 먼저 두 개의 클러스터와 몇 개의 이상치를 포함하는 데이터셋을 생성한 후, Isolation Forest 모델을 학습하여 이상치를 식별합니다. 마지막으로 모델의 결정 경계를 시각화하여 내부 데이터 포인트와 이상치를 어떻게 분리하는지 확인합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
