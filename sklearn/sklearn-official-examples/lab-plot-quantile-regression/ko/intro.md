# 소개

이 튜토리얼에서는 scikit-learn 을 사용하여 분위수 회귀를 수행하는 방법을 보여줍니다. 두 개의 합성 데이터 세트를 생성하여 분위수 회귀가 어떻게 중요하지 않은 조건부 분위수를 예측할 수 있는지 보여줄 것입니다. `QuantileRegressor` 클래스를 사용하여 중앙값과 5% 및 95% 로 고정된 낮은 분위수 및 높은 분위수를 추정할 것입니다. `QuantileRegressor`를 `LinearRegression`과 비교하고 평균 절대 오차 (MAE) 및 평균 제곱 오차 (MSE) 를 사용하여 성능을 평가할 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
