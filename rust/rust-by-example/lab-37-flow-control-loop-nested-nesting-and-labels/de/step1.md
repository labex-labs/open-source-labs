# Verschachtelung und Labels

Es ist möglich, äußere Schleifen in verschachtelten Schleifen mit `break` oder `continue` zu beenden oder zu überspringen. In diesen Fällen müssen die Schleifen mit einem `'label` versehen werden, und das Label muss an die `break`/`continue`-Anweisung übergeben werden.

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
