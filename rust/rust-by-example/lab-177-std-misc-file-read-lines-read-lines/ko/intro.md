# 소개

이 실습에서는 Rust 에서 파일에서 라인을 읽는 데 대한 단순 구현과 더 효율적인 구현을 제공합니다. 단순한 방법은 파일을 하나의 문자열로 읽어 `read_to_string`을 사용하고, 그런 다음 라인으로 분할하는 반면, 더 효율적인 방법은 전체 내용을 메모리에 로드하지 않고 파일을 라인 단위로 읽는 `BufReader`를 사용합니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
