# 소개

이 실습에서는 RBF 커널의 특징 맵을 RBFSampler 및 Nystroem 을 사용하여 근사하여 SVM 을 사용한 숫자 데이터셋 분류에 대한 특징 맵을 근사합니다. 원래 공간에서 선형 SVM, 근사 매핑을 사용한 선형 SVM, 커널화된 SVM 을 사용한 결과를 비교합니다. 다양한 수의 몬테 카를로 샘플링 (RBFSampler 의 경우 랜덤 푸리에 특징을 사용) 과 근사 매핑을 위한 훈련 세트의 서로 다른 크기의 부분 집합에 대한 시간 및 정확도를 보여줍니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증을 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
