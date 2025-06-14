# 소개

이 랩에서는 Rust 프로그래밍 언어의 맥락에서 별칭 (aliasing) 의 개념을 탐구합니다. 별칭은 동일한 데이터에 대한 여러 참조가 생성되는 상황을 의미하며, 불변 (immutable) 또는 가변 (mutable) 차용 (borrow) 형태로 나타납니다.

> **참고:** 랩에서 파일 이름을 지정하지 않은 경우, 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고, `rustc main.rs && ./main`으로 컴파일하고 실행할 수 있습니다.
