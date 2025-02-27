# Tipos de claves alternativas/personalizadas

Cualquier tipo que implemente los tratos `Eq` y `Hash` puede ser una clave en `HashMap`. Esto incluye:

- `bool` (aunque no es muy útil ya que solo hay dos claves posibles)
- `int`, `uint` y todas sus variaciones
- `String` y `&str` (consejo: puede tener un `HashMap` con claves de tipo `String` y llamar a `.get()` con un `&str`)

Tenga en cuenta que `f32` y `f64` **no** implementan `Hash`, probablemente porque los errores de precisión de punto flotante harían que utilizar los mismos como claves de hashmap fuera terriblemente propenso a errores.

Todas las clases de colección implementan `Eq` y `Hash` si su tipo contenido también implementa respectivamente `Eq` y `Hash`. Por ejemplo, `Vec<T>` implementará `Hash` si `T` implementa `Hash`.

Puede implementar fácilmente `Eq` y `Hash` para un tipo personalizado con solo una línea: `#[derive(PartialEq, Eq, Hash)]`

El compilador se encargará del resto. Si desea tener más control sobre los detalles, puede implementar `Eq` y/o `Hash` usted mismo. Esta guía no cubrirá los detalles de la implementación de `Hash`.

Para experimentar con el uso de una `struct` en `HashMap`, intentemos crear un sistema de inicio de sesión de usuario muy simple:

```rust
use std::collections::HashMap;

// Eq requiere que derive PartialEq en el tipo.
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
