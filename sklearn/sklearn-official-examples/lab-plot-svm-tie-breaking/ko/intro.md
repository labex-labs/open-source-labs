# 소개

이 실습에서는 SVM 결정 경계에 미치는 SVM 타이 브레이킹 (tie-breaking) 의 효과를 소개합니다. SVM 에서 타이 브레이킹은 두 개 이상의 클래스의 거리가 같을 때 발생하는 충돌을 해결하는 메커니즘입니다. `decision_function_shape='ovr'`일 때 기본적으로 활성화되어 있지 않으며, 비용이 많이 들기 때문입니다. 따라서 이 실습에서는 다중 클래스 분류 문제에 대한 `break_ties` 매개변수의 효과와 `decision_function_shape='ovr'`를 보여줍니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)을 연습에 사용할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
