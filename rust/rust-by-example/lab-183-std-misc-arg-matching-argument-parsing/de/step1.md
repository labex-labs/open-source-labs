# Argument-Parsing

Mustererkennung kann verwendet werden, um einfache Argumente zu parsen:

```rust
use std::env;

fn increase(number: i32) {
    println!("{}", number + 1);
}

fn decrease(number: i32) {
    println!("{}", number - 1);
}

fn help() {
    println!("usage:
match_args <string>
    Überprüfen, ob der gegebene String die Antwort ist.
match_args {{increase|decrease}} <integer>
    Erhöhen oder Verringern der gegebenen ganzen Zahl um eins.");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    match args.len() {
        // keine Argumente übergeben
        1 => {
            println!("Mein Name ist'match_args'. Versuchen Sie, einige Argumente zu übergeben!");
        },
        // ein Argument übergeben
        2 => {
            match args[1].parse() {
                Ok(42) => println!("Dies ist die Antwort!"),
                _ => println!("Dies ist nicht die Antwort."),
            }
        },
        // ein Befehl und ein Argument übergeben
        3 => {
            let cmd = &args[1];
            let num = &args[2];
            // die Zahl parsen
            let number: i32 = match num.parse() {
                Ok(n) => {
                    n
                },
                Err(_) => {
                    eprintln!("error: zweites Argument ist keine ganze Zahl");
                    help();
                    return;
                },
            };
            // den Befehl parsen
            match &cmd[..] {
                "increase" => increase(number),
                "decrease" => decrease(number),
                _ => {
                    eprintln!("error: ungültiger Befehl");
                    help();
                },
            }
        },
        // alle anderen Fälle
        _ => {
            // eine Hilfsmeldung anzeigen
            help();
        }
    }
}
```

```shell
$./match_args Rust
Dies ist nicht die Antwort.
$./match_args 42
Dies ist die Antwort!
$./match_args do something
error: zweites Argument ist keine ganze Zahl
usage:
match_args <string>
    Überprüfen, ob der gegebene String die Antwort ist.
match_args {increase|decrease} <integer>
    Erhöhen oder Verringern der gegebenen ganzen Zahl um eins.
$./match_args do 42
error: ungültiger Befehl
usage:
match_args <string>
    Überprüfen, ob der gegebene String die Antwort ist.
match_args {increase|decrease} <integer>
    Erhöhen oder Verringern der gegebenen ganzen Zahl um eins.
$./match_args increase 42
43
```
