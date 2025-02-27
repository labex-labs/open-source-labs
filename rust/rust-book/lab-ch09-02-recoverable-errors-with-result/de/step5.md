# Weiterreichen von Fehlern

Wenn die Implementierung einer Funktion etwas aufruft, das fehlschlagen kann, können Sie statt der Fehlerbehandlung innerhalb der Funktion selbst den Fehler an den aufrufenden Code zurückgeben, sodass dieser entscheiden kann, was zu tun ist. Dies wird als _weiterreichen_ des Fehlers bezeichnet und gibt dem aufrufenden Code mehr Kontrolle, da dort möglicherweise mehr Informationen oder Logik vorhanden ist, die bestimmt, wie der Fehler behandelt werden soll, als Sie in Ihrem Codekontext zur Verfügung haben.

Beispielsweise zeigt Listing 9-6 eine Funktion, die einen Benutzernamen aus einer Datei liest. Wenn die Datei nicht existiert oder nicht gelesen werden kann, gibt diese Funktion diese Fehler an den Code zurück, der die Funktion aufgerufen hat.

Dateiname: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

1 fn read_username_from_file() -> Result<String, io::Error> {
  2 let username_file_result = File::open("hello.txt");

  3 let mut username_file = match username_file_result {
      4 Ok(file) => file,
      5 Err(e) => return Err(e),
    };

  6 let mut username = String::new();

  7 match username_file.read_to_string(&mut username) {
      8 Ok(_) => Ok(username),
      9 Err(e) => Err(e),
    }
}
```

Listing 9-6: Eine Funktion, die Fehler an den aufrufenden Code zurückgibt, indem sie `match` verwendet

Diese Funktion kann auf eine viel kürzere Weise geschrieben werden, aber wir beginnen zunächst, sie vielmehr manuell zu schreiben, um die Fehlerbehandlung zu erkunden; am Ende werden wir die kürzere Weise zeigen. Schauen wir uns zuerst den Rückgabetyp der Funktion an: `Result<String, io::Error>` \[1\]. Dies bedeutet, dass die Funktion einen Wert vom Typ `Result<T, E>` zurückgibt, wobei der generische Parameter `T` mit dem konkreten Typ `String` und der generische Typ `E` mit dem konkreten Typ `io::Error` ausgefüllt wurde.

Wenn diese Funktion erfolgreich verläuft, ohne Probleme, erhält der Code, der diese Funktion aufruft, einen `Ok`-Wert, der eine `String` enthält - den `username`, den diese Funktion aus der Datei gelesen hat \[8\]. Wenn diese Funktion Probleme遇到, erhält der aufrufende Code einen `Err`-Wert, der eine Instanz von `io::Error` enthält, die weitere Informationen über die Probleme enthält. Wir haben `io::Error` als Rückgabetyp dieser Funktion gewählt, weil dies恰巧 der Typ des Fehlerwerts ist, der von beiden Operationen zurückgegeben wird, die wir in der Funktionskörper dieser Funktion aufrufen, die fehlschlagen können: die `File::open`-Funktion \[2\] und die `read_to_string`-Methode \[7\].

Der Funktionskörper beginnt mit dem Aufruf der `File::open`-Funktion \[2\]. Dann behandeln wir den `Result`-Wert mit einem `match`, ähnlich wie dem `match` in Listing 9-4. Wenn `File::open` erfolgreich ist, wird der Dateihandle in der Mustervariable `file` \[4\] zum Wert in der mutablen Variable `username_file` \[3\] und die Funktion setzt fort. Im `Err`-Fall rufen wir statt `panic!` das `return`-Schlüsselwort auf, um ganz frühzeitig aus der Funktion auszusteigen und den Fehlerwert von `File::open`, jetzt in der Mustervariable `e`, als Fehlerwert dieser Funktion an den aufrufenden Code zurückzugeben \[5\].

Wenn wir also einen Dateihandle in `username_file` haben, erstellt die Funktion dann eine neue `String` in der Variable `username` \[6\] und ruft die `read_to_string`-Methode auf dem Dateihandle in `username_file` auf, um den Inhalt der Datei in `username` zu lesen \[7\]. Die `read_to_string`-Methode gibt ebenfalls ein `Result` zurück, da sie fehlschlagen kann, auch wenn `File::open` erfolgreich war. Wir brauchen daher ein weiteres `match`, um dieses `Result` zu behandeln: Wenn `read_to_string` erfolgreich ist, hat unsere Funktion erfolgreich abgeschlossen, und wir geben den Benutzernamen aus der Datei, der jetzt in `username` ist, in einem `Ok` zurück. Wenn `read_to_string` fehlschlägt, geben wir den Fehlerwert auf die gleiche Weise zurück, wie wir den Fehlerwert im `match` zurückgegeben haben, das den Rückgabewert von `File::open` behandelt hat. Wir müssen jedoch nicht explizit `return` sagen, da dies der letzte Ausdruck in der Funktion ist \[9\].

Der Code, der diesen Code aufruft, wird dann das Erhalten eines `Ok`-Werts, der einen Benutzernamen enthält, oder eines `Err`-Werts, der eine `io::Error` enthält, behandeln. Es liegt an dem aufrufenden Code, zu entscheiden, was mit diesen Werten zu tun ist. Wenn der aufrufende Code einen `Err`-Wert erhält, kann er `panic!` aufrufen und das Programm abstürzen, einen Standardbenutzernamen verwenden oder den Benutzernamen an einem anderen Ort als aus einer Datei abrufen, beispielsweise. Wir haben nicht genug Informationen darüber, was der aufrufende Code tatsächlich tun möchte, daher leiten wir alle Erfolg- oder Fehlerinformationen nach oben weiter, damit er sie entsprechend behandeln kann.

Dieses Muster des Weiterreichsens von Fehlern ist in Rust so üblich, dass Rust den Fragezeichen-Operator `?` bereitstellt, um dies zu erleichtern.
