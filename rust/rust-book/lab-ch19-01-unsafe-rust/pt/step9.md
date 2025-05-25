# Acessando Campos de uma Union

A ação final que funciona apenas com `unsafe` é acessar campos de uma union. Uma `union` é semelhante a uma `struct`, mas apenas um campo declarado é usado em uma instância específica de cada vez. Unions são usados principalmente para interagir com unions em código C. Acessar campos de union é unsafe porque o Rust não pode garantir o tipo de dados atualmente armazenados na instância da union. Você pode aprender mais sobre unions na Referência do Rust em \*https://doc.rust-lang.org/reference/items/unions.html\*\*.
