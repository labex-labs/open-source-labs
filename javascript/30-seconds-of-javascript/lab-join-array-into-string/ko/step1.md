# 배열을 문자열로 결합하는 방법

배열의 모든 요소를 문자열로 결합하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 다음 매개변수를 사용하여 `join()` 함수를 사용합니다.
   - `arr`: 결합할 배열입니다.
   - `separator` (선택 사항): 배열의 요소 사이에 사용할 구분 기호입니다. 지정하지 않으면 기본 구분 기호 `,`가 사용됩니다.
   - `end` (선택 사항): 배열의 마지막 두 요소 사이에 사용할 구분 기호입니다. 지정하지 않으면 기본적으로 `separator`와 동일한 값이 사용됩니다.
3. `join()` 함수는 `Array.prototype.reduce()`를 사용하여 배열의 요소를 문자열로 결합합니다.
4. 최종 문자열이 반환됩니다.

다음은 `join()` 함수의 코드입니다.

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
          ? acc + val
          : acc + val + separator,
    ""
  );
```

다음은 `join()` 함수를 사용하는 몇 가지 예입니다.

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
