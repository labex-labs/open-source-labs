# References and Borrowing

Listing 4-5 의 튜플 코드의 문제는 `calculate_length` 호출 후에도 `String`을 계속 사용할 수 있도록 `String`을 호출 함수로 반환해야 한다는 것입니다. 왜냐하면 `String`이 `calculate_length`로 이동했기 때문입니다. 대신, `String` 값에 대한 참조를 제공할 수 있습니다. *참조 (reference)*는 포인터와 유사하며, 해당 주소에 저장된 데이터에 접근하기 위해 따라갈 수 있는 주소입니다. 해당 데이터는 다른 변수가 소유합니다. 포인터와 달리, 참조는 해당 참조의 수명 동안 특정 유형의 유효한 값을 가리키도록 보장됩니다.

다음은 값의 소유권을 가져가는 대신 객체에 대한 참조를 매개변수로 갖는 `calculate_length` 함수를 정의하고 사용하는 방법입니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

먼저, 변수 선언과 함수 반환 값의 모든 튜플 코드가 사라진 것을 확인하십시오. 둘째, `&s1`을 `calculate_length`에 전달하고, 정의에서 `String` 대신 `&String`을 사용한다는 점에 유의하십시오. 이 앰퍼샌드는 *참조 (references)*를 나타내며, 소유권을 가져가지 않고도 일부 값을 참조할 수 있도록 합니다. 그림 4-5 는 이 개념을 보여줍니다.

그림 4-5: `String s1`을 가리키는 `&String s`의 다이어그램

> 참고: `&`를 사용하여 참조하는 것의 반대는 *역참조 (dereferencing)*이며, 역참조 연산자 `*`로 수행됩니다. 8 장에서 역참조 연산자의 사용법을 살펴보고, 15 장에서 역참조에 대한 자세한 내용을 논의할 것입니다.

여기서 함수 호출을 자세히 살펴보겠습니다.

```rust
let s1 = String::from("hello");

let len = calculate_length(&s1);
```

`&s1` 구문을 사용하면 `s1`의 값을 *참조 (refer)*하지만 소유하지 않는 참조를 만들 수 있습니다. 소유하지 않기 때문에, 참조가 사용을 멈출 때 가리키는 값은 삭제되지 않습니다.

마찬가지로, 함수의 시그니처는 `&`를 사용하여 매개변수 `s`의 유형이 참조임을 나타냅니다. 몇 가지 설명 주석을 추가해 보겠습니다.

```rust
fn calculate_length(s: &String) -> usize { // s is a reference to a String
    s.len()
} // Here, s goes out of scope. But because it does not have ownership of what
  // it refers to, the String is not dropped
```

변수 `s`가 유효한 범위는 모든 함수 매개변수의 범위와 동일하지만, 참조가 소유권을 갖지 않기 때문에 `s`가 사용을 멈출 때 참조가 가리키는 값은 삭제되지 않습니다. 함수가 실제 값 대신 참조를 매개변수로 갖는 경우, 소유권을 돌려주기 위해 값을 반환할 필요가 없습니다. 왜냐하면 우리는 소유권을 갖지 않았기 때문입니다.

참조를 만드는 행위를 *빌림 (borrowing)*이라고 부릅니다. 실제 생활에서와 마찬가지로, 어떤 것을 소유한 사람이 있다면, 그 사람에게서 빌릴 수 있습니다. 다 사용하면 돌려줘야 합니다. 당신은 그것을 소유하지 않습니다.

그렇다면 빌리고 있는 것을 수정하려고 하면 어떻게 될까요? Listing 4-6 의 코드를 시도해 보십시오. 스포일러 경고: 작동하지 않습니다!

파일 이름: `src/main.rs`

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

Listing 4-6: 빌린 값을 수정하려는 시도

다음은 오류입니다.

```bash
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&`
reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                        ------- help: consider changing this to be a mutable
reference: `&mut String`
8 |     some_string.push_str(", world");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so
the data it refers to cannot be borrowed as mutable
```

변수가 기본적으로 불변인 것처럼, 참조도 마찬가지입니다. 참조하고 있는 것을 수정할 수 없습니다.
