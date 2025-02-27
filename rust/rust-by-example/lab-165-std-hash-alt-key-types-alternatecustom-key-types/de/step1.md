# Alternativer/benutzerdefinierter Schlüsseltypen

Jeder Typ, der die `Eq`- und `Hash`-Traits implementiert, kann ein Schlüssel in einer `HashMap` sein. Dies umfasst:

- `bool` (wenngleich nicht sehr nützlich, da es nur zwei mögliche Schlüssel gibt)
- `int`, `uint` und alle davon abgeleiteten Variationen
- `String` und `&str` (Tipp: Sie können eine `HashMap` mit `String` als Schlüssel haben und `.get()` mit einem `&str` aufrufen)

Beachten Sie, dass `f32` und `f64` `Hash` nicht implementieren, wahrscheinlich weil Gleitkomma-Präzisionsfehler dazu führen würden, sie als Hashtabellenschlüssel zu verwenden, was zu schwerwiegenden Fehlern führen würde.

Alle Sammlungsklassen implementieren `Eq` und `Hash`, wenn auch der von ihnen enthaltene Typ `Eq` und `Hash` implementiert. Beispielsweise wird `Vec<T>` `Hash` implementieren, wenn `T` `Hash` implementiert.

Sie können `Eq` und `Hash` für einen benutzerdefinierten Typ mit nur einer Zeile leicht implementieren: `#[derive(PartialEq, Eq, Hash)]`

Der Compiler wird den Rest erledigen. Wenn Sie mehr Kontrolle über die Details möchten, können Sie `Eq` und/oder `Hash` selbst implementieren. In dieser Anleitung werden die Details der Implementierung von `Hash` nicht behandelt.

Um mit der Verwendung einer `struct` in einer `HashMap` zu experimentieren, versuchen wir, ein sehr einfaches Benutzeranmeldesystem zu implementieren:

```rust
use std::collections::HashMap;

// Eq erfordert, dass Sie PartialEq für den Typ ableiten.
#[derive(PartialEq, Eq, Hash)]
struct Account<'a>{
    username: &'a str,
    password: &'a str,
}

struct AccountInfo<'a>{
    name: &'a str,
    email: &'a str,
}

type Accounts<'a> = HashMap<Account<'a>, AccountInfo<'a>>;

fn try_logon<'a>(accounts: &Accounts<'a>,
        username: &'a str, password: &'a str){
    println!("Username: {}", username);
    println!("Password: {}", password);
    println!("Versuche Anmeldung...");

    let logon = Account {
        username,
        password,
    };

    match accounts.get(&logon) {
        Some(account_info) => {
            println!("Erfolgreiche Anmeldung!");
            println!("Name: {}", account_info.name);
            println!("Email: {}", account_info.email);
        },
        _ => println!("Anmeldung fehlgeschlagen!"),
    }
}

fn main(){
    let mut accounts: Accounts = HashMap::new();

    let account = Account {
        username: "j.everyman",
        password: "password123",
    };

    let account_info = AccountInfo {
        name: "John Everyman",
        email: "j.everyman@email.com",
    };

    accounts.insert(account, account_info);

    try_logon(&accounts, "j.everyman", "psasword123");

    try_logon(&accounts, "j.everyman", "password123");
}
```
