# String Slices (문자열 슬라이스)

*String slice*는 `String`의 일부에 대한 참조이며 다음과 같습니다.

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

전체 `String`에 대한 참조 대신, `hello`는 `[0..5]` 비트로 지정된 `String`의 일부에 대한 참조입니다. `[starting_index..ending_index]`를 지정하여 대괄호 안의 범위를 사용하여 슬라이스를 생성합니다. 여기서 `starting_index`는 슬라이스의 첫 번째 위치이고 `ending_index`는 슬라이스의 마지막 위치보다 하나 더 큽니다. 내부적으로 슬라이스 데이터 구조는 시작 위치와 슬라이스의 길이를 저장하며, 이는 `ending_index`에서 `starting_index`를 뺀 값에 해당합니다. 따라서 `let world = &s[6..11];`의 경우, `world`는 `s`의 인덱스 6 에 있는 바이트에 대한 포인터와 길이 값 `5`를 포함하는 슬라이스가 됩니다.

그림 4-6 은 이를 다이어그램으로 보여줍니다.

그림 4-6: `String`의 일부를 참조하는 문자열 슬라이스

Rust 의 `..` 범위 구문을 사용하면 인덱스 0 에서 시작하려는 경우 두 점 앞의 값을 삭제할 수 있습니다. 즉, 다음은 동일합니다.

```rust
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
```

마찬가지로, 슬라이스에 `String`의 마지막 바이트가 포함된 경우 후행 숫자를 삭제할 수 있습니다. 즉, 다음은 동일합니다.

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[3..len];
let slice = &s[3..];
```

전체 문자열의 슬라이스를 가져오기 위해 두 값 모두 삭제할 수도 있습니다. 따라서 다음은 동일합니다.

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[0..len];
let slice = &s[..];
```

> 참고: 문자열 슬라이스 범위 인덱스는 유효한 UTF-8 문자 경계에서 발생해야 합니다. 멀티바이트 문자 중간에 문자열 슬라이스를 생성하려고 하면 프로그램이 오류와 함께 종료됩니다. 문자열 슬라이스를 소개하기 위해 이 섹션에서는 ASCII 만 가정하고 있습니다. UTF-8 처리에 대한 자세한 내용은 "문자열로 UTF-8 인코딩된 텍스트 저장"을 참조하세요.

이 모든 정보를 염두에 두고 `first_word`를 다시 작성하여 슬라이스를 반환해 보겠습니다. "문자열 슬라이스"를 나타내는 유형은 `&str`로 작성됩니다.

파일 이름: `src/main.rs`

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Listing 4-7 에서와 마찬가지로, 첫 번째 공백을 찾아 단어의 끝에 대한 인덱스를 얻습니다. 공백을 찾으면 문자열의 시작과 공백의 인덱스를 시작 및 종료 인덱스로 사용하여 문자열 슬라이스를 반환합니다.

이제 `first_word`를 호출하면 기본 데이터에 연결된 단일 값을 다시 받습니다. 값은 슬라이스의 시작점에 대한 참조와 슬라이스의 요소 수로 구성됩니다.

슬라이스를 반환하는 것은 `second_word` 함수에도 작동합니다.

```rust
fn second_word(s: &String) -> &str {
```

이제 컴파일러가 `String`에 대한 참조가 유효하도록 보장하므로 엉망으로 만들기가 훨씬 더 어려운 간단한 API 가 있습니다. Listing 4-8 의 프로그램에서 첫 번째 단어의 끝에 대한 인덱스를 얻었지만 문자열을 지워서 인덱스가 유효하지 않게 된 경우를 기억하세요? 해당 코드는 논리적으로 잘못되었지만 즉각적인 오류는 표시되지 않았습니다. 문제는 나중에 비어 있는 문자열로 첫 번째 단어 인덱스를 계속 사용하려고 하면 나타났을 것입니다. 슬라이스는 이 버그를 불가능하게 만들고 코드에 문제가 있음을 훨씬 더 빨리 알 수 있게 해줍니다. `first_word`의 슬라이스 버전을 사용하면 컴파일 시 오류가 발생합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // error!

    println!("the first word is: {word}");
}
```

다음은 컴파일러 오류입니다.

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- immutable borrow occurs here
17 |
18 |     s.clear(); // error!
   |     ^^^^^^^^^ mutable borrow occurs here
19 |
20 |     println!("the first word is: {word}");
   |                                   ---- immutable borrow later used here
```

차용 규칙에서 무언에 대한 불변 참조가 있는 경우 가변 참조를 가져올 수도 없다는 것을 기억하세요. `clear`는 `String`을 잘라야 하므로 가변 참조를 가져와야 합니다. `clear` 호출 후의 `println!`은 `word`의 참조를 사용하므로 불변 참조가 해당 시점에도 활성 상태여야 합니다. Rust 는 `clear`의 가변 참조와 `word`의 불변 참조가 동시에 존재하지 못하도록 하며, 컴파일이 실패합니다. Rust 는 API 를 사용하기 쉽게 만들었을 뿐만 아니라 컴파일 시 전체 오류 클래스를 제거했습니다!
