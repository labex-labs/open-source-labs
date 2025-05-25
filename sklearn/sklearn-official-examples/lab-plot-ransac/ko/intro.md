# 소개

이 실습에서는 scikit-learn 의 RANSAC 알고리즘을 사용하여 결함 있는 데이터에 선형 모델을 강건하게 적합하는 방법을 보여줍니다. 일반적인 선형 회귀 분석기는 이상치에 민감하며, 적합된 직선은 데이터의 실제 기저 관계에서 쉽게 벗어날 수 있습니다. RANSAC 회귀 분석기는 자동으로 데이터를 내부 데이터 포인트 (inliers) 와 외부 데이터 포인트 (outliers) 로 분류하고, 적합된 직선은 식별된 내부 데이터 포인트에 의해서만 결정됩니다. scikit-learn 의 `make_regression` 데이터셋을 사용하여 이상치가 있는 랜덤 데이터를 생성하고, 이 데이터에 선형 모델과 RANSAC 회귀 분석기를 모두 적합해 보겠습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제약으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
