# Verwenden von externen Funktionen, um externen Code aufzurufen

Manchmal muss dein Rust-Code mit Code interagieren, der in einer anderen Sprache geschrieben wurde. Dazu hat Rust das Schlüsselwort `extern`, das die Erstellung und Verwendung einer _Foreign Function Interface_ _(FFI)_ erleichtert, was eine Möglichkeit ist, für eine Programmiersprache Funktionen zu definieren und es einer anderen (fremden) Programmiersprache zu ermöglichen, diese Funktionen aufzurufen.

Listing 19-8 zeigt, wie man eine Integration mit der `abs`-Funktion aus der C-Standardbibliothek einrichtet. Funktionen, die innerhalb von `extern`-Blöcken deklariert werden, sind immer unsicher, um von Rust-Code aus aufgerufen zu werden. Der Grund dafür ist, dass andere Sprachen die Regeln und Garantien von Rust nicht durchsetzen und Rust diese nicht überprüfen kann, sodass die Verantwortung bei dem Programmierer liegt, um die Sicherheit zu gewährleisten.

Dateiname: `src/main.rs`

```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!(
            "Absolute value of -3 according to C: {}",
            abs(-3)
        );
    }
}
```

Listing 19-8: Deklarieren und Aufrufen einer `extern`-Funktion, die in einer anderen Sprache definiert ist

Innerhalb des `extern "C"`-Blocks listieren wir die Namen und Signaturen von externen Funktionen aus einer anderen Sprache, die wir aufrufen möchten. Der `"C"`-Teil definiert, welche _application binary interface_ _(ABI)_ die externe Funktion verwendet: Das ABI definiert, wie die Funktion auf Assembly-Ebene aufgerufen wird. Das `"C"`-ABI ist der am häufigsten verwendete und folgt dem ABI der C-Programmiersprache.

> **Aufrufen von Rust-Funktionen aus anderen Sprachen**
>
> Wir können auch `extern` verwenden, um eine Schnittstelle zu erstellen, die anderen Sprachen ermöglicht, Rust-Funktionen aufzurufen. Anstatt einen ganzen `extern`-Block zu erstellen, fügen wir das `extern`-Schlüsselwort hinzu und geben das zu verwendende ABI vor dem `fn`-Schlüsselwort für die relevante Funktion an. Wir müssen auch eine `#[no_mangle]`-Annotation hinzufügen, um dem Rust-Compiler zu sagen, dass er den Namen dieser Funktion nicht verzerren soll. _Verzerren_ ist, wenn ein Compiler den Namen, den wir einer Funktion gegeben haben, in einen anderen Namen umwandelt, der mehr Informationen für andere Teile des Kompilierungsprozesses enthält, aber weniger menschlich lesbar ist. Jeder Programmiersprachen-Compiler verzerren die Namen etwas unterschiedlich, sodass für eine Rust-Funktion, die von anderen Sprachen benannt werden soll, wir den Namenverzerrung des Rust-Compilers deaktivieren müssen.
>
> Im folgenden Beispiel wird die `call_from_c`-Funktion für C-Code zugänglich gemacht, nachdem sie in eine Shared Library kompiliert und von C aus verknüpft wurde:
>
>     #[no_mangle]
>     pub extern "C" fn call_from_c() {
>         println!("Just called a Rust function from C!");
>     }
>
> Diese Verwendung von `extern` erfordert keine `unsafe`.
