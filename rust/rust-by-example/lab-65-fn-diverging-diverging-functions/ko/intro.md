# 소개

이 실습에서는 Rust 에서 `!`로 표시되는 발산 함수 (diverging function) 에 대해 배웁니다. 발산 함수는 절대로 반환하지 않으며, 반환 타입은 빈 타입입니다. 이는 단 하나의 가능한 값만을 갖는 `()` 타입과 다릅니다. 발산 함수는 `match` 분기와 같이 다른 타입으로 캐스팅해야 할 때 유용할 수 있습니다. 또한, 영원히 루프하거나 프로세스를 종료하는 함수의 반환 타입이기도 합니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
