# RefCell`<T>` und das Muster der inneren Veränderbarkeit

_Interne Veränderbarkeit_ ist ein Entwurfsmuster in Rust, das es Ihnen ermöglicht, Daten zu mutieren, auch wenn es unveränderte Referenzen auf diese Daten gibt; normalerweise ist diese Aktion durch die Leihregeln verboten. Um Daten zu mutieren, verwendet das Muster `unsafe`-Code innerhalb einer Datenstruktur, um Rusts übliche Regeln, die die Mutation und das Entleihen regeln, zu umgehen. Unsafe-Code signalisiert dem Compiler, dass wir die Regeln manuell überprüfen, anstatt auf den Compiler zu verlassen, um sie für uns zu überprüfen; wir werden unsafe-Code im Kapitel 19 ausführlicher besprechen.

Wir können nur dann Typen verwenden, die das Muster der inneren Veränderbarkeit verwenden, wenn wir gewährleisten können, dass die Leihregeln zur Laufzeit eingehalten werden, obwohl der Compiler dies nicht gewährleisten kann. Der involvierte `unsafe`-Code wird dann in eine sichere API eingewickelt, und der äußere Typ bleibt immer noch unveränderlich.

Lassen Sie uns dieses Konzept erkunden, indem wir uns den Typ `RefCell<T>` ansehen, der das Muster der inneren Veränderbarkeit folgt.
