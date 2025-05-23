# 요약

이 랩에서는 파이썬에서 코루틴을 사용하여 데이터 처리 파이프라인을 구축하는 방법을 배웠습니다. 주요 개념에는 코루틴의 작동 방식, 초기화 (priming) 의 필요성, 초기화를 위한 데코레이터 (decorators) 사용과 같은 코루틴 기본 사항 이해가 포함됩니다. 또한 `send()` 메서드를 통해 파이프라인을 통해 데이터를 푸시하는 데이터 흐름을 탐색했으며, 이는 제너레이터 (generator) 의 "풀 (pull)" 모델과는 다릅니다.

또한 CSV 데이터 구문 분석, 레코드 필터링 및 출력 형식 지정과 같은 작업에 특화된 코루틴을 만들었습니다. 여러 코루틴을 연결하여 파이프라인을 구성하고 필터링 및 변환 작업을 구현하는 방법을 배웠습니다. 코루틴은 스트리밍 데이터 처리를 위한 강력한 접근 방식을 제공하여 관심사의 깔끔한 분리 (separation of concerns) 와 개별 단계의 쉬운 수정을 가능하게 합니다.
