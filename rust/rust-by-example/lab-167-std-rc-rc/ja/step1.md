# `Rc`

複数の所有権が必要な場合、`Rc`（参照カウント）を使用できます。`Rc`は参照の数を追跡します。これは、`Rc`の中にラップされた値の所有者の数を意味します。

`Rc`がクローンされるたびに、`Rc`の参照カウントは1増加し、クローンされた`Rc`の1つがスコープ外になるたびに1減少します。`Rc`の参照カウントがゼロになると（所有者がいなくなることを意味します）、`Rc`と値の両方が破棄されます。

`Rc`をクローンすると、深いコピーは行われません。クローンは、ラップされた値への別のポインタを作成し、カウントを増やします。

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Rc examples".to_string();
    {
        println!("--- rc_a is created ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("Reference Count of rc_a: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a is cloned to rc_b ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("Reference Count of rc_b: {}", Rc::strong_count(&rc_b));
            println!("Reference Count of rc_a: {}", Rc::strong_count(&rc_a));

            // Two `Rc`s are equal if their inner values are equal
            println!("rc_a and rc_b are equal: {}", rc_a.eq(&rc_b));

            // We can use methods of a value directly
            println!("Length of the value inside rc_a: {}", rc_a.len());
            println!("Value of rc_b: {}", rc_b);

            println!("--- rc_b is dropped out of scope ---");
        }

        println!("Reference Count of rc_a: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a is dropped out of scope ---");
    }

    // Error! `rc_examples` already moved into `rc_a`
    // And when `rc_a` is dropped, `rc_examples` is dropped together
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ Try uncommenting this line
}
```
