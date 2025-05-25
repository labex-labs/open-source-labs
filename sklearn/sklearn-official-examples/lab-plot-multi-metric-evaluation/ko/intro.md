# 소개

이 튜토리얼에서는 Scikit-Learn 의 GridSearchCV 함수에 대해 배웁니다. GridSearchCV 는 주어진 모델에 대한 최상의 하이퍼파라미터를 검색하는 함수입니다. 추정기의 지정된 파라미터 값에 대한 철저한 검색 (exhaustive search) 을 수행합니다. 이러한 방법을 적용하는 데 사용되는 추정기의 파라미터는 파라미터 그리드에 대한 교차 검증 그리드 검색 (cross-validated grid-search) 을 통해 최적화됩니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
