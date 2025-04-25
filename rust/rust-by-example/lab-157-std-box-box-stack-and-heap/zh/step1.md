# 装箱、栈和堆

在 Rust 中，所有值默认都是在栈上分配的。通过创建一个 `Box<T>`，值可以被“装箱”（在堆上分配）。一个装箱是指向类型为 `T` 的堆分配值的智能指针。当一个装箱超出作用域时，其析构函数会被调用，内部对象被销毁，堆上的内存被释放。

装箱值可以使用 `*` 运算符进行解引用；这会移除一层间接引用。

```rust
use std::mem;

#[allow(dead_code)]
#[derive(Debug, Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

// 一个矩形可以通过其左上角和右下角在空间中的位置来指定
#[allow(dead_code)]
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

fn origin() -> Point {
    Point { x: 0.0, y: 0.0 }
}

fn boxed_origin() -> Box<Point> {
    // 在堆上分配这个点，并返回指向它的指针
    Box::new(Point { x: 0.0, y: 0.0 })
}

fn main() {
    // （所有类型注释都是多余的）
    // 栈分配的变量
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 }
    };

    // 堆分配的矩形
    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 },
    });

    // 函数的输出可以被装箱
    let boxed_point: Box<Point> = Box::new(origin());

    // 双重间接引用
    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    println!("Point 在栈上占用 {} 字节",
             mem::size_of_val(&point));
    println!("Rectangle 在栈上占用 {} 字节",
             mem::size_of_val(&rectangle));

    // 装箱大小 == 指针大小
    println!("装箱后的 Point 在栈上占用 {} 字节",
             mem::size_of_val(&boxed_point));
    println!("装箱后的 Rectangle 在栈上占用 {} 字节",
             mem::size_of_val(&boxed_rectangle));
    println!("装箱后的箱子在栈上占用 {} 字节",
             mem::size_of_val(&box_in_a_box));

    // 将 `boxed_point` 中包含的数据复制到 `unboxed_point`
    let unboxed_point: Point = *boxed_point;
    println!("解装箱后的 Point 在栈上占用 {} 字节",
             mem::size_of_val(&unboxed_point));
}
```
