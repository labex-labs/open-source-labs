# RefCell`<T>`/Rc`<T>`와 Mutex`<T>`/Arc`<T>`의 유사점

`counter`가 불변이지만 내부 값에 대한 가변 참조를 얻을 수 있다는 것을 눈치챘을 것입니다. 이는 `Mutex<T>`가 `Cell` 패밀리가 하는 것처럼 내부 가변성을 제공한다는 것을 의미합니다. 15 장에서 `Rc<T>` 내부의 내용을 변경할 수 있도록 `RefCell<T>`를 사용했던 방식과 마찬가지로, `Arc<T>` 내부의 내용을 변경하기 위해 `Mutex<T>`를 사용합니다.

또 다른 주목할 세부 사항은 `Mutex<T>`를 사용할 때 Rust 가 모든 종류의 논리적 오류로부터 보호할 수 없다는 것입니다. 15 장에서 `Rc<T>`를 사용하면 두 개의 `Rc<T>` 값이 서로를 참조하여 메모리 누수를 일으키는 참조 사이클을 생성할 위험이 있다는 것을 기억하십시오. 마찬가지로, `Mutex<T>`는 _deadlock_(교착 상태) 을 생성할 위험이 있습니다. 이는 연산이 두 개의 리소스를 잠가야 하고 두 스레드가 각각 하나의 잠금을 획득하여 서로 영원히 기다리게 될 때 발생합니다. 교착 상태에 관심이 있다면, 교착 상태가 있는 Rust 프로그램을 만들고, 모든 언어에서 뮤텍스에 대한 교착 상태 완화 전략을 연구한 다음, Rust 에서 구현해 보십시오. `Mutex<T>` 및 `MutexGuard`에 대한 표준 라이브러리 API 문서는 유용한 정보를 제공합니다.

이 장을 마무리하면서 `Send` 및 `Sync` 트레이트와 사용자 정의 타입과 함께 사용하는 방법에 대해 이야기하겠습니다.
