# Types de clés alternatifs/ personnalisés

N'importe quel type qui implémente les traits `Eq` et `Hash` peut être une clé dans un `HashMap`. Cela inclut :

- `bool` (quoique pas très utile car il n'y a que deux clés possibles)
- `int`, `uint` et toutes leurs variantes
- `String` et `&str` (astuce : vous pouvez avoir un `HashMap` indexé par `String` et appeler `.get()` avec un `&str`)

Notez que `f32` et `f64` n'implémentent pas `Hash`, probablement parce que les erreurs de précision des nombres à virgule flottante rendraient l'utilisation de ces types comme clés de hashmap très sujette à des erreurs.

Toutes les classes de collection implémentent `Eq` et `Hash` si leur type contenu implémente également respectivement `Eq` et `Hash`. Par exemple, `Vec<T>` implémentera `Hash` si `T` implémente `Hash`.

Vous pouvez facilement implémenter `Eq` et `Hash` pour un type personnalisé avec une seule ligne : `#[derive(PartialEq, Eq, Hash)]`

Le compilateur s'en chargera du reste. Si vous voulez plus de contrôle sur les détails, vous pouvez implémenter `Eq` et/ou `Hash` vous-même. Ce guide ne couvrira pas les détails de l'implémentation de `Hash`.

Pour tester l'utilisation d'un `struct` dans un `HashMap`, essayons de créer un système de connexion d'utilisateur très simple :

```rust
use std::collections::HashMap;

// Eq nécessite que vous dérivez PartialEq sur le type.
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
    println!("Attempting logon...");

    let logon = Account {
        username,
        password,
    };

    match accounts.get(&logon) {
        Some(account_info) => {
            println!("Successful logon!");
            println!("Name: {}", account_info.name);
            println!("Email: {}", account_info.email);
        },
        _ => println!("Login failed!"),
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
