# 可变参数接口

可变参数接口可以接受任意数量的参数。例如，`println!` 可以根据格式字符串接受任意数量的参数。

我们可以将上一节中的 `calculate!` 宏扩展为可变参数形式：

```rust
macro_rules! calculate {
    // 单个 `eval` 的模式
    (eval $e:expr) => {
        {
            let val: usize = $e; // 强制类型为整数
            println!("{} = {}", stringify!{$e}, val);
        }
    };

    // 递归分解多个 `eval`
    (eval $e:expr, $(eval $es:expr),+) => {{
        calculate! { eval $e }
        calculate! { $(eval $es),+ }
    }};
}

fn main() {
    calculate! { // 看呐！可变参数的 `calculate!`！
        eval 1 + 2,
        eval 3 + 4,
        eval (2 * 3) + 1
    }
}
```

输出：

```txt
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7
```
