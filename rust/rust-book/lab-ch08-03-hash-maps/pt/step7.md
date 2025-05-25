# Adicionando uma Chave e Valor Somente se uma Chave Não Estiver Presente

É comum verificar se uma chave específica já existe no hash map com um valor e, em seguida, tomar as seguintes ações: se a chave existir no hash map, o valor existente deve permanecer como está; se a chave não existir, insira-a e um valor para ela.

Hash maps têm uma API especial para isso chamada `entry` que recebe a chave que você deseja verificar como um parâmetro. O valor de retorno do método `entry` é um enum chamado `Entry` que representa um valor que pode ou não existir. Digamos que queremos verificar se a chave para a equipe Amarela tem um valor associado a ela. Se não tiver, queremos inserir o valor `50`, e o mesmo para a equipe Azul. Usando a API `entry`, o código se parece com a Listagem 8-24.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);

scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);

println!("{:?}", scores);
```

Listagem 8-24: Usando o método `entry` para inserir somente se a chave já não tiver um valor

O método `or_insert` em `Entry` é definido para retornar uma referência mutável ao valor para a chave `Entry` correspondente se essa chave existir e, se não, ele insere o parâmetro como o novo valor para esta chave e retorna uma referência mutável ao novo valor. Essa técnica é muito mais limpa do que escrever a lógica nós mesmos e, além disso, funciona melhor com o verificador de empréstimo (borrow checker).

A execução do código na Listagem 8-24 imprimirá `{"Yellow": 50, "Blue": 10}`. A primeira chamada para `entry` inserirá a chave para a equipe Amarela com o valor `50` porque a equipe Amarela não tem um valor já. A segunda chamada para `entry` não alterará o hash map porque a equipe Azul já tem o valor `10`.
