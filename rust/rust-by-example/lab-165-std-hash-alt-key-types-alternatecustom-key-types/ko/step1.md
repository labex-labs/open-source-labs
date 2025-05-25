# 대체/사용자 지정 키 유형

`HashMap`에서 키로 사용할 수 있는 유형은 `Eq` 및 `Hash` 트레이트를 구현하는 모든 유형입니다. 이에 포함되는 유형은 다음과 같습니다.

- `bool` (두 개의 가능한 키만 있으므로 유용하지 않음)
- `int`, `uint` 및 그 모든 변형
- `String` 및 `&str` (팁: `String`으로 키가 지정된 `HashMap`을 가지고 `&str`로 `.get()`를 호출할 수 있음)

`f32` 및 `f64`는 해시를 구현하지 않습니다. 부동 소수점 정밀도 오류로 인해 해시맵 키로 사용하면 오류가 발생할 가능성이 높기 때문입니다.

모든 컬렉션 클래스는 포함된 유형이 각각 `Eq` 및 `Hash`를 구현하는 경우 `Eq` 및 `Hash`를 구현합니다. 예를 들어, `Vec<T>`는 `T`가 `Hash`를 구현하는 경우 `Hash`를 구현합니다.

단 한 줄로 사용자 지정 유형에 `Eq` 및 `Hash`를 쉽게 구현할 수 있습니다. `#[derive(PartialEq, Eq, Hash)]`

컴파일러가 나머지 작업을 수행합니다. 자세한 내용을 제어하려면 `Eq` 및/또는 `Hash`를 직접 구현할 수 있습니다. 이 가이드에서는 `Hash` 구현의 세부 사항을 다루지 않습니다.

`HashMap`에서 `struct`를 사용하는 방법을 연습하기 위해 매우 간단한 사용자 로그인 시스템을 만들어 보겠습니다.

```rust
use std::collections::HashMap;

// Eq 는 유형에 PartialEq 를 파생해야 합니다.
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
