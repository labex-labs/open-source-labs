# Coerções Implícitas de Deref com Funções e Métodos

_Coerção de Deref_ converte uma referência a um tipo que implementa o trait `Deref` em uma referência a outro tipo. Por exemplo, a coerção de deref pode converter `&String` em `&str` porque `String` implementa o trait `Deref` de forma que ele retorna `&str`. A coerção de deref é uma conveniência que o Rust realiza em argumentos para funções e métodos, e funciona apenas em tipos que implementam o trait `Deref`. Ela acontece automaticamente quando passamos uma referência ao valor de um tipo específico como argumento para uma função ou método que não corresponde ao tipo de parâmetro na definição da função ou método. Uma sequência de chamadas ao método `deref` converte o tipo que fornecemos no tipo que o parâmetro precisa.

A coerção de deref foi adicionada ao Rust para que os programadores que escrevem chamadas de funções e métodos não precisem adicionar tantas referências e desreferenciações explícitas com `&` e `*`. O recurso de coerção de deref também nos permite escrever mais código que pode funcionar para referências ou ponteiros inteligentes.

Para ver a coerção de deref em ação, vamos usar o tipo `MyBox<T>` que definimos na Listagem 15-8, bem como a implementação de `Deref` que adicionamos na Listagem 15-10. A Listagem 15-11 mostra a definição de uma função que tem um parâmetro de fatia de string.

Nome do arquivo: `src/main.rs`

```rust
fn hello(name: &str) {
    println!("Hello, {name}!");
}
```

Listagem 15-11: Uma função `hello` que tem o parâmetro `name` do tipo `&str`

Podemos chamar a função `hello` com uma fatia de string como argumento, como `hello("Rust");`, por exemplo. A coerção de deref torna possível chamar `hello` com uma referência a um valor do tipo `MyBox<String>`, conforme mostrado na Listagem 15-12.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&m);
}
```

Listagem 15-12: Chamando `hello` com uma referência a um valor `MyBox<String>`, que funciona por causa da coerção de deref

Aqui estamos chamando a função `hello` com o argumento `&m`, que é uma referência a um valor `MyBox<String>`. Como implementamos o trait `Deref` em `MyBox<T>` na Listagem 15-10, o Rust pode transformar `&MyBox<String>` em `&String` chamando `deref`. A biblioteca padrão fornece uma implementação de `Deref` em `String` que retorna uma fatia de string, e isso está na documentação da API para `Deref`. O Rust chama `deref` novamente para transformar o `&String` em `&str`, que corresponde à definição da função `hello`.

Se o Rust não implementasse a coerção de deref, teríamos que escrever o código na Listagem 15-13 em vez do código na Listagem 15-12 para chamar `hello` com um valor do tipo `&MyBox<String>`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&(*m)[..]);
}
```

Listagem 15-13: O código que teríamos que escrever se o Rust não tivesse coerção de deref

O `(*m)` desreferencia o `MyBox<String>` em um `String`. Em seguida, o `&` e `[..]` pegam uma fatia de string do `String` que é igual à string inteira para corresponder à assinatura de `hello`. Este código sem coerções de deref é mais difícil de ler, escrever e entender com todos esses símbolos envolvidos. A coerção de deref permite que o Rust lide com essas conversões para nós automaticamente.

Quando o trait `Deref` é definido para os tipos envolvidos, o Rust analisará os tipos e usará `Deref::deref` quantas vezes forem necessárias para obter uma referência para corresponder ao tipo do parâmetro. O número de vezes que `Deref::deref` precisa ser inserido é resolvido em tempo de compilação, portanto, não há penalidade em tempo de execução por tirar proveito da coerção de deref!
