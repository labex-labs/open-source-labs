# 가변 참조 (Mutable References)

Listing 4-6 의 코드를 수정하여 빌린 값을 수정할 수 있도록 하려면 *가변 참조 (mutable reference)*를 사용하는 몇 가지 작은 조정만 하면 됩니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

먼저 `s`를 `mut`로 변경합니다. 그런 다음 `change` 함수를 호출하는 곳에서 `&mut s`로 가변 참조를 만들고, 함수 시그니처를 `some_string: &mut String`으로 업데이트하여 가변 참조를 허용하도록 합니다. 이렇게 하면 `change` 함수가 빌린 값을 변경한다는 것을 매우 명확하게 알 수 있습니다.

가변 참조에는 한 가지 큰 제한 사항이 있습니다. 값에 대한 가변 참조가 있는 경우 해당 값에 대한 다른 참조를 가질 수 없습니다. `s`에 대한 두 개의 가변 참조를 만들려고 시도하는 이 코드는 실패합니다.

파일 이름: `src/main.rs`

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{r1}, {r2}");
```

다음은 오류입니다.

```bash
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{r1}, {r2}");
  |                -- first borrow later used here
```

이 오류는 이 코드가 유효하지 않다고 말합니다. 왜냐하면 한 번에 `s`를 가변적으로 두 번 이상 빌릴 수 없기 때문입니다. 첫 번째 가변 빌림은 `r1`에 있으며 `println!`에서 사용될 때까지 지속되어야 하지만, 해당 가변 참조를 생성하고 사용하기 전에 `r2`에서 `r1`과 동일한 데이터를 빌리는 다른 가변 참조를 만들려고 했습니다.

동일한 데이터에 대한 여러 가변 참조를 동시에 방지하는 제한 사항은 매우 제어된 방식으로 변경을 허용합니다. 이것은 새로운 Rust 사용자들이 어려움을 겪는 부분인데, 대부분의 언어에서는 원하는 때마다 변경할 수 있기 때문입니다. 이 제한 사항을 갖는 것의 장점은 Rust 가 컴파일 시간에 데이터 경합 (data race) 을 방지할 수 있다는 것입니다. *데이터 경합 (data race)*은 경쟁 조건 (race condition) 과 유사하며, 다음 세 가지 동작이 발생할 때 발생합니다.

- 두 개 이상의 포인터가 동시에 동일한 데이터에 접근합니다.
- 포인터 중 적어도 하나는 데이터를 쓰기 위해 사용됩니다.
- 데이터에 대한 접근을 동기화하는 데 사용되는 메커니즘이 없습니다.

데이터 경합은 정의되지 않은 동작을 유발하며, 런타임에 추적하려고 할 때 진단하고 수정하기 어려울 수 있습니다. Rust 는 데이터 경합이 있는 코드를 컴파일하는 것을 거부함으로써 이 문제를 방지합니다!

항상 그렇듯이, 중괄호를 사용하여 새 범위를 만들 수 있으며, 여러 가변 참조를 허용하지만 *동시적 (simultaneous)*인 것은 허용하지 않습니다.

```rust
let mut s = String::from("hello");

{
    let r1 = &mut s;
} // r1 goes out of scope here, so we can make a new reference with no problems

let r2 = &mut s;
```

Rust 는 가변 참조와 불변 참조를 결합하는 데에도 유사한 규칙을 적용합니다. 이 코드는 오류를 발생시킵니다.

```rust
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
let r3 = &mut s; // BIG PROBLEM

println!("{r1}, {r2}, and {r3}");
```

다음은 오류입니다.

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // no problem
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // no problem
6 |     let r3 = &mut s; // BIG PROBLEM
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{r1}, {r2}, and {r3}");
  |                -- immutable borrow later used here
```

휴! 동일한 값에 대한 불변 참조가 있는 동안 가변 참조를 가질 수도 _없습니다_.

불변 참조를 사용하는 사람은 값이 갑자기 자신 아래에서 변경될 것이라고 예상하지 않습니다! 그러나 여러 불변 참조는 허용됩니다. 왜냐하면 데이터를 읽기만 하는 사람은 다른 사람의 데이터 읽기에 영향을 미칠 수 있는 능력이 없기 때문입니다.

참조의 범위는 도입된 지점부터 해당 참조가 마지막으로 사용될 때까지 시작된다는 점에 유의하십시오. 예를 들어, 이 코드는 불변 참조의 마지막 사용, 즉 `println!`이 가변 참조가 도입되기 전에 발생하기 때문에 컴파일됩니다.

```rust
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
println!("{r1} and {r2}");
// variables r1 and r2 will not be used after this point

let r3 = &mut s; // no problem
println!("{r3}");
```

불변 참조 `r1`과 `r2`의 범위는 마지막으로 사용되는 `println!` 후에 끝나며, 이는 가변 참조 `r3`가 생성되기 전입니다. 이러한 범위는 겹치지 않으므로 이 코드는 허용됩니다. 컴파일러는 참조가 범위의 끝 지점 전에 더 이상 사용되지 않음을 알 수 있습니다.

빌림 오류가 때로는 답답할 수 있지만, Rust 컴파일러가 잠재적인 버그를 조기에 (런타임이 아닌 컴파일 시간에) 지적하고 문제가 정확히 어디에 있는지 보여주고 있다는 것을 기억하십시오. 그러면 데이터가 생각했던 것과 다른 이유를 추적할 필요가 없습니다.
