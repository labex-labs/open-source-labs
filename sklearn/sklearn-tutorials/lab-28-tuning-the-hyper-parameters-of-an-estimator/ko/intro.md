# 소개

하이퍼파라미터는 추정기 (estimator) 에 의해 직접 학습되지 않는 파라미터입니다. 추정기 클래스의 생성자에 인수로 전달됩니다. 추정기의 하이퍼파라미터를 조정하는 것은 효과적인 머신 러닝 모델을 구축하는 중요한 단계입니다. 이는 모델의 최상의 성능을 얻는 최적의 하이퍼파라미터 조합을 찾는 것을 포함합니다.

Scikit-learn 은 최상의 하이퍼파라미터를 검색하기 위한 여러 도구를 제공합니다: `GridSearchCV`와 `RandomizedSearchCV`입니다. 이 실습에서는 이러한 도구를 사용하여 하이퍼파라미터를 조정하는 과정을 살펴볼 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
