# Mehrfach-Eigentum mit mehreren Threads

Im Kapitel 15 haben wir einem Wert mehrere Besitzer gegeben, indem wir den Smart-Pointer `Rc<T>` verwendet haben, um einen referenzzählenden Wert zu erstellen. Lassen Sie uns das hier wieder tun und sehen, was passiert. Wir werden das `Mutex<T>` in `Rc<T>` in Listing 16-14 einwickeln und das `Rc<T>` klonen, bevor wir die Eigentumsgewalt an den Thread übertragen.

Dateiname: `src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Listing 16-14: Versuch, `Rc<T>` zu verwenden, um mehreren Threads das `Mutex<T>` zu geben

Wir kompilieren erneut und erhalten... unterschiedliche Fehler! Der Compiler lehrt uns viel.

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

Wow, diese Fehlermeldung ist sehr wortreich! Hier ist der wichtige Teil, auf den Sie sich konzentrieren sollten: ``Rc<Mutex<i32>>` cannot be sent between threads safely` [1]. Der Compiler sagt uns auch den Grund dafür: `the trait `Send` is not implemented for `Rc<Mutex<i32>>`` \[2\]. Wir werden im nächsten Abschnitt über `Send` sprechen: es ist eines der Traits, die gewährleistet, dass die Typen, die wir mit Threads verwenden, für die Verwendung in konkurrierenden Situationen geeignet sind.

Leider ist es nicht sicher, `Rc<T>` über Threads hinweg zu teilen. Wenn `Rc<T>` die Referenzzählung verwaltet, erhöht es die Anzahl für jeden Aufruf von `clone` und verringert die Anzahl, wenn jeder Klon fallen gelassen wird. Aber es verwendet keine konkurrenzspezifischen Primitiven, um sicherzustellen, dass Änderungen an der Anzahl nicht von einem anderen Thread unterbrochen werden können. Dies könnte zu falschen Zählungen führen - subtilen Fehlern, die wiederum zu Speicherlecks oder einem Wert führen können, der vor dem Ende der Verwendung fallen gelassen wird. Was wir brauchen, ist ein Typ, der genau wie `Rc<T>` ist, aber der Änderungen an der Referenzzählung auf einem threadsicheren Weg vornimmt.
