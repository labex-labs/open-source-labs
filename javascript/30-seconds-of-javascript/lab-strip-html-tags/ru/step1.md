# Как удалить HTML/XML теги из строки

Чтобы удалить HTML/XML теги из строки, можно использовать регулярное выражение. Следуйте шагам:

1. Откройте Терминал/SSH
2. Введите `node`, чтобы начать практиковаться в написании кода
3. Используйте следующий код:

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. Протестируйте функцию на следующем примере:

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

Это удалит все HTML/XML теги из входной строки и вернет оставшийся текст.
