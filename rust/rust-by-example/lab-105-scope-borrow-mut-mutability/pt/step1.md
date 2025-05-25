# Mutabilidade

Dados mutáveis podem ser emprestados de forma mutável usando `&mut T`. Isso é chamado de _referência mutável_ e dá acesso de leitura/escrita ao tomador emprestado (borrower). Em contraste, `&T` empresta os dados via uma referência imutável, e o tomador emprestado pode ler os dados, mas não modificá-los:

```rust
#[allow(dead_code)]
#[derive(Clone, Copy)]
struct Book {
    // `&'static str` é uma referência a uma string alocada em memória somente leitura
    author: &'static str,
    title: &'static str,
    year: u32,
}

// Esta função recebe uma referência a um livro
fn borrow_book(book: &Book) {
    println!("Eu emprestei imutavelmente {} - edição {}", book.title, book.year);
}

// Esta função recebe uma referência a um livro mutável e muda `year` para 2014
fn new_edition(book: &mut Book) {
    book.year = 2014;
    println!("Eu emprestei mutavelmente {} - edição {}", book.title, book.year);
}

fn main() {
    // Cria um Book imutável chamado `immutabook`
    let immutabook = Book {
        // literais de string têm o tipo `&'static str`
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };

    // Cria uma cópia mutável de `immutabook` e chama-a de `mutabook`
    let mut mutabook = immutabook;

    // Empresta imutavelmente um objeto imutável
    borrow_book(&immutabook);

    // Empresta imutavelmente um objeto mutável
    borrow_book(&mutabook);

    // Empresta um objeto mutável como mutável
    new_edition(&mut mutabook);

    // Erro! Não é possível emprestar um objeto imutável como mutável
    new_edition(&mut immutabook);
    // FIXME ^ Comente esta linha
}
```
