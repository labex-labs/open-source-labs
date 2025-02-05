# 组合器：`and_then`

`map()` 被描述为一种简化 `match` 语句的可链式调用方式。然而，在返回 `Option<T>` 的函数上使用 `map()` 会导致嵌套的 `Option<Option<T>>`。将多个调用链接在一起可能会变得令人困惑。这就是另一个名为 `and_then()` 的组合器（在某些语言中称为 flatmap）发挥作用的地方。

`and_then()` 使用包装的值调用其函数输入，并返回结果。如果 `Option` 为 `None`，则它返回 `None`。

在以下示例中，`cookable_v3()` 返回一个 `Option<Food>`。使用 `map()` 而不是 `and_then()` 会得到一个 `Option<Option<Food>>`，这对于 `eat()` 来说是一个无效类型。

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// 我们没有制作寿司的食材。
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// 除了蓝带菜，我们有其他所有菜品的食谱。
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// 要制作一道菜，我们既需要食谱也需要食材。
// 我们可以用一连串的 `match` 来表示这个逻辑：
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// 用 `and_then()` 可以更方便地将其简洁地重写为：
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// 否则，我们需要将 `Option<Option<Food>>` 进行 `flatten()`
// 以得到一个 `Option<Food>`：
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
