# 소개

이 튜토리얼에서는 Matplotlib 을 사용하여 스케일 불변 각도 레이블을 만드는 방법을 배웁니다. 각도 주석은 종종 선 사이 또는 원형 호를 사용하여 도형 내부의 각도를 표시하는 데 사용됩니다. Matplotlib 은 `~.patches.Arc`를 제공하지만, 이러한 목적으로 직접 사용할 때 내재된 문제는 데이터 공간에서 원형인 호가 디스플레이 공간에서 반드시 원형이 아니라는 것입니다. 또한, 호의 반경은 실제 데이터 좌표와 독립적인 좌표계에서 정의하는 것이 가장 좋습니다. 적어도 주석이 무한대로 커지지 않고 플롯을 자유롭게 확대/축소할 수 있으려면 말입니다. 이는 호의 중심은 데이터 공간에서 정의되지만 반경은 포인트 또는 픽셀과 같은 물리적 단위 또는 Axes 차원의 비율로 정의되는 솔루션을 필요로 합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 액세스하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중에 문제가 발생하면 언제든지 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 신속하게 해결해 드리겠습니다.
