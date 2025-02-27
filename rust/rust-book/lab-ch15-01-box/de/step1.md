# Verwenden von `Box<T>`{=html} um auf Daten auf dem Heap zu verweisen

Der einfachste Smart-Pointer ist eine _Box_, deren Typ als `Box<T>` geschrieben wird. Boxen ermöglichen es Ihnen, Daten auf dem Heap statt auf dem Stack zu speichern. Was auf dem Stack bleibt, ist der Zeiger auf die Heap-Daten. Siehe Kapitel 4, um den Unterschied zwischen Stack und Heap zu überprüfen.

Boxen haben keine Leistungseinbußen, außer dass sie ihre Daten auf dem Heap statt auf dem Stack speichern. Aber sie haben auch keine vielen zusätzlichen Funktionen. Sie werden sie am häufigsten in diesen Situationen verwenden:

- Wenn Sie einen Typ haben, dessen Größe zur Compile-Zeit nicht bekannt sein kann, und Sie einen Wert dieses Typs in einem Kontext verwenden möchten, der eine exakte Größe erfordert
- Wenn Sie eine große Menge an Daten haben und Sie die Eigentumsübertragung möchten, aber sicherstellen, dass die Daten nicht kopiert werden, wenn Sie dies tun
- Wenn Sie einen Wert besitzen und Sie sich nur darum kümmern, dass es ein Typ ist, der ein bestimmtes Merkmal implementiert, anstatt eines bestimmten Typs zu sein

Wir werden die erste Situation in "Enabling Recursive Types with Boxes" demonstrieren. Im zweiten Fall kann die Übertragung der Eigentumsübertragung einer großen Menge an Daten lange Zeit in Anspruch nehmen, da die Daten auf dem Stack herumkopiert werden. Um die Leistung in dieser Situation zu verbessern, können wir die große Menge an Daten in einer Box auf dem Heap speichern. Dann wird nur die kleine Menge an Zeigerdaten auf dem Stack herumkopiert, während die von ihr referenzierten Daten an einem Ort auf dem Heap bleiben. Der dritte Fall ist als _Trait-Objekt_ bekannt, und "Using Trait Objects That Allow for Values of Different Types" widmet sich diesem Thema. Was Sie hier lernen, werden Sie also wieder in diesem Abschnitt anwenden!
