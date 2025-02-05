# 结构体

使用 `struct` 关键字可以创建三种类型的结构体（“struct”）：

- 元组结构体，本质上就是具名元组。
- 经典的C结构体
- 单元结构体，没有字段，对泛型很有用。

```rust
// 一个用于隐藏未使用代码警告的属性。
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// 一个单元结构体
struct Unit;

// 一个元组结构体
struct Pair(i32, f32);

// 一个有两个字段的结构体
struct Point {
    x: f32,
    y: f32,
}

// 结构体可以作为另一个结构体的字段被复用
struct Rectangle {
    // 一个矩形可以通过其左上角和右下角在空间中的位置来指定。
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // 使用字段初始化简写创建结构体
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // 打印结构体的调试信息
    println!("{:?}", peter);

    // 实例化一个 `Point`
    let point: Point = Point { x: 10.3, y: 0.4 };

    // 访问点的字段
    println!("point coordinates: ({}, {})", point.x, point.y);

    // 通过使用结构体更新语法来使用另一个结构体的字段，创建一个新的点
    let bottom_right = Point { x: 5.2,..point };

    // `bottom_right.y` 将与 `point.y` 相同，因为我们使用了 `point` 中的那个字段
    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // 使用 `let` 绑定解构点
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // 结构体实例化也是一个表达式
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // 实例化一个单元结构体
    let _unit = Unit;

    // 实例化一个元组结构体
    let pair = Pair(1, 0.1);

    // 访问元组结构体的字段
    println!("pair contains {:?} and {:?}", pair.0, pair.1);

    // 解构一个元组结构体
    let Pair(integer, decimal) = pair;

    println!("pair contains {:?} and {:?}", integer, decimal);
}
```

## 活动

1. 添加一个函数 `rect_area`，用于计算 `Rectangle` 的面积（尝试使用嵌套解构）。
2. 添加一个函数 `square`，它接受一个 `Point` 和一个 `f32` 作为参数，并返回一个 `Rectangle`，其左上角位于该点，宽度和高度与 `f32` 相对应。
