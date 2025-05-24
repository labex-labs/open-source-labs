# JavaScript 를 사용하여 문자열을 숫자로 해싱하는 방법

JavaScript 를 사용하여 입력 문자열을 정수로 해싱하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `String.prototype.split()` 및 `Array.prototype.reduce()` 메서드를 사용하여 비트 시프팅을 활용하여 입력 문자열의 해시를 생성합니다.
3. 다음은 해싱 알고리즘을 구현하는 `sdbm` 함수의 코드입니다.

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4. 함수를 테스트하려면 문자열 인수를 사용하여 호출합니다.

```js
sdbm("name"); // -3521204949
```

이렇게 하면 입력 문자열 "name"에 대한 해시 값이 반환됩니다.
