# 소개

이 튜토리얼에서는 scikit-learn 에서 커널 근사 기술을 사용하는 방법을 안내합니다.

서포트 벡터 머신 (SVM) 과 같은 커널 방법은 비선형 분류에 강력한 기술입니다. 이러한 방법은 입력 데이터를 고차원 특징 공간으로 매핑하는 커널 함수의 개념에 의존합니다. 그러나 명시적인 특징 매핑을 사용하는 것은, 특히 대규모 데이터셋의 경우 계산적으로 비용이 많이 들 수 있습니다. 커널 근사 방법은 커널 특징 공간의 저차원 근사값을 생성하여 해결책을 제공합니다.

이 튜토리얼에서는 Nystroem 방법, Radial Basis Function(RBF) 커널 근사, Additive Chi Squared(ACS) 커널 근사, Skewed Chi Squared(SCS) 커널 근사, 그리고 Tensor Sketch 를 사용한 다항식 커널 근사를 포함하여 scikit-learn 에서 사용 가능한 여러 커널 근사 기술을 탐색할 것입니다. 이러한 기술을 사용하는 방법과 장단점에 대해 설명할 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근하십시오.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
