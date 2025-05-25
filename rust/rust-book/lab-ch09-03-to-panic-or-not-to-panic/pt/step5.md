# Criando Tipos Personalizados para Validação

Vamos levar a ideia de usar o sistema de tipos do Rust para garantir que temos um valor válido um passo adiante e analisar a criação de um tipo personalizado para validação. Recorde o jogo de adivinhação no Capítulo 2, no qual nosso código pediu ao usuário para adivinhar um número entre 1 e 100. Nunca validamos que o palpite do usuário estava entre esses números antes de verificá-lo em relação ao nosso número secreto; apenas validamos que o palpite era positivo. Nesse caso, as consequências não foram muito graves: nossa saída de "Muito alto" ou "Muito baixo" ainda estaria correta. Mas seria um aprimoramento útil para orientar o usuário em direção a palpites válidos e ter um comportamento diferente quando o usuário adivinha um número fora do intervalo em comparação com quando o usuário digita, por exemplo, letras.

Uma maneira de fazer isso seria analisar o palpite como um `i32` em vez de apenas um `u32` para permitir números potencialmente negativos e, em seguida, adicionar uma verificação para o número estar no intervalo, assim:

Nome do arquivo: `src/main.rs`

```rust
loop {
    --snip--

    let guess: i32 = match guess.trim().parse() {
        Ok(num) => num,
        Err(_) => continue,
    };

    if guess < 1 || guess > 100 {
        println!("O número secreto estará entre 1 e 100.");
        continue;
    }

    match guess.cmp(&secret_number) {
        --snip--
}
```

A expressão `if` verifica se nosso valor está fora do intervalo, informa ao usuário sobre o problema e chama `continue` para iniciar a próxima iteração do loop e pedir outro palpite. Após a expressão `if`, podemos prosseguir com as comparações entre `guess` e o número secreto sabendo que `guess` está entre 1 e 100.

No entanto, esta não é uma solução ideal: se fosse absolutamente crítico que o programa operasse apenas em valores entre 1 e 100, e tivesse muitas funções com esse requisito, ter uma verificação como essa em cada função seria tedioso (e pode impactar o desempenho).

Em vez disso, podemos criar um novo tipo e colocar as validações em uma função para criar uma instância do tipo em vez de repetir as validações em todos os lugares. Dessa forma, é seguro para as funções usarem o novo tipo em suas assinaturas e usar com confiança os valores que recebem. A Listagem 9-13 mostra uma maneira de definir um tipo `Guess` que só criará uma instância de `Guess` se a função `new` receber um valor entre 1 e 100.

Nome do arquivo: `src/lib.rs`

```rust
1 pub struct Guess {
    value: i32,
}

impl Guess {
  2 pub fn new(value: i32) -> Guess {
      3 if value < 1 || value > 100 {
          4 panic!(
                "O valor do palpite deve estar entre 1 e 100, obtido {}.",
                value
            );
        }

      5 Guess { value }
    }

  6 pub fn value(&self) -> i32 {
        self.value
    }
}
```

Listagem 9-13: Um tipo `Guess` que só continuará com valores entre 1 e 100

Primeiro, definimos uma struct chamada `Guess` que tem um campo chamado `value` que contém um `i32` \[1]. É aqui que o número será armazenado.

Em seguida, implementamos uma função associada chamada `new` em `Guess` que cria instâncias de valores `Guess` \[2]. A função `new` é definida para ter um parâmetro chamado `value` do tipo `i32` e para retornar um `Guess`. O código no corpo da função `new` testa `value` para garantir que esteja entre 1 e 100 \[3]. Se `value` não passar neste teste, fazemos uma chamada `panic!` \[4], que alertará o programador que está escrevendo o código de chamada que ele tem um bug que precisa corrigir, porque criar um `Guess` com um `value` fora desse intervalo violaria o contrato em que `Guess::new` está confiando. As condições em que `Guess::new` pode entrar em pânico devem ser discutidas em sua documentação da API voltada para o público; abordaremos as convenções de documentação que indicam a possibilidade de um `panic!` na documentação da API que você cria no Capítulo 14. Se `value` passar no teste, criamos um novo `Guess` com seu campo `value` definido como o parâmetro `value` e retornamos o `Guess` \[5].

Em seguida, implementamos um método chamado `value` que empresta `self`, não tem nenhum outro parâmetro e retorna um `i32` \[6]. Esse tipo de método às vezes é chamado de _getter_ porque seu objetivo é obter alguns dados de seus campos e retorná-los. Este método público é necessário porque o campo `value` da struct `Guess` é privado. É importante que o campo `value` seja privado para que o código que usa a struct `Guess` não possa definir `value` diretamente: o código fora do módulo _deve_ usar a função `Guess::new` para criar uma instância de `Guess`, garantindo assim que não haja como um `Guess` ter um `value` que não tenha sido verificado pelas condições na função `Guess::new`.

Uma função que tem um parâmetro ou retorna apenas números entre 1 e 100 pode então declarar em sua assinatura que recebe ou retorna um `Guess` em vez de um `i32` e não precisaria fazer nenhuma verificação adicional em seu corpo.
