# 别名

数据可以被无数次不可变借用，但在不可变借用期间，原始数据不能被可变借用。另一方面，一次只允许有一个可变借用。只有在可变引用最后一次被使用之后，原始数据才能再次被借用。

```rust
struct Point { x: i32, y: i32, z: i32 }

fn main() {
    let mut point = Point { x: 0, y: 0, z: 0 };

    let borrowed_point = &point;
    let another_borrow = &point;

    // 可以通过引用和原始所有者访问数据
    println!("Point has coordinates: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // 错误！不能将 `point` 作为可变借用，因为它当前正被不可变借用。
    // let mutable_borrow = &mut point;
    // TODO ^ 尝试取消注释这一行

    // 这里再次使用借用的值
    println!("Point has coordinates: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // 不可变引用在代码的其余部分不再使用，因此可以用可变引用重新借用。
    let mutable_borrow = &mut point;

    // 通过可变引用更改数据
    mutable_borrow.x = 5;
    mutable_borrow.y = 2;
    mutable_borrow.z = 1;

    // 错误！不能将 `point` 作为不可变借用，因为它当前正被可变借用。
    // let y = &point.y;
    // TODO ^ 尝试取消注释这一行

    // 错误！不能打印，因为 `println!` 需要一个不可变引用。
    // println!("Point Z coordinate is {}", point.z);
    // TODO ^ 尝试取消注释这一行

    // 可以！可变引用可以作为不可变引用传递给 `println!`
    println!("Point has coordinates: ({}, {}, {})",
                mutable_borrow.x, mutable_borrow.y, mutable_borrow.z);

    // 可变引用在代码的其余部分不再使用，因此可以重新借用
    let new_borrowed_point = &point;
    println!("Point now has coordinates: ({}, {}, {})",
             new_borrowed_point.x, new_borrowed_point.y, new_borrowed_point.z);
}
```
