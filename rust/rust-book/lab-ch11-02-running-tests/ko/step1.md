# 테스트 실행 제어 방법

`cargo run`이 코드를 컴파일한 다음 결과 바이너리를 실행하는 것처럼, `cargo test`는 코드를 테스트 모드로 컴파일하고 결과 테스트 바이너리를 실행합니다. `cargo test`에 의해 생성된 바이너리의 기본 동작은 모든 테스트를 병렬로 실행하고 테스트 실행 중에 생성된 출력을 캡처하여 출력이 표시되지 않도록 하고 테스트 결과와 관련된 출력을 더 쉽게 읽을 수 있도록 하는 것입니다. 그러나 명령줄 옵션을 지정하여 이 기본 동작을 변경할 수 있습니다.

일부 명령줄 옵션은 `cargo test`로 전달되고, 일부는 결과 테스트 바이너리로 전달됩니다. 이 두 가지 유형의 인수를 구분하기 위해, `cargo test`로 전달되는 인수를 나열한 다음 구분자 `--`를 사용하고, 그 다음에 테스트 바이너리로 전달되는 인수를 나열합니다. `cargo test --help`를 실행하면 `cargo test`와 함께 사용할 수 있는 옵션이 표시되고, `cargo test -- --help`를 실행하면 구분자 뒤에 사용할 수 있는 옵션이 표시됩니다.
