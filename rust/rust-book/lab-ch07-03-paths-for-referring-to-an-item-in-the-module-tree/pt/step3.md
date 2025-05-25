# Iniciando Caminhos Relativos com `super`

Podemos construir caminhos relativos que começam no módulo pai, em vez do módulo atual ou da raiz da crate, usando `super` no início do caminho. Isso é como iniciar um caminho do sistema de arquivos com a sintaxe `..`. Usar `super` nos permite referenciar um item que sabemos que está no módulo pai, o que pode facilitar a reorganização da árvore de módulos quando o módulo está intimamente relacionado ao pai, mas o pai pode ser movido para outro lugar na árvore de módulos algum dia.

Considere o código na Listagem 7-8 que modela a situação em que um chef corrige um pedido incorreto e o leva pessoalmente ao cliente. A função `fix_incorrect_order` definida no módulo `back_of_house` chama a função `deliver_order` definida no módulo pai, especificando o caminho para `deliver_order`, começando com `super`.

Nome do arquivo: `src/lib.rs`

```rust
fn deliver_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        super::deliver_order();
    }

    fn cook_order() {}
}
```

Listagem 7-8: Chamando uma função usando um caminho relativo começando com `super`

A função `fix_incorrect_order` está no módulo `back_of_house`, então podemos usar `super` para ir para o módulo pai de `back_of_house`, que neste caso é `crate`, a raiz. De lá, procuramos por `deliver_order` e o encontramos. Sucesso! Achamos que o módulo `back_of_house` e a função `deliver_order` provavelmente permanecerão na mesma relação um com o outro e serão movidos juntos caso decidamos reorganizar a árvore de módulos da crate. Portanto, usamos `super` para que tenhamos menos lugares para atualizar o código no futuro, caso este código seja movido para um módulo diferente.
