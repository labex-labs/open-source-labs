# Fälle, in denen du mehr Informationen hast als der Compiler

Es wäre ebenfalls angemessen, `unwrap` oder `expect` aufzurufen, wenn du andere Logik hast, die gewährleistet, dass der `Result`-Wert einen `Ok`-Wert haben wird, aber die Logik ist etwas, das der Compiler nicht versteht. Du hast immer noch einen `Result`-Wert, den du behandeln musst: Die von dir aufgerufene Operation hat im Allgemeinen immer noch die Möglichkeit, fehlzuschlagen, auch wenn dies in deiner speziellen Situation logisch unmöglich ist. Wenn du durch manuelles Überprüfen des Codes sicher sein kannst, dass du niemals einen `Err`-Varianten haben wirst, ist es völlig akzeptabel, `unwrap` aufzurufen, und es ist sogar besser, den Grund in der `expect`-Nachricht zu dokumentieren, warum du glaubst, dass du niemals einen `Err`-Varianten haben wirst. Hier ist ein Beispiel:

```rust
use std::net::IpAddr;

let home: IpAddr = "127.0.0.1"
 .parse()
 .expect("Hardcoded IP address should be valid");
```

Wir erstellen eine `IpAddr`-Instanz, indem wir einen hardcodierten String parsen. Wir können sehen, dass `127.0.0.1` eine gültige IP-Adresse ist, daher ist es hier akzeptabel, `expect` zu verwenden. Ein hardcodierter, gültiger String ändert jedoch den Rückgabetyp der `parse`-Methode nicht: Wir erhalten immer noch einen `Result`-Wert, und der Compiler wird uns weiterhin dazu zwingen, das `Result` so zu behandeln, als wäre der `Err`-Varianten eine Möglichkeit, weil der Compiler nicht intelligent genug ist, zu erkennen, dass dieser String immer eine gültige IP-Adresse ist. Wenn die IP-Adresszeichenfolge von einem Benutzer stammt, anstatt in das Programm hardcodiert zu sein, und daher tatsächlich die Möglichkeit eines Fehlschlags hat, würden wir auf jeden Fall den `Result` auf eine robusterere Weise behandeln wollen. Die Erwähnung der Annahme, dass diese IP-Adresse hardcodiert ist, wird uns dazu veranlassen, `expect` in besseren Fehlerbehandlungs-Code zu ändern, wenn wir in Zukunft die IP-Adresse von einer anderen Quelle beziehen müssen.
