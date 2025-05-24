# 배열을 압축하고 결합하는 방법에 대한 팁

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

배열에서 falsy 값을 제거하고 나머지 값을 문자열로 결합하는 방법은 다음과 같습니다.

- `Array.prototype.filter()`를 사용하여 `false`, `null`, `0`, `""`, `undefined`, `NaN`과 같은 falsy 값을 필터링합니다.
- `Array.prototype.join()`을 사용하여 나머지 값을 문자열로 결합합니다.

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

그런 다음 함수를 호출하고 배열을 인수로 전달합니다.

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
