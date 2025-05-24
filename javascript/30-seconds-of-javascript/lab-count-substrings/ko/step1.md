# JavaScript 를 사용하여 문자열 내 부분 문자열 개수 세는 방법

코딩 연습을 하려면 터미널/SSH 를 열고 `node`를 입력하세요. 이 JavaScript 함수는 주어진 문자열에서 지정된 부분 문자열의 발생 횟수를 계산합니다.

이 함수를 사용하려면 다음 단계를 따르세요.

1. `str`과 `searchValue`의 두 매개변수를 받는 `countSubstrings`라는 함수를 선언합니다.
2. `count`와 `i`의 두 변수를 초기화합니다.
3. `Array.prototype.indexOf()` 메서드를 사용하여 `str`에서 `searchValue`를 검색합니다.
4. 값을 찾으면 `count` 변수를 증가시키고 `i` 변수를 업데이트합니다.
5. `Array.prototype.indexOf()`에서 반환된 값이 `-1`이 되는 즉시 반환되는 `while` 루프를 사용합니다.
6. `count` 변수를 반환합니다.

다음은 `countSubstrings` 함수의 코드입니다.

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
