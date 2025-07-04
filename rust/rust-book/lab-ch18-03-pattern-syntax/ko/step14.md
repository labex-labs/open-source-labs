# 이름에 \_를 사용하여 사용하지 않는 변수 (An Unused Variable by Starting Its Name with \_)

변수를 생성했지만 어디에서도 사용하지 않으면 Rust 는 일반적으로 경고를 발행합니다. 사용하지 않는 변수는 버그일 수 있기 때문입니다. 그러나 프로토타입을 만들거나 프로젝트를 시작하는 경우와 같이 아직 사용하지 않을 변수를 생성할 수 있는 것이 유용할 때가 있습니다. 이러한 상황에서는 변수 이름을 밑줄로 시작하여 사용하지 않는 변수에 대한 경고를 받지 않도록 Rust 에 지시할 수 있습니다. Listing 18-20 에서 두 개의 사용하지 않는 변수를 생성하지만 이 코드를 컴파일하면 그 중 하나에 대해서만 경고를 받게 됩니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let _x = 5;
    let y = 10;
}
```

Listing 18-20: 사용하지 않는 변수 경고를 피하기 위해 변수 이름을 밑줄로 시작하기

여기서는 변수 `y`를 사용하지 않는다는 경고를 받지만, `_x`를 사용하지 않는다는 경고는 받지 않습니다.

`_`만 사용하는 것과 밑줄로 시작하는 이름을 사용하는 것 사이에는 미묘한 차이가 있습니다. 구문 `_x`는 여전히 값을 변수에 바인딩하는 반면, `_`는 전혀 바인딩하지 않습니다. 이러한 구분이 중요한 경우를 보여주기 위해 Listing 18-21 은 오류를 제공합니다.

파일 이름: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_s) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listing 18-21: 밑줄로 시작하는 사용하지 않는 변수는 여전히 값을 바인딩하며, 이는 값의 소유권을 가질 수 있습니다.

`s` 값이 여전히 `_s`로 이동하여 `s`를 다시 사용할 수 없으므로 오류가 발생합니다. 그러나 밑줄 자체를 사용하면 값에 바인딩되지 않습니다. Listing 18-22 는 `s`가 `_`로 이동하지 않으므로 오류 없이 컴파일됩니다.

파일 이름: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listing 18-22: 밑줄을 사용하면 값을 바인딩하지 않습니다.

이 코드는 `s`를 아무것에도 바인딩하지 않으므로 제대로 작동합니다. 즉, 이동되지 않습니다.
