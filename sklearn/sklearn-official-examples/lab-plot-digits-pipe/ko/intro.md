# 소개

이 실습에서는 주성분 분석 (PCA) 과 로지스틱 회귀를 사용하여 차원 축소 및 분류 파이프라인을 구축합니다. scikit-learn 라이브러리를 사용하여 PCA 를 통해 숫자 데이터셋에서 비지도 차원 축소를 수행합니다. 그런 다음 분류를 위해 로지스틱 회귀 모델을 사용합니다. GridSearchCV 를 사용하여 PCA 의 차원을 설정하고 PCA 절단과 분류기 정규화의 최적 조합을 찾을 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증을 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
