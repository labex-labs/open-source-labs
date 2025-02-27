# Альтернативные/настраиваемые типы ключей

Любой тип, реализующий трейты `Eq` и `Hash`, может быть ключом в `HashMap`. Это включает в себя:

- `bool` (хотя это не очень полезно, так как есть только два возможных ключа)
- `int`, `uint` и все их вариации
- `String` и `&str` (хитрость: вы можете иметь `HashMap`, ключи которого типа `String`, и вызывать `.get()` с `&str`)

Обратите внимание, что `f32` и `f64` не реализуют `Hash`, вероятно, потому что ошибки точности с плавающей запятой сделают использование их в качестве ключей в хэш-мапе крайне ошибочным.

Все классы коллекций реализуют `Eq` и `Hash`, если их содержащий тип также соответственно реализует `Eq` и `Hash`. Например, `Vec<T>` реализует `Hash`, если `T` реализует `Hash`.

Вы можете легко реализовать `Eq` и `Hash` для пользовательского типа всего за одну строку: `#[derive(PartialEq, Eq, Hash)]`

Компилятор сделает остальное. Если вы хотите более тщательно контролировать детали, вы можете реализовать `Eq` и/или `Hash` самостоятельно. В этом руководстве не будут рассмотрены детали реализации `Hash`.

Для эксперимента с использованием `struct` в `HashMap` давайте попробуем сделать очень простую систему входа пользователя:

```rust
use std::collections::HashMap;

// Eq требует, чтобы вы выводили PartialEq для типа.
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
