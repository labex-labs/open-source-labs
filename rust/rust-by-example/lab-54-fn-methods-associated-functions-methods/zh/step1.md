# 关联函数与方法

有些函数与特定类型相关联。它们有两种形式：关联函数和方法。关联函数是在某个类型上定义的一般函数，而方法是在类型的特定实例上调用的关联函数。

```rust
struct Point {
    x: f64,
    y: f64,
}

// 实现块，所有 `Point` 的关联函数和方法都放在这里
impl Point {
    // 这是一个“关联函数”，因为这个函数与
    // 特定类型 `Point` 相关联。
    //
    // 关联函数不需要通过实例调用。
    // 这些函数通常用作构造函数。
    fn origin() -> Point {
        Point { x: 0.0, y: 0.0 }
    }

    // 另一个关联函数，接受两个参数：
    fn new(x: f64, y: f64) -> Point {
        Point { x: x, y: y }
    }
}

struct Rectangle {
    p1: Point,
    p2: Point,
}

impl Rectangle {
    // 这是一个方法
    // `&self` 是 `self: &Self` 的语法糖，其中 `Self` 是
    // 调用者对象的类型。在这种情况下 `Self` = `Rectangle`
    fn area(&self) -> f64 {
        // `self` 通过点运算符访问结构体字段
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        // `abs` 是 `f64` 类型的一个方法，返回调用者的绝对值
        ((x1 - x2) * (y1 - y2)).abs()
    }

    fn perimeter(&self) -> f64 {
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        2.0 * ((x1 - x2).abs() + (y1 - y2).abs())
    }

    // 这个方法要求调用者对象是可变的
    // `&mut self` 展开为 `self: &mut Self`
    fn translate(&mut self, x: f64, y: f64) {
        self.p1.x += x;
        self.p2.x += x;

        self.p1.y += y;
        self.p2.y += y;
    }
}

// `Pair` 拥有资源：两个堆分配的整数
struct Pair(Box<i32>, Box<i32>);

impl Pair {
    // 这个方法“消耗”调用者对象的资源
    // `self` 展开为 `self: Self`
    fn destroy(self) {
        // 解构 `self`
        let Pair(first, second) = self;

        println!("Destroying Pair({}, {})", first, second);

        // `first` 和 `second` 超出作用域并被释放
    }
}

fn main() {
    let rectangle = Rectangle {
        // 使用双冒号调用关联函数
        p1: Point::origin(),
        p2: Point::new(3.0, 4.0),
    };

    // 使用点运算符调用方法
    // 注意第一个参数 `&self` 是隐式传递的，即
    // `rectangle.perimeter()` 等同于 `Rectangle::perimeter(&rectangle)`
    println!("Rectangle perimeter: {}", rectangle.perimeter());
    println!("Rectangle area: {}", rectangle.area());

    let mut square = Rectangle {
        p1: Point::origin(),
        p2: Point::new(1.0, 1.0),
    };

    // 错误！`rectangle` 是不可变的，但这个方法需要一个可变对象
    //rectangle.translate(1.0, 0.0);
    // TODO ^ 尝试取消注释这一行

    // 可以！可变对象可以调用可变方法
    square.translate(1.0, 1.0);

    let pair = Pair(Box::new(1), Box::new(2));

    pair.destroy();

    // 错误！之前的 `destroy` 调用“消耗”了 `pair`
    //pair.destroy();
    // TODO ^ 尝试取消注释这一行
}
```
