# A Trait `Iterator` e o Método `next`

Todos os iteradores implementam um _trait_ (característica) chamado `Iterator` que é definido na biblioteca padrão. A definição do _trait_ se parece com isto:

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // methods with default implementations elided
}
```

Observe que esta definição usa alguma sintaxe nova: `type Item` e `Self::Item`, que estão definindo um _tipo associado_ com este _trait_. Falaremos sobre tipos associados em profundidade no Capítulo 19. Por enquanto, tudo o que você precisa saber é que este código diz que implementar o _trait_ `Iterator` requer que você também defina um tipo `Item`, e este tipo `Item` é usado no tipo de retorno do método `next`. Em outras palavras, o tipo `Item` será o tipo retornado do iterador.

O _trait_ `Iterator` só exige que os implementadores definam um método: o método `next`, que retorna um item do iterador por vez, envolto em `Some`, e, quando a iteração termina, retorna `None`.

Podemos chamar o método `next` em iteradores diretamente; a Listagem 13-12 demonstra quais valores são retornados de chamadas repetidas para `next` no iterador criado a partir do vetor.

Nome do arquivo: `src/lib.rs`

```rust
#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
```

Listagem 13-12: Chamando o método `next` em um iterador

Observe que precisamos tornar `v1_iter` mutável: chamar o método `next` em um iterador altera o estado interno que o iterador usa para acompanhar onde ele está na sequência. Em outras palavras, este código _consome_, ou usa, o iterador. Cada chamada para `next` consome um item do iterador. Não precisávamos tornar `v1_iter` mutável quando usamos um loop `for` porque o loop assumiu a propriedade de `v1_iter` e o tornou mutável nos bastidores.

Observe também que os valores que obtemos das chamadas para `next` são referências imutáveis aos valores no vetor. O método `iter` produz um iterador sobre referências imutáveis. Se quisermos criar um iterador que assume a propriedade de `v1` e retorna valores próprios, podemos chamar `into_iter` em vez de `iter`. Da mesma forma, se quisermos iterar sobre referências mutáveis, podemos chamar `iter_mut` em vez de `iter`.
