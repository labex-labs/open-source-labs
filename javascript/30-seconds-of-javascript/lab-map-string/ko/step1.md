# 문자열 내 문자 매핑 함수

이 함수를 사용하여 문자열 내 문자를 매핑하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `String.prototype.split()`과 `Array.prototype.map()`을 사용하여 주어진 문자열의 각 문자에 대해 제공된 함수 `fn`을 호출합니다.
- `Array.prototype.join()`을 사용하여 문자 배열을 새로운 문자열로 다시 결합합니다.
- 콜백 함수 `fn`은 세 개의 인수를 받습니다: 현재 문자, 현재 문자의 인덱스, 그리고 `mapString`이 호출된 문자열입니다.

다음은 함수 코드입니다:

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

사용 예시:

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
