# 소개

이 실습에서는 `while` 키워드를 사용하여 지정된 조건이 참인 동안 반복되는 루프를 만드는 방법을 배웁니다. 이 사용법을 보여주기 위해 Rust 로 FizzBuzz 프로그램을 작성합니다. 이 프로그램은 `while` 루프를 사용하여 1 부터 100 까지의 숫자를 반복합니다. 루프 내부에서 현재 숫자가 3 과 5 로 나누어지는지 (즉, 15 의 배수인지) 확인하고, 그런 경우 "fizzbuzz"를 출력합니다. 숫자가 3 으로만 나누어지는 경우 "fizz"를 출력하고, 5 로만 나누어지는 경우 "buzz"를 출력합니다. 다른 모든 숫자의 경우에는 숫자 자체를 출력합니다. 루프는 카운터 변수가 101 에 도달할 때까지 계속되며, 각 숫자 또는 레이블을 출력한 후 증가합니다.

> **참고:** 실습에서 파일 이름을 지정하지 않으면 원하는 파일 이름을 사용할 수 있습니다. 예를 들어 `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일 및 실행할 수 있습니다.
