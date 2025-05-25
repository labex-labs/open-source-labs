# 소개

이 랩에서는 Python Matplotlib 에서 agg 백엔드를 직접 사용하여 이미지를 생성하는 과정을 안내합니다. agg 백엔드는 pyplot 인터페이스를 사용하여 그림, 그림 닫기 등을 관리하지 않고 코드에 대한 완전한 제어를 원하는 웹 애플리케이션 개발자에게 유용합니다. 이 랩에서는 agg 캔버스의 내용을 파일로 저장하는 방법과 이를 numpy 배열로 추출하는 방법을 보여줍니다. 이 numpy 배열은 Pillow 로 전달될 수 있습니다.

## VM 팁

VM 시작이 완료되면, 왼쪽 상단을 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한 사항으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중에 문제가 발생하면 언제든지 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 신속하게 해결해 드리겠습니다.
