# 소개

최근접 이웃 회귀는 머신 러닝 알고리즘으로, 새로운 데이터 포인트의 값을 예측하기 위해 학습 데이터 세트에서 k 개의 가장 가까운 데이터 포인트를 찾고, 그 평균값을 사용하여 새로운 값을 예측합니다. 이 실습에서는 scikit-learn 을 사용하여 k-최근접 이웃을 이용한 회귀 문제 해결 방법과 중심점 (barycenter) 및 일정 가중치를 사용한 타겟 보간법을 보여줍니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)을 연습에 사용할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
