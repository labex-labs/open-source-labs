# 스레드와 함께 move 클로저 사용하기

`thread::spawn`에 전달되는 클로저와 함께 `move` 키워드를 자주 사용합니다. 이는 클로저가 환경에서 사용하는 값의 소유권을 가져와서 해당 값의 소유권을 한 스레드에서 다른 스레드로 이전하기 때문입니다. "클로저로 환경 캡처하기"에서 클로저의 맥락에서 `move`에 대해 논의했습니다. 이제 `move`와 `thread::spawn` 간의 상호 작용에 더 집중하겠습니다.

Listing 16-1 에서 `thread::spawn`에 전달하는 클로저가 인수를 받지 않는다는 점에 유의하세요. 생성된 스레드의 코드에서 메인 스레드의 데이터를 사용하지 않고 있습니다. 메인 스레드의 데이터를 생성된 스레드에서 사용하려면 생성된 스레드의 클로저가 필요한 값을 캡처해야 합니다. Listing 16-3 은 메인 스레드에서 벡터를 생성하고 이를 생성된 스레드에서 사용하려는 시도를 보여줍니다. 그러나 잠시 후에 보시겠지만, 이것은 아직 작동하지 않습니다.

파일 이름: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Listing 16-3: 다른 스레드에서 메인 스레드가 생성한 벡터를 사용하려는 시도

클로저는 `v`를 사용하므로 `v`를 캡처하여 클로저의 환경의 일부로 만듭니다. `thread::spawn`은 이 클로저를 새로운 스레드에서 실행하므로, 해당 새로운 스레드 내에서 `v`에 접근할 수 있어야 합니다. 그러나 이 예제를 컴파일하면 다음과 같은 오류가 발생합니다.

```bash
error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?}", v);
  |                                           - `v` is borrowed here
  |
note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |       let handle = thread::spawn(|| {
  |  __________________^
7 | |         println!("Here's a vector: {:?}", v);
8 | |     });
  | |______^
help: to force the closure to take ownership of `v` (and any other referenced
variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                                ++++
```

Rust 는 `v`를 캡처하는 방법을 *추론*하고, `println!`은 `v`에 대한 참조만 필요하므로 클로저는 `v`를 빌리려고 시도합니다. 그러나 문제가 있습니다. Rust 는 생성된 스레드가 얼마나 오래 실행될지 알 수 없으므로, `v`에 대한 참조가 항상 유효한지 알 수 없습니다.

Listing 16-4 는 `v`에 대한 유효하지 않은 참조가 있을 가능성이 더 높은 시나리오를 제공합니다.

파일 이름: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    drop(v); // oh no!

    handle.join().unwrap();
}
```

Listing 16-4: 메인 스레드에서 `v`를 삭제하는 클로저가 있는 스레드가 `v`에 대한 참조를 캡처하려고 시도

Rust 가 이 코드를 실행하도록 허용했다면, 생성된 스레드가 전혀 실행되지 않고 즉시 백그라운드로 이동될 가능성이 있습니다. 생성된 스레드는 내부에 `v`에 대한 참조를 가지고 있지만, 메인 스레드는 15 장에서 논의한 `drop` 함수를 사용하여 즉시 `v`를 삭제합니다. 그런 다음 생성된 스레드가 실행을 시작하면 `v`는 더 이상 유효하지 않으므로, 이에 대한 참조도 유효하지 않습니다. 아, 안돼!

Listing 16-3 의 컴파일러 오류를 수정하려면 오류 메시지의 조언을 사용할 수 있습니다.

    help: to force the closure to take ownership of `v` (and any other referenced
    variables), use the `move` keyword
      |
    6 |     let handle = thread::spawn(move || {
      |                                ++++

클로저 앞에 `move` 키워드를 추가하면 Rust 가 값을 빌리는 대신 클로저가 사용 중인 값의 소유권을 가져오도록 강제합니다. Listing 16-5 에 표시된 Listing 16-3 에 대한 수정 사항은 의도한 대로 컴파일되고 실행됩니다.

파일 이름: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Listing 16-5: `move` 키워드를 사용하여 클로저가 사용하는 값의 소유권을 가져오도록 강제

메인 스레드가 `drop`을 호출한 Listing 16-4 의 코드를 수정하기 위해 동일한 작업을 시도하고 `move` 클로저를 사용할 수도 있습니다. 그러나 이 수정 사항은 작동하지 않습니다. Listing 16-4 가 시도하는 작업은 다른 이유로 허용되지 않기 때문입니다. 클로저에 `move`를 추가하면 `v`를 클로저의 환경으로 이동시키고, 메인 스레드에서 더 이상 `drop`을 호출할 수 없게 됩니다. 대신 다음과 같은 컴파일러 오류가 발생합니다.

```bash
error[E0382]: use of moved value: `v`
  --> src/main.rs:10:10
   |
4  |     let v = vec![1, 2, 3];
   |         - move occurs because `v` has type `Vec<i32>`, which does not
implement the `Copy` trait
5  |
6  |     let handle = thread::spawn(move || {
   |                                ------- value moved into closure here
7  |         println!("Here's a vector: {:?}", v);
   |                                           - variable moved due to use in
closure
...
10 |     drop(v); // oh no!
   |          ^ value used here after move
```

Rust 의 소유권 규칙이 다시 우리를 구했습니다! Listing 16-3 의 코드에서 오류가 발생한 이유는 Rust 가 보수적으로 작동하여 스레드에 대해 `v`를 빌리기만 했기 때문입니다. 즉, 메인 스레드가 이론적으로 생성된 스레드의 참조를 무효화할 수 있었습니다. Rust 에 `v`의 소유권을 생성된 스레드로 이동하도록 지시함으로써, 메인 스레드가 더 이상 `v`를 사용하지 않을 것이라고 Rust 에 보장하는 것입니다. Listing 16-4 를 동일한 방식으로 변경하면, 메인 스레드에서 `v`를 사용하려고 할 때 소유권 규칙을 위반하게 됩니다. `move` 키워드는 Rust 의 보수적인 기본 빌림을 무시합니다. 소유권 규칙을 위반하도록 허용하지 않습니다.

이제 스레드가 무엇인지와 스레드 API 에서 제공하는 메서드를 다뤘으므로, 스레드를 사용할 수 있는 몇 가지 상황을 살펴보겠습니다.
