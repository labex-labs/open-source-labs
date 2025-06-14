# 소개

이 실습에서는 Rust 에서 서로 다른 타입 간 변환에 사용되는 `From` 및 `Into` 트레이트의 개념을 탐구합니다. 이러한 트레이트는 본질적으로 연결되어 있으며, `Into`는 `From`의 역입니다. `From` 트레이트는 타입이 다른 타입으로부터 자신을 생성하는 방법을 정의할 수 있도록 하여 타입 간 쉬운 변환을 가능하게 합니다. `Into` 트레이트는 필요할 때 자동으로 `From` 구현을 호출합니다. 두 트레이트 모두 사용자 정의 타입에 구현될 수 있어 타입 변환에 유연성을 제공합니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
