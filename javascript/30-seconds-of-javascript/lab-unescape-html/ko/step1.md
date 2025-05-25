# HTML Unescape (언이스케이프)

이 함수는 escape 된 HTML 문자를 unescape 합니다. 사용하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력합니다.
3. 다음 코드를 복사하여 붙여넣습니다.

```js
const unescapeHTML = (str) =>
  str.replace(
    /&amp;|&lt;|&gt;|&#39;|&quot;/g,
    (tag) =>
      ({
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#39;": "'",
        "&quot;": '"'
      })[tag] || tag
  );
```

4. `unescapeHTML` 함수를 호출하고 escape 된 문자가 포함된 문자열을 전달합니다.
5. 함수는 unescaped 된 문자열을 반환합니다.

사용 예시:

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
