# HashMap

벡터가 정수 인덱스를 사용하여 값을 저장하는 것과 달리, `HashMap`은 키를 사용하여 값을 저장합니다. `HashMap` 키는 부울, 정수, 문자열 또는 `Eq` 및 `Hash` 트레이트를 구현하는 다른 유형일 수 있습니다. 다음 섹션에서 자세히 설명합니다.

벡터와 마찬가지로 `HashMap`도 크기가 조절될 수 있지만, 여분의 공간이 있을 때 `HashMap`은 스스로 크기를 줄일 수도 있습니다. `HashMap::with_capacity(uint)`를 사용하여 특정 초기 용량으로 `HashMap`을 생성하거나, 기본 초기 용량 (권장) 으로 `HashMap`을 얻으려면 `HashMap::new()`를 사용할 수 있습니다.

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "죄송합니다. 전화 연결이 실패했습니다.
            전화를 끊고 다시 시도하십시오.",
        "645-7689" => "안녕하세요, 미스터 멋진 피자입니다. 제 이름은 프레드입니다.
            오늘 무엇을 드릴까요?",
        _ => "안녕하세요! 누구신가요?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // 참조를 받아 Option<&V>를 반환합니다.
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Daniel 에게 전화: {}", call(number)),
        _ => println!("Daniel 의 번호가 없습니다."),
    }

    // `HashMap::insert()` 는 새 값이면 `None`, 그렇지 않으면 `Some(value)` 를 반환합니다.
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Ashley 에게 전화: {}", call(number)),
        _ => println!("Ashley 의 번호가 없습니다."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` 는 임의의 순서로 ('a key, &'a value) 쌍을 생성하는 반복자를 반환합니다.
    for (contact, &number) in contacts.iter() {
        println!("{}에게 전화: {}", contact, call(number));
    }
}
```

해싱 및 해시 맵 (때로는 해시 테이블이라고도 함) 작동 방식에 대한 자세한 내용은 해시 테이블 위키피디아를 참조하십시오.
