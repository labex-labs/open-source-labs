# 소개

이 랩에서는 pandas 라이브러리에서 희소 데이터 구조를 사용하는 방법을 안내합니다. 이는 대부분의 데이터가 유사한 값 (예: 0 또는 NaN) 으로 구성되어 메모리에서 더 효율적으로 표현할 수 있는 대용량 데이터를 다루는 시나리오에서 유용합니다. `SparseArray`, `SparseDtype`, 희소 접근자 (sparse accessor), 희소 계산 및 scipy 희소 행렬과의 상호 작용에 대해 배우게 됩니다.

## VM 팁

VM 시작이 완료되면, 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 신속하게 해결해 드리겠습니다.
