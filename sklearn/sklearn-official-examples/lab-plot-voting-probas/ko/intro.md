# 소개

이 실습에서는 Scikit-Learn 의 VotingClassifier 가 계산한 클래스 확률을 시각화하는 방법을 배웁니다. LogisticRegression, GaussianNB, 그리고 RandomForestClassifier 를 포함한 세 가지 다른 분류기를 사용하고, VotingClassifier 를 통해 예측된 확률을 평균화합니다. 그런 다음 각 분류기를 학습 데이터 세트에 맞추고 데이터 세트의 첫 번째 샘플에 대한 예측된 클래스 확률을 플롯하여 확률 가중치를 시각화합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
