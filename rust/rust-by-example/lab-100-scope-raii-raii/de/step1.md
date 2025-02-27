# RAII

Variablen in Rust tun mehr als nur Daten auf dem Stack zu speichern: Sie besitzen auch Ressourcen, z.B. `Box<T>` besitzt Speicher im Heap. Rust erzwingt RAII (Resource Acquisition Is Initialization), sodass jedes Mal, wenn ein Objekt außerhalb seines Gültigkeitsbereichs gelangt, sein Destruktor aufgerufen wird und seine besitzten Ressourcen freigegeben werden.

Dieses Verhalten schützt vor Fehlern durch Ressourcenlecks, sodass Sie nie wieder manuell Speicher freigeben müssen oder sich um Speicherlecks kümmern! Hier ist ein kurzes Beispiel:

```rust
// raii.rs
fn create_box() {
    // Allokiere einen Integer im Heap
    let _box1 = Box::new(3i32);

    // `_box1` wird hier zerstört und der Speicher wird freigegeben
}

fn main() {
    // Allokiere einen Integer im Heap
    let _box2 = Box::new(5i32);

    // Ein geschachtelter Gültigkeitsbereich:
    {
        // Allokiere einen Integer im Heap
        let _box3 = Box::new(4i32);

        // `_box3` wird hier zerstört und der Speicher wird freigegeben
    }

    // Viele Boxen nur zum Spaß erzeugen
    // Es ist nicht erforderlich, den Speicher manuell zu freigeben!
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` wird hier zerstört und der Speicher wird freigegeben
}
```

Natürlich können wir die Speicherfehler mit `valgrind` doppelt überprüfen:

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc raii.rs && valgrind./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command:./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```

Keine Lecks hier!

## Destruktor

Der Begriff des Destruktors in Rust wird durch das \[`Drop`\]-Attribut bereitgestellt. Der Destruktor wird aufgerufen, wenn die Ressource außerhalb ihres Gültigkeitsbereichs gelangt. Dieses Attribut muss nicht für jeden Typ implementiert werden, sondern nur für Ihren Typ, wenn Sie seine eigene Destruktorkonfiguration benötigen.

Führen Sie das folgende Beispiel aus, um zu sehen, wie das \[`Drop`\]-Attribut funktioniert. Wenn die Variable in der `main`-Funktion außerhalb ihres Gültigkeitsbereichs gelangt, wird der benutzerdefinierte Destruktor aufgerufen.

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop wird zerstört");
    }
}

fn main() {
    let x = ToDrop;
    println!("Ein ToDrop erstellt!");
}
```
