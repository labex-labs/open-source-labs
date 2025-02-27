# Der Unterschied zwischen Makros und Funktionen

Im Grunde genommen sind Makros eine Möglichkeit, Code zu schreiben, der anderen Code erzeugt, was als _Metaprogrammierung_ bekannt ist. Im Anhang C besprechen wir das `derive`-Attribut, das Ihnen eine Implementierung verschiedener Traits erzeugt. Wir haben auch die Makros `println!` und `vec!` im gesamten Buch verwendet. Alle diese Makros _expandieren_, um mehr Code zu erzeugen, als den Code, den Sie manuell geschrieben haben.

Die Metaprogrammierung ist nützlich, um die Menge an Code zu reduzieren, den Sie schreiben und pflegen müssen, was auch eine der Rollen von Funktionen ist. Allerdings haben Makros einige zusätzliche Kräfte, die Funktionen nicht haben.

Die Signatur einer Funktion muss die Anzahl und den Typ der Parameter angeben, die die Funktion hat. Makros hingegen können eine variable Anzahl von Parametern akzeptieren: wir können `println!("hello")` mit einem Argument oder `println!("hello {}", name)` mit zwei Argumenten aufrufen. Außerdem werden Makros vor der Interpretation des Codes durch den Compiler expandiert, sodass ein Makro beispielsweise ein Trait für einen bestimmten Typ implementieren kann. Eine Funktion kann das nicht, da sie zur Laufzeit aufgerufen wird und ein Trait zur Compilezeit implementiert werden muss.

Der Nachteil der Implementierung eines Makros anstelle einer Funktion ist, dass Makrodefinitionen komplexer als Funktionsdefinitionen sind, da Sie Rust-Code schreiben, der Rust-Code erzeugt. Aufgrund dieser Indirektion sind Makrodefinitionen im Allgemeinen schwieriger zu lesen, zu verstehen und zu pflegen als Funktionsdefinitionen.

Ein weiterer wichtiger Unterschied zwischen Makros und Funktionen ist, dass Sie Makros _vor_ ihrem Aufruf in einer Datei definieren oder in den Gültigkeitsbereich bringen müssen, im Gegensatz zu Funktionen, die Sie überall definieren und überall aufrufen können.
