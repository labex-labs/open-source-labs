# 부분 문자열의 인덱스

주어진 문자열에서 부분 문자열의 모든 인덱스를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 내장 메서드 `Array.prototype.indexOf()`를 사용하여 `str`에서 `searchValue`를 검색합니다.
3. 값이 발견되면 `yield`를 사용하여 인덱스를 반환하고 인덱스 `i`를 업데이트합니다.
4. `Array.prototype.indexOf()`에서 반환된 값이 `-1`이 되는 즉시 제너레이터를 종료하는 `while` 루프를 사용합니다.

위 단계를 구현하는 예제 코드는 다음과 같습니다.

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

다음 코드로 함수를 테스트할 수 있습니다.

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
