# Laufzeitüberprüfung der Leihregeln mit RefCell`<T>`

Im Gegensatz zu `Rc<T>` repräsentiert der Typ `RefCell<T>` die alleinige Eigentumsverhältnisse über die von ihm gehaltenen Daten. Was unterscheidet `RefCell<T>` also von einem Typ wie `Box<T>`? Erinnern Sie sich an die Leihregeln, die Sie im Kapitel 4 gelernt haben:

- Zu einem bestimmten Zeitpunkt können Sie entweder eine veränderbare Referenz oder beliebig viele unveränderbare Referenzen haben (aber nicht beide).
- Referenzen müssen immer gültig sein.

Bei Referenzen und `Box<T>` werden die Invarianten der Leihregeln zur Compilezeit überprüft. Bei `RefCell<T>` werden diese Invarianten zur Laufzeit überprüft. Bei Referenzen erhalten Sie bei Verstoß gegen diese Regeln einen Compilerfehler. Bei `RefCell<T>` wird Ihr Programm bei einem Verstoß gegen diese Regeln abstürzen und beenden.

Die Vorteile der Überprüfung der Leihregeln zur Compilezeit sind, dass Fehler früher im Entwicklungsprozess erkannt werden und dass die Laufzeitleistung nicht beeinträchtigt wird, da alle Analysen im Voraus abgeschlossen sind. Aus diesen Gründen ist die Überprüfung der Leihregeln zur Compilezeit in den meisten Fällen die beste Wahl, weshalb dies die Standardmethode von Rust ist.

Der Vorteil der Überprüfung der Leihregeln zur Laufzeit ist dagegen, dass bestimmte sicherheitsrelevante Szenarien dann möglich sind, die durch die Compilezeitprüfungen verboten wären. Statische Analysen wie der Rust-Compiler sind von Natur aus konservativ. Einige Eigenschaften von Code sind unmöglich zu erkennen, indem man den Code analysiert: Das berühmteste Beispiel ist das Halteproblem, das außerhalb des Rahmens dieses Buches liegt, aber ein interessantes Thema für die Recherche.

Da einige Analysen unmöglich sind, kann der Rust-Compiler möglicherweise ein korrektes Programm ablehnen, wenn er nicht sicher ist, dass der Code den Eigentumsregeln entspricht; auf diese Weise ist er konservativ. Wenn Rust ein fehlerhaftes Programm akzeptierte, könnten die Benutzer nicht auf die Garantien vertrauen, die Rust gibt. Wenn Rust jedoch ein korrektes Programm ablehnt, wird der Programmierer belastet, aber nichts Katastrophales kann passieren. Der Typ `RefCell<T>` ist nützlich, wenn Sie sicher sind, dass Ihr Code den Leihregeln folgt, aber der Compiler nicht in der Lage ist, dies zu verstehen und zu gewährleisten.

Ähnlich wie `Rc<T>` ist `RefCell<T>` nur für die Verwendung in einthreadigen Szenarien vorgesehen und gibt Ihnen einen Compilerfehler, wenn Sie versuchen, es in einem mehrthreadigen Kontext zu verwenden. Wir werden im Kapitel 16 darüber sprechen, wie man die Funktionalität von `RefCell<T>` in einem mehrthreadigen Programm erhalten kann.

Hier ist eine Zusammenfassung der Gründe, warum man `Box<T>`, `Rc<T>` oder `RefCell<T>` wählt:

- `Rc<T>` ermöglicht mehrere Besitzer der gleichen Daten; `Box<T>` und `RefCell<T>` haben jeweils einen Besitzer.
- `Box<T>` erlaubt unveränderbare oder veränderbare Leihvorgänge, die zur Compilezeit überprüft werden; `Rc<T>` erlaubt nur unveränderbare Leihvorgänge, die zur Compilezeit überprüft werden; `RefCell<T>` erlaubt unveränderbare oder veränderbare Leihvorgänge, die zur Laufzeit überprüft werden.
- Da `RefCell<T>` veränderbare Leihvorgänge zur Laufzeit erlaubt, können Sie den Wert innerhalb von `RefCell<T>` mutieren, auch wenn `RefCell<T>` unveränderbar ist.

Das Mutieren des Werts innerhalb eines unveränderbaren Werts ist das Muster der _inneren Veränderbarkeit_. Betrachten wir eine Situation, in der die innere Veränderbarkeit nützlich ist, und untersuchen, wie dies möglich ist.
