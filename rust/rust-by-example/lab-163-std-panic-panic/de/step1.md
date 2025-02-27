# `panic!`

Das `panic!`-Makro kann verwendet werden, um einen Fehler zu erzeugen und den Stapel zu entspannen. Während des Entspannens kümmert sich die Laufzeit darum, alle von einem Thread _besitzten_ Ressourcen freizugeben, indem sie den Destruktor aller seiner Objekte aufruft.

Da wir mit Programmen arbeiten, die nur einen Thread haben, wird `panic!` dazu führen, dass das Programm die Fehlermeldung ausgibt und beendet wird.

```rust
// Re-Implementierung der ganzzahligen Division (/)
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // Division durch Null löst einen Fehler aus
        panic!("division by zero");
    } else {
        dividend / divisor
    }
}

// Die `main`-Aufgabe
fn main() {
    // Heap-zugewiesene Ganzzahl
    let _x = Box::new(0i32);

    // Diese Operation wird einen Fehler im Task auslösen
    division(3, 0);

    println!("Dieser Punkt wird nicht erreicht!");

    // `_x` sollte zu diesem Zeitpunkt zerstört werden
}
```

Lassen Sie uns überprüfen, dass `panic!` keinen Speicher verliert.

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Verhindert, dass REUSE die Copyright-Zeile im Beispielcode auswertet -->
```

```shell
$ rustc panic.rs && valgrind./panic
==4401== Memcheck, a memory error detector
==4401== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==4401== Using Valgrind-3.10.0.SVN and LibVEX; rerun with -h for copyright info
==4401== Command:./panic
==4401==
thread '<main>' panicked at 'division by zero', panic.rs:5
==4401==
==4401== HEAP SUMMARY:
==4401==     in use at exit: 0 bytes in 0 blocks
==4401==   total heap usage: 18 allocs, 18 frees, 1,648 bytes allocated
==4401==
==4401== All heap blocks were freed -- no leaks are possible
==4401==
==4401== For counts of detected and suppressed errors, rerun with: -v
==4401== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```
