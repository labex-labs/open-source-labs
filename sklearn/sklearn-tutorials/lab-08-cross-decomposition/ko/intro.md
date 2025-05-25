# 소개

scikit-learn 의 `cross_decomposition` 모듈은 차원 축소 및 회귀를 위한 지도 학습 추정기 (supervised estimators) 를 포함하며, 특히 부분 최소 제곱 (PLS) 알고리즘을 제공합니다. 이러한 알고리즘은 두 행렬 사이의 기본적인 관계를 찾아, 변환된 행렬 간의 공분산이 최대가 되도록 두 행렬을 저차원 공간에 투영합니다.

이 실습에서는 scikit-learn 에서 제공하는 다양한 교차 분해 알고리즘을 탐색하고, 차원 축소 및 회귀 작업에 사용하는 방법을 배웁니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제약으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
