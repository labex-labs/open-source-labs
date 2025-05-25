# Referências e Empréstimos (References and Borrowing)

O problema com o código da tupla no Listing 4-5 é que precisamos retornar a `String` para a função chamadora para que possamos continuar usando a `String` após a chamada para `calculate_length`, porque a `String` foi movida para `calculate_length`. Em vez disso, podemos fornecer uma referência ao valor `String`. Uma _referência_ é como um ponteiro, pois é um endereço que podemos seguir para acessar os dados armazenados nesse endereço; esses dados são de propriedade de alguma outra variável. Ao contrário de um ponteiro, uma referência tem a garantia de apontar para um valor válido de um tipo específico durante a vida útil dessa referência.

Aqui está como você definiria e usaria uma função `calculate_length` que tem uma referência a um objeto como um parâmetro em vez de assumir a propriedade do valor:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Primeiro, observe que todo o código da tupla na declaração da variável e no valor de retorno da função desapareceu. Segundo, observe que passamos `&s1` para `calculate_length` e, em sua definição, pegamos `&String` em vez de `String`. Esses "e comerciais" representam _referências_ e permitem que você se refira a algum valor sem assumir a propriedade dele. A Figura 4-5 ilustra esse conceito.

Figura 4-5: Um diagrama de `&String s` apontando para `String s1`

> Nota: O oposto de referenciar usando `&` é _dereferenciar_ (dereferencing), que é realizado com o operador de desreferência, `*`. Veremos alguns usos do operador de desreferência no Capítulo 8 e discutiremos os detalhes da desreferenciação no Capítulo 15.

Vamos analisar mais de perto a chamada da função aqui:

```rust
let s1 = String::from("hello");

let len = calculate_length(&s1);
```

A sintaxe `&s1` nos permite criar uma referência que _se refere_ ao valor de `s1`, mas não o possui. Como não o possui, o valor para o qual aponta não será descartado quando a referência parar de ser usada.

Da mesma forma, a assinatura da função usa `&` para indicar que o tipo do parâmetro `s` é uma referência. Vamos adicionar algumas anotações explicativas:

```rust
fn calculate_length(s: &String) -> usize { // s é uma referência a uma String
    s.len()
} // Aqui, s sai do escopo. Mas como não tem a propriedade do que
  // se refere, a String não é descartada
```

O escopo em que a variável `s` é válida é o mesmo que o escopo de qualquer parâmetro de função, mas o valor apontado pela referência não é descartado quando `s` para de ser usado, porque `s` não tem propriedade. Quando as funções têm referências como parâmetros em vez dos valores reais, não precisaremos retornar os valores para devolver a propriedade, porque nunca tivemos a propriedade.

Chamamos a ação de criar uma referência de _empréstimo_ (borrowing). Como na vida real, se uma pessoa possui algo, você pode emprestá-lo dela. Quando terminar, você tem que devolvê-lo. Você não é o dono.

Então, o que acontece se tentarmos modificar algo que estamos emprestando? Experimente o código no Listing 4-6. Alerta de spoiler: não funciona!

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

Listing 4-6: Tentando modificar um valor emprestado

Aqui está o erro:

```bash
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&`
reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                        ------- help: consider changing this to be a mutable
reference: `&mut String`
8 |     some_string.push_str(", world");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so
the data it refers to cannot be borrowed as mutable
```

Assim como as variáveis são imutáveis por padrão, as referências também são. Não podemos modificar algo ao qual temos uma referência.
