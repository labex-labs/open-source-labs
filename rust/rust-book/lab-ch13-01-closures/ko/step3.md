# 클로저 타입 추론 및 어노테이션

함수와 클로저 사이에는 더 많은 차이점이 있습니다. 클로저는 일반적으로 `fn` 함수처럼 매개변수 또는 반환 값의 타입을 주석 처리할 필요가 없습니다. 함수에는 타입 어노테이션이 필요합니다. 왜냐하면 타입은 사용자에게 노출되는 명시적 인터페이스의 일부이기 때문입니다. 이 인터페이스를 엄격하게 정의하는 것은 모든 사람이 함수가 사용하는 값과 반환하는 값의 타입에 동의하도록 보장하는 데 중요합니다. 반면에 클로저는 이와 같이 노출된 인터페이스에서 사용되지 않습니다. 클로저는 변수에 저장되고 이름을 지정하지 않고 라이브러리 사용자에게 노출하지 않고 사용됩니다.

클로저는 일반적으로 짧고 임의의 시나리오가 아닌 좁은 컨텍스트 내에서만 관련이 있습니다. 이러한 제한된 컨텍스트 내에서 컴파일러는 대부분의 변수 타입 (컴파일러가 클로저 타입 어노테이션도 필요로 하는 드문 경우도 있습니다) 의 타입을 추론할 수 있는 방식과 유사하게 매개변수와 반환 타입의 타입을 추론할 수 있습니다.

변수와 마찬가지로, 엄격하게 필요한 것보다 더 장황해지는 대가로 명시성과 명확성을 높이려면 타입 어노테이션을 추가할 수 있습니다. 클로저에 대한 타입 어노테이션은 Listing 13-2 에 표시된 정의와 같습니다. 이 예제에서는 Listing 13-1 에서 했던 것처럼 클로저를 인수로 전달하는 위치에서 정의하는 대신 클로저를 정의하고 변수에 저장합니다.

파일 이름: `src/main.rs`

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

Listing 13-2: 클로저에서 선택적 매개변수 및 반환 값 타입의 타입 어노테이션 추가

타입 어노테이션을 추가하면 클로저의 구문이 함수의 구문과 더 유사해 보입니다. 여기서는 매개변수에 1 을 더하는 함수와 동일한 동작을 하는 클로저를 정의하여 비교합니다. 관련 부분을 정렬하기 위해 몇 개의 공백을 추가했습니다. 이것은 클로저 구문이 파이프 사용과 선택적인 구문의 양을 제외하고 함수 구문과 어떻게 유사한지 보여줍니다.

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

첫 번째 줄은 함수 정의를 보여주고 두 번째 줄은 완전히 주석 처리된 클로저 정의를 보여줍니다. 세 번째 줄에서는 클로저 정의에서 타입 어노테이션을 제거합니다. 네 번째 줄에서는 클로저 본문에 표현식이 하나만 있기 때문에 선택적인 중괄호를 제거합니다. 이것들은 모두 호출될 때 동일한 동작을 생성하는 유효한 정의입니다. `add_one_v3` 및 `add_one_v4` 줄은 타입을 사용으로부터 추론할 수 있도록 클로저를 평가해야 컴파일할 수 있습니다. 이것은 `Vec`에 타입을 추론할 수 있도록 Rust 가 `Vec`에 타입 어노테이션이나 일부 타입의 값을 삽입해야 하는 `let v = Vec::new();`와 유사합니다.

클로저 정의의 경우 컴파일러는 각 매개변수와 반환 값에 대해 하나의 구체적인 타입을 추론합니다. 예를 들어, Listing 13-3 은 매개변수로 받은 값을 반환하는 짧은 클로저의 정의를 보여줍니다. 이 클로저는 이 예제를 제외하고는 그다지 유용하지 않습니다. 정의에 타입 어노테이션을 추가하지 않았다는 점에 유의하십시오. 타입 어노테이션이 없으므로, 여기에서 처음 `String`으로 수행한 것처럼 모든 타입으로 클로저를 호출할 수 있습니다. 그런 다음 정수로 `example_closure`를 호출하려고 하면 오류가 발생합니다.

파일 이름: `src/main.rs`

```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

Listing 13-3: 타입이 추론된 클로저를 두 개의 다른 타입으로 호출하려고 시도

컴파일러는 다음과 같은 오류를 제공합니다.

```bash
error[E0308]: mismatched types
 --> src/main.rs:5:29
  |
5 |     let n = example_closure(5);
  |                             ^- help: try using a conversion method:
`.to_string()`
  |                             |
  |                             expected struct `String`, found integer
```

`String` 값으로 `example_closure`를 처음 호출할 때 컴파일러는 `x`의 타입과 클로저의 반환 타입을 `String`으로 추론합니다. 그런 다음 해당 타입은 `example_closure`의 클로저에 고정되고, 동일한 클로저로 다른 타입을 사용하려고 시도하면 타입 오류가 발생합니다.
