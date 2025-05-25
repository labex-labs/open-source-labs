# Tipos de chave alternativos/personalizados

Qualquer tipo que implemente os traits `Eq` e `Hash` pode ser uma chave em um `HashMap`. Isso inclui:

- `bool` (embora não seja muito útil, pois existem apenas duas chaves possíveis)
- `int`, `uint` e todas as suas variações
- `String` e `&str` (dica: você pode ter um `HashMap` chaveado por `String` e chamar `.get()` com um `&str`)

Observe que `f32` e `f64` _não_ implementam `Hash`, provavelmente porque erros de precisão de ponto flutuante tornariam seu uso como chaves de hashmap terrivelmente propenso a erros.

Todas as classes de coleção implementam `Eq` e `Hash` se o tipo contido também implementar, respectivamente, `Eq` e `Hash`. Por exemplo, `Vec<T>` implementará `Hash` se `T` implementar `Hash`.

Você pode facilmente implementar `Eq` e `Hash` para um tipo personalizado com apenas uma linha: `#[derive(PartialEq, Eq, Hash)]`

O compilador fará o restante. Se você quiser mais controle sobre os detalhes, pode implementar `Eq` e/ou `Hash` você mesmo. Este guia não abordará os detalhes da implementação de `Hash`.

Para experimentar o uso de uma `struct` em um `HashMap`, vamos tentar criar um sistema de login de usuário muito simples:

```rust
use std::collections::HashMap;

// Eq requer que você derive PartialEq no tipo.
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
    println!("Tentando login...");

    let logon = Account {
        username,
        password,
    };

    match accounts.get(&logon) {
        Some(account_info) => {
            println!("Login bem-sucedido!");
            println!("Nome: {}", account_info.name);
            println!("Email: {}", account_info.email);
        },
        _ => println!("Login falhou!"),
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
