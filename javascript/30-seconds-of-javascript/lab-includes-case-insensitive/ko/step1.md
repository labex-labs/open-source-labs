# 대소문자 구분 없는 부분 문자열 검색

문자열에 대소문자를 구분하지 않고 부분 문자열이 포함되어 있는지 확인하려면 다음 단계를 따르세요.

- `'i'` 플래그를 사용하여 `RegExp` 생성자를 사용하여 주어진 `searchString`과 일치하는 정규 표현식 (regular expression) 을 생성하고 대소문자를 무시합니다.
- `RegExp.prototype.test()`를 사용하여 문자열에 부분 문자열이 포함되어 있는지 확인합니다.

다음은 예시 코드 조각입니다.

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

이 함수를 테스트하려면 다음을 실행할 수 있습니다.

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
