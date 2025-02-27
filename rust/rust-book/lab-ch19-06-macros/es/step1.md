# Macros

Hemos utilizado macros como `println!` en todo este libro, pero no hemos explorado por completo qué es una macro y cómo funciona. El término _macro_ se refiere a una familia de características en Rust: macros _declarativas_ con `macro_rules!` y tres tipos de macros _procedimentales_:

- Macros personalizadas `#[derive]` que especifican el código agregado con el atributo `derive` utilizado en structs y enums
- Macros similares a atributos que definen atributos personalizados que se pueden utilizar en cualquier elemento
- Macros similares a funciones que se parecen a llamadas a funciones pero operan sobre los tokens especificados como su argumento

Hablaremos de cada una de estas a continuación, pero primero, echemos un vistazo a por qué necesitamos macros cuando ya tenemos funciones.
