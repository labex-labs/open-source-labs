# 소개

이 랩에서는 단일 변수의 구조 분해 내에서 부분 이동 (partial move) 에 대해 배우며, 여기서 `by-move` 및 `by-reference` 패턴 바인딩을 동시에 사용할 수 있습니다. 이는 변수의 부분 이동을 초래하여 일부 부분을 이동시키는 동시에 다른 부분은 여전히 참조할 수 있도록 합니다. 부모 변수가 부분적으로 이동된 경우, 이후에는 전체로 사용할 수 없지만, 참조만 되고 이동되지 않은 부분은 여전히 사용할 수 있습니다.

> **참고:** 랩에서 파일 이름을 지정하지 않은 경우, 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일하고 실행할 수 있습니다.
