# JavaScript 에서 문자열 들여쓰기 함수

주어진 문자열의 각 줄에 들여쓰기를 추가하려면 JavaScript 에서 `indentString()` 함수를 사용할 수 있습니다. 이 함수는 `str`, `count`, 그리고 `indent` 세 개의 인수를 받습니다.

- `str` 인수는 들여쓰기하려는 문자열을 나타냅니다.
- `count` 인수는 각 줄을 몇 번 들여쓰기할지 결정합니다.
- `indent` 인수는 선택 사항이며 들여쓰기에 사용할 문자를 나타냅니다. 제공하지 않으면 기본값은 단일 공백 문자 (`' '`) 입니다.

다음은 `indentString()` 함수의 코드입니다.

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

이 함수를 사용하려면 원하는 인수로 호출하기만 하면 됩니다. 몇 가지 예는 다음과 같습니다.

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

첫 번째 예에서 `indentString('Lorem\nIpsum', 2)`는 `'  Lorem\n  Ipsum'`을 반환합니다. 즉, 입력 문자열의 각 줄이 공백 문자로 두 번 들여쓰기되었습니다.

두 번째 예에서 `indentString('Lorem\nIpsum', 2, '_')`는 `'__Lorem\n__Ipsum'`을 반환합니다. 즉, 입력 문자열의 각 줄이 밑줄 문자 (`'_'`) 로 두 번 들여쓰기되었습니다.
