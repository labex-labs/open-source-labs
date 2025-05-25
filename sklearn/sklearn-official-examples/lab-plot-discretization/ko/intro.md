# 소개

이 실습에서는 Scikit-learn 의 KBinsDiscretizer 클래스를 사용하여 연속적인 특징을 이산화하는 방법을 보여줍니다. 이산화는 특징 값을 여러 구간 (bin) 으로 나누어 연속적인 특징을 이산적인 특징으로 변환하는 과정입니다. 이는 선형 관계만 모델링할 수 있는 선형 모델을 사용하거나 의사결정 트리의 복잡성을 줄이는 데 유용할 수 있습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
