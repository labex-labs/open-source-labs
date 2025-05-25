# 소개

이 튜토리얼에서는 등척성 회귀 (isotonic regression) 에 대해 배웁니다. 등척성 회귀는 비모수적 회귀 기법으로, 학습 데이터의 평균 제곱 오차를 최소화하면서 함수의 비감소 근사값을 찾습니다. 파이썬의 인기 머신러닝 라이브러리인 scikit-learn 을 사용하여 등척성 회귀를 구현하고 선형 회귀와 비교해 보겠습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제약으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
