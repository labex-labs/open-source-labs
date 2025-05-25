# Drop Trait 을 사용한 정리 작업에서 코드 실행

스마트 포인터 패턴에 중요한 두 번째 트레이트는 `Drop`입니다. 이 트레이트를 사용하면 값이 스코프 밖으로 벗어나기 직전에 발생하는 작업을 사용자 정의할 수 있습니다. 모든 타입에 대해 `Drop` 트레이트의 구현을 제공할 수 있으며, 해당 코드는 파일이나 네트워크 연결과 같은 리소스를 해제하는 데 사용될 수 있습니다.

스마트 포인터의 맥락에서 `Drop`을 소개하는 이유는 `Drop` 트레이트의 기능이 거의 항상 스마트 포인터를 구현할 때 사용되기 때문입니다. 예를 들어, `Box<T>`가 drop 될 때 박스가 가리키는 힙의 공간을 할당 해제합니다.

일부 언어에서는 일부 타입의 경우 프로그래머가 해당 타입의 인스턴스 사용을 마칠 때마다 메모리 또는 리소스를 해제하는 코드를 호출해야 합니다. 예로는 파일 핸들, 소켓 및 잠금이 있습니다. 만약 잊어버리면 시스템이 과부하되어 충돌할 수 있습니다. Rust 에서는 값이 스코프 밖으로 벗어날 때 특정 코드 조각이 실행되도록 지정할 수 있으며, 컴파일러가 이 코드를 자동으로 삽입합니다. 결과적으로 특정 타입의 인스턴스 사용이 완료된 프로그램의 모든 곳에 정리 코드를 배치하는 데 주의할 필요가 없으며, 여전히 리소스 누수를 방지할 수 있습니다!

`Drop` 트레이트를 구현하여 값이 스코프 밖으로 벗어날 때 실행할 코드를 지정합니다. `Drop` 트레이트는 `self`에 대한 가변 참조를 받는 `drop`이라는 메서드 하나를 구현하도록 요구합니다. Rust 가 `drop`을 호출하는 시점을 확인하기 위해, 지금은 `println!` 문으로 `drop`을 구현해 보겠습니다.

Listing 15-14 는 `CustomSmartPointer` 구조체를 보여줍니다. 이 구조체의 유일한 사용자 정의 기능은 인스턴스가 스코프 밖으로 벗어날 때 `Dropping CustomSmartPointer!`를 출력하여 Rust 가 `drop` 메서드를 실행하는 시점을 보여주는 것입니다.

