# Capturing

Closures sind von Natur aus flexibel und werden das tun, was die Funktionalität erfordert, um das Closure ohne Annotation zu machen. Dies ermöglicht es, das Capturing flexibel an den Anwendungsfall anzupassen, manchmal verschiebend und manchmal entleihend. Closures können Variablen erfassen:

- per Referenz: `&T`
- per mutabler Referenz: `&mut T`
- per Wert: `T`

Sie bevorzugen es, Variablen per Referenz zu erfassen und gehen nur niedriger, wenn erforderlich.

```rust
fn main() {
    use std::mem;

    let color = String::from("green");

    // Ein Closure, um `color` auszugeben, das sofort `color` entleiht (`&`) und
    // die Entleihe und das Closure in der `print`-Variable speichert. Es wird
    // bis zum letzten Mal die Entleihe beibehalten, wenn `print` verwendet wird.
    //
    // `println!` erfordert nur Argumente per unveränderlicher Referenz, daher
    // erlegt es keine restriktiveren Anforderungen.
    let print = || println!("`color`: {}", color);

    // Rufen Sie das Closure mit der Entleihe auf.
    print();

    // `color` kann erneut unverändert entliehen werden, da das Closure nur
    // eine unveränderliche Referenz auf `color` hält.
    let _reborrow = &color;
    print();

    // Ein Verschieben oder erneute Entleihe ist nach der letzten Verwendung von
    // `print` möglich
    let _color_moved = color;


    let mut count = 0;
    // Ein Closure, um `count` zu erhöhen, könnte entweder `&mut count` oder
    // `count` nehmen, aber `&mut count` ist weniger restriktiv, daher nimmt
    // es das. Entleiht sofort `count`.
    //
    // Ein `mut` ist erforderlich bei `inc`, da eine `&mut` innerhalb gespeichert
    // ist. Daher mutiert das Aufrufen des Closures das Closure, was einen `mut`
    // erfordert.
    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    // Rufen Sie das Closure mit einer mutablen Entleihe auf.
    inc();

    // Das Closure entleiht immer noch `count` mutabel, da es später aufgerufen
    // wird. Ein Versuch, es erneut zu entleihen, führt zu einem Fehler.
    // let _reborrow = &count;
    // ^ TODO: Versuchen Sie, diese Zeile auszukommentieren.
    inc();

    // Das Closure muss `&mut count` nicht mehr entleihen. Daher ist es
    // möglich, es erneut zu entleihen, ohne einen Fehler zu erhalten
    let _count_reborrowed = &mut count;


    // Ein nicht kopierbarer Typ.
    let movable = Box::new(3);

    // `mem::drop` erfordert `T`, daher muss dies per Wert genommen werden. Ein
    // kopierbarer Typ würde in das Closure kopiert, wobei der Originalwert
    // unberührt bleibt.
    // Ein nicht kopierbarer Typ muss verschoben werden, daher wird `movable`
    // sofort in das Closure verschoben.
    let consume = || {
        println!("`movable`: {:?}", movable);
        mem::drop(movable);
    };

    // `consume` konsumiert die Variable, daher kann dies nur einmal aufgerufen
    // werden.
    consume();
    // consume();
    // ^ TODO: Versuchen Sie, diese Zeile auszukommentieren.
}
```

Das Verwenden von `move` vor den vertikalen Schläuchen zwingt das Closure, die Besitznahme der erfassten Variablen zu übernehmen:

```rust
fn main() {
    // `Vec` hat nicht-kopierende Semantik.
    let haystack = vec![1, 2, 3];

    let contains = move |needle| haystack.contains(needle);

    println!("{}", contains(&1));
    println!("{}", contains(&4));

    // println!("There're {} elements in vec", haystack.len());
    // ^ Wenn Sie die obige Zeile auskommentieren, wird ein
    // Kompilierfehler auftreten, da der Entleihprüfer nicht erlaubt,
    // die Variable erneut zu verwenden, nachdem sie verschoben wurde.

    // Wenn Sie `move` aus der Signatur des Closures entfernen, wird das
    // Closure die _haystack_-Variable unverändert entleihen, daher ist
    // _haystack_ immer noch verfügbar und das Auskommentieren der
    // obigen Zeile verursacht keinen Fehler.
}
```
