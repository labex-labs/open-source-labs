# 组合器：`map`

`match` 是处理 `Option` 的一种有效方法。然而，你最终可能会发现频繁使用它很繁琐，特别是对于仅对输入有效操作的情况。在这些情况下，可以使用组合器以模块化的方式管理控制流。

`Option` 有一个名为 `map()` 的内置方法，它是一个组合器，用于将 `Some -> Some` 和 `None -> None` 进行简单映射。多个 `map()` 调用可以链接在一起，以提供更大的灵活性。

在以下示例中，`process()` 替换了它之前的所有函数，同时保持简洁。

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// 给食物削皮。如果没有食物，那么返回 `None`。
// 否则，返回削了皮的食物。
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// 切食物。如果没有食物，那么返回 `None`。
// 否则，返回切好的食物。
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// 烹饪食物。在这里，我们展示使用 `map()` 而不是 `match` 来处理情况。
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// 一个按顺序给食物削皮、切块和烹饪的函数。
// 我们链接多个 `map()` 的使用来简化代码。
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
     .map(|Peeled(f)| Chopped(f))
     .map(|Chopped(f)| Cooked(f))
}

// 在尝试吃食物之前检查是否有食物！
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
    // 现在让我们试试看起来更简单的 `process()`。
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```
