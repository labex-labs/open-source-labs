# Einfügen und Bezeichnungen

Es ist möglich, äußere Schleifen mit `break` oder `continue` zu beenden, wenn es um geschachtelte Schleifen geht. In diesen Fällen müssen die Schleifen mit einem `'Bezeichnung` versehen werden, und die Bezeichnung muss an die `break`-/`continue`-Anweisung übergeben werden.

```rust
#![allow(unreachable_code)]

fn main() {
    'äußerste: Schleife {
        println!("Innerhalb der äußeren Schleife");

        'innere: Schleife {
            println!("Innerhalb der inneren Schleife");

            // Dies würde nur die innere Schleife beenden
            //break;

            // Dies beendet die äußere Schleife
            break 'äußerste;
        }

        println!("Dieser Punkt wird nie erreicht");
    }

    println!("Außerhalb der äußeren Schleife");
}
```