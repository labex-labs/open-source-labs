# массивы/срезы

Похоже на кортежи, массивы и срезы можно деструктурировать следующим образом:

```rust
fn main() {
    // Попробуйте изменить значения в массиве или сделать его среза!
    let array = [1, -2, 6];

    match array {
        // Привязывает второй и третий элементы к соответствующим переменным
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // Einzige Werte können mit _ ignoriert werden
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {} und array[1] wurde ignoriert",
            third
        ),

        // Вы также можете привязать некоторые и игнорировать остальные
        [-1, second,..] => println!(
            "array[0] = -1, array[1] = {} und все остальные были игнорированы",
            second
        ),
        // Код ниже не скомпилируется
        // [-1, second] =>...

        // Или сохранить их в другом массиве/срезе (тип зависит от
        // того, с каким значением сравнивается)
        [3, second, tail @..] => println!(
            "array[0] = 3, array[1] = {} и остальные элементы были {:?}",
            second, tail
        ),

        // Объединяя эти шаблоны, мы можем, например, привязать первый и
        // последнее значения и сохранить остальные в одном массиве
        [first, middle @.., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```

**Примечание**: Вместо "Einzige Werte können mit _ ignoriert werden" можно использовать "Одно значение можно игнорировать с помощью _". Также "und все остальные были игнорированы" можно заменить на "и все остальные были проигнорированы". Эти изменения сделаны для более точного и естественного перевода.
