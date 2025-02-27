# Schleifenbezeichnungen zur Unterscheidung zwischen mehreren Schleifen

Wenn Sie Schleifen innerhalb von Schleifen haben, gelten `break` und `continue` für die innerste Schleife an diesem Punkt. Optionaler können Sie einer Schleife eine _Schleifenbezeichnung_ zuweisen, die Sie dann mit `break` oder `continue` verwenden können, um anzugeben, dass diese Schlüsselwörter auf die markierte Schleife anstatt auf die innerste Schleife anwenden. Schleifenbezeichnungen müssen mit einem einfachen Anführungszeichen beginnen. Hier ist ein Beispiel mit zwei geschachtelten Schleifen:

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

Die äußere Schleife hat die Bezeichnung `'counting_up` und zählt von 0 bis 2 hoch. Die innere Schleife ohne Bezeichnung zählt von 10 bis 9 runter. Der erste `break`, der keine Bezeichnung angibt, wird nur die innere Schleife beenden. Die Anweisung `break 'counting_up;` wird die äußere Schleife beenden. Dieser Code gibt folgendes aus:

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
