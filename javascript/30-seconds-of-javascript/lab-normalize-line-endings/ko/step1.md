# 줄 바꿈 문자 정규화 함수

문자열의 줄 바꿈 문자를 정규화하려면 다음 함수를 사용할 수 있습니다.

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- `String.prototype.replace()`를 정규 표현식과 함께 사용하여 줄 바꿈 문자를 일치시키고 `normalized` 버전으로 바꿉니다.
- 기본적으로 `normalized` 버전은 `'\r\n'`으로 설정됩니다.
- 다른 `normalized` 버전을 사용하려면 두 번째 인수로 전달합니다.

다음은 몇 가지 예시입니다.

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
