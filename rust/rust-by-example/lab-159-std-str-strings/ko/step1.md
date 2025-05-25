# 문자열 (Strings)

Rust 에는 두 가지 유형의 문자열이 있습니다: `String`과 `&str`.

`String`은 바이트 벡터 (`Vec<u8>`) 로 저장되지만, 항상 유효한 UTF-8 시퀀스임을 보장합니다. `String`은 힙에 할당되고, 크기가 늘어날 수 있으며, null 로 종료되지 않습니다.

`&str`은 슬라이스 (`&[u8]`) 로, 항상 유효한 UTF-8 시퀀스를 가리키며, `&[T]`가 `Vec<T>`를 보는 것처럼 `String`을 보기 위해 사용될 수 있습니다.

```rust
fn main() {
    // (모든 타입 어노테이션은 불필요합니다)
    // 읽기 전용 메모리에 할당된 문자열에 대한 참조
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Pangram: {}", pangram);

    // 단어를 역순으로 반복합니다. 새로운 문자열은 할당되지 않습니다.
    println!("Words in reverse");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // 문자를 벡터로 복사하고, 정렬하고, 중복을 제거합니다.
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // 비어 있고 크기가 늘어날 수 있는 `String` 을 생성합니다.
    let mut string = String::new();
    for c in chars {
        // 문자열 끝에 문자를 삽입합니다.
        string.push(c);
        // 문자열 끝에 문자열을 삽입합니다.
        string.push_str(", ");
    }

    // 트리밍된 문자열은 원래 문자열의 슬라이스이므로, 새로운 할당이 수행되지 않습니다.
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Used characters: {}", trimmed_str);

    // 힙에 문자열을 할당합니다.
    let alice = String::from("I like dogs");
    // 새로운 메모리를 할당하고 수정된 문자열을 저장합니다.
    let bob: String = alice.replace("dog", "cat");

    println!("Alice says: {}", alice);
    println!("Bob says: {}", bob);
}
```

더 많은 `str`/`String` 메서드는 `std::str` 및 `std::string` 모듈에서 찾을 수 있습니다.

## 리터럴과 이스케이프 (Literals and escapes)

특수 문자가 포함된 문자열 리터럴을 작성하는 방법에는 여러 가지가 있습니다. 모두 유사한 `&str`을 생성하므로, 작성하기에 가장 편리한 형식을 사용하는 것이 좋습니다. 마찬가지로, 바이트 문자열 리터럴을 작성하는 방법도 여러 가지가 있으며, 모두 `&[u8; N]`을 생성합니다.

일반적으로 특수 문자는 백슬래시 문자 (`\`) 로 이스케이프됩니다. 이렇게 하면 인쇄할 수 없는 문자나 입력 방법을 모르는 문자까지 포함하여 모든 문자를 문자열에 추가할 수 있습니다. 리터럴 백슬래시를 원하면 다른 백슬래시로 이스케이프합니다: `\\`

리터럴 내에서 발생하는 문자열 또는 문자 리터럴 구분 기호는 이스케이프해야 합니다: `"\""`, `'\''`.

```rust
fn main() {
    // 16 진수 값을 사용하여 바이트를 작성하기 위해 이스케이프를 사용할 수 있습니다...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("What are you doing\x3F (\\x3F means ?) {}", byte_escape);

    // ...또는 유니코드 코드 포인트를 사용할 수 있습니다.
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("Unicode character {} (U+211D) is called {}",
                unicode_codepoint, character_name );


    let long_string = "String literals
                        can span multiple lines.
                        The linebreak and indentation here ->\
                        <- can be escaped too!";
    println!("{}", long_string);
}
```

때로는 이스케이프해야 하는 문자가 너무 많거나, 문자열을 있는 그대로 작성하는 것이 훨씬 더 편리할 수 있습니다. 이럴 때 raw 문자열 리터럴이 사용됩니다.

```rust
fn main() {
    let raw_str = r"Escapes don't work here: \x3F \u{211D}";
    println!("{}", raw_str);

    // raw 문자열에 따옴표가 필요한 경우, #을 두 쌍 추가합니다.
    let quotes = r#"And then I said: "There is no escape!""#;
    println!("{}", quotes);

    // 문자열에 "#"이 필요한 경우, 구분 기호에 더 많은 #을 사용하면 됩니다.
    // 최대 65535 개의 #을 사용할 수 있습니다.
    let longer_delimiter = r###"A string with "# in it. And even "##!"###;
    println!("{}", longer_delimiter);
}
```

UTF-8 이 아닌 문자열을 원하십니까? (기억하세요, `str`과 `String`은 유효한 UTF-8 이어야 합니다). 아니면 대부분 텍스트인 바이트 배열을 원하십니까? 바이트 문자열이 해결해 드립니다!

```rust
use std::str;

fn main() {
    // 이것은 실제로 `&str` 이 아닙니다.
    let bytestring: &[u8; 21] = b"this is a byte string";

    // 바이트 배열에는 `Display` 트레이트가 없으므로, 인쇄하는 데 약간 제한이 있습니다.
    println!("A byte string: {:?}", bytestring);

    // 바이트 문자열은 바이트 이스케이프를 가질 수 있습니다...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    // ...하지만 유니코드 이스케이프는 없습니다.
    // let escaped = b"\u{211D} is not allowed";
    println!("Some escaped bytes: {:?}", escaped);


    // Raw 바이트 문자열은 raw 문자열과 동일하게 작동합니다.
    let raw_bytestring = br"\u{211D} is not escaped here";
    println!("{:?}", raw_bytestring);

    // 바이트 배열을 `str` 로 변환하는 데 실패할 수 있습니다.
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("And the same as text: '{}'", my_str);
    }

    let _quotes = br#"You can also use "fancier" formatting, \
                    like with normal raw strings"#;

    // 바이트 문자열은 UTF-8 일 필요가 없습니다.
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" in SHIFT-JIS

    // 하지만 항상 `str` 로 변환할 수 있는 것은 아닙니다.
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("Conversion successful: '{}'", my_str),
        Err(e) => println!("Conversion failed: {:?}", e),
    };
}
```

문자 인코딩 간의 변환을 위해서는 `encoding` 크레이트를 확인하십시오.

문자열 리터럴을 작성하고 문자를 이스케이프하는 방법에 대한 자세한 목록은 Rust Reference 의 'Tokens' 챕터에서 제공됩니다.
