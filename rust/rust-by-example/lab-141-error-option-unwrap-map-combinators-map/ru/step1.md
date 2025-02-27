# Комбинаторы: `map`

`match` - это допустимый метод для обработки `Option`. Однако, вы, возможно, в конечном итоге найдете, что его частое использование утомительно, особенно при операциях, которые допустимы только для входных данных. В таких случаях комбинаторы можно использовать для управления потоком управления модульно.

`Option` имеет встроенный метод `map()`, комбинатор для простого сопоставления `Some -> Some` и `None -> None`. Несколько вызовов `map()` можно связать вместе для большей гибкости.

В следующем примере `process()` заменяет все предыдущие функции, оставаясь компактной.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// К削ению продуктов. Если их нет, то возвращаем `None`.
// В противном случае возвращаем очищенный продукт.
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// Крошению продуктов. Если их нет, то возвращаем `None`.
// В противном случае возвращаем нарезанный продукт.
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// Готовке продуктов. Здесь мы демонстрируем `map()`, вместо `match` для обработки случаев.
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// Функция для последовательного очистки, нарезания и приготовления продуктов.
// Мы связываем несколько использований `map()` для упрощения кода.
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
     .map(|Peeled(f)| Chopped(f))
     .map(|Chopped(f)| Cooked(f))
}

// Проверяем, есть ли продукты перед попыткой съесть их!
fn eat(food: Option<Cooked>) {
    match food {
        Some(food) => println!("Mmm. I love {:?}", food),
        None       => println!("Oh no! It wasn't edible."),
    }
}

fn main() {
    let apple = Some(Food::Apple);
    let carrot = Some(Food::Carrot);
    let potato = None;

    let cooked_apple = cook(chop(peel(apple)));
    let cooked_carrot = cook(chop(peel(carrot)));
    // Теперь попробуем более простой `process()`.
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```
