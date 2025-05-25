# 소개

이 랩은 Matplotlib 에서 날짜 정밀도와 에포크 (epoch) 를 처리하는 방법을 단계별로 보여주는 랩입니다. Matplotlib 는 이러한 날짜를 인식하고 부동 소수점 숫자로 변환하는 단위 변환기를 사용하여 `.datetime` 객체와 `numpy.datetime64` 객체를 사용할 수 있습니다. Matplotlib 3.3 이전에는 이 변환의 기본값으로 "0000-12-31T00:00:00" 이후의 일수를 나타내는 부동 소수점이 반환되었습니다. Matplotlib 3.3 부터는 "1970-01-01T00:00:00" 이후의 일수가 기본값입니다. 이는 최신 날짜에 대해 더 많은 해상도를 허용합니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 액세스하십시오.

때로는 Jupyter Notebook 로딩이 완료될 때까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한 사항으로 인해 작업의 유효성 검사는 자동화할 수 없습니다.

학습 중에 문제가 발생하면 언제든지 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 신속하게 해결해 드리겠습니다.
