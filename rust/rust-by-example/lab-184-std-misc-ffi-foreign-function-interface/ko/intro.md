# 소개

이 실습에서는 Rust 의 Foreign Function Interface(FFI) 를 학습합니다. FFI 를 통해 `extern` 블록 내에 외래 함수를 선언하고 `#[link]` 속성에 외래 라이브러리 이름을 지정하여 C 라이브러리와 상호 작용할 수 있습니다. 이 코드 예제는 `libm` 라이브러리의 외부 함수를 호출하여 단정밀도 복소수의 제곱근을 계산하고 복소수의 코사인을 계산하는 방법을 보여줍니다. 일반적으로 이러한 안전하지 않은 외래 함수 호출 주변에 안전한 래퍼 (safe wrappers) 를 사용합니다. 이 실습에서는 단정밀도 복소수의 최소 구현을 포함하고, 안전하지 않은 연산을 래핑한 안전한 API 를 호출하는 방법을 보여줍니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs` 파일을 사용하고 `rustc main.rs && ./main` 명령어로 컴파일 및 실행할 수 있습니다.
