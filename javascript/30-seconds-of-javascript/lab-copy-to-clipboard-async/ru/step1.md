# Функция для копирования строки в буфер обмена

Для копирования строки в буфер обмена используйте функцию `copyToClipboardAsync`. Функция возвращает промис, который разрешается, когда содержимое буфера обмена обновлено. Вот шаги:

1. Проверьте, доступен ли API буфера обмена, проверив, являются ли `Navigator`, `Navigator.clipboard` и `Navigator.clipboard.writeText` истинными с использованием инструкции `if`.
2. Если API буфера обмена доступен, используйте `Clipboard.writeText()` для записи заданного значения `str` в буфер обмена.
3. Возвращаем результат `Clipboard.writeText()`, который является промисом, разрешающимся, когда содержимое буфера обмена обновлено.
4. Если API буфера обмена недоступен, отклоните промис с соответствующим сообщением об ошибке с использованием `Promise.reject()`.
5. Если вам нужно поддерживать старые браузеры, используйте `Document.execCommand()` вместо `Clipboard.writeText()`. Вы можете узнать больше об этом в сниппете `copyToClipboard`.

Вот функция `copyToClipboardAsync`:

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

Для использования функции вызовите `copyToClipboardAsync` с строкой, которую вы хотите скопировать, в качестве аргумента, вот так:

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' скопировано в буфер обмена.
```
