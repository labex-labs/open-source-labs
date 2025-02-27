# Комбинаторы: `and_then`

`map()` описывался как цепляемый способ упрощения инструкций `match`. Однако использование `map()` для функции, возвращающей `Option<T>`, приводит к вложенному `Option<Option<T>>`. Затем цепочка нескольких вызовов может стать запутанной. Именно здесь на помощь приходит другой комбинатор, называемый `and_then()`, который в некоторых языках известен как flatmap.

`and_then()` вызывает свою функцию-аргумент с обёрнутым значением и возвращает результат. Если `Option` равно `None`, то возвращается `None` вместо этого.

В следующем примере `cookable_v3()` возвращает `Option<Food>`. Использование `map()` вместо `and_then()` дало бы `Option<Option<Food>>`, что является недопустимым типом для `eat()`.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// У нас нет ингредиентов для приготовления Суши.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// У нас есть рецепт для всего, кроме Кор-дон-Блю.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// Чтобы приготовить блюдо, нам нужны как рецепт, так и ингредиенты.
// Мы можем представить логику в виде цепочки `match`:
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// Это можно удобно переписать более компактно с использованием `and_then()`:
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// В противном случае нам пришлось бы `flatten()` `Option<Option<Food>>`,
// чтобы получить `Option<Food>`:
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
