# 소개

주성분 회귀 (PCR) 와 부분 최소 제곱 회귀 (PLS) 는 회귀 분석에 사용되는 두 가지 방법입니다. PCR 은 훈련 데이터에 PCA 를 적용한 후 변환된 샘플에 회귀자를 훈련시키는 것을 포함합니다. PCA 변환은 비지도 학습이므로 대상에 대한 정보를 사용하지 않습니다. 결과적으로, 대상이 낮은 분산을 가진 방향과 강하게 상관되는 일부 데이터 세트에서 PCR 의 성능이 저하될 수 있습니다.

PLS 는 변환기이자 회귀자이며 PCR 과 매우 유사합니다. 변환된 데이터에 선형 회귀자를 적용하기 전에 샘플에 차원 축소를 적용하기도 합니다. PCR 과의 주요 차이점은 PLS 변환이 지도 학습이라는 것입니다. 따라서 위에서 언급한 문제가 발생하지 않습니다.

이 실험실에서는 소규모 데이터 세트에서 PCR 과 PLS 를 비교할 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
