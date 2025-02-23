# Проверка, является ли среда Travis CI

Для проверки, запускается ли ваша программа на Travis CI, используйте функцию `isTravisCI()`. Эта функция проверяет, присутствуют ли переменные окружения `TRAVIS` и `CI`.

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

Для начала работы с Travis CI откройте Терминал/SSH и введите `node`.
