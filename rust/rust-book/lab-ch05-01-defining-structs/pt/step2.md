# Usando a Abreviatura de Inicialização de Campo

Como os nomes dos parâmetros e os nomes dos campos da struct são exatamente os mesmos na Listagem 5-4, podemos usar a sintaxe de _abreviação de inicialização de campo_ (field init shorthand) para reescrever `build_user` para que se comporte exatamente da mesma forma, mas não tenha a repetição de `username` e `email`, como mostrado na Listagem 5-5.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

Listagem 5-5: Uma função `build_user` que usa a abreviação de inicialização de campo porque os parâmetros `username` e `email` têm o mesmo nome dos campos da struct

Aqui, estamos criando uma nova instância da struct `User`, que tem um campo chamado `email`. Queremos definir o valor do campo `email` para o valor no parâmetro `email` da função `build_user`. Como o campo `email` e o parâmetro `email` têm o mesmo nome, só precisamos escrever `email` em vez de `email: email`.
