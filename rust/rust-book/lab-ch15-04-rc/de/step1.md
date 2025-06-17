# Rc`<T>`, der referenzzählende Smart Pointer

In den meisten Fällen ist die Eigentumszuordnung klar: Du weißt genau, welche Variable ein bestimmter Wert besitzt. Es gibt jedoch Fälle, in denen ein einzelner Wert mehrere Besitzer haben kann. Beispielsweise in Graphen-Datenstrukturen können mehrere Kanten auf den gleichen Knoten verweisen, und dieser Knoten wird konzeptionell von allen Kanten, die auf ihn verweisen, besessen. Ein Knoten sollte nicht bereinigt werden, es sei denn, er hat keine Kanten, die auf ihn verweisen, und somit keine Besitzer.

Du musst die Mehrfachbesitzung explizit aktivieren, indem du den Rust-Typ `Rc<T>` verwendest, was eine Abkürzung für _Referenzzählung_ ist. Der Typ `Rc<T>` verfolgt die Anzahl der Referenzen auf einen Wert, um zu bestimmen, ob der Wert noch in Gebrauch ist. Wenn es keine Referenzen auf einen Wert gibt, kann der Wert bereinigt werden, ohne dass sich irgendwelche Referenzen ungültig machen.

Stelle dir `Rc<T>` wie einen Fernseher in einem Wohnzimmer vor. Wenn eine Person hereinkommt, um fernzusehen, schaltet sie ihn an. Andere können in den Raum kommen und fernsehen. Wenn die letzte Person den Raum verlässt, schaltet sie den Fernseher aus, weil er nicht mehr genutzt wird. Wenn jemand den Fernseher aus schaltet, während andere noch fernsehen, würde es einen Aufruhr unter den verbleibenden Fernsehzuschauern geben!

Wir verwenden den Typ `Rc<T>`, wenn wir einige Daten auf dem Heap für mehrere Teile unseres Programms zu lesen planen und wir zur Compile-Zeit nicht bestimmen können, welcher Teil das Daten zuletzt verwenden wird. Wenn wir wüssten, welcher Teil zuletzt fertig wäre, könnten wir einfach diesen Teil zum Besitzer der Daten machen, und die normalen Eigentumsregeln, die zur Compile-Zeit angewendet werden, würden in Kraft treten.

Beachte, dass `Rc<T>` nur für einfache Thread-Szenarien geeignet ist. Wenn wir in Kapitel 16 über die Parallelität sprechen, werden wir uns mit der Referenzzählung in multithreaded Programmen befassen.
