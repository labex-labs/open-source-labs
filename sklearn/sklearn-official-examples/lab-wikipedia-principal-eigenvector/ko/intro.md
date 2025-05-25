# 소개

이 실습에서는 위키피디아 문서 내 링크 그래프를 분석하여 고유벡터 중심성에 따라 문서의 상대적 중요도를 평가합니다. 주요 고유벡터를 계산하는 전통적인 방법은 멱법입니다. 여기서는 scikit-learn 에 구현된 Martinsson 의 무작위 SVD 알고리즘을 사용할 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
