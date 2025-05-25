# 소개

이 실습에서는 Scikit-Learn 의 `VotingClassifier`를 사용하여 두 가지 특징에 기반한 아이리스 꽃의 종류를 예측합니다. `DecisionTreeClassifier`, `KNeighborsClassifier`, 그리고 `SVC` 분류기를 개별적으로 예측한 결과를 비교하고, `VotingClassifier`를 사용하여 예측 결과를 결합하여 더 나은 결과를 얻을 수 있는지 확인합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
