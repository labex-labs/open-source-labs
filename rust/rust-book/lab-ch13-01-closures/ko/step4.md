# 참조 캡처 또는 소유권 이동

클로저는 환경에서 세 가지 방식으로 값을 캡처할 수 있으며, 이는 함수가 매개변수를 가져올 수 있는 세 가지 방식과 직접적으로 매핑됩니다. 불변으로 빌리기, 가변으로 빌리기, 소유권을 가져오기입니다. 클로저는 캡처된 값으로 함수 본문이 수행하는 작업에 따라 이러한 방식 중 어느 것을 사용할지 결정합니다.

Listing 13-4 에서, 값을 출력하기 위해 불변 참조만 필요하기 때문에 `list`라는 벡터에 대한 불변 참조를 캡처하는 클로저를 정의합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
  2 only_borrows();
    println!("After calling closure: {:?}", list);
}
```

Listing 13-4: 불변 참조를 캡처하는 클로저 정의 및 호출

이 예제는 또한 변수가 클로저 정의에 바인딩될 수 있음 \[1]을 보여주며, 나중에 변수 이름이 함수 이름인 것처럼 변수 이름과 괄호를 사용하여 클로저를 호출할 수 있습니다 \[2].

`list`에 대한 여러 개의 불변 참조를 동시에 가질 수 있으므로, 클로저 정의 전, 클로저 정의 후, 클로저 호출 전, 클로저 호출 후에도 `list`에 계속 접근할 수 있습니다. 이 코드는 컴파일되고 실행되며 다음을 출력합니다.

    Before defining closure: [1, 2, 3]
    Before calling closure: [1, 2, 3]
    From closure: [1, 2, 3]
    After calling closure: [1, 2, 3]

다음으로, Listing 13-5 에서 클로저 본문을 변경하여 `list` 벡터에 요소를 추가합니다. 이제 클로저는 가변 참조를 캡처합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {:?}", list);
}
```

Listing 13-5: 가변 참조를 캡처하는 클로저 정의 및 호출

이 코드는 컴파일되고 실행되며 다음을 출력합니다.

```rust
Before defining closure: [1, 2, 3]
After calling closure: [1, 2, 3, 7]
```

`borrows_mutably` 클로저의 정의와 호출 사이에 더 이상 `println!`이 없다는 점에 유의하십시오. `borrows_mutably`가 정의되면 `list`에 대한 가변 참조를 캡처합니다. 클로저를 호출한 후에는 클로저를 다시 사용하지 않으므로 가변 빌림이 종료됩니다. 클로저 정의와 클로저 호출 사이에는 가변 빌림이 있는 경우 다른 빌림이 허용되지 않으므로 출력을 위한 불변 빌림이 허용되지 않습니다. 거기에 `println!`을 추가하여 어떤 오류 메시지가 나오는지 확인해 보세요!

클로저 본문이 엄격하게 소유권이 필요하지 않더라도 클로저가 환경에서 사용하는 값의 소유권을 가져오도록 강제하려면 매개변수 목록 앞에 `move` 키워드를 사용할 수 있습니다.

이 기술은 주로 클로저를 새 스레드로 전달하여 새 스레드가 데이터를 소유하도록 데이터를 이동할 때 유용합니다. 스레드와 스레드를 사용하려는 이유에 대해서는 동시성에 대해 이야기할 때 16 장에서 자세히 설명하겠지만, 지금은 `move` 키워드가 필요한 클로저를 사용하여 새 스레드를 생성하는 방법을 간략하게 살펴보겠습니다. Listing 13-6 은 메인 스레드 대신 새 스레드에서 벡터를 출력하도록 수정된 Listing 13-4 를 보여줍니다.

파일 이름: `src/main.rs`

```rust
use std::thread;

fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 thread::spawn(move || {
      2 println!("From thread: {:?}", list)
    }).join().unwrap();
}
```

Listing 13-6: 스레드에 대한 클로저가 `list`의 소유권을 가져오도록 강제하기 위해 `move` 사용

새 스레드를 생성하고 스레드에 인수로 실행할 클로저를 제공합니다. 클로저 본문은 목록을 출력합니다. Listing 13-4 에서 클로저는 출력을 위해 필요한 `list`에 대한 최소한의 접근 권한이므로 불변 참조를 사용하여 `list`를 캡처했습니다. 이 예제에서는 클로저 본문이 여전히 불변 참조만 필요하지만 \[2], 클로저 정의의 시작 부분에 `move` 키워드 \[1]를 넣어 `list`가 클로저로 이동해야 함을 지정해야 합니다. 새 스레드는 메인 스레드의 나머지 부분이 완료되기 전에 완료될 수 있거나, 메인 스레드가 먼저 완료될 수 있습니다. 메인 스레드가 `list`의 소유권을 유지하지만 새 스레드 전에 종료되어 `list`를 삭제하면 스레드의 불변 참조가 유효하지 않게 됩니다. 따라서 컴파일러는 참조가 유효하도록 `list`가 새 스레드에 제공된 클로저로 이동하도록 요구합니다. `move` 키워드를 제거하거나 클로저가 정의된 후 메인 스레드에서 `list`를 사용하여 어떤 컴파일러 오류가 발생하는지 확인해 보세요!
