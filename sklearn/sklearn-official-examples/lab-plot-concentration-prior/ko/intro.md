# 소개

이 실습에서는 scikit-learn 의 `BayesianGaussianMixture` 클래스를 사용하여 세 개의 가우시안 혼합으로 구성된 예제 데이터 세트를 맞추는 방법을 보여줍니다. 이 클래스는 `weight_concentration_prior_type` 매개변수를 사용하여 농도 사전 (prior) 을 지정하여 자동으로 혼합 구성 요소의 수를 조정할 수 있습니다. 이 실습에서는 0 이 아닌 가중치를 가진 구성 요소의 수를 선택하기 위해 디리클레 분포 사전과 디리클레 프로세스 사전을 사용하는 차이점을 보여줍니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
