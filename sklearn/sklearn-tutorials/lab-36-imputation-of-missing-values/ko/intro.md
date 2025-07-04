# 소개

많은 실제 데이터셋은 누락된 값을 포함하고 있으며, 이는 완전하고 수치적인 데이터를 가정하는 머신 러닝 알고리즘을 사용할 때 문제를 일으킬 수 있습니다. 이러한 경우, 사용 가능한 데이터를 최대한 활용하기 위해 누락된 값을 적절하게 처리하는 것이 중요합니다. 일반적인 전략 중 하나는 누락된 값을 데이터의 알려진 부분을 기반으로 채우는 것인, 이를 임퓨테이션 (imputation) 이라고 합니다.

이 튜토리얼에서는 파이썬의 인기 머신 러닝 라이브러리인 scikit-learn 을 사용하여 누락된 값을 임퓨테이션하는 다양한 전략을 살펴볼 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
