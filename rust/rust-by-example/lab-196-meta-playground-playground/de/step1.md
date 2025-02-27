# Playground

Der [Rust Playground](https://play.rust-lang.org/) ist eine Möglichkeit, mit Rust-Code über eine Weboberfläche zu experimentieren.

## Verwenden mit `mdbook`

In `mdbook` kannst du Codebeispiele spielbar und bearbeitbar machen.

```rust
fn main() {
    println!("Hello World!");
}
```

Dadurch kann der Leser sowohl deinen Codesample ausführen, als auch ihn modifizieren und anpassen. Der Schlüssel hier ist das Hinzufügen des Wortes `editable` zu deinem Codefence-Block, getrennt durch einen Komma.

````markdown
```rust
//...place your code here
```
````

Zusätzlich kannst du `ignore` hinzufügen, wenn du möchtest, dass `mdbook` deinen Code überspringt, wenn es baut und testet.

````markdown
```rust
//...place your code here
```
````

## Verwenden mit Dokumentationen

Du hast vielleicht in einigen der offiziellen Rust-Dokumentationen einen Button bemerkt, der "Ausführen" sagt, der den Codesample in einem neuen Tab im Rust Playground öffnet. Diese Funktion wird aktiviert, wenn du das #\[doc\]-Attribut `html_playground_url` verwendest.
