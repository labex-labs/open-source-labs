# Паттерн ref

При сопоставлении шаблонов или деструктуризации с использованием связывания `let` ключевое слово `ref` можно использовать для получения ссылок на поля структуры/кортежа. Ниже приведены несколько примеров, где это может быть полезно:

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // `ref`-заимствование слева от присваивания эквивалентно
    // `&`-заимствованию справа.
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 равно ref_c2: {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // `ref` также допустимо при деструктуризации структуры.
    let _copy_of_x = {
        // `ref_to_x` - это ссылка на поле `x` структуры `point`.
        let Point { x: ref ref_to_x, y: _ } = point;

        // Возвращаем копию поля `x` структуры `point`.
        *ref_to_x
    };

    // Изменяемая копия `point`
    let mut mutable_point = point;

    {
        // `ref` можно комбинировать с `mut`, чтобы получить изменяемые ссылки.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // Изменяем поле `y` структуры `mutable_point` с использованием изменяемой ссылки.
        *mut_ref_to_y = 1;
    }

    println!("point равно ({}, {})", point.x, point.y);
    println!("mutable_point равно ({}, {})", mutable_point.x, mutable_point.y);

    // Изменяемый кортеж, содержащий указатель
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // Деструктурируем `mutable_tuple`, чтобы изменить значение `last`.
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tuple равен {:?}", mutable_tuple);
}
```
