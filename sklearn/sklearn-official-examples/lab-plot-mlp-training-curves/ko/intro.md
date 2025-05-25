# 소개

이 실습에서는 Scikit-learn MLPClassifier 를 사용하여 SGD 와 Adam 을 포함한 다양한 확률적 학습 전략의 성능을 비교하는 과정을 안내합니다. MLPClassifier 는 역전파를 사용하여 신경망의 가중치를 최적화하는 신경망 분류기입니다. 이 실습의 목표는 서로 다른 확률적 학습 전략이 MLPClassifier 의 학습 손실 곡선에 어떤 영향을 미치는지 보여주는 것입니다. 이 예제에서는 여러 개의 작은 데이터셋을 사용하지만, 이러한 예제에서 보여주는 일반적인 경향은 대규모 데이터셋에도 적용되는 것으로 보입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
