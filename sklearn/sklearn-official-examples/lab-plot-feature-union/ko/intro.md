# 소개

이 실습에서는 파이썬의 scikit-learn 라이브러리를 사용하여 여러 특징 추출 방법을 연결하는 방법을 배웁니다. PCA 와 단변량 선택으로 얻은 특징을 결합하기 위해 `FeatureUnion` 변환기를 사용합니다. 이 변환기를 사용하여 특징을 결합하면 전체 프로세스에 대한 교차 검증 및 그리드 검색을 수행할 수 있는 이점이 있습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
