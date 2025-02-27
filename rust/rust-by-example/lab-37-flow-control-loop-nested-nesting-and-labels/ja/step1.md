# ネストとラベル

ネストされたループを扱う際に、外側のループを `break` または `continue` することが可能です。この場合、ループには `'label` というラベルを付ける必要があり、そのラベルを `break`/`continue` 文に渡す必要があります。

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
