# Einführung

In diesem Lab untersuchen wir die Angabe von Lebensdauern in Trait-Methoden, was ähnlich zu Funktionen ist. Dabei muss auch in der `impl`-Blöcke die Lebensdauer angegeben werden. Der bereitgestellte Code zeigt ein Beispiel, in dem eine Struktur `Borrowed` eine Lebensdauerangabe hat, und das `Default`-Trait für sie mit der annotierten Lebensdauer implementiert wird. Die Hauptfunktion erstellt dann eine Instanz von `Borrowed` mit der Methode `Default::default()`, was die Verwendung von Lebensdauern in Trait-Methoden zeigt.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
