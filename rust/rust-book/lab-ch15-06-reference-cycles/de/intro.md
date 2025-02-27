# Einführung

Willkommen zu **Reference Cycles Can Leak Memory**. Dieser Lab ist Teil des [Rust Buchs](https://doc.rust-lang.org/book/). Du kannst deine Rust-Fähigkeiten in LabEx üben.

In diesem Lab untersuchen wir, wie Rusts Garantien für die Arbeitsspeicher-Sicherheit es schwierig, aber nicht unmöglich macht, versehentlich Arbeitsspeicher-Lecks zu erzeugen, insbesondere wenn `Rc<T>` und `RefCell<T>` verwendet werden, was zu Referenzzirkeln führen kann, die verhindern, dass Werte gelöscht werden und somit Arbeitsspeicher verlieren.
