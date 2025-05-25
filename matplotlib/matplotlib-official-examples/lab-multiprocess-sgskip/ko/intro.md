# 소개

이 랩에서는 multiprocessing 라이브러리와 Matplotlib 를 사용하여 별도의 프로세스에서 생성된 데이터를 플롯하는 방법을 배우게 됩니다. 플로팅과 데이터 생성을 각각 처리하기 위해 `ProcessPlotter`와 `NBPlot`이라는 두 개의 클래스를 생성할 것입니다. `NBPlot` 클래스는 임의의 데이터를 생성하여 파이프를 통해 `ProcessPlotter` 클래스로 전송하고, `ProcessPlotter` 클래스는 이 데이터를 실시간으로 플롯합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 액세스하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한 사항으로 인해 작업의 유효성 검사는 자동화할 수 없습니다.

학습 중에 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 즉시 해결해 드리겠습니다.
