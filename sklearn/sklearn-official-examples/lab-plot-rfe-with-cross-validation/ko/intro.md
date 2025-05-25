# 소개

이 실습에서는 scikit-learn 을 사용하여 교차 검증을 통한 재귀적 특징 제거 (RFECV) 를 단계별로 구현하는 과정을 살펴볼 것입니다. RFECV 는 모델 구축에 사용할 관련 특징의 하위 집합을 선택하는 특징 선택 (feature selection) 에 사용됩니다. 15 개의 특징 중 3 개는 정보적이고, 2 개는 중복되며, 10 개는 정보가 없는 특징을 사용하여 분류 작업을 수행할 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
