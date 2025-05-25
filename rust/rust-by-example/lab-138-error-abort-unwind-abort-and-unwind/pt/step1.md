# `abort` e `unwind`

A seção anterior ilustra o mecanismo de tratamento de erros `panic`. Diferentes caminhos de código podem ser compilados condicionalmente com base na configuração de pânico. Os valores atuais disponíveis são `unwind` e `abort`.

Com base no exemplo anterior da limonada, usamos explicitamente a estratégia de pânico para exercitar diferentes linhas de código.

```rust

fn drink(beverage: &str) {
   // Você não deve beber muitas bebidas açucaradas.
    if beverage == "lemonade" {
        if cfg!(panic="abort"){ println!("Esta não é a sua festa. Corra!!!!");}
        else{ println!("Cuspa fora!!!!");}
    }
    else{ println!("Um pouco de {} refrescante é tudo que preciso.", beverage); }
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

Aqui está outro exemplo, focando na reescrita de `drink()` e usando explicitamente a palavra-chave `unwind`.

```rust

#[cfg(panic = "unwind")]
fn ah(){ println!("Cuspa fora!!!!");}

#[cfg(not(panic="unwind"))]
fn ah(){ println!("Esta não é a sua festa. Corra!!!!");}

fn drink(beverage: &str){
    if beverage == "lemonade"{ ah();}
    else{println!("Um pouco de {} refrescante é tudo que preciso.", beverage);}
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

A estratégia de pânico pode ser definida a partir da linha de comando usando `abort` ou `unwind`.

```console
rustc lemonade.rs -C panic=abort
```
