# Definieren und Instanziieren von Structs

Structs ähneln Tuples, wie in "The Tuple Type" diskutiert, in dem beide mehrere zusammenhängende Werte speichern. Wie bei Tuples können die Elemente eines Structs unterschiedliche Typen sein. Anders als bei Tuples benennst du in einem Struct jedes Datenstück, sodass klar ist, was die Werte bedeuten. Das Hinzufügen dieser Namen bedeutet, dass Structs flexibler als Tuples sind: Du musst dich nicht auf die Reihenfolge der Daten verlassen, um die Werte einer Instanz anzugeben oder zuzugreifen.

Um einen Struct zu definieren, geben wir das Schlüsselwort `struct` ein und benennen den gesamten Struct. Der Name eines Structs sollte die Bedeutung der zusammengefassten Datenstücke beschreiben. Dann definieren wir innerhalb geschweifter Klammern die Namen und Typen der Datenstücke, die wir _Felder_ nennen. Beispielsweise zeigt Listing 5-1 einen Struct, der Informationen über ein Benutzerkonto speichert.

Dateiname: `src/main.rs`

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

Listing 5-1: Eine `User`-Struct-Definition

Um einen Struct nach seiner Definition zu verwenden, erstellen wir eine _Instanz_ dieses Structs, indem wir konkrete Werte für jedes Feld angeben. Wir erstellen eine Instanz, indem wir den Namen des Structs angeben und dann geschweifte Klammern hinzufügen, die Schlüssel: Wert-Paare enthalten, wobei die Schlüssel die Namen der Felder sind und die Werte die Daten sind, die wir in diese Felder speichern möchten. Wir müssen die Felder nicht in der gleichen Reihenfolge angeben, in der wir sie im Struct deklariert haben. Mit anderen Worten, die Struct-Definition ist wie eine allgemeine Vorlage für den Typ, und Instanzen füllen diese Vorlage mit bestimmten Daten aus, um Werte des Typs zu erstellen. Beispielsweise können wir einen bestimmten Benutzer wie in Listing 5-2 deklarieren.

Dateiname: `src/main.rs`

```rust
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

Listing 5-2: Erstellen einer Instanz des `User`-Structs

Um einen bestimmten Wert aus einem Struct zu erhalten, verwenden wir die Punktnotation. Beispielsweise verwenden wir `user1.email`, um die E-Mail-Adresse dieses Benutzers zuzugreifen. Wenn die Instanz änderbar ist, können wir einen Wert ändern, indem wir die Punktnotation verwenden und in ein bestimmtes Feld zuweisen. Listing 5-3 zeigt, wie man den Wert im `email`-Feld einer änderbaren `User`-Instanz ändert.

Dateiname: `src/main.rs`

```rust
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
}
```

Listing 5-3: Ändern des Werts im `email`-Feld einer `User`-Instanz

Beachte, dass die gesamte Instanz änderbar sein muss; Rust erlaubt es uns nicht, nur bestimmte Felder als änderbar zu markieren. Wie bei jedem Ausdruck können wir eine neue Instanz des Structs als den letzten Ausdruck im Funktionskörper konstruieren, um diese neue Instanz implizit zurückzugeben.

Listing 5-4 zeigt eine `build_user`-Funktion, die eine `User`-Instanz mit der angegebenen E-Mail und dem Benutzernamen zurückgibt. Das `active`-Feld erhält den Wert `true`, und das `sign_in_count` erhält einen Wert von `1`.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

Listing 5-4: Eine `build_user`-Funktion, die eine E-Mail und einen Benutzernamen übernimmt und eine `User`-Instanz zurückgibt

Es ergibt Sinn, die Funktionsparameter mit denselben Namen wie die Struct-Felder zu benennen, aber das Wiederholen der `email`- und `username`-Feldnamen und -variablen ist etwas lästig. Wenn der Struct mehr Felder hätte, würde das Wiederholen jedes Namens noch ärgerlich sein. Zum Glück gibt es eine praktische Abkürzung!
