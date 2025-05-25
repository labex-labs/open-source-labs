# 소개

이 랩에서는 Python Pandas 에서 Copy-On-Write (CoW) 개념을 이해하고 구현하는 방법에 대한 단계별 가이드를 제공합니다. CoW 는 복사를 가능한 한 늦게 수행함으로써 성능과 메모리 사용량을 향상시키는 최적화 전략입니다. 또한, 여러 객체의 의도하지 않은 수정을 방지하는 데도 도움이 됩니다.

## VM 팁

VM 시작이 완료되면, 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 실습을 위해 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속하십시오.

때로는 Jupyter Notebook 이 로딩을 완료하는 데 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한 사항으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 언제든지 Labby 에게 문의하십시오. 세션 후 피드백을 제공해주시면 문제를 신속하게 해결해 드리겠습니다.
