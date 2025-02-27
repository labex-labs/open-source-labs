# In Enum-Definitionen

Wie bei Strukturen können wir Enums definieren, um generische Datentypen in ihren Varianten zu speichern. Schauen wir uns noch einmal das `Option<T>`-Enum an, das die Standardbibliothek bereitstellt und das wir im Kapitel 6 verwendet haben:

```rust
enum Option<T> {
    Some(T),
    None,
}
```

Diese Definition sollte Ihnen jetzt mehr Sinn machen. Wie Sie sehen können, ist das `Option<T>`-Enum generisch über den Typ `T` und hat zwei Varianten: `Some`, die einen Wert vom Typ `T` enthält, und eine `None`-Variante, die keinen Wert enthält. Indem wir das `Option<T>`-Enum verwenden, können wir das abstrakte Konzept eines optionalen Werts ausdrücken, und da `Option<T>` generisch ist, können wir diese Abstraktion unabhängig vom Typ des optionalen Werts verwenden.

Enums können auch mehrere generische Typen verwenden. Die Definition des `Result`-Enums, das wir im Kapitel 9 verwendet haben, ist ein Beispiel:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Das `Result`-Enum ist generisch über zwei Typen, `T` und `E`, und hat zwei Varianten: `Ok`, die einen Wert vom Typ `T` enthält, und `Err`, die einen Wert vom Typ `E` enthält. Diese Definition macht es bequem, das `Result`-Enum überall zu verwenden, wo wir eine Operation haben, die erfolgreich sein kann (einen Wert eines bestimmten Typs `T` zurückgeben) oder fehlschlagen kann (einen Fehler eines bestimmten Typs `E` zurückgeben). Tatsächlich haben wir dies verwendet, um eine Datei zu öffnen in Listing 9-3, wobei `T` mit dem Typ `std::fs::File` ausgefüllt wurde, wenn die Datei erfolgreich geöffnet wurde, und `E` mit dem Typ `std::io::Error` ausgefüllt wurde, wenn es Probleme beim Öffnen der Datei gab.

Wenn Sie in Ihrem Code Situationen erkennen, in denen mehrere Struktur- oder Enum-Definitionen nur in den Typen der Werte, die sie enthalten, unterschiedlich sind, können Sie die Duplikation vermeiden, indem Sie generische Typen verwenden.
