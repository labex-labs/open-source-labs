# 문 (Statements) 과 표현식 (Expressions)

함수 본문은 일련의 문 (statements) 으로 구성되며, 선택적으로 표현식 (expression) 으로 끝납니다. 지금까지 다룬 함수에는 끝나는 표현식이 포함되지 않았지만, 문 (statement) 의 일부로 표현식을 보셨습니다. Rust 는 표현식 기반 언어이므로 이를 이해하는 것이 중요합니다. 다른 언어는 동일한 구분을 갖지 않으므로 문과 표현식이 무엇인지, 그리고 그 차이가 함수 본문에 어떤 영향을 미치는지 살펴보겠습니다.

- **문 (Statements)**: 어떤 작업을 수행하고 값을 반환하지 않는 지침입니다.
- **표현식 (Expressions)**: 결과 값을 평가합니다. 몇 가지 예를 살펴보겠습니다.

우리는 실제로 이미 문과 표현식을 사용했습니다. `let` 키워드를 사용하여 변수를 만들고 값을 할당하는 것은 문입니다. Listing 3-1 에서 `let y = 6;`은 문입니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let y = 6;
}
```

Listing 3-1: 하나의 문을 포함하는 `main` 함수 선언

함수 정의도 문입니다. 앞의 전체 예제 자체가 문입니다.

문은 값을 반환하지 않습니다. 따라서 다음 코드에서 시도하는 것처럼 `let` 문을 다른 변수에 할당할 수 없습니다. 오류가 발생합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = (let y = 6);
}
```

이 프로그램을 실행하면 다음과 같은 오류가 발생합니다.

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found statement (`let`)
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: variable declaration using `let` is a statement

error[E0658]: `let` expressions in this position are unstable
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: see issue #53667 <https://github.com/rust-lang/rust/issues/53667> for
more information
```

`let y = 6` 문은 값을 반환하지 않으므로 `x`가 바인딩할 것이 없습니다. 이것은 C 및 Ruby 와 같은 다른 언어에서 발생하는 것과는 다릅니다. 여기서 할당은 할당 값을 반환합니다. 이러한 언어에서는 `x = y = 6`을 작성하여 `x`와 `y` 모두 값 `6`을 갖도록 할 수 있습니다. Rust 에서는 그렇지 않습니다.

표현식은 값을 평가하고 Rust 에서 작성할 나머지 코드의 대부분을 구성합니다. `5 + 6`과 같은 수학 연산을 생각해 보세요. 이는 값 `11`로 평가되는 표현식입니다. 표현식은 문의 일부가 될 수 있습니다. Listing 3-1 에서 문 `let y = 6;`의 `6`은 값 `6`으로 평가되는 표현식입니다. 함수를 호출하는 것은 표현식입니다. 매크로를 호출하는 것은 표현식입니다. 중괄호로 생성된 새로운 범위 블록은 표현식입니다. 예를 들어:

파일 이름: `src/main.rs`

```rust
fn main() {
  1 let y = {2
        let x = 3;
      3 x + 1
    };

    println!("The value of y is: {y}");
}
```

표현식 \[2]는 이 경우 `4`로 평가되는 블록입니다. 해당 값은 `let` 문 \[1]의 일부로 `y`에 바인딩됩니다. 지금까지 보았던 대부분의 줄과 달리 세미콜론이 없는 줄 \[3]에 유의하세요. 표현식은 끝나는 세미콜론을 포함하지 않습니다. 표현식의 끝에 세미콜론을 추가하면 문으로 바뀌고 값을 반환하지 않습니다. 다음으로 함수 반환 값과 표현식을 탐구할 때 이 점을 염두에 두세요.
