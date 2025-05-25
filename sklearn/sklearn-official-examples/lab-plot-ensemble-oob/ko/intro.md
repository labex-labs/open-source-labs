# 소개

이 실습에서는 Python scikit-learn 라이브러리를 사용하여 랜덤 포레스트 모델의 Out-Of-Bag (OOB) 오류율을 측정하는 방법을 보여줍니다. OOB 오류율은 각 학습 관측치에 대해 해당 관측치가 포함되지 않은 부트스트랩 샘플의 트리 예측을 사용하여 계산된 평균 오류입니다. 이를 통해 랜덤 포레스트 모델을 학습하는 동안 학습 및 검증을 수행할 수 있습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
