# O _Lifetime_ `Static`

Um _lifetime_ especial que precisamos discutir é `'static`, que denota que a referência afetada _pode_ viver durante toda a duração do programa. Todos os literais de string têm o _lifetime_ `'static`, que podemos anotar da seguinte forma:

```rust
let s: &'static str = "I have a static lifetime.";
```

O texto desta string é armazenado diretamente no binário do programa, que está sempre disponível. Portanto, o _lifetime_ de todos os literais de string é `'static`.

Você pode ver sugestões para usar o _lifetime_ `'static` em mensagens de erro. Mas antes de especificar `'static` como o _lifetime_ para uma referência, pense se a referência que você tem realmente vive durante todo o _lifetime_ do seu programa ou não, e se você quer que ela viva. Na maioria das vezes, uma mensagem de erro sugerindo o _lifetime_ `'static` resulta da tentativa de criar uma referência pendente ou uma incompatibilidade dos _lifetimes_ disponíveis. Nesses casos, a solução é corrigir esses problemas, não especificar o _lifetime_ `'static`.
