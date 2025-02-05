# 使用闭包捕获环境

我们首先来研究如何使用闭包从其定义的环境中捕获值以供后续使用。假设这样一个场景：我们的T恤公司会时不时地向邮件列表中的某个人赠送一件独家限量版T恤作为促销活动。邮件列表中的人可以选择在个人资料中添加他们最喜欢的颜色。如果被选中获得免费T恤的人设置了他们最喜欢的颜色，他们就会得到那种颜色的T恤。如果这个人没有指定最喜欢的颜色，他们就会得到公司目前库存最多的那种颜色的T恤。

实现这个功能有很多种方法。在这个例子中，我们将使用一个名为 `ShirtColor` 的枚举，它有 `Red` 和 `Blue` 两个变体（为了简单起见，限制了可用颜色的数量）。我们用一个 `Inventory` 结构体来表示公司的库存，该结构体有一个名为 `shirts` 的字段，它包含一个 `Vec<ShirtColor>`，表示当前库存的T恤颜色。在 `Inventory` 上定义的 `giveaway` 方法获取免费T恤获奖者的可选颜色偏好，并返回这个人将得到的T恤颜色。清单13-1展示了这种设置。

文件名：`src/main.rs`

```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(
        &self,
        user_preference: Option<ShirtColor>,
    ) -> ShirtColor {
      1 user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
      2 shirts: vec![
            ShirtColor::Blue,
            ShirtColor::Red,
            ShirtColor::Blue,
        ],
    };

    let user_pref1 = Some(ShirtColor::Red);
  3 let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
  4 let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

清单13-1：T恤公司的赠送情况

在 `main` 中定义的 `store` 有两件蓝色T恤和一件红色T恤，用于这次限量版促销活动的分发 \[2\]。我们分别对有红色T恤偏好的用户 \[3\] 和没有任何偏好的用户 \[4\] 调用 `giveaway` 方法。

同样，这段代码可以用多种方式实现，在这里，为了专注于闭包，我们除了 `giveaway` 方法的主体使用了闭包外，其他都使用了你已经学过的概念。在 `giveaway` 方法中，我们将用户偏好作为 `Option<ShirtColor>` 类型的参数获取，并在 `user_preference` 上调用 `unwrap_or_else` 方法 \[1\]。`Option<T>` 上的 `unwrap_or_else` 方法是由标准库定义的。它接受一个参数：一个没有参数且返回 `T` 类型值的闭包（`T` 是存储在 `Option<T>` 的 `Some` 变体中的相同类型，在这种情况下是 `ShirtColor`）。如果 `Option<T>` 是 `Some` 变体，`unwrap_or_else` 返回 `Some` 中的值。如果 `Option<T>` 是 `None` 变体，`unwrap_or_else` 调用闭包并返回闭包返回的值。

我们将闭包表达式 `|| self.most_stocked()` 作为 `unwrap_or_else` 的参数。这是一个本身没有参数的闭包（如果闭包有参数，它们会出现在两个竖线之间）。闭包的主体调用 `self.most_stocked()`。我们在这里定义闭包，并且如果需要结果，`unwrap_or_else` 的实现会在之后计算这个闭包。

运行这段代码会输出以下内容：

```rust
The user with preference Some(Red) gets Red
The user with preference None gets Blue
```

这里一个有趣的方面是，我们传递了一个在当前 `Inventory` 实例上调用 `self.most_stocked()` 的闭包。标准库不需要知道我们定义的 `Inventory` 或 `ShirtColor` 类型，也不需要知道我们在这个场景中想要使用的逻辑。闭包捕获了对 `self` `Inventory` 实例的不可变引用，并将其与我们指定的代码一起传递给 `unwrap_or_else` 方法。另一方面，函数不能以这种方式捕获它们的环境。
