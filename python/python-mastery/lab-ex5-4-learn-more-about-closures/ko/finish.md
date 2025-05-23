# 요약

이 랩에서는 Python 의 클로저 (closure) 에 대한 고급 측면에 대해 배웠습니다. 먼저, 클로저를 데이터 구조로 사용하는 것을 탐구했습니다. 이는 데이터를 캡슐화하고 클래스나 전역 변수에 의존하지 않고도 함수가 호출 간에 상태를 유지할 수 있도록 합니다. 둘째, 클로저가 코드 생성기 (code generator) 역할을 하여 속성 유효성 검사에 대한 보다 기능적인 접근 방식으로 타입 검사 (type checking) 를 갖춘 속성 객체를 생성하는 방법을 살펴보았습니다.

또한 디스크립터 프로토콜 (descriptor protocol) 과 `__set_name__` 메서드를 사용하여 클래스 정의에서 이름을 자동으로 캡처하는 우아한 타입 검사 속성을 만드는 방법을 배웠습니다. 이러한 기술은 클로저의 강력함과 유연성을 보여주며, 복잡한 동작을 간결하게 구현할 수 있도록 합니다. 클로저와 디스크립터를 이해하면 유지 관리 가능하고 강력한 Python 코드를 생성하기 위한 더 많은 도구를 얻을 수 있습니다.
