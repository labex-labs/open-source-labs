# Понимание объектов в JavaScript

Прежде чем мы начнем преобразовывать ключи объектов в нижний регистр, давайте разберемся, что такое объекты JavaScript и как с ними работать.

В JavaScript объект представляет собой коллекцию пар ключ-значение. Ключи являются строками (или Symbol), а значения могут быть любого типа данных, включая другие объекты.

Начнем с открытия интерактивной оболочки Node.js:

1. Откройте терминал в вашем WebIDE.
2. Введите `node` и нажмите Enter.

Теперь вы должны увидеть приглашение Node.js (`>`), которое позволяет вам напрямую вводить код JavaScript.

Создадим простой объект с ключами в смешанном регистре:

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

Введите этот код в приглашение Node.js и нажмите Enter. Чтобы увидеть объект, просто введите `user` и нажмите Enter:

```javascript
user;
```

Вы должны увидеть следующий вывод:

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

Как вы можете видеть, в этом объекте ключи имеют разные стили написания. На следующем шаге мы научимся обращаться к этим ключам и преобразовывать их в нижний регистр.