Filename: `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

Listing 15-14: `Drop` 트레이트를 구현하는 `CustomSmartPointer` 구조체로, 정리 코드를 넣을 위치입니다.

`Drop` 트레이트는 prelude 에 포함되어 있으므로 스코프로 가져올 필요가 없습니다. `CustomSmartPointer` \[1]에 `Drop` 트레이트를 구현하고 `println!` \[2]을 호출하는 `drop` 메서드에 대한 구현을 제공합니다. `drop` 메서드의 본문은 타입의 인스턴스가 스코프 밖으로 벗어날 때 실행하려는 모든 로직을 넣는 곳입니다. 여기서는 Rust 가 `drop`을 호출하는 시점을 시각적으로 보여주기 위해 텍스트를 출력하고 있습니다.

`main`에서 \[3]과 \[4]에서 `CustomSmartPointer`의 두 인스턴스를 생성한 다음 `CustomSmartPointers created` \[5]를 출력합니다. `main` \[6]의 끝에서 `CustomSmartPointer`의 인스턴스가 스코프 밖으로 벗어나면 Rust 는 `drop` 메서드 \[2]에 넣은 코드를 호출하여 최종 메시지를 출력합니다. `drop` 메서드를 명시적으로 호출할 필요가 없다는 점에 유의하세요.

이 프로그램을 실행하면 다음과 같은 출력을 볼 수 있습니다.

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

Rust 는 인스턴스가 스코프 밖으로 벗어날 때 자동으로 `drop`을 호출하여 우리가 지정한 코드를 호출했습니다. 변수는 생성된 역순으로 drop 되므로 `d`가 `c`보다 먼저 drop 되었습니다. 이 예제의 목적은 `drop` 메서드가 작동하는 방식에 대한 시각적 가이드를 제공하는 것입니다. 일반적으로는 print 메시지 대신 타입이 실행해야 하는 정리 코드를 지정합니다.

불행히도 자동 `drop` 기능을 비활성화하는 것은 간단하지 않습니다. `drop`을 비활성화하는 것은 일반적으로 필요하지 않습니다. `Drop` 트레이트의 요점은 자동으로 처리된다는 것입니다. 그러나 때때로 값을 일찍 정리하고 싶을 수 있습니다. 한 가지 예는 잠금을 관리하는 스마트 포인터를 사용할 때입니다. 동일한 스코프의 다른 코드가 잠금을 획득할 수 있도록 잠금을 해제하는 `drop` 메서드를 강제로 실행하고 싶을 수 있습니다. Rust 는 `Drop` 트레이트의 `drop` 메서드를 수동으로 호출할 수 없도록 합니다. 대신, 스코프가 끝나기 전에 값을 강제로 drop 하려면 표준 라이브러리에서 제공하는 `std::mem::drop` 함수를 호출해야 합니다.

Listing 15-14 의 `main` 함수를 Listing 15-15 와 같이 수정하여 `Drop` 트레이트의 `drop` 메서드를 수동으로 호출하려고 하면 컴파일러 오류가 발생합니다.

Filename: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-15: 일찍 정리하기 위해 `Drop` 트레이트의 `drop` 메서드를 수동으로 호출하려고 시도

이 코드를 컴파일하려고 하면 다음과 같은 오류가 발생합니다.

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

이 오류 메시지는 `drop`을 명시적으로 호출할 수 없다고 명시합니다. 오류 메시지는 *destructor*라는 용어를 사용하는데, 이는 인스턴스를 정리하는 함수에 대한 일반적인 프로그래밍 용어입니다. *destructor*는 인스턴스를 생성하는 *constructor*와 유사합니다. Rust 의 `drop` 함수는 특정 destructor 입니다.

Rust 는 `drop`을 명시적으로 호출할 수 없도록 합니다. Rust 가 `main`의 끝에서 값에 대해 자동으로 `drop`을 호출하기 때문입니다. 이렇게 하면 Rust 가 동일한 값을 두 번 정리하려고 시도하기 때문에 _double free_ 오류가 발생합니다.

값이 스코프 밖으로 벗어날 때 `drop`의 자동 삽입을 비활성화할 수 없으며, `drop` 메서드를 명시적으로 호출할 수도 없습니다. 따라서 값을 일찍 강제로 정리해야 하는 경우 `std::mem::drop` 함수를 사용합니다.

`std::mem::drop` 함수는 `Drop` 트레이트의 `drop` 메서드와 다릅니다. 강제로 drop 하려는 값을 인수로 전달하여 호출합니다. 이 함수는 prelude 에 있으므로 Listing 15-15 의 `main`을 수정하여 Listing 15-16 과 같이 `drop` 함수를 호출할 수 있습니다.

Filename: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-16: `std::mem::drop`을 호출하여 값이 스코프 밖으로 벗어나기 전에 명시적으로 drop

이 코드를 실행하면 다음이 출력됩니다.

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

`Dropping CustomSmartPointer with data`some data`!` 텍스트는 `CustomSmartPointer created.`와 `CustomSmartPointer dropped before the end of main.` 텍스트 사이에 출력되어 `drop` 메서드 코드가 해당 시점에서 `c`를 drop 하기 위해 호출됨을 보여줍니다.

`Drop` 트레이트 구현에 지정된 코드를 여러 가지 방법으로 사용하여 정리를 편리하고 안전하게 만들 수 있습니다. 예를 들어, 이를 사용하여 자체 메모리 할당자를 만들 수 있습니다! `Drop` 트레이트와 Rust 의 소유권 시스템을 사용하면 Rust 가 자동으로 정리하므로 정리하는 것을 기억할 필요가 없습니다.

또한 여전히 사용 중인 값을 실수로 정리하여 발생하는 문제에 대해 걱정할 필요가 없습니다. 참조가 항상 유효하도록 보장하는 소유권 시스템은 값이 더 이상 사용되지 않을 때 `drop`이 한 번만 호출되도록 보장합니다.

`Box<T>`와 스마트 포인터의 몇 가지 특성을 검토했으므로 표준 라이브러리에 정의된 다른 몇 가지 스마트 포인터를 살펴보겠습니다.
