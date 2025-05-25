# 악센트 제거

이 함수는 문자열에서 악센트를 제거합니다.

- `String.prototype.normalize()`를 사용하여 문자열을 정규화된 유니코드 형식으로 변환합니다.
- `String.prototype.replace()`를 사용하여 주어진 유니코드 범위 내의 분음 부호를 빈 문자열로 대체합니다.

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

이 함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력합니다. 그런 다음 문자열을 인수로 사용하여 함수를 호출합니다.

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
