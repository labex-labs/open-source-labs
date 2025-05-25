# Como a Coerção de Deref Interage com a Mutabilidade

Semelhante a como você usa o trait `Deref` para substituir o operador `*` em referências imutáveis, você pode usar o trait `DerefMut` para substituir o operador `*` em referências mutáveis.

O Rust faz a coerção de deref quando encontra tipos e implementações de traits em três casos:

- De `&T` para `&U` quando `T: Deref<Target=U>`
- De `&mut T` para `&mut U` quando `T: DerefMut<Target=U>`
- De `&mut T` para `&U` quando `T: Deref<Target=U>`

Os dois primeiros casos são os mesmos, exceto que o segundo implementa a mutabilidade. O primeiro caso afirma que, se você tem um `&T`, e `T` implementa `Deref` para algum tipo `U`, você pode obter um `&U` de forma transparente. O segundo caso afirma que a mesma coerção de deref acontece para referências mutáveis.

O terceiro caso é mais complicado: o Rust também irá coagir uma referência mutável para uma imutável. Mas o inverso _não_ é possível: referências imutáveis nunca serão coagidas para referências mutáveis. Por causa das regras de empréstimo (borrowing rules), se você tem uma referência mutável, essa referência mutável deve ser a única referência a esses dados (caso contrário, o programa não compilaria). Converter uma referência mutável em uma referência imutável nunca quebrará as regras de empréstimo. Converter uma referência imutável em uma referência mutável exigiria que a referência imutável inicial fosse a única referência imutável a esses dados, mas as regras de empréstimo não garantem isso. Portanto, o Rust não pode fazer a suposição de que converter uma referência imutável em uma referência mutável é possível.
