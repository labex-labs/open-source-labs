# Objekte enthalten Daten und Verhalten

Das Buch _Design Patterns: Elements of Reusable Object-Oriented Software_ von Erich Gamma, Richard Helm, Ralph Johnson und John Vlissides (Addison-Wesley, 1994), das üblicherweise als _The Gang of Four_ -Buch bezeichnet wird, ist ein Katalog von objektorientierten Designmustern. Es definiert die OOP auf diese Weise:

Objektorientierte Programme bestehen aus Objekten. Ein _Objekt_ verpackt sowohl Daten als auch die Prozeduren, die auf diesen Daten operieren. Die Prozeduren werden typischerweise als _Methoden_ oder _Operationen_ bezeichnet.

Unter Verwendung dieser Definition ist Rust objektorientiert: Structs und Enums haben Daten, und `impl` -Blöcke bieten Methoden für Structs und Enums. Auch wenn Structs und Enums mit Methoden nicht als _Objekte_ bezeichnet werden, bieten sie die gleiche Funktionalität gemäß der Definition von Objekten durch die Gruppe von Vier.
