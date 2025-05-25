# 소개

이 실습에서는 개발 종속성 (development dependencies) 의 개념을 설명합니다. 개발 종속성은 `Cargo.toml` 파일의 `[dev-dependencies]` 섹션에 추가되며, 테스트, 예제 또는 벤치마크에 사용됩니다. 개발 종속성의 예로 `pretty_assertions`가 있습니다. 이 라이브러리는 `assert_eq!` 및 `assert_ne!`와 같은 표준 매크로를 확장하여 다채로운 차이점을 제공합니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs` 파일을 사용하고 `rustc main.rs && ./main` 명령어로 컴파일 및 실행할 수 있습니다.
