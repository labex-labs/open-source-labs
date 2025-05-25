# Retornando Valores de Loops

Um dos usos de um `loop` é tentar novamente uma operação que você sabe que pode falhar, como verificar se uma thread concluiu seu trabalho. Você também pode precisar passar o resultado dessa operação para fora do loop para o restante do seu código. Para fazer isso, você pode adicionar o valor que deseja retornar após a expressão `break` que você usa para parar o loop; esse valor será retornado do loop para que você possa usá-lo, como mostrado aqui:

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {result}");
}
```

Antes do loop, declaramos uma variável chamada `counter` e a inicializamos com `0`. Em seguida, declaramos uma variável chamada `result` para armazenar o valor retornado do loop. Em cada iteração do loop, adicionamos `1` à variável `counter` e, em seguida, verificamos se o `counter` é igual a `10`. Quando é, usamos a palavra-chave `break` com o valor `counter * 2`. Após o loop, usamos um ponto e vírgula para finalizar a instrução que atribui o valor a `result`. Finalmente, imprimimos o valor em `result`, que neste caso é `20`.
