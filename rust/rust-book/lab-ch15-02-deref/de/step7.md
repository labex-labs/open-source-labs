# Wie Deref-Zwangsumwandlung mit Veränderbarkeit interagiert

Ähnlich wie Sie das `Deref`-Trait verwenden, um den `*`-Operator für unveränderliche Referenzen zu überschreiben, können Sie das `DerefMut`-Trait verwenden, um den `*`-Operator für veränderliche Referenzen zu überschreiben.

Rust führt Deref-Zwangsumwandlungen aus, wenn es in drei Fällen Typen und Trait-Implementierungen findet:

- Von `&T` zu `&U`, wenn `T: Deref<Target=U>`
- Von `&mut T` zu `&mut U`, wenn `T: DerefMut<Target=U>`
- Von `&mut T` zu `&U`, wenn `T: Deref<Target=U>`

Die ersten beiden Fälle sind identisch, außer dass der zweite die Veränderbarkeit implementiert. Der erste Fall besagt, dass wenn Sie eine `&T` haben und `T` `Deref` zu einem gewissen Typ `U` implementiert, Sie transparent eine `&U` erhalten können. Der zweite Fall besagt, dass die gleiche Deref-Zwangsumwandlung für veränderliche Referenzen erfolgt.

Der dritte Fall ist komplizierter: Rust wird auch eine veränderliche Referenz in eine unveränderliche umwandeln. Die Umkehrung ist jedoch _nicht_ möglich: unveränderliche Referenzen werden niemals in veränderliche Referenzen umgewandelt. Aufgrund der Entlehnungsregeln, wenn Sie eine veränderliche Referenz haben, muss diese die einzige Referenz auf die Daten sein (sonst würde das Programm nicht kompilieren). Das Konvertieren einer veränderlichen Referenz in eine unveränderliche Referenz wird die Entlehnungsregeln niemals verletzen. Das Konvertieren einer unveränderlichen Referenz in eine veränderliche Referenz würde erfordern, dass die ursprüngliche unveränderliche Referenz die einzige unveränderliche Referenz auf die Daten ist, aber die Entlehnungsregeln gewährleisten dies nicht. Daher kann Rust nicht davon ausgehen, dass das Konvertieren einer unveränderlichen Referenz in eine veränderliche Referenz möglich ist.
