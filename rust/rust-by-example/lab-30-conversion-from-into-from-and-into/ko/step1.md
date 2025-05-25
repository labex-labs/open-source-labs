# `From` 및 `Into`

[`From`](#from) 및 [`Into`](#into) 트레이트는 본질적으로 연결되어 있으며, 이는 실제 구현의 일부입니다. 타입 B 에서 타입 A 로 변환할 수 있다면 타입 A 에서 타입 B 로 변환할 수 있어야 한다는 것을 쉽게 짐작할 수 있습니다.

## `From`

[`From`](#from) 트레이트는 타입이 다른 타입으로부터 자신을 생성하는 방법을 정의할 수 있도록 하여 여러 타입 간 변환을 위한 매우 간단한 메커니즘을 제공합니다. 원시 타입 및 일반적인 타입의 변환을 위한 이 트레이트의 수많은 구현이 표준 라이브러리 내에 존재합니다.

예를 들어, `str`을 `String`으로 쉽게 변환할 수 있습니다.

```rust
let my_str = "hello";
let my_string = String::from(my_str);
```

마찬가지로, 사용자 정의 타입에 대한 변환을 정의할 수 있습니다.

```rust
use std::convert::From;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

fn main() {
    let num = Number::from(30);
    println!("My number is {:?}", num);
}
```

## `Into`

[`Into`](#into) 트레이트는 단순히 `From` 트레이트의 역입니다. 즉, 타입에 `From` 트레이트를 구현했으면 `Into`는 필요할 때 이를 호출합니다.

`Into` 트레이트를 사용하려면 일반적으로 변환할 타입을 명시해야 합니다. 컴파일러는 대부분의 경우 이를 자동으로 추론할 수 없기 때문입니다. 하지만 이는 기능을 무료로 얻는다는 점을 고려하면 작은 단점입니다.

```rust
use std::convert::Into;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl Into<Number> for i32 {
    fn into(self) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int = 5;
    // 타입 주석을 제거해 보세요
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```
