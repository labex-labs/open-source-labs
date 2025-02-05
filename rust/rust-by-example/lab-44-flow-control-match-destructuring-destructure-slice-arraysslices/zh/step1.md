# 数组/切片

与元组类似，数组和切片可以通过这种方式解构：

```rust
fn main() {
    // 尝试更改数组中的值，或者将其变为切片！
    let array = [1, -2, 6];

    match array {
        // 将第二个和第三个元素绑定到各自的变量
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // 单个值可以用 _ 忽略
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {} 且 array[1] 被忽略",
            third
        ),

        // 你也可以绑定部分值并忽略其余值
        [-1, second,..] => println!(
            "array[0] = -1, array[1] = {} 且所有其他值都被忽略",
            second
        ),
        // 下面的代码不会编译
        // [-1, second] =>...

        // 或者将它们存储在另一个数组/切片中（类型取决于
        // 与之匹配的值的类型）
        [3, second, tail @..] => println!(
            "array[0] = 3, array[1] = {} 且其他元素为 {:?}",
            second, tail
        ),

        // 结合这些模式，例如，我们可以绑定第一个和
        // 最后一个值，并将其余值存储在一个数组中
        [first, middle @.., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```
