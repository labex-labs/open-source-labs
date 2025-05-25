# Criando um Novo Hash Map

Uma maneira de criar um hash map vazio é usar `new` e adicionar elementos com `insert`. Na Listagem 8-20, estamos acompanhando as pontuações de duas equipes cujos nomes são _Blue_ (Azul) e _Yellow_ (Amarelo). A equipe Azul começa com 10 pontos, e a equipe Amarela começa com 50.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
```

Listagem 8-20: Criando um novo hash map e inserindo algumas chaves e valores

Observe que precisamos primeiro `use` (usar) o `HashMap` da parte de coleções da biblioteca padrão. Das nossas três coleções comuns, esta é a menos usada, então ela não está incluída nos recursos trazidos para o escopo automaticamente no prelúdio. Hash maps também têm menos suporte da biblioteca padrão; não há uma macro embutida para construí-los, por exemplo.

Assim como os vetores, hash maps armazenam seus dados no heap. Este `HashMap` tem chaves do tipo `String` e valores do tipo `i32`. Como os vetores, hash maps são homogêneos: todas as chaves devem ter o mesmo tipo, e todos os valores devem ter o mesmo tipo.
