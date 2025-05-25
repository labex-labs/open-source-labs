# 소개

이 실습에서는 Scikit-learn 라이브러리의 `TargetEncoder` 클래스를 사용하는 방법을 배웁니다. 타겟 인코딩은 범주형 데이터를 머신 러닝 알고리즘의 입력으로 사용할 수 있는 숫자 데이터로 변환하는 기술입니다. `TargetEncoder`는 범주형 특징의 각 범주를 해당 범주에 대한 타겟 변수의 평균으로 대체합니다. 이 방법은 범주형 특징과 타겟 변수 사이에 강한 관계가 있는 경우 유용합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습용 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
