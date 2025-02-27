# Funktionszeiger

Wir haben bereits darüber gesprochen, wie man Closures an Funktionen übergibt; man kann auch reguläre Funktionen an Funktionen übergeben! Diese Technik ist nützlich, wenn man eine bereits definierte Funktion übergeben möchte, anstatt einen neuen Closure zu definieren. Funktionen werden in den Typ `fn` (mit einem kleinen _f_) umgewandelt, nicht zu verwechseln mit dem Closure-Trait `Fn`. Der Typ `fn` wird als _Funktionszeiger_ bezeichnet. Das Übergeben von Funktionen mit Funktionszeigern ermöglicht es Ihnen, Funktionen als Argumente für andere Funktionen zu verwenden.

Die Syntax zum Angeben, dass ein Parameter ein Funktionszeiger ist, ähnelt der von Closures, wie in Listing 19-27 gezeigt, wo wir eine Funktion `add_one` definiert haben, die 1 zu ihrem Parameter addiert. Die Funktion `do_twice` nimmt zwei Parameter: einen Funktionszeiger auf jede Funktion, die einen `i32`-Parameter annimmt und einen `i32` zurückgibt, und einen `i32-Wert`. Die Funktion `do_twice` ruft die Funktion `f` zweimal auf, übergibt ihr den `arg`-Wert und addiert dann die beiden Funktionsaufruf-Ergebnisse zusammen. Die `main`-Funktion ruft `do_twice` mit den Argumenten `add_one` und `5` auf.

Dateiname: `src/main.rs`

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

fn main() {
    let answer = do_twice(add_one, 5);

    println!("The answer is: {answer}");
}
```

Listing 19-27: Verwendung des Typs `fn`, um einen Funktionszeiger als Argument zu akzeptieren

Dieser Code gibt `The answer is: 12` aus. Wir geben an, dass der Parameter `f` in `do_twice` ein `fn` ist, das einen Parameter vom Typ `i32` annimmt und einen `i32` zurückgibt. Wir können dann `f` im Körper von `do_twice` aufrufen. In `main` können wir den Funktionsnamen `add_one` als erstes Argument an `do_twice` übergeben.

Im Gegensatz zu Closures ist `fn` ein Typ und nicht ein Trait, daher geben wir `fn` direkt als Parametertyp an, anstatt einen generischen Typparameter mit einem der `Fn`-Traits als Trait-Bound zu deklarieren.

Funktionszeiger implementieren alle drei Closure-Traits (`Fn`, `FnMut` und `FnOnce`), was bedeutet, dass Sie immer einen Funktionszeiger als Argument für eine Funktion übergeben können, die einen Closure erwartet. Es ist am besten, Funktionen mit einem generischen Typ und einem der Closure-Traits zu schreiben, damit Ihre Funktionen sowohl Funktionen als auch Closures akzeptieren können.

Allerdings ist ein Beispiel dafür, wo man nur `fn` und keine Closures akzeptieren möchte, wenn man mit externem Code interagiert, der keine Closures hat: C-Funktionen können Funktionen als Argumente akzeptieren, aber C hat keine Closures.

Als Beispiel dafür, wo man entweder einen inline definierten Closure oder eine benannte Funktion verwenden könnte, betrachten wir die Verwendung der `map`-Methode, die vom `Iterator`-Trait in der Standardbibliothek bereitgestellt wird. Um die `map`-Funktion zu verwenden, um einen Vektor von Zahlen in einen Vektor von Strings umzuwandeln, könnten wir einen Closure verwenden, wie folgt:

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(|i| i.to_string())
 .collect();
```

Oder wir könnten eine benannte Funktion als Argument für `map` angeben, statt des Closures, wie folgt:

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(ToString::to_string)
 .collect();
```

Beachten Sie, dass wir die vollqualifizierte Syntax verwenden müssen, über die wir in "Erweiterte Traits" gesprochen haben, da es mehrere Funktionen mit dem Namen `to_string` gibt.

Hier verwenden wir die `to_string`-Funktion, die im `ToString`-Trait definiert ist, die die Standardbibliothek für jeden Typ implementiert hat, der `Display` implementiert.

Denken Sie sich aus "Enum-Werte" zurück, dass der Name jeder Enum-Variante, die wir definieren, auch eine Initialisierungsfunktion wird. Wir können diese Initialisierungsfunktionen als Funktionszeiger verwenden, die die Closure-Traits implementieren, was bedeutet, dass wir die Initialisierungsfunktionen als Argumente für Methoden angeben können, die Closures erwarten, wie folgt:

```rust
enum Status {
    Value(u32),
    Stop,
}

let list_of_statuses: Vec<Status> = (0u32..20)
 .map(Status::Value)
 .collect();
```

Hier erstellen wir `Status::Value`-Instanzen, indem wir jede `u32`-Wert im Bereich verwenden, auf dem `map` aufgerufen wird, indem wir die Initialisierungsfunktion von `Status::Value` verwenden. Einige Leute bevorzugen diesen Stil und einige Leute bevorzugen es, Closures zu verwenden. Sie kompilieren zu demselben Code, daher verwenden Sie den Stil, der Ihnen am klarsten ist.
