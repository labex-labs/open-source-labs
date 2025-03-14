# Стек

## Задача

Реализуйте стек на основе связанного списка на Python с такими методами:

- push: добавляет элемент в вершину стека
- pop: удаляет и возвращает элемент из вершины стека. Если стек пуст, возвращает None.
- peek: возвращает элемент из вершины стека без его удаления. Если стек пуст, возвращает None.
- is_empty: возвращает True, если стек пуст, иначе False.

## Требования

Следующие требования должны быть выполнены:

- При удалении элемента из пустого стека возвращать None.
- Реализация должна использовать связанный список.
- Реализация должна быть на Python.
- Реализация должна включать четыре метода: push, pop, peek и is_empty.

## Пример использования

### Добавление элемента (push)

- Добавление в пустой стек: stack.push(1)
- Добавление в непустой стек: stack.push(2)

### Удаление элемента (pop)

- Удаление из пустого стека: stack.pop() -> None
- Удаление из стека с одним элементом: stack.pop() -> 1
- Удаление из стека с несколькими элементами: stack.pop() -> 2

### Просмотр верхнего элемента (peek)

- Просмотр в пустом стеке: stack.peek() -> None
- Просмотр в стеке с одним или более элементами: stack.peek() -> 2

### Проверка на пустоту (is_empty)

- Проверка пустоты в пустом стеке: stack.is_empty() -> True
- Проверка пустоты в стеке с одним или более элементами: stack.is_empty() -> False
