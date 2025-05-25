# for 루프

## for 와 범위

`for in` 구문은 `Iterator`를 반복하는 데 사용될 수 있습니다. 반복자를 만드는 가장 쉬운 방법 중 하나는 범위 표기법 `a..b`를 사용하는 것입니다. 이것은 `a` (포함) 에서 `b` (제외) 까지 1 씩 증가하는 값을 생성합니다.

`while` 대신 `for`를 사용하여 FizzBuzz 를 작성해 보겠습니다.

```rust
fn main() {
    // `n` 은 각 반복에서 1, 2, ..., 100 의 값을 가집니다.
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

또는 양쪽 끝을 포함하는 범위를 위해 `a..=b`를 사용할 수 있습니다. 위의 코드는 다음과 같이 작성할 수 있습니다.

```rust
fn main() {
    // `n` 은 각 반복에서 1, 2, ..., 100 의 값을 가집니다.
    for n in 1..=100 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## for 와 반복자

`for in` 구문은 여러 가지 방법으로 `Iterator`와 상호 작용할 수 있습니다. 반복자 트레이트에 대한 섹션에서 논의했듯이, 기본적으로 `for` 루프는 컬렉션에 `into_iter` 함수를 적용합니다. 그러나 이것이 컬렉션을 반복자로 변환하는 유일한 방법은 아닙니다.

`into_iter`, `iter` 및 `iter_mut`는 컬렉션을 반복자로 변환하는 방식이 다르며, 데이터에 대한 다른 뷰를 제공합니다.

- `iter` - 이것은 각 반복에서 컬렉션의 각 요소를 빌려옵니다. 따라서 루프 후에도 컬렉션은 변경되지 않고 재사용할 수 있습니다.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter() {
        match name {
            &"Ferris" => println!("There is a rustacean among us!"),
            // TODO ^ &를 삭제하고 "Ferris"만 일치시켜보세요.
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
}
```

- `into_iter` - 이것은 컬렉션을 소비하므로 각 반복에서 정확한 데이터가 제공됩니다. 컬렉션이 소비되면 루프 내에서 '이동'되었기 때문에 재사용할 수 없습니다.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        match name {
            "Ferris" => println!("There is a rustacean among us!"),
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ 이 줄을 주석 처리하세요.
}
```

- `iter_mut` - 이것은 컬렉션의 각 요소를 가변적으로 빌려와서 컬렉션을 자리에서 수정할 수 있도록 합니다.

```rust
fn main() {
    let mut names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "There is a rustacean among us!",
            _ => "Hello",
        }
    }

    println!("names: {:?}", names);
}
```

위의 코드 조각에서 `match` 분기의 유형에 유의하십시오. 이것이 반복 유형의 주요 차이점입니다. 유형의 차이로 인해 수행할 수 있는 작업이 달라집니다.
