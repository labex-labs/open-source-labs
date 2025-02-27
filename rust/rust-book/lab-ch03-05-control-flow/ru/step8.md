# Метки цикла для устранения неоднозначности при наличии нескольких циклов

Если у вас есть циклы внутри циклов, то `break` и `continue` применяются к самому внутреннему циклу в текущей точке. Вы можете необязательно указать _метку цикла_ для цикла, которую можно затем использовать с `break` или `continue`, чтобы указать, что эти ключевые слова применяются к помеченному циклу, а не к самому внутреннему циклу. Метки цикла должны начинаться с одинарной кавычки. Вот пример с двумя вложенными циклами:

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

Внешний цикл имеет метку `'counting_up`, и он будет считать от 0 до 2. Внутренний цикл без метки будет считать от 10 до 9. Первый `break`, не указывающий метку, выйдёт только из внутреннего цикла. Строка `break 'counting_up;` выйдёт из внешнего цикла. Этот код выводит:

       Compiling loops v0.1.0 (file:///projects/loops)
        Finished dev [unoptimized + debuginfo] target(s) in 0.58s
         Running `target/debug/loops`
    count = 0
    remaining = 10
    remaining = 9
    count = 1
    remaining = 10
    remaining = 9
    count = 2
    remaining = 10
    End count = 2
