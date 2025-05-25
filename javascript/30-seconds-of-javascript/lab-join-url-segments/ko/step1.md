# URL 세그먼트 결합 및 정규화

주어진 URL 세그먼트를 함께 결합하고 결과 URL 을 정규화하려면 다음 단계를 따르세요.

1. `Array.prototype.join()`을 사용하여 URL 세그먼트를 결합합니다.
2. 일련의 `String.prototype.replace()` 호출과 다양한 정규 표현식 (regular expression) 을 사용하여 다음을 통해 결과 URL 을 정규화합니다.
   - 이중 슬래시 제거
   - 프로토콜에 적절한 슬래시 추가
   - 매개변수 앞의 슬래시 제거
   - 매개변수를 `'&'`로 결합하고 첫 번째 매개변수 구분 기호를 정규화

URL 세그먼트를 결합하고 정규화하려면 아래 코드 스니펫을 사용하세요.

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

사용 예시:

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
