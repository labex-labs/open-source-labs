# 소개

이 랩에서는 코루틴을 사용하여 데이터 처리 파이프라인을 구축하는 방법을 배우게 됩니다. 파이썬의 강력한 기능인 코루틴은 협력적 멀티태스킹을 지원하여 함수가 일시 중지되었다가 나중에 실행을 재개할 수 있도록 합니다.

이 랩의 목표는 파이썬에서 코루틴이 어떻게 작동하는지 이해하고, 코루틴 기반의 데이터 처리 파이프라인을 구현하며, 여러 코루틴 단계를 통해 데이터를 변환하는 것입니다. `cofollow.py` (코루틴 기반 파일 팔로워) 와 `coticker.py` (코루틴을 사용하는 주식 시세 표시기 애플리케이션) 의 두 파일을 생성합니다. 이전 연습에서 `stocksim.py` 프로그램이 백그라운드에서 실행 중이며 로그 파일에 주식 데이터를 생성하고 있다고 가정합니다.
