# Box, стек и кучу

Все значения в Rust по умолчанию выделяются на стеке. Значения можно "упаковать" (выделить в куче), создав `Box<T>`. Box - это умный указатель на значение типа `T`, выделенное в куче. Когда box выходит из области видимости, вызывается его деструктор, внутренний объект уничтожается, и память в куче освобождается.

Значения, помещенные в box, можно разыменовать с помощью оператора `*`; это удаляет один уровень косвенности.

```rust
use std::mem;

#[allow(dead_code)]
#[derive(Debug, Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

// Прямоугольник можно определить по координатам его верхнего левого и нижнего правого углов
#[allow(dead_code)]
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

fn origin() -> Point {
    Point { x: 0.0, y: 0.0 }
}

fn boxed_origin() -> Box<Point> {
    // Выделить эту точку в куче и вернуть указатель на нее
    Box::new(Point { x: 0.0, y: 0.0 })
}

fn main() {
    // (все аннотации типов лишние)
    // Переменные, выделенные на стеке
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 }
    };

    // Прямоугольник, выделенный в куче
    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 },
    });

    // Результат функции можно поместить в box
    let boxed_point: Box<Point> = Box::new(origin());

    // Двойная косвенность
    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    println!("Точка занимает {} байт на стеке",
             mem::size_of_val(&point));
    println!("Прямоугольник занимает {} байт на стеке",
             mem::size_of_val(&rectangle));

    // Размер box равен размеру указателя
    println!("Boxed точка занимает {} байт на стеке",
             mem::size_of_val(&boxed_point));
    println!("Boxed прямоугольник занимает {} байт на стеке",
             mem::size_of_val(&boxed_rectangle));
    println!("Boxed box занимает {} байт на стеке",
             mem::size_of_val(&box_in_a_box));

    // Скопировать данные из `boxed_point` в `unboxed_point`
    let unboxed_point: Point = *boxed_point;
    println!("Unboxed точка занимает {} байт на стеке",
             mem::size_of_val(&unboxed_point));
}
```
