# 구조체 정의의 생명주기 어노테이션

지금까지 우리가 정의한 구조체는 모두 소유된 타입을 가지고 있습니다. 참조를 저장하는 구조체를 정의할 수 있지만, 이 경우 구조체 정의의 모든 참조에 생명주기 어노테이션을 추가해야 합니다. Listing 10-24 는 문자열 슬라이스를 저장하는 `ImportantExcerpt`라는 구조체를 가지고 있습니다.

Filename: `src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
        .split('.')
        .next()
        .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

Listing 10-24: 생명주기 어노테이션이 필요한 참조를 저장하는 구조체

이 구조체는 문자열 슬라이스를 저장하는 단일 필드 `part`를 가지고 있으며, 이는 참조입니다 \[2]. 제네릭 데이터 타입과 마찬가지로, 구조체 이름 뒤에 꺾쇠 괄호 안에 제네릭 생명주기 매개변수의 이름을 선언하여 구조체 정의 본문에서 생명주기 매개변수를 사용할 수 있습니다 \[1]. 이 어노테이션은 `ImportantExcerpt`의 인스턴스가 `part` 필드에 저장된 참조보다 오래 지속될 수 없음을 의미합니다.

여기 `main` 함수는 변수 `novel` \[3]이 소유한 `String` \[4]의 첫 번째 문장에 대한 참조를 저장하는 `ImportantExcerpt` 구조체의 인스턴스를 생성합니다 \[5]. `novel`의 데이터는 `ImportantExcerpt` 인스턴스가 생성되기 전에 존재합니다. 또한, `novel`은 `ImportantExcerpt`가 범위를 벗어날 때까지 범위를 벗어나지 않으므로, `ImportantExcerpt` 인스턴스의 참조는 유효합니다.
