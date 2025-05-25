# 소개

이 실습에서는 와인 리뷰 데이터셋에서 다양한 범주형 인코더의 성능을 비교합니다. 예측 대상 변수로 'points' 열을 사용합니다. 다음 인코더를 비교합니다: TargetEncoder, OneHotEncoder, OrdinalEncoder, 그리고 범주 제거. 또한, `HistGradientBoostingRegressor`의 기본 범주형 특징 지원 방법도 살펴봅니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습용 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
