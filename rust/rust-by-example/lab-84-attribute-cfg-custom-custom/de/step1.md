# Anpassung

Einige Bedingungen wie `target_os` werden von `rustc` implizit bereitgestellt, aber benutzerdefinierte Bedingungen müssen an `rustc` über das Flag `--cfg` übergeben werden.

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("Bedingung erfüllt!");
}

fn main() {
    conditional_function();
}
```

Versuchen Sie, dies auszuführen, um zu sehen, was passiert, wenn das benutzerdefinierte `cfg`-Flag fehlt.

Mit dem benutzerdefinierten `cfg`-Flag:

```shell
$ rustc --cfg some_condition custom.rs && ./custom
Bedingung erfüllt!
```
