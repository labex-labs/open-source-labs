# Traits as Parameters

Jetzt, nachdem Sie wissen, wie Sie Traits definieren und implementieren, können wir untersuchen, wie Sie Traits verwenden, um Funktionen zu definieren, die viele verschiedene Typen akzeptieren. Wir werden das `Summary`-Trait, das wir in Listing 10-13 auf den Typen `NewsArticle` und `Tweet` implementiert haben, verwenden, um eine `notify`-Funktion zu definieren, die die `summarize`-Methode auf ihrem `item`-Parameter aufruft, der vom Typ ist, der das `Summary`-Trait implementiert. Dazu verwenden wir die `impl Trait`-Syntax wie folgt:

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

Anstatt einen konkreten Typ für den `item`-Parameter anzugeben, geben wir das `impl`-Schlüsselwort und den Traitnamen an. Dieser Parameter akzeptiert jeden Typ, der das angegebene Trait implementiert. Im Körper von `notify` können wir beliebige Methoden auf `item` aufrufen, die aus dem `Summary`-Trait stammen, wie `summarize`. Wir können `notify` aufrufen und jedes `NewsArticle`- oder `Tweet`-Objekt übergeben. Code, der die Funktion mit einem anderen Typ wie `String` oder `i32` aufruft, wird nicht kompilieren, da diese Typen nicht `Summary` implementieren.
