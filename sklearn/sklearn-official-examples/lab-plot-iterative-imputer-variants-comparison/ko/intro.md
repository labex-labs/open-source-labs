# 소개

이 실습에서는 Scikit-Learn 의 `IterativeImputer` 클래스를 사용하여 데이터 세트에서 누락된 값을 대체하는 방법을 배웁니다. 캘리포니아 주택 데이터 세트에서 각 행에서 임의의 하나의 값을 제거한 후 `BayesianRidge` 추정기를 사용할 때 `IterativeImputer`에 가장 적합한 추정기를 비교해 보겠습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
