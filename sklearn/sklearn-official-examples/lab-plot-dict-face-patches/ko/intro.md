# 소개

이 실습에서는 scikit-learn API 를 사용하여 얼굴 이미지의 대규모 데이터셋을 처리하고 얼굴을 나타내는 20x20 이미지 패치 세트를 학습하는 방법을 보여줍니다. 이 실습의 핵심은 온라인 학습을 사용하는 것입니다. 이미지를 하나씩 로드하고 처리하며 각 이미지에서 50 개의 임의 패치를 추출합니다. 10 개의 이미지에서 500 개의 패치를 축적한 후 온라인 KMeans 객체, MiniBatchKMeans 의 partial_fit 메서드를 실행합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 로드되는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
