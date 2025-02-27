# `abort` и `unwind`

Предыдущий раздел иллюстрирует механизм обработки ошибок `panic`. Различные кодовые пути могут быть условно скомпилированы в зависимости от настройки panic. Текущие доступные значения — это `unwind` и `abort`.

На основе предыдущего примера с лимонадом мы явно используем стратегию panic для выполнения различных строк кода.

```rust

fn drink(beverage: &str) {
   // You shouldn't drink too much sugary beverages.
    if beverage == "lemonade" {
        if cfg!(panic="abort"){ println!("This is not your party. Run!!!!");}
        else{ println!("Spit it out!!!!");}
    }
    else{ println!("Some refreshing {} is all I need.", beverage); }
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

Вот еще один пример, в котором мы сосредоточимся на переписывании `drink()` и явно используем ключевое слово `unwind`.

```rust

#[cfg(panic = "unwind")]
fn ah(){ println!("Spit it out!!!!");}

#[cfg(not(panic="unwind"))]
fn ah(){ println!("This is not your party. Run!!!!");}

fn drink(beverage: &str){
    if beverage == "lemonade"{ ah();}
    else{println!("Some refreshing {} is all I need.", beverage);}
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

Стратегию panic можно установить из командной строки, используя `abort` или `unwind`.

```console
rustc lemonade.rs -C panic=abort
```
