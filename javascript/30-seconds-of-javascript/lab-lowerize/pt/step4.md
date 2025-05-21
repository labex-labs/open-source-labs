# Lidando com Casos Extremos (Edge Cases)

Nossa função funciona bem para objetos simples, mas e quanto a casos mais complexos? Vamos explorar alguns casos extremos e ver como nossa função os trata.

## Objetos Vazios

Primeiro, vamos testar com um objeto vazio:

```javascript
lowerizeKeys({});
```

A saída deve ser um objeto vazio:

```
{}
```

## Objetos com Objetos Aninhados

E se o objeto contiver objetos aninhados? Vamos tentar isso:

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

A saída será:

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

Observe que apenas a chave de nível superior `User` é convertida para minúsculas. As chaves dentro dos objetos aninhados permanecem inalteradas.

Para lidar com objetos aninhados, precisaríamos modificar nossa função para processar recursivamente todos os objetos. Vamos criar uma versão aprimorada:

```javascript
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};
```

Esta função aprimorada:

1. Verifica se cada valor também é um objeto (e não um array ou nulo)
2. Se for, ela se chama recursivamente nesse objeto aninhado
3. Caso contrário, ela usa o valor original

Vamos testá-la com nosso objeto aninhado:

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

Agora você deve ver todas as chaves convertidas para minúsculas, mesmo em objetos aninhados:

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

Ótimo trabalho! Você criou uma função avançada que pode lidar com objetos aninhados.
