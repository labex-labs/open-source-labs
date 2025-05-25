# 요약

이 랩에서는 `multiprocessing` 라이브러리와 Matplotlib 을 사용하여 별도의 프로세스에서 생성된 데이터를 플로팅하는 방법을 배웠습니다. 플로팅과 데이터 생성을 각각 처리하기 위해 `ProcessPlotter`와 `NBPlot` 두 개의 클래스를 생성했습니다. `NBPlot` 클래스는 임의의 데이터를 생성하여 파이프를 통해 `ProcessPlotter` 클래스로 전송했으며, `ProcessPlotter`는 이 데이터를 실시간으로 플로팅했습니다.
