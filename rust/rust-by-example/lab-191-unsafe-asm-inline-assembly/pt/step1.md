# Montagem Inline

Rust fornece suporte para montagem inline através do macro `asm!`. Pode ser usado para incorporar montagem escrita manualmente na saída de montagem gerada pelo compilador. Geralmente, isto não é necessário, mas pode ser útil quando o desempenho ou o tempo de execução exigidos não podem ser alcançados de outra forma. O acesso a primitivas de hardware de baixo nível, por exemplo, em código de kernel, também pode exigir esta funcionalidade.

> **Nota**: os exemplos aqui são apresentados em montagem x86/x86-64, mas outras arquiteturas também são suportadas.

A montagem inline é atualmente suportada nas seguintes arquiteturas:

- x86 e x86-64
- ARM
- AArch64
- RISC-V

## Uso Básico

Comecemos com o exemplo mais simples possível:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

unsafe {
    asm!("nop");
}
# }
```

Isto irá inserir uma instrução NOP (sem operação) na montagem gerada pelo compilador. Note que todas as invocações `asm!` têm de estar dentro de um bloco `unsafe`, pois podem inserir instruções arbitrárias e violar vários invariantes. As instruções a serem inseridas são listadas no primeiro argumento do macro `asm!` como uma literal de string.

## Entradas e Saídas

Agora, inserir uma instrução que não faz nada é bastante aborrecido. Vamos fazer algo que realmente atue sobre os dados:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64;
unsafe {
    asm!("mov {}, 5", out(reg) x);
}
assert_eq!(x, 5);
# }
```

Isto irá escrever o valor `5` na variável `u64` `x`. Pode ver que a literal de string que usamos para especificar as instruções é na verdade uma string de modelo. É regida pelas mesmas regras que as strings de formato Rust. No entanto, os argumentos inseridos no modelo parecem um pouco diferentes do que pode estar habituado. Primeiro, precisamos especificar se a variável é uma entrada ou uma saída da montagem inline. Neste caso, é uma saída. Declarámos isto escrevendo `out`. Também precisamos especificar em que tipo de registo a montagem espera a variável. Neste caso, colocamo-la num registo de propósito geral arbitrário especificando `reg`. O compilador escolherá um registo apropriado para inserir no modelo e lerá a variável a partir daí após a montagem inline terminar a sua execução.

Vejamos outro exemplo que também utiliza uma entrada:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let i: u64 = 3;
let o: u64;
unsafe {
    asm!(
        "mov {0}, {1}",
        "add {0}, 5",
        out(reg) o,
        in(reg) i,
    );
}
assert_eq!(o, 8);
# }
```

Isto irá adicionar `5` à entrada na variável `i` e escrever o resultado na variável `o`. A forma específica como esta montagem faz isto é primeiro copiar o valor de `i` para a saída e, em seguida, adicionar `5` a ele.

O exemplo mostra algumas coisas:

Primeiro, podemos ver que `asm!` permite múltiplos argumentos de string de modelo; cada um é tratado como uma linha separada de código de montagem, como se todos estivessem unidos com novas linhas entre eles. Isto facilita a formatação do código de montagem.

Segundo, podemos ver que as entradas são declaradas escrevendo `in` em vez de `out`.

Terceiro, podemos ver que podemos especificar um número de argumento ou nome, como em qualquer string de formato. Para modelos de montagem inline, isto é particularmente útil, pois os argumentos são frequentemente usados mais de uma vez. Para montagem inline mais complexa, o uso desta facilidade é geralmente recomendado, pois melhora a legibilidade e permite a reorganização de instruções sem alterar a ordem dos argumentos.

Podemos refinar ainda mais o exemplo acima para evitar a instrução `mov`:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut x: u64 = 3;
unsafe {
    asm!("add {0}, 5", inout(reg) x);
}
assert_eq!(x, 8);
# }
```

Podemos ver que `inout` é usado para especificar um argumento que é simultaneamente entrada e saída. Isto difere da especificação separada de entrada e saída, pois garante a atribuição de ambos ao mesmo registo.

Também é possível especificar variáveis diferentes para as partes de entrada e saída de um operando `inout`:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let x: u64 = 3;
let y: u64;
unsafe {
    asm!("add {0}, 5", inout(reg) x => y);
}
assert_eq!(y, 8);
# }
```

## Operandos de saída atrasados

O compilador Rust é conservador com a sua alocação de operandos. Assume-se que um `out` pode ser escrito a qualquer momento e, portanto, não pode partilhar a sua localização com qualquer outro argumento. No entanto, para garantir um desempenho ótimo, é importante usar o menor número possível de registos, para que não tenham de ser guardados e carregados em torno do bloco de montagem inline. Para atingir isto, Rust fornece um especificador `lateout`. Isto pode ser usado em qualquer saída que só seja escrita após todas as entradas terem sido consumidas. Existe também uma variante `inlateout` deste especificador.

Aqui está um exemplo onde `inlateout` _não_ pode ser usado no modo `release` ou em outros casos otimizados:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
let c: u64 = 4;
unsafe {
    asm!(
        "add {0}, {1}",
        "add {0}, {2}",
        inout(reg) a,
        in(reg) b,
        in(reg) c,
    );
}
assert_eq!(a, 12);
# }
```

O acima poderia funcionar bem em casos não otimizados (modo `Debug`), mas se quiser desempenho otimizado (modo `release` ou outros casos otimizados), não funcionaria.

Isto porque, em casos otimizados, o compilador é livre de alocar o mesmo registo para as entradas `b` e `c`, uma vez que sabe que têm o mesmo valor. No entanto, deve alocar um registo separado para `a`, uma vez que usa `inout` e não `inlateout`. Se `inlateout` fosse usado, então `a` e `c` poderiam ser alocados ao mesmo registo, caso em que a primeira instrução para sobrescrever o valor de `c` e causar que o código de montagem produza o resultado errado.

No entanto, o exemplo seguinte pode usar `inlateout`, uma vez que a saída só é modificada após a leitura de todos os registos de entrada:

```rust
# #[cfg(target_arch = "x86_64")] {
use std::arch::asm;

let mut a: u64 = 4;
let b: u64 = 4;
unsafe {
    asm!("add {0}, {1}", inlateout(reg) a, in(reg) b);
}
assert_eq!(a, 8);
# }
```

Como pode ver, este fragmento de montagem ainda funcionará corretamente se `a` e `b` forem atribuídos ao mesmo registo.

(Continua...)
