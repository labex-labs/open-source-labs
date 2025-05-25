# Combinadores: `map`

`match` é um método válido para lidar com `Option`s. No entanto, você pode eventualmente achar o uso intensivo tedioso, especialmente com operações válidas apenas com uma entrada. Nesses casos, os combinadores podem ser usados para gerenciar o fluxo de controle de forma modular.

`Option` tem um método embutido chamado `map()`, um combinador para o mapeamento simples de `Some -> Some` e `None -> None`. Múltiplas chamadas `map()` podem ser encadeadas para ainda mais flexibilidade.

No exemplo a seguir, `process()` substitui todas as funções anteriores, mantendo-se compacto.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// Descascando comida. Se não houver, então retorna `None`.
// Caso contrário, retorna a comida descascada.
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// Cortando comida. Se não houver, então retorna `None`.
// Caso contrário, retorna a comida cortada.
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// Cozinhando comida. Aqui, mostramos `map()` em vez de `match` para o tratamento de casos.
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// Uma função para descascar, cortar e cozinhar comida, tudo em sequência.
// Encadeamos múltiplos usos de `map()` para simplificar o código.
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
        .map(|Peeled(f)| Chopped(f))
        .map(|Chopped(f)| Cooked(f))
}

// Verifique se há comida ou não antes de tentar comê-la!
fn eat(food: Option<Cooked>) {
    match food {
        Some(food) => println!("Mmm. I love {:?}", food),
        None       => println!("Oh no! It wasn't edible."),
    }
}

fn main() {
    let apple = Some(Food::Apple);
    let carrot = Some(Food::Carrot);
    let potato = None;

    let cooked_apple = cook(chop(peel(apple)));
    let cooked_carrot = cook(chop(peel(carrot)));
    // Vamos tentar o `process()` com uma aparência mais simples agora.
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```
