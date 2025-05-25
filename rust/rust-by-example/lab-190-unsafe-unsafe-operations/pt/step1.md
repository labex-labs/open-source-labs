# Operações Inseguras

Como introdução a esta seção, para emprestar das documentações oficiais, "deve-se tentar minimizar a quantidade de código inseguro em uma base de código". Com isso em mente, vamos começar! As anotações inseguras em Rust são usadas para contornar as proteções implementadas pelo compilador; especificamente, existem quatro principais usos para o `unsafe`:

- desreferenciando ponteiros brutos
- chamando funções ou métodos que são `unsafe` (incluindo a chamada de uma função através de FFI, veja [um capítulo anterior do livro])
- acessando ou modificando variáveis estáticas mutáveis
- implementando traits inseguras

## Ponteiros Brutos

Ponteiros brutos `*` e referências `&T` funcionam de forma semelhante, mas as referências são sempre seguras porque o verificador de empréstimos garante que apontam para dados válidos. A desreferenciação de um ponteiro bruto só pode ser feita dentro de um bloco `unsafe`.

```rust
fn main() {
    let raw_p: *const u32 = &10;

    unsafe {
        assert!(*raw_p == 10);
    }
}
```

## Chamando Funções Inseguras

Algumas funções podem ser declaradas como `unsafe`, o que significa que é responsabilidade do programador garantir a correção, em vez do compilador. Um exemplo disso é `std::slice::from_raw_parts`, que cria um slice dado um ponteiro para o primeiro elemento e um comprimento.

```rust
use std::slice;

fn main() {
    let some_vector = vec![1, 2, 3, 4];

    let pointer = some_vector.as_ptr();
    let length = some_vector.len();

    unsafe {
        let my_slice: &[u32] = slice::from_raw_parts(pointer, length);

        assert_eq!(some_vector.as_slice(), my_slice);
    }
}
```

Para `slice::from_raw_parts`, uma das premissas que _deve_ ser mantida é que o ponteiro passado aponta para memória válida e que a memória apontada é do tipo correto. Se esses invariantes não forem mantidos, o comportamento do programa é indefinido e não se sabe o que acontecerá.
