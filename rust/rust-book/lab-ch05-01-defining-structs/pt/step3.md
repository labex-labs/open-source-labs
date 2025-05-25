# Criando Instâncias a partir de Outras Instâncias com a Sintaxe de Atualização de Struct

É frequentemente útil criar uma nova instância de uma struct que inclua a maioria dos valores de outra instância, mas altere alguns. Você pode fazer isso usando a _sintaxe de atualização de struct_ (struct update syntax).

Primeiro, na Listagem 5-6, mostramos como criar uma nova instância `User` em `user2` regularmente, sem a sintaxe de atualização. Definimos um novo valor para `email`, mas, de outra forma, usamos os mesmos valores de `user1` que criamos na Listagem 5-2.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    --snip--

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
}
```

Listagem 5-6: Criando uma nova instância `User` usando um dos valores de `user1`

Usando a sintaxe de atualização de struct, podemos obter o mesmo efeito com menos código, como mostrado na Listagem 5-7. A sintaxe `..` especifica que os campos restantes não definidos explicitamente devem ter o mesmo valor que os campos na instância fornecida.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    --snip--


    let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };
}
```

Listagem 5-7: Usando a sintaxe de atualização de struct para definir um novo valor de `email` para uma instância `User`, mas para usar o restante dos valores de `user1`

O código na Listagem 5-7 também cria uma instância em `user2` que tem um valor diferente para `email`, mas tem os mesmos valores para os campos `username`, `active` e `sign_in_count` de `user1`. O `..user1` deve vir por último para especificar que quaisquer campos restantes devem obter seus valores dos campos correspondentes em `user1`, mas podemos escolher especificar valores para quantos campos quisermos em qualquer ordem, independentemente da ordem dos campos na definição da struct.

Observe que a sintaxe de atualização de struct usa `=` como uma atribuição; isso ocorre porque ela move os dados, assim como vimos em "Variáveis e Dados Interagindo com Move". Neste exemplo, não podemos mais usar `user1` após criar `user2` porque a `String` no campo `username` de `user1` foi movida para `user2`. Se tivéssemos dado a `user2` novos valores `String` para `email` e `username`, e, portanto, usado apenas os valores `active` e `sign_in_count` de `user1`, então `user1` ainda seria válido após criar `user2`. Tanto `active` quanto `sign_in_count` são tipos que implementam o trait `Copy`, então o comportamento que discutimos em "Dados Apenas na Stack: Copy" se aplicaria.
