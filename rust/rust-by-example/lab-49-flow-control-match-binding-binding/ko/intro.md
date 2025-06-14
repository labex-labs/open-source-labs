# 소개

이 실습에서는 Rust 에서의 바인딩 개념을 탐구합니다. 바인딩은 변수에 간접적으로 접근하고, 재바인딩 없이 변수를 분기하고 사용할 수 있도록 합니다. `match` 문에서 `@` 기호는 값을 이름에 바인딩하는 데 사용됩니다. 값을 특정 범위에 바인딩하는 방법과 `Option`과 같은 `enum` 변형을 "구조 분해"하는 방법을 포함한 예제가 제공됩니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
