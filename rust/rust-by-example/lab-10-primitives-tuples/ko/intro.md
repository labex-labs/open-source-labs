# 소개

이 랩에서는 Rust 의 튜플 (tuple) 을 탐구합니다. 튜플은 서로 다른 타입의 값들을 묶어 놓은 컬렉션이며, 괄호를 사용하여 생성됩니다. 튜플은 함수 인자 (argument) 및 반환 값으로 사용될 수 있으며, 함수가 여러 값을 반환할 수 있도록 합니다. 튜플은 다른 튜플의 멤버로도 사용될 수 있습니다. Rust 는 튜플 내의 값에 접근하기 위해 튜플 인덱싱 (tuple indexing) 을 제공합니다. 튜플은 출력 가능하며, 바인딩 (binding) 을 생성하기 위해 분해 (destructure) 될 수 있습니다. 또한, 구조체 (struct) 의 출력 형식을 사용자 정의하기 위해 `fmt::Display` 트레이트 (trait) 를 추가하는 방법을 배웁니다. 마지막으로, 행렬 (matrix) 의 두 요소를 교환하는 `transpose` 함수를 구현하는 활동을 수행합니다.

> **참고:** 랩에서 파일 이름을 지정하지 않은 경우, 원하는 파일 이름을 사용할 수 있습니다. 예를 들어, `main.rs`를 사용하고 `rustc main.rs && ./main`으로 컴파일하고 실행할 수 있습니다.
