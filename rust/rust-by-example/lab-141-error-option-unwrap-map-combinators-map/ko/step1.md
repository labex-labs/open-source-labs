# 컴비네이터: `map`

`match`는 `Option`을 처리하는 유효한 방법입니다. 하지만 특히 입력값에 대해서만 유효한 연산의 경우, 결국에는 과도한 사용이 지루하게 느껴질 수 있습니다. 이러한 경우, 컴비네이터를 사용하여 제어 흐름을 모듈 방식으로 관리할 수 있습니다.

`Option`에는 `map()`이라는 내장 메서드가 있습니다. 이는 `Some -> Some` 및 `None -> None`의 간단한 매핑을 위한 컴비네이터입니다. 여러 개의 `map()` 호출을 함께 연결하여 더욱 유연하게 사용할 수 있습니다.

다음 예제에서 `process()`는 이전의 모든 함수를 대체하면서도 간결함을 유지합니다.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// 음식을 껍질을 벗깁니다. 음식이 없으면 `None` 을 반환합니다.
// 그렇지 않으면 껍질을 벗긴 음식을 반환합니다.
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// 음식을 자릅니다. 음식이 없으면 `None` 을 반환합니다.
// 그렇지 않으면 자른 음식을 반환합니다.
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// 음식을 요리합니다. 여기서는 케이스 처리를 위해 `match` 대신 `map()` 을 사용합니다.
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// 음식을 껍질을 벗기고, 자르고, 요리하는 함수입니다.
// 코드를 단순화하기 위해 `map()` 을 여러 번 사용합니다.
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
        .map(|Peeled(f)| Chopped(f))
        .map(|Chopped(f)| Cooked(f))
}

// 먹기 전에 음식이 있는지 확인합니다!
fn eat(food: Option<Cooked>) {
    match food {
        Some(food) => println!("냠냠. {:?} 너무 맛있어!", food),
        None       => println!("아, 안 돼! 먹을 수 없었어."),
    }
}

fn main() {
    let apple = Some(Food::Apple);
    let carrot = Some(Food::Carrot);
    let potato = None;

    let cooked_apple = cook(chop(peel(apple)));
    let cooked_carrot = cook(chop(peel(carrot)));
    // 이제 더 간단해 보이는 `process()` 를 사용해 봅시다.
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```
