# 소개

이 실습에서는 Rust 에서 구조 분해 (destructuring) 와 참조 해제 (dereferencing) 개념을 탐구하고, C/C++ 와 같은 언어와의 사용 차이점을 강조합니다. 구조 분해는 `&`, `ref`, `ref mut`를 사용하여 참조를 할당하고 일치시키는 반면, 참조 해제는 `*`를 사용하여 참조가 가리키는 값에 접근합니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
