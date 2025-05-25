# Definindo e Instanciando Structs

Structs são semelhantes a tuplas, discutidas em "O Tipo Tupla", pois ambas armazenam múltiplos valores relacionados. Como as tuplas, as partes de uma struct podem ser de tipos diferentes. Diferentemente das tuplas, em uma struct você nomeará cada parte dos dados para que fique claro o que os valores significam. Adicionar esses nomes significa que as structs são mais flexíveis do que as tuplas: você não precisa depender da ordem dos dados para especificar ou acessar os valores de uma instância.

Para definir uma struct, inserimos a palavra-chave `struct` e nomeamos a struct inteira. O nome de uma struct deve descrever a significância das partes dos dados que estão sendo agrupadas. Então, dentro de chaves, definimos os nomes e tipos das partes dos dados, que chamamos de _campos_ (fields). Por exemplo, a Listagem 5-1 mostra uma struct que armazena informações sobre uma conta de usuário.

Nome do arquivo: `src/main.rs`

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

Listagem 5-1: Uma definição de struct `User`

Para usar uma struct depois de defini-la, criamos uma _instância_ (instance) dessa struct especificando valores concretos para cada um dos campos. Criamos uma instância declarando o nome da struct e, em seguida, adicionamos chaves contendo pares chave: valor, onde as chaves são os nomes dos campos e os valores são os dados que queremos armazenar nesses campos. Não precisamos especificar os campos na mesma ordem em que os declaramos na struct. Em outras palavras, a definição da struct é como um modelo geral para o tipo, e as instâncias preenchem esse modelo com dados específicos para criar valores do tipo. Por exemplo, podemos declarar um usuário específico como mostrado na Listagem 5-2.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

Listagem 5-2: Criando uma instância da struct `User`

Para obter um valor específico de uma struct, usamos a notação de ponto. Por exemplo, para acessar o endereço de e-mail deste usuário, usamos `user1.email`. Se a instância for mutável, podemos alterar um valor usando a notação de ponto e atribuindo a um campo específico. A Listagem 5-3 mostra como alterar o valor no campo `email` de uma instância `User` mutável.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
}
```

Listagem 5-3: Alterando o valor no campo `email` de uma instância `User`

Observe que toda a instância deve ser mutável; Rust não nos permite marcar apenas certos campos como mutáveis. Como com qualquer expressão, podemos construir uma nova instância da struct como a última expressão no corpo da função para retornar implicitamente essa nova instância.

A Listagem 5-4 mostra uma função `build_user` que retorna uma instância `User` com o e-mail e o nome de usuário fornecidos. O campo `active` recebe o valor de `true`, e o `sign_in_count` recebe um valor de `1`.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

Listagem 5-4: Uma função `build_user` que recebe um e-mail e um nome de usuário e retorna uma instância `User`

Faz sentido nomear os parâmetros da função com o mesmo nome dos campos da struct, mas ter que repetir os nomes dos campos e variáveis `email` e `username` é um pouco tedioso. Se a struct tivesse mais campos, repetir cada nome ficaria ainda mais irritante. Felizmente, existe uma abreviação conveniente!
