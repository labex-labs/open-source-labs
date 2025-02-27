# Unsafe Superkräfte

Um zu unsafe Rust zu wechseln, verwendest du das Schlüsselwort `unsafe` und startest dann einen neuen Block, in dem der unsafe Code steht. In unsafe Rust kannst du fünf Aktionen ausführen, die du in safe Rust nicht ausführen kannst, was wir als _unsafe Superkräfte_ bezeichnen. Diese Superkräfte umfassen die Fähigkeit:

1.  Ein rohen Zeiger zu dereferenzieren
2.  Eine unsichere Funktion oder Methode aufzurufen
3.  Ein mutables statisches Variable zuzugreifen oder zu modifizieren
4.  Ein unsicheres Trait zu implementieren
5.  Felder von `union`s zuzugreifen

Es ist wichtig zu verstehen, dass `unsafe` den Borrow-Checker nicht deaktiviert oder keine anderen Sicherheitsüberprüfungen von Rust deaktiviert: Wenn du in unsafe Code eine Referenz verwendest, wird sie immer noch überprüft. Das Schlüsselwort `unsafe` gibt dir nur Zugang zu diesen fünf Funktionen, die dann von dem Compiler nicht auf Speichersicherheit überprüft werden. Du erhältst immer noch einen gewissen Grad an Sicherheit innerhalb eines unsafe Blocks.

Zusätzlich bedeutet `unsafe` nicht, dass der Code innerhalb des Blocks notwendigerweise gefährlich ist oder dass er definitiv Speichersicherheitsfehler haben wird: Die Absicht ist, dass als Programmierer du sicherstellst, dass der Code innerhalb eines `unsafe` Blocks den Speicher auf eine gültige Weise zugreift.

Menschen können fehlerhaft sein und Fehler werden passieren, aber indem diese fünf unsicheren Operationen in Blöcken mit `unsafe` annotiert sein müssen, weißt du, dass alle Fehler, die mit der Speichersicherheit zusammenhängen, innerhalb eines `unsafe` Blocks liegen müssen. Halte `unsafe` Blöcke klein; du wirst es später dankbar sein, wenn du Speicherfehler untersuchst.

Um unsafe Code so weit wie möglich zu isolieren, ist es am besten, diesen Code in eine sichere Abstraktion zu kapseln und eine sichere Schnittstelle bereitzustellen, über die wir später im Kapitel sprechen werden, wenn wir uns unsicheren Funktionen und Methoden widmen. Teile der Standardbibliothek werden als sichere Abstraktionen über unsafe Code implementiert, der überprüft wurde. Das Umhüllen von unsafe Code in eine sichere Abstraktion verhindert, dass die Verwendung von `unsafe` in alle Orte ausleckt, an denen du oder deine Benutzer die Funktionalität verwenden möchten, die mit unsafe Code implementiert wurde, denn das Verwenden einer sicheren Abstraktion ist sicher.

Lass uns nacheinander die fünf unsafe Superkräfte betrachten. Wir werden auch einige Abstraktionen betrachten, die eine sichere Schnittstelle zu unsafe Code bieten.
