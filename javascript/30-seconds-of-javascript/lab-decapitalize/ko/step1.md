# 문자열 소문자 변환을 위한 Javascript 함수

문자열의 첫 글자를 소문자로 변환하려면 다음 JavaScript 함수를 사용하십시오.

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

이 함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음, 소문자로 변환하려는 문자열을 첫 번째 인수로 전달하여 `decapitalize` 함수를 호출하십시오.

선택적으로, 두 번째 인수 `upperRest`를 `true`로 설정하여 나머지 문자열을 대문자로 변환할 수 있습니다. `upperRest`가 제공되지 않으면 기본값은 `false`입니다.

다음은 몇 가지 예입니다.

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
