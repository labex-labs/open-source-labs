# 소개

이 실습에서 코드 예제의 모듈 파일 계층 구조는 다음과 같이 나타낼 수 있습니다. "my"라는 디렉토리가 있으며, 이 디렉토리에는 "inaccessible.rs"와 "nested.rs"라는 두 개의 파일이 있습니다. 또한 "my.rs"라는 파일과 "split.rs"라는 파일이 있습니다. "split.rs" 파일에는 "my.rs" 파일에 정의된 "my" 모듈이 포함되어 있으며, "my.rs" 파일에는 각각 "inaccessible.rs"와 "nested.rs" 파일에 정의된 "inaccessible"와 "nested" 모듈이 포함되어 있습니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
