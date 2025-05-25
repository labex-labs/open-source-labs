# 컴비네이터: `and_then`

`map()`은 `match` 문을 단순화하는 체인 가능한 방법으로 설명되었습니다. 그러나 `Option<T>`를 반환하는 함수에 `map()`을 사용하면 중첩된 `Option<Option<T>>`가 발생합니다. 여러 호출을 함께 연결하면 혼란스러워질 수 있습니다. 바로 여기서, 일부 언어에서 flatmap 으로 알려진 `and_then()`이라는 또 다른 컴비네이터가 등장합니다.

`and_then()`은 래핑된 값으로 입력 함수를 호출하고 결과를 반환합니다. `Option`이 `None`인 경우, 대신 `None`을 반환합니다.

다음 예제에서 `cookable_v3()`는 `Option<Food>`를 반환합니다. `and_then()` 대신 `map()`을 사용하면 `Option<Option<Food>>`가 생성되는데, 이는 `eat()`에 유효하지 않은 타입입니다.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// We don't have the ingredients to make Sushi.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// We have the recipe for everything except Cordon Bleu.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// To make a dish, we need both the recipe and the ingredients.
// We can represent the logic with a chain of `match`es:
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// This can conveniently be rewritten more compactly with `and_then()`:
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// Otherwise we'd need to `flatten()` an `Option<Option<Food>>`
// to get an `Option<Food>`:
fn cookable_v2(food: Food) -> Option<Food> {
    have_recipe(food).map(have_ingredients).flatten()
}

fn eat(food: Food, day: Day) {
    match cookable_v3(food) {
        Some(food) => println!("Yay! On {:?} we get to eat {:?}.", day, food),
        None       => println!("Oh no. We don't get to eat on {:?}?", day),
    }
}

fn main() {
    let (cordon_bleu, steak, sushi) = (Food::CordonBleu, Food::Steak, Food::Sushi);

    eat(cordon_bleu, Day::Monday);
    eat(steak, Day::Tuesday);
    eat(sushi, Day::Wednesday);
}
```
