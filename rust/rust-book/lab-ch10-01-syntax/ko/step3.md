# 함수 정의에서

제네릭을 사용하는 함수를 정의할 때, 일반적으로 매개변수와 반환 값의 데이터 타입을 지정하는 함수 시그니처 (signature) 에 제네릭을 배치합니다. 이렇게 하면 코드가 더 유연해지고 함수 호출자에게 더 많은 기능을 제공하는 동시에 코드 중복을 방지할 수 있습니다.

`largest` 함수를 계속 사용하면서, Listing 10-4 는 슬라이스에서 가장 큰 값을 찾는 두 개의 함수를 보여줍니다. 그런 다음 이들을 제네릭을 사용하는 단일 함수로 결합할 것입니다.

파일 이름: `src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

Listing 10-4: 이름과 시그니처의 타입만 다른 두 개의 함수

`largest_i32` 함수는 Listing 10-3 에서 추출한 함수로, 슬라이스에서 가장 큰 `i32`를 찾습니다. `largest_char` 함수는 슬라이스에서 가장 큰 `char`를 찾습니다. 함수 본문은 동일한 코드를 가지고 있으므로, 단일 함수에 제네릭 타입 매개변수를 도입하여 중복을 제거해 보겠습니다.

새로운 단일 함수에서 타입을 매개변수화하려면, 함수에 대한 값 매개변수와 마찬가지로 타입 매개변수의 이름을 지정해야 합니다. 타입 매개변수 이름으로 어떤 식별자 (identifier) 든 사용할 수 있습니다. 하지만 관례적으로 Rust 의 타입 매개변수 이름은 짧고, 종종 한 글자이며, Rust 의 타입 명명 규칙은 CamelCase 이므로 `T`를 사용합니다. *type*의 약자인 `T`는 대부분의 Rust 프로그래머가 선택하는 기본값입니다.

함수 본문에서 매개변수를 사용할 때는 컴파일러가 해당 이름의 의미를 알 수 있도록 시그니처에 매개변수 이름을 선언해야 합니다. 마찬가지로, 함수 시그니처에서 타입 매개변수 이름을 사용할 때는 사용하기 전에 타입 매개변수 이름을 선언해야 합니다. 제네릭 `largest` 함수를 정의하려면, 다음과 같이 함수 이름과 매개변수 목록 사이에 꺾쇠 괄호 `<>` 안에 타입 이름 선언을 넣습니다.

```rust
fn largest<T>(list: &[T]) -> &T {
```

이 정의는 다음과 같이 읽습니다: `largest` 함수는 어떤 타입 `T`에 대해 제네릭입니다. 이 함수에는 `list`라는 매개변수가 하나 있는데, 이는 타입 `T`의 값 슬라이스입니다. `largest` 함수는 동일한 타입 `T`의 값에 대한 참조를 반환합니다.

Listing 10-5 는 시그니처에 제네릭 데이터 타입을 사용하는 결합된 `largest` 함수 정의를 보여줍니다. 이 Listing 은 또한 `i32` 값 슬라이스 또는 `char` 값으로 함수를 호출하는 방법을 보여줍니다. 이 코드는 아직 컴파일되지 않지만, 이 챕터의 뒷부분에서 수정할 것입니다.

파일 이름: `src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

Listing 10-5: 제네릭 타입 매개변수를 사용하는 `largest` 함수; 아직 컴파일되지 않음

이 코드를 지금 컴파일하면 다음과 같은 오류가 발생합니다.

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

도움말 텍스트는 `std::cmp::PartialOrd`를 언급하는데, 이는 *트레이트 (trait)*이며, 다음 섹션에서 트레이트에 대해 이야기할 것입니다. 지금은 이 오류가 `largest`의 본문이 `T`가 될 수 있는 모든 가능한 타입에 대해 작동하지 않는다는 것을 나타낸다는 것을 알아두세요. 본문에서 타입 `T`의 값을 비교하려는 경우, 값을 정렬할 수 있는 타입만 사용할 수 있습니다. 비교를 활성화하기 위해 표준 라이브러리에는 타입에 구현할 수 있는 `std::cmp::PartialOrd` 트레이트가 있습니다 (이 트레이트에 대한 자세한 내용은 부록 C 참조). 도움말 텍스트의 제안을 따르면, `T`에 유효한 타입을 `PartialOrd`를 구현하는 타입으로만 제한하고, 이 예제는 컴파일됩니다. 왜냐하면 표준 라이브러리는 `i32`와 `char` 모두에 대해 `PartialOrd`를 구현하기 때문입니다.
