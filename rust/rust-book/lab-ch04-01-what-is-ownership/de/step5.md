# Arbeitsspeicher und Zuweisung

Im Fall eines String-Literals kennen wir den Inhalt zur Compile-Zeit, sodass der Text direkt in das endgültige ausführbare Programm hartenkodiert ist. Deshalb sind String-Literale schnell und effizient. Aber diese Eigenschaften resultieren nur aus der Unveränderlichkeit des String-Literals. Leider können wir nicht für jedes Stück Text, dessen Größe zur Compile-Zeit unbekannt ist und die sich während der Programmausführung ändern kann, einen Arbeitsspeicherblock in das Binärprogramm einfügen.

Mit dem `String`-Typ müssen wir, um einen veränderlichen, wachsenden Text zu unterstützen, einen Arbeitsspeicherplatz auf dem Heap reservieren, der zur Compile-Zeit unbekannt ist, um den Inhalt zu speichern. Dies bedeutet:

- Der Arbeitsspeicher muss zur Laufzeit vom Arbeitsspeicherzuweisungsdienst angefordert werden.
- Wir brauchen eine Möglichkeit, diesen Arbeitsspeicherplatz zurückzugeben, wenn wir mit unserem `String` fertig sind.

Der erste Teil wird von uns erledigt: Wenn wir `String::from` aufrufen, fordert seine Implementierung den benötigten Arbeitsspeicherplatz an. Dies ist in den meisten Programmiersprachen weit verbreitet.

Der zweite Teil ist jedoch unterschiedlich. In Sprachen mit einem _Garbage Collector (GC)_ überwacht der GC den Arbeitsspeicher und bereinigt nicht mehr verwendeten Speicher, und wir müssen uns nicht darum kümmern. In den meisten Sprachen ohne GC ist es unsere Verantwortung, zu identifizieren, wann der Arbeitsspeicher nicht mehr verwendet wird, und Code aufzurufen, um ihn explizit freizugeben, genauso wie wir ihn angefordert haben. Dies hat sich historisch als schwieriges Programmierproblem erwiesen. Wenn wir vergessen, verschwenden wir Arbeitsspeicher. Wenn wir es zu früh tun, haben wir eine ungültige Variable. Wenn wir es zweimal tun, ist das ebenfalls ein Fehler. Wir müssen genau eine `allocate` mit genau einer `free` verknüpfen.

Rust wählt einen anderen Weg: Der Arbeitsspeicher wird automatisch zurückgegeben, sobald die Variable, die ihn besitzt, außerhalb ihres Gültigkeitsbereichs fällt. Hier ist eine Version unseres Bereichsbeispiels aus Listing 4-1, bei der wir einen `String` anstelle eines String-Literals verwenden:

    {
        let s = String::from("hello"); // s ist ab diesem Zeitpunkt gültig

        // mache etwas mit s
    }                                  // dieser Bereich ist jetzt vorbei, und s ist nicht mehr gültig

Es gibt einen natürlichen Zeitpunkt, zu dem wir den Arbeitsspeicherplatz zurückgeben können, den unser `String` benötigt, dem Arbeitsspeicherzuweisungsdienst: wenn `s` außerhalb seines Gültigkeitsbereichs fällt. Wenn eine Variable außerhalb ihres Gültigkeitsbereichs fällt, ruft Rust eine spezielle Funktion für uns auf. Diese Funktion heißt `drop`, und hier kann der Autor von `String` den Code einfügen, um den Arbeitsspeicherplatz zurückzugeben. Rust ruft `drop` automatisch bei der schließenden geschweiften Klammer auf.

> Hinweis: In C++ wird dieses Muster des Freigebens von Ressourcen am Ende der Lebensdauer eines Elements manchmal als _Resource Acquisition Is Initialization_ _(RAII)_ bezeichnet. Die `drop`-Funktion in Rust sollte Ihnen vertraut sein, wenn Sie RAII-Muster verwendet haben.

Dieses Muster hat einen tiefgreifenden Einfluss auf die Art und Weise, wie Rust-Code geschrieben wird. Es mag momentan einfach erscheinen, aber das Verhalten des Codes kann in komplexeren Situationen unerwartet sein, wenn wir mehrere Variablen verwenden möchten, die auf dem Heap zugewiesenen Daten nutzen. Lassen Sie uns einige dieser Situationen jetzt untersuchen.
