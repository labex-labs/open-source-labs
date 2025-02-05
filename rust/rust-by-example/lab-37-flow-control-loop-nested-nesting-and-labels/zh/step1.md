# 嵌套与标签

在处理嵌套循环时，可以使用 `break` 或 `continue` 来控制外层循环。在这种情况下，循环必须用某个 `'标签` 进行标注，并且该标签必须传递给 `break`/`continue` 语句。

```rust
#![allow(unreachable_code)]

fn main() {
    'outer: loop {
        println!("进入外层循环");

        'inner: loop {
            println!("进入内层循环");

            // 这只会中断内层循环
            //break;

            // 这会中断外层循环
            break 'outer;
        }

        println!("这一行永远不会被执行到");
    }

    println!("退出外层循环");
}
```
