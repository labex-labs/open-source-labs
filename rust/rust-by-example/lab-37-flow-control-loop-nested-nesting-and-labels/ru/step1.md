# Вложенные циклы и метки

При работе с вложенными циклами можно использовать операторы `break` или `continue` для внешних циклов. В таких случаях циклы должны быть помечены некоторой `'меткой`, и эта метка должна быть передана в оператор `break`/`continue`.

```rust
#![allow(unreachable_code)]

fn main() {
    'outer: loop {
        println!("Entered the outer loop");

        'inner: loop {
            println!("Entered the inner loop");

            // This would break only the inner loop
            //break;

            // This breaks the outer loop
            break 'outer;
        }

        println!("This point will never be reached");
    }

    println!("Exited the outer loop");
}
```
