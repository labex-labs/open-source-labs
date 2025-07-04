# 소개

이 랩에서는 Rust 의 형식화된 출력 기능을 설명합니다. `std::fmt` 모듈은 출력 작업을 처리하기 위해 `format!`, `print!`, `println!`, `eprint!`, 그리고 `eprintln!`과 같은 매크로를 제공합니다. 이러한 매크로를 사용하면 해당 인수로 대체되는 자리 표시자를 사용하여 텍스트를 형식화할 수 있습니다. 위치 인자 및 명명된 인자를 사용할 수 있으며, 형식 지정 문자를 사용하여 다양한 형식 지정을 적용할 수 있습니다. 또한 매크로는 텍스트 정렬, 숫자 패딩, 그리고 소수점 숫자의 정밀도 설정을 지원합니다. `fmt::Display` 트레이트는 사용자 친화적인 방식으로 텍스트를 형식화하는 데 사용되며, `fmt::Debug` 트레이트는 디버깅 목적으로 사용됩니다. Rust 는 또한 컴파일 시간에 형식 지정의 정확성을 검사합니다. 또한, `fmt::Display` 트레이트를 구현하면 자동으로 `ToString` 트레이트가 구현되며, 사용자 정의 타입은 출력이 가능하도록 `fmt::Display` 트레이트를 구현해야 합니다. 이 랩에는 형식화된 출력 매크로와 트레이트를 사용하는 연습을 위한 활동도 포함되어 있습니다.

> **참고:** 랩에서 파일 이름을 지정하지 않은 경우, 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일하고 실행할 수 있습니다.
