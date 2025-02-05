# 使结构体和枚举变为公共的

我们也可以使用 `pub` 将结构体和枚举指定为公共的，但在结构体和枚举中使用 `pub` 还有一些额外的细节。如果我们在结构体定义之前使用 `pub`，我们会使结构体变为公共的，但结构体的字段仍然是私有的。我们可以根据具体情况使每个字段变为公共的或保持私有。在清单 7-9 中，我们定义了一个公共的 `back_of_house::Breakfast` 结构体，其中 `toast` 字段是公共的，但 `seasonal_fruit` 字段是私有的。这模拟了餐厅中的一种情况，顾客可以选择餐食搭配的面包类型，但厨师根据当季和库存情况决定搭配哪种水果。可用的水果变化很快，所以顾客无法选择水果，甚至看不到他们会得到哪种水果。

文件名：`src/lib.rs`

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // 点一份夏季的黑麦面包早餐
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // 改变我们想要的面包类型
    meal.toast = String::from("Wheat");
    println!("我想要{}面包", meal.toast);

    // 如果我们取消注释下一行，它将无法编译；我们不被允许
    // 查看或修改餐食搭配的当季水果
    // meal.seasonal_fruit = String::from("blueberries");
}
```

清单 7-9：一个有一些公共字段和一些私有字段的结构体

因为 `back_of_house::Breakfast` 结构体中的 `toast` 字段是公共的，在 `eat_at_restaurant` 中我们可以使用点号表示法读写 `toast` 字段。注意，在 `eat_at_restaurant` 中我们不能使用 `seasonal_fruit` 字段，因为 `seasonal_fruit` 是私有的。尝试取消注释修改 `seasonal_fruit` 字段值的那一行，看看会得到什么错误！

另外，注意因为 `back_of_house::Breakfast` 有一个私有字段，结构体需要提供一个公共的关联函数来构造 `Breakfast` 的实例（我们在这里将其命名为 `summer`）。如果 `Breakfast` 没有这样的函数，我们就不能在 `eat_at_restaurant` 中创建 `Breakfast` 的实例，因为我们不能在 `eat_at_restaurant` 中设置私有 `seasonal_fruit` 字段的值。

相比之下，如果我们使一个枚举变为公共的，那么它的所有变体也都是公共的。我们只需要在 `enum` 关键字之前加上 `pub`，如清单 7-10 所示。

文件名：`src/lib.rs`

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

清单 7-10：将一个枚举指定为公共的会使其所有变体都变为公共的。

因为我们使 `Appetizer` 枚举变为公共的，所以我们可以在 `eat_at_restaurant` 中使用 `Soup` 和 `Salad` 变体。

除非枚举的变体是公共的，否则枚举不是很有用；在每种情况下都必须用 `pub` 注释所有枚举变体很麻烦，所以枚举变体的默认情况是公共的。结构体在其字段不是公共的情况下通常也很有用，所以结构体字段遵循默认情况下所有内容都是私有的一般规则，除非用 `pub` 注释。

还有一种涉及 `pub` 的情况我们还没有讨论，那就是我们最后一个模块系统特性：`use` 关键字。我们将首先单独介绍 `use`，然后展示如何将 `pub` 和 `use` 结合起来。
