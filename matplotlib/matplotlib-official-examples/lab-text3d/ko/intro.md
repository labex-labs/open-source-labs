# 소개

이 랩에서는 Python 의 Matplotlib 라이브러리를 사용하여 3D 플롯에 텍스트 주석을 배치하는 방법을 시연합니다. 다음 기능이 다루어집니다.

- 세 가지 유형의 _zdir_ 값을 사용하여 `~.Axes3D.text` 함수 사용: None, 축 이름 (예: 'x'), 또는 방향 튜플 (예: (1, 1, 0)).
- color 키워드를 사용하여 `~.Axes3D.text` 함수 사용.
- `.text2D` 함수를 사용하여 ax 객체의 고정된 위치에 텍스트 배치.

## VM 팁

VM 시작이 완료되면, 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중에 문제가 발생하면 언제든지 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 신속하게 해결해 드리겠습니다.
