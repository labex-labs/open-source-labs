# 소개

이 실습에서는 `process::Child`가 종료될 때까지 기다리는 방법을 배울 수 있습니다. `Child::wait`를 호출하면 `process::ExitStatus`를 반환합니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
