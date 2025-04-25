# 代替/カスタム キー型

`Eq` と `Hash` トレイトを実装する任意の型は、`HashMap` のキーとなることができます。これには以下が含まれます。

- `bool`（ただし、キーが 2 つしかないためあまり役に立たない）
- `int`、`uint` およびそのすべてのバリエーション
- `String` と `&str`（ヒント：`String` でキー付きの `HashMap` を持ち、`&str` で `.get()` を呼び出すことができます）

`f32` と `f64` は `Hash` を実装していません。おそらく、浮動小数点数の精度エラーのため、ハッシュマップのキーとして使用すると非常にエラーが発生しやすくなるためです。

すべてのコレクション クラスは、その中に含まれる型がそれぞれ `Eq` と `Hash` を実装している場合、`Eq` と `Hash` を実装します。たとえば、`T` が `Hash` を実装している場合、`Vec<T>` は `Hash` を実装します。

カスタム型に対して `Eq` と `Hash` を簡単に実装することができます。ただ 1 行で済みます。`#[derive(PartialEq, Eq, Hash)]`

コンパイラが残りの作業を行います。詳細についてもっとコントロールしたい場合は、自分で `Eq` と/または `Hash` を実装することができます。このガイドでは、`Hash` を実装する詳細については説明しません。

`HashMap` で `struct` を使用して遊んでみましょう。非常に単純なユーザーログオン システムを作成してみましょう。

```rust
use std::collections::HashMap;

// Eq は、型に対して PartialEq を派生する必要があります。
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
