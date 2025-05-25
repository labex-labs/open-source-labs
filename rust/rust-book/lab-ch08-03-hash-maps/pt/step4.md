# Hash Maps e Propriedade (Ownership)

Para tipos que implementam o trait `Copy`, como `i32`, os valores são copiados para o hash map. Para valores próprios (owned values) como `String`, os valores serão movidos e o hash map será o proprietário desses valores, como demonstrado na Listagem 8-22.

```rust
use std::collections::HashMap;

let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name and field_value are invalid at this point, try
// using them and see what compiler error you get!
```

Listagem 8-22: Mostrando que as chaves e os valores são de propriedade do hash map assim que são inseridos

Não podemos usar as variáveis `field_name` e `field_value` depois que elas foram movidas para o hash map com a chamada para `insert`.

Se inserirmos referências a valores no hash map, os valores não serão movidos para o hash map. Os valores aos quais as referências apontam devem ser válidos por pelo menos o tempo que o hash map for válido. Falaremos mais sobre esses problemas em "Validando Referências com Lifetimes".
