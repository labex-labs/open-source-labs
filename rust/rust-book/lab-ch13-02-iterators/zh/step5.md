# 使用捕获其环境的闭包

许多迭代器适配器都将闭包作为参数，通常我们作为迭代器适配器参数指定的闭包将是捕获其环境的闭包。

对于这个示例，我们将使用接受闭包的 `filter` 方法。闭包从迭代器中获取一个项目并返回一个 `bool`。如果闭包返回 `true`，该值将包含在 `filter` 产生的迭代中。如果闭包返回 `false`，该值将不被包含。

在清单 13-16 中，我们将 `filter` 与一个从其环境中捕获 `shoe_size` 变量的闭包一起使用，以遍历 `Shoe` 结构体实例的集合。它将只返回指定尺码的鞋子。

文件名：`src/lib.rs`

```rust
#[derive(PartialEq, Debug)]
struct Shoe {
    size: u32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn filters_by_size() {
        let shoes = vec![
            Shoe {
                size: 10,
                style: String::from("sneaker"),
            },
            Shoe {
                size: 13,
                style: String::from("sandal"),
            },
            Shoe {
                size: 10,
                style: String::from("boot"),
            },
        ];

        let in_my_size = shoes_in_size(shoes, 10);

        assert_eq!(
            in_my_size,
            vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker")
                },
                Shoe {
                    size: 10,
                    style: String::from("boot")
                },
            ]
        );
    }
}
```

清单 13-16：将 `filter` 方法与捕获 `shoe_size` 的闭包一起使用

`shoes_in_size` 函数将鞋子向量的所有权和鞋子尺码作为参数。它返回一个只包含指定尺码鞋子的向量。

在 `shoes_in_size` 的主体中，我们调用 `into_iter` 创建一个获取向量所有权的迭代器。然后我们调用 `filter` 将该迭代器适配成一个新的迭代器，该迭代器只包含闭包返回 `true` 的元素。

闭包从环境中捕获 `shoe_size` 参数，并将该值与每只鞋子的尺码进行比较，只保留指定尺码的鞋子。最后，调用 `collect` 将适配后的迭代器返回的值收集到一个由函数返回的向量中。

测试表明，当我们调用 `shoes_in_size` 时，我们只会得到与我们指定的值具有相同尺码的鞋子。
