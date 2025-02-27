# Tubes

La structure `std::Child` représente un processus enfant en cours d'exécution et expose les descripteurs `stdin`, `stdout` et `stderr` pour interagir avec le processus sous-jacent via des tubes.

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // Lance la commande `wc`
    let process = match Command::new("wc")
                             .stdin(Stdio::piped())
                             .stdout(Stdio::piped())
                             .spawn() {
        Err(why) => panic!("couldn't spawn wc: {}", why),
        Ok(process) => process,
    };

    // Écrit une chaîne dans l'`stdin` de `wc`.
    //
    // `stdin` a le type `Option<ChildStdin>`, mais puisque nous savons que cette instance
    // doit en avoir un, nous pouvons directement `unwrap` it.
    match process.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(why) => panic!("couldn't write to wc stdin: {}", why),
        Ok(_) => println!("sent pangram to wc"),
    }

    // Parce que `stdin` ne vit pas après les appels ci-dessus, il est `drop`é,
    // et le tube est fermé.
    //
    // Cela est très important, sinon `wc` ne commencerait pas à traiter
    // l'entrée que nous venons d'envoyer.

    // Le champ `stdout` a également le type `Option<ChildStdout>` donc doit être déballé.
    let mut s = String::new();
    match process.stdout.unwrap().read_to_string(&mut s) {
        Err(why) => panic!("couldn't read wc stdout: {}", why),
        Ok(_) => print!("wc responded with:\n{}", s),
    }
}
```
