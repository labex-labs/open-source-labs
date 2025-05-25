# 문자열 순열 알고리즘

중복된 문자를 포함하는 문자열의 모든 순열을 생성하려면 다음 알고리즘을 사용하십시오.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀 (recursion) 를 사용하여 주어진 문자열의 모든 가능한 순열을 생성합니다.
3. 주어진 문자열의 각 문자에 대해 나머지 문자에 대한 모든 부분 순열을 생성합니다.
4. `Array.prototype.map()`을 사용하여 문자를 각 부분 순열과 결합합니다.
5. `Array.prototype.reduce()`를 사용하여 모든 순열을 하나의 배열로 결합합니다.
6. 기본 사례는 `String.prototype.length`가 `2` 또는 `1`일 때입니다.
7. ⚠️ **경고**: 실행 시간은 각 문자에 따라 기하급수적으로 증가합니다. 8~10 자 이상의 문자열의 경우, 환경이 모든 다른 조합을 해결하려고 시도하면서 멈출 수 있습니다.

다음은 알고리즘에 대한 JavaScript 코드입니다.

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val
          )
        ),
      []
    );
};
```

다음 코드로 `stringPermutations` 함수를 테스트할 수 있습니다.

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
