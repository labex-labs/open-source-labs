# 소개

이 랩에서는 Rust 의 명시적 생명주기 어노테이션 (explicit lifetime annotations) 개념을 소개합니다. 이는 차용 검사기 (borrow checker) 가 참조 (reference) 의 유효성을 결정하는 데 사용됩니다.

> **참고:** 랩에서 파일 이름을 지정하지 않은 경우, 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고, `rustc main.rs && ./main`으로 컴파일하고 실행할 수 있습니다.
