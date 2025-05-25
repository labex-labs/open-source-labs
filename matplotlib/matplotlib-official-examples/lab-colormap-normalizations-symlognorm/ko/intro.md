# 소개

데이터 시각화에서 컬러맵 (colormap) 은 색상을 통해 수치 데이터를 표현하는 데 사용됩니다. 하지만, 때로는 데이터 분포가 비선형적일 수 있으며, 이는 데이터의 세부 사항을 구별하기 어렵게 만들 수 있습니다. 이러한 경우, 컬러맵 정규화 (colormap normalization) 를 사용하여 컬러맵을 비선형 방식으로 데이터에 매핑하여 데이터를 보다 정확하게 시각화할 수 있습니다. Matplotlib 은 `SymLogNorm` 및 `AsinhNorm`을 포함한 여러 정규화 방법을 제공하며, 이를 사용하여 컬러맵을 정규화할 수 있습니다. 이 랩에서는 `SymLogNorm` 및 `AsinhNorm`을 사용하여 컬러맵을 비선형 데이터에 매핑하는 방법을 보여줍니다.

## VM 팁

VM 시작이 완료되면, 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 액세스하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중에 문제가 발생하면 언제든지 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 즉시 해결해 드리겠습니다.
