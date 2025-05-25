# O Tipo Array

Outra forma de ter uma coleção de múltiplos valores é com um _array_ (vetor). Diferente de uma tupla, cada elemento de um array deve ter o mesmo tipo. Diferente de arrays em algumas outras linguagens, arrays em Rust têm um comprimento fixo.

Escrevemos os valores em um array como uma lista separada por vírgulas dentro de colchetes:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
}
```

Arrays são úteis quando você quer que seus dados sejam alocados na pilha (stack) em vez do heap (vamos discutir a pilha e o heap mais no Capítulo 4) ou quando você quer garantir que sempre terá um número fixo de elementos. Um array não é tão flexível quanto o tipo vetor, no entanto. Um _vetor_ (vector) é um tipo de coleção semelhante fornecido pela biblioteca padrão que _pode_ crescer ou diminuir de tamanho. Se você não tiver certeza se deve usar um array ou um vetor, é provável que deva usar um vetor. O Capítulo 8 discute vetores com mais detalhes.

No entanto, arrays são mais úteis quando você sabe que o número de elementos não precisará mudar. Por exemplo, se você estivesse usando os nomes dos meses em um programa, provavelmente usaria um array em vez de um vetor porque sabe que ele sempre conterá 12 elementos:

```rust
let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
```

Você escreve o tipo de um array usando colchetes com o tipo de cada elemento, um ponto e vírgula e, em seguida, o número de elementos no array, assim:

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

Aqui, `i32` é o tipo de cada elemento. Após o ponto e vírgula, o número `5` indica que o array contém cinco elementos.

Você também pode inicializar um array para conter o mesmo valor para cada elemento, especificando o valor inicial, seguido por um ponto e vírgula e, em seguida, o comprimento do array em colchetes, como mostrado aqui:

```rust
let a = [3; 5];
```

O array chamado `a` conterá `5` elementos que serão todos definidos para o valor `3` inicialmente. Isso é o mesmo que escrever `let a = [3, 3, 3, 3, 3];` mas de uma forma mais concisa.
