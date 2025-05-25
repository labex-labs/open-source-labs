# 소개

이 실습에서는 KNeighborsClassifier 를 사용하기 전에 k-최근접 이웃을 미리 계산하는 방법을 보여줍니다. KNeighborsClassifier 는 내부적으로 최근접 이웃을 계산할 수 있지만, 미리 계산하면 매개변수 제어를 세밀하게 조정하거나 여러 번 사용할 때 캐싱하거나 사용자 정의 구현을 할 수 있는 등 여러 가지 이점이 있습니다. 여기서는 파이프라인의 캐싱 기능을 사용하여 KNeighborsClassifier 의 여러 적합 (fit) 사이에 최근접 이웃 그래프를 캐싱합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제약으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
