# 소개

이 랩에서는 Rust 에서 구조체의 출력 형식을 사용자 정의하기 위해 `fmt::Display` 트레이트를 구현하는 방법을 배우게 됩니다. 또한 `fmt::Display`와 `fmt::Debug`의 차이점과 제네릭 컨테이너 타입에 대한 `fmt::Display`의 제한 사항도 살펴볼 것입니다. 마지막으로, 새로운 `Complex` 구조체에 대해 `fmt::Display` 트레이트를 구현하고 특정 형식으로 출력하는 활동을 수행하게 됩니다.

> **참고:** 랩에서 파일 이름을 지정하지 않은 경우, 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일하고 실행할 수 있습니다.
