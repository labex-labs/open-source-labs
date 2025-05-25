# 소개

양분할 군집화 (Biclustering) 는 데이터 행렬의 행과 열을 동시에 군집화하는 방법입니다. 이를 통해 데이터 행렬 내 특정 속성을 가진 하위 행렬을 식별할 수 있습니다. 양분할 군집화는 데이터 분석, 이미지 처리 및 생물정보학과 같은 다양한 분야에서 유용합니다.

이 실습에서는 scikit-learn 의 `sklearn.cluster.bicluster` 모듈을 사용하여 양분할 군집화를 수행하는 방법을 배울 것입니다. 우리는 두 가지 일반적인 양분할 군집화 알고리즘, 스펙트럼 공동 군집화 (Spectral Co-Clustering) 와 스펙트럼 양분할 군집화 (Spectral Biclustering) 를 탐색할 것입니다. 이러한 알고리즘은 행과 열을 양분할 군집에 정의하고 할당하는 방식이 다릅니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근하십시오.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
