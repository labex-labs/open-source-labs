# Static (정적)

Rust 에는 몇 가지 예약된 라이프타임 이름이 있습니다. 그 중 하나가 `'static`입니다. 다음 두 가지 상황에서 이를 접할 수 있습니다.

```rust
// 'static 라이프타임을 가진 참조:
let s: &'static str = "hello world";

// 트레이트 바운드의 일부로서의 'static:
fn generic<T>(x: T) where T: 'static {}
```

두 경우 모두 관련이 있지만 미묘하게 다르며, 이는 Rust 를 배울 때 흔히 혼란을 야기하는 원인입니다. 각 상황에 대한 몇 가지 예는 다음과 같습니다.

## 참조 라이프타임

참조 라이프타임으로서의 `'static`은 참조가 가리키는 데이터가 실행 중인 프로그램의 전체 라이프타임 동안 존재함을 나타냅니다. 더 짧은 라이프타임으로 강제 변환될 수 있습니다.

`'static` 라이프타임을 가진 변수를 만드는 두 가지 방법이 있으며, 둘 다 바이너리의 읽기 전용 메모리에 저장됩니다.

- `static` 선언으로 상수를 만듭니다.
- `string` 리터럴을 만듭니다. 이 리터럴은 `&'static str` 형식을 갖습니다.

각 방법의 예는 다음과 같습니다.

```rust
// `'static` 라이프타임을 가진 상수를 만듭니다.
static NUM: i32 = 18;

// `NUM` 에 대한 참조를 반환하며, 여기서 `'static`
// 라이프타임은 입력 인수의 라이프타임으로 강제 변환됩니다.
fn coerce_static<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // `string` 리터럴을 만들고 출력합니다:
        let static_string = "I'm in read-only memory";
        println!("static_string: {}", static_string);

        // `static_string` 이 범위를 벗어나면, 참조는
        // 더 이상 사용할 수 없지만 데이터는 바이너리에 남아 있습니다.
    }

    {
        // `coerce_static` 에 사용할 정수를 만듭니다:
        let lifetime_num = 9;

        // `NUM` 을 `lifetime_num` 의 라이프타임으로 강제 변환합니다:
        let coerced_static = coerce_static(&lifetime_num);

        println!("coerced_static: {}", coerced_static);
    }

    println!("NUM: {} stays accessible!", NUM);
}
```

## 트레이트 바운드

트레이트 바운드로서, 이는 해당 타입이 비정적 (non-static) 참조를 포함하지 않음을 의미합니다. 예를 들어, 수신자는 원하는 만큼 오랫동안 해당 타입을 유지할 수 있으며, 삭제할 때까지 유효하지 않게 되지 않습니다.

이것이 의미하는 바는 소유된 데이터는 항상 `'static` 라이프타임 바운드를 통과하지만, 해당 소유된 데이터에 대한 참조는 일반적으로 그렇지 않다는 것을 이해하는 것이 중요합니다.

```rust
use std::fmt::Debug;

fn print_it( input: impl Debug + 'static ) {
    println!( "'static value passed in is: {:?}", input );
}

fn main() {
    // i 는 소유되었고 참조를 포함하지 않으므로 'static 입니다:
    let i = 5;
    print_it(i);

    // 이런, &i 는 main() 의 범위에 의해 정의된 라이프타임만 가지므로
    // 'static 이 아닙니다:
    print_it(&i);
}
```

컴파일러는 다음과 같이 알려줍니다.

```ignore
error[E0597]: `i` does not live long enough
  --> src/lib.rs:15:15
   |
15 |     print_it(&i);
   |     ---------^^--
   |     |         |
   |     |         borrowed value does not live long enough
   |     argument requires that `i` is borrowed for `'static`
16 | }
   | - `i` dropped here while still borrowed
```
