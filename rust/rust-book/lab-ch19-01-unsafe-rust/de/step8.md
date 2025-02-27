# Implementieren eines unsicheren Traits

Wir können `unsafe` verwenden, um ein unsicheres Trait zu implementieren. Ein Trait ist unsicher, wenn mindestens eine seiner Methoden eine Invariante hat, die der Compiler nicht verifizieren kann. Wir deklarieren, dass ein Trait `unsafe` ist, indem wir das `unsafe`-Schlüsselwort vor `trait` hinzufügen und die Implementierung des Traits ebenfalls als `unsafe` markieren, wie in Listing 19-11 gezeigt.

    unsafe trait Foo {
        // Methoden gehen hier
    }

    unsafe impl Foo for i32 {
        // Methodenimplementierungen gehen hier
    }

Listing 19-11: Definieren und Implementieren eines unsicheren Traits

Durch die Verwendung von `unsafe impl` versprechen wir, dass wir die Invarianten einhalten werden, die der Compiler nicht verifizieren kann.

Als Beispiel erinnern wir uns an die `Send`- und `Sync`-Marker-Traits, über die wir in "Erweiterbare Konkurrenz mit den Send- und Sync-Traits" diskutiert haben: Der Compiler implementiert diese Traits automatisch, wenn unsere Typen ausschließlich aus `Send`- und `Sync`-Typen bestehen. Wenn wir einen Typ implementieren, der einen Typ enthält, der nicht `Send` oder `Sync` ist, wie z. B. rohe Zeiger, und wir diesen Typ als `Send` oder `Sync` markieren möchten, müssen wir `unsafe` verwenden. Rust kann nicht verifizieren, dass unser Typ die Garantien einhält, dass er sicher über Threads verschickt werden kann oder von mehreren Threads aus zugegriffen werden kann; daher müssen wir diese Prüfungen manuell vornehmen und dies mit `unsafe` anzeigen.
