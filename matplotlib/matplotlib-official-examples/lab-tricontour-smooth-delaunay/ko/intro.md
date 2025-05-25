# 소개

이 튜토리얼은 Matplotlib 을 사용하여 고해상도 삼각 등고선 플롯을 생성하는 방법을 보여줍니다. 삼각 등고선 (Tricontouring) 은 비정형 삼각 메쉬 (unstructured triangular mesh) 에서 데이터를 표현하는 데 사용되는 기술입니다. 데이터가 불규칙하게 간격이 떨어진 지점에서 수집되거나, 데이터가 본질적으로 삼각 형태를 띨 때 자주 사용됩니다. 이 튜토리얼에서는 임의의 점 집합을 생성하고, 해당 점에 대한 들로네 삼각 분할 (Delaunay triangulation) 을 수행하고, 메쉬의 일부 삼각형을 마스크 처리하고, 데이터를 정제 및 보간하고, 마지막으로 Matplotlib 의 `tricontour` 함수를 사용하여 정제된 데이터를 플롯하는 방법을 보여줍니다.

## VM 팁

VM 시작이 완료되면, 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중에 문제가 발생하면 언제든지 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 신속하게 해결해 드리겠습니다.
