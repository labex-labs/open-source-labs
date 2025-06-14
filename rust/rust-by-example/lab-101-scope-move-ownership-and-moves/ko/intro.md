# 소개

이 랩에서는 Rust 에서 변수가 리소스의 소유권을 가지며 하나의 소유자만 가질 수 있다는 점을 설명합니다. 이는 리소스가 여러 번 해제되는 것을 방지합니다. 변수가 할당되거나 함수 인수가 값으로 전달될 때 리소스의 소유권이 이전되는데, 이를 "이동 (move)"이라고 합니다. 이동 후에는 이전 소유자를 더 이상 사용할 수 없어서, 댕글링 포인터 (dangling pointer) 생성을 방지합니다. 코드 예제는 스택 할당 및 힙 할당 변수의 소유권이 어떻게 이전되는지, 그리고 소유권이 이동된 후 변수에 접근하면 어떤 오류가 발생하는지를 보여주면서 이러한 개념을 설명합니다.

> **참고:** 랩에서 파일 이름을 지정하지 않은 경우, 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일하고 실행할 수 있습니다.
