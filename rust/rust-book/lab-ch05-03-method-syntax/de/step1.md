# Methoden-Syntax

_Methoden_ ähneln Funktionen: Wir deklarieren sie mit dem `fn`-Schlüsselwort und einem Namen, sie können Parameter und einen Rückgabewert haben und enthalten einige Codezeilen, die ausgeführt werden, wenn die Methode von irgendwo anders aufgerufen wird. Anders als Funktionen werden Methoden innerhalb des Kontexts einer Struktur (oder eines Enums oder eines Trait-Objekts, die wir in Kapitel 6 und Kapitel 17 behandeln) definiert, und ihr erster Parameter ist immer `self`, der die Instanz der Struktur darstellt, auf der die Methode aufgerufen wird.
