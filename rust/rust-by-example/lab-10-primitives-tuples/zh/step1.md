# 元组

元组是不同类型值的集合。元组使用括号 `()` 构建，每个元组本身是一个具有类型签名 `(T1, T2,...)` 的值，其中 `T1`、`T2` 是其成员的类型。函数可以使用元组返回多个值，因为元组可以容纳任意数量的值。

```rust
// 元组可用作函数参数和返回值。
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` 可用于将元组的成员绑定到变量。
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// 以下结构体用于活动。
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // 一个包含多种不同类型的元组。
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // 可以使用元组索引从元组中提取值。
    println!("长元组的第一个值：{}", long_tuple.0);
    println!("长元组的第二个值：{}", long_tuple.1);

    // 元组可以作为其他元组的成员。
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // 元组是可打印的。
    println!("元组的元组：{:?}", tuple_of_tuples);

    // 但是长元组（超过 12 个元素）不能被打印。
    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    //println!("过长的元组：{:?}", too_long_tuple);
    // TODO ^ 取消注释上面两行以查看编译器错误

    let pair = (1, true);
    println!("对是 {:?}", pair);

    println!("反转后的对是 {:?}", reverse(pair));

    // 要创建单元素元组，需要逗号来将它们与括号包围的字面量区分开。
    println!("单元素元组：{:?}", (5u32,));
    println!("只是一个整数：{:?}", (5u32));

    // 元组可以解构以创建绑定。
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

## 活动

1. **回顾**：在上面的示例中，向 `Matrix` 结构体添加 `fmt::Display` 特性，这样如果你从打印调试格式 `{:?}` 切换到显示格式 `{}`, 你会看到以下输出：

   ```plaintext
   ( 1.1 1.2 )
   ( 2.1 2.2 )
   ```

   你可能需要回顾一下打印显示的示例。

2. 以 `reverse` 函数为模板添加一个 `transpose` 函数，该函数接受一个矩阵作为参数，并返回一个交换了两个元素的矩阵。例如：

   ```rust
   println!("矩阵:\n{}", matrix);
   println!("转置:\n{}", transpose(matrix));
   ```

   结果输出为：

   ```plaintext
   矩阵：
   ( 1.1 1.2 )
   ( 2.1 2.2 )
   转置：
   ( 1.1 2.1 )
   ( 1.2 2.2 )
   ```
