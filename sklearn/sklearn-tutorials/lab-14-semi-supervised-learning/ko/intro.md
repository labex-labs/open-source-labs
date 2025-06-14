# 소개

이 실습에서는 레이블이 지정된 학습 데이터와 레이블이 지정되지 않은 학습 데이터가 혼합된 머신러닝 유형인 준지도 학습 (semi-supervised learning) 개념을 탐구합니다. 준지도 학습 알고리즘은 레이블이 지정되지 않은 데이터를 활용하여 모델의 성능을 향상시키고 새로운 샘플에 대한 일반화 능력을 높일 수 있습니다. 이는 레이블이 지정된 데이터가 적고 레이블이 지정되지 않은 데이터가 많은 경우에 특히 유용합니다.

이 실습에서는 자기훈련 (Self Training) 과 레이블 전파 (Label Propagation) 라는 두 가지 준지도 학습 알고리즘에 중점을 둘 것입니다. 파이썬의 인기 머신러닝 라이브러리인 scikit-learn 을 사용하여 이러한 알고리즘을 구현하고 사용하는 방법을 배울 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
