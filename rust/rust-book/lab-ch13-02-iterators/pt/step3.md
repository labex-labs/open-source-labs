# Métodos que Consomem o Iterador

O _trait_ `Iterator` possui vários métodos diferentes com implementações padrão fornecidas pela biblioteca padrão; você pode descobrir sobre esses métodos consultando a documentação da API da biblioteca padrão para o _trait_ `Iterator`. Alguns desses métodos chamam o método `next` em sua definição, e é por isso que você é obrigado a implementar o método `next` ao implementar o _trait_ `Iterator`.

Métodos que chamam `next` são chamados de _adaptadores consumidores_ porque chamá-los usa o iterador. Um exemplo é o método `sum`, que assume a propriedade do iterador e itera pelos itens chamando repetidamente `next`, consumindo assim o iterador. À medida que itera, ele adiciona cada item a um total acumulado e retorna o total quando a iteração é concluída. A Listagem 13-13 tem um teste ilustrando o uso do método `sum`.

Nome do arquivo: `src/lib.rs`

```rust
#[test]
fn iterator_sum() {
    let v1 = vec![1, 2, 3];

    let v1_iter = v1.iter();

    let total: i32 = v1_iter.sum();

    assert_eq!(total, 6);
}
```

Listagem 13-13: Chamando o método `sum` para obter o total de todos os itens no iterador

Não podemos usar `v1_iter` após a chamada para `sum` porque `sum` assume a propriedade do iterador no qual o chamamos.
