# 문자열 복수형 처리

주어진 숫자를 기반으로 단어의 복수형을 처리하려면 `pluralize` 함수를 사용하십시오. 터미널/SSH 를 열고 `node`를 입력하여 시작합니다. 이 함수는 입력 숫자에 따라 단수 또는 복수 형태의 단어를 반환할 수 있습니다. 또한 사용자 정의 복수형을 사용하기 위해 선택적 딕셔너리 (dictionary) 를 제공할 수도 있습니다.

`pluralize` 함수를 정의하려면 `word`와 선택적 `plural` 형태를 받는 클로저 (closure) 를 사용하십시오. 입력 `num`이 `-1` 또는 `1`이면 `word`의 단수형을 반환합니다. 그렇지 않으면 `plural` 형태를 반환합니다. 사용자 정의 `plural` 형태가 제공되지 않으면 함수는 기본적으로 단수 `word` + `s`를 사용합니다.

첫 번째 인수가 객체인 경우 `pluralize` 함수는 제공된 딕셔너리를 사용하여 `word`의 올바른 복수형을 해결할 수 있는 새로운 함수를 반환합니다.

다음은 `pluralize` 함수의 작동 방식입니다.

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

`pluralize` 함수는 다음과 같이 사용할 수 있습니다.

```js
pluralize(0, "apple"); // 'apples'
pluralize(1, "apple"); // 'apple'
pluralize(2, "apple"); // 'apples'
pluralize(2, "person", "people"); // 'people'
```

사용자 정의 복수형의 딕셔너리가 있는 경우, 주어진 `word`에 대해 자동으로 올바른 복수형을 사용하는 `autoPluralize` 함수를 만들 수 있습니다.

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
