# 소개

이 실습에서는 `ColumnTransformer`를 사용하여 다양한 전처리 및 특징 추출 파이프라인을 특징의 서브셋에 적용하는 방법을 보여줍니다. 이는 특히 이종 데이터 유형을 포함하는 데이터셋의 경우 유용합니다. 숫자 특징은 스케일링하고, 범주형 특징은 원 - 핫 인코딩할 수 있기 때문입니다.

이 실습에서는 OpenML 의 타이타닉 데이터셋을 사용하여 `ColumnTransformer`를 사용하여 범주형 및 숫자 데이터를 모두 전처리하는 파이프라인을 구축하고, 이를 사용하여 로지스틱 회귀 모델을 학습합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습용 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
