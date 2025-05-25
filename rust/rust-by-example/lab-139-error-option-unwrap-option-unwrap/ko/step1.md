# `Option` & `unwrap`

지난 예제에서 우리는 원할 때 프로그램 오류를 유발할 수 있음을 보여주었습니다. 우리는 설탕이 든 레모네이드를 마시면 프로그램이 `panic`하도록 했습니다. 하지만 _어떤_ 음료를 기대했지만 받지 못하면 어떻게 될까요? 그 경우도 마찬가지로 좋지 않으므로 처리해야 합니다!

레모네이드와 마찬가지로 널 문자열 (`""`) 에 대해 테스트할 수 있습니다. Rust 를 사용하고 있으므로, 컴파일러가 음료가 없는 경우를 지적하도록 해보겠습니다.

`std` 라이브러리의 `Option<T>`라는 `enum`은 부재 가능성이 있을 때 사용됩니다. 이는 두 가지 "옵션" 중 하나로 나타납니다.

- `Some(T)`: 타입 `T`의 요소가 발견되었습니다.
- `None`: 요소가 발견되지 않았습니다.

이러한 경우는 `match`를 통해 명시적으로 처리하거나 `unwrap`을 사용하여 암시적으로 처리할 수 있습니다. 암시적 처리는 내부 요소를 반환하거나 `panic`을 발생시킵니다.

`expect`를 사용하여 수동으로 `panic`을 사용자 정의할 수 있지만, `unwrap`은 그렇지 않으면 명시적 처리보다 덜 의미 있는 출력을 제공합니다. 다음 예제에서 명시적 처리는 원하는 경우 `panic`할 수 있는 옵션을 유지하면서 더 제어된 결과를 생성합니다.

```rust
// The adult has seen it all, and can handle any drink well.
// All drinks are handled explicitly using `match`.
fn give_adult(drink: Option<&str>) {
    // Specify a course of action for each case.
    match drink {
        Some("lemonade") => println!("Yuck! Too sugary."),
        Some(inner)   => println!("{}? How nice.", inner),
        None          => println!("No drink? Oh well."),
    }
}

// Others will `panic` before drinking sugary drinks.
// All drinks are handled implicitly using `unwrap`.
fn drink(drink: Option<&str>) {
    // `unwrap` returns a `panic` when it receives a `None`.
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("I love {}s!!!!!", inside);
}

fn main() {
    let water  = Some("water");
    let lemonade = Some("lemonade");
    let void  = None;

    give_adult(water);
    give_adult(lemonade);
    give_adult(void);

    let coffee = Some("coffee");
    let nothing = None;

    drink(coffee);
    drink(nothing);
}
```
