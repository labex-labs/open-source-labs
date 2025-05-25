# 소개

이 튜토리얼에서는 Detection Error Tradeoff (DET) 곡선과 Receiver Operating Characteristic (ROC) 곡선을 비교해 볼 것입니다. DET 곡선은 ROC 곡선의 변형으로, y 축에 True Positive Rate (TPR) 대신 False Negative Rate (FNR) 를 표시합니다. 머신 러닝을 위한 인기있는 파이썬 라이브러리인 scikit-learn 을 사용하여 합성 데이터를 생성하고, ROC 및 DET 곡선을 통해 두 분류기의 임계값별 통계적 성능을 비교해 보겠습니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습용 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속하십시오.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공해 주시면 문제를 신속하게 해결해 드리겠습니다.
