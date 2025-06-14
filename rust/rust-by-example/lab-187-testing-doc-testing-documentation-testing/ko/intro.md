# 소개

이 실습에서 Rust 프로젝트를 문서화하는 주요 방법은 CommonMark Markdown 사양으로 작성된 소스 코드에 설명 주석을 추가하는 것입니다. 이 주석은 코드 블록을 포함할 수 있습니다. Rust 는 정확성을 관리하며, 이러한 코드 블록은 컴파일되어 설명 문서 테스트로 사용됩니다. 이러한 테스트는 `cargo test` 명령을 사용할 때 자동으로 실행됩니다. 설명 문서 테스트의 목적은 기능을 연습하는 예제 역할을 하고, 설명 문서의 예제를 완전한 코드 스니펫으로 사용할 수 있도록 하는 것입니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
