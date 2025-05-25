# 소개

기계 학습에서 특징 선택은 중요한 단계입니다. 이는 모델의 정확성과 성능을 향상시키기 위해 데이터 세트에서 가장 관련성이 높은 특징을 선택하는 것을 포함합니다. scikit-learn 에서는 `sklearn.feature_selection` 모듈이 특징 선택 및 차원 축소를 위한 다양한 방법을 제공합니다.

이 실습에서는 scikit-learn 을 사용하여 특징 선택 과정을 안내합니다. 낮은 분산을 가진 특징 제거, 단변량 특징 선택, 재귀적 특징 제거 및 SelectFromModel 을 사용한 특징 선택과 같은 기술을 다룰 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
