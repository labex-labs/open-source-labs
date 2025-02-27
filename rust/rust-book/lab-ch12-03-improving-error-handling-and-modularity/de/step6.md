# Fixing the Error Handling

Jetzt werden wir uns um die Verbesserung unserer Fehlerbehandlung kümmern. Denken Sie daran, dass das Versuchen, auf die Werte im `args`-Vektor an Index 1 oder Index 2 zuzugreifen, dazu führen wird, dass das Programm abstürzt, wenn der Vektor weniger als drei Elemente enthält. Versuchen Sie, das Programm ohne Argumente auszuführen; es wird so aussehen:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'index out of bounds: the len is 1 but
the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

Die Zeile `index out of bounds: the len is 1 but the index is 1` ist eine Fehlermeldung für Programmierer. Sie wird unseren Endbenutzern nicht helfen, zu verstehen, was sie stattdessen tun sollten. Lassen Sie uns das jetzt beheben.
