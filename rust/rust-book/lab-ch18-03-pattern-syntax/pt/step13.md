# Partes de um Valor com um \_ Aninhado

Também podemos usar `_` dentro de outro padrão para ignorar apenas parte de um valor, por exemplo, quando queremos testar apenas parte de um valor, mas não temos uso para as outras partes no código correspondente que queremos executar. A Listagem 18-18 mostra o código responsável por gerenciar o valor de uma configuração. Os requisitos de negócios são que o usuário não deve ter permissão para substituir uma personalização existente de uma configuração, mas pode desativar a configuração e dar-lhe um valor se ela estiver atualmente desativada.

Nome do arquivo: `src/main.rs`

```rust
let mut setting_value = Some(5);
let new_setting_value = Some(10);

match (setting_value, new_setting_value) {
    (Some(_), Some(_)) => {
        println!("Can't overwrite an existing customized value");
    }
    _ => {
        setting_value = new_setting_value;
    }
}

println!("setting is {:?}", setting_value);
```

Listagem 18-18: Usando um sublinhado dentro de padrões que correspondem a variantes `Some` quando não precisamos usar o valor dentro do `Some`

Este código imprimirá `Can't overwrite an existing customized value` e, em seguida, `setting is Some(5)`. No primeiro braço do `match`, não precisamos corresponder ou usar os valores dentro de nenhuma variante `Some`, mas precisamos testar o caso em que `setting_value` e `new_setting_value` são a variante `Some`. Nesse caso, imprimimos a razão para não alterar `setting_value`, e ele não é alterado.

Em todos os outros casos (se `setting_value` ou `new_setting_value` for `None`) expressos pelo padrão `_` no segundo braço, queremos permitir que `new_setting_value` se torne `setting_value`.

Também podemos usar sublinhados em vários lugares dentro de um padrão para ignorar valores específicos. A Listagem 18-19 mostra um exemplo de ignorar o segundo e o quarto valores em uma tupla de cinco itens.

Nome do arquivo: `src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Some numbers: {first}, {third}, {fifth}");
    }
}
```

Listagem 18-19: Ignorando várias partes de uma tupla

Este código imprimirá `Some numbers: 2, 8, 32`, e os valores `4` e `16` serão ignorados.
