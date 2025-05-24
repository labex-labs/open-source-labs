# 문자열이 아나그램인지 확인하는 JavaScript 함수

문자열이 다른 문자열의 아나그램인지 확인하려면 다음 JavaScript 함수를 사용하십시오. 대소문자를 구분하지 않으며 공백, 구두점 및 특수 문자를 무시합니다.

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음 두 개의 문자열을 인수로 사용하여 함수를 호출합니다.

```js
isAnagram("iceman", "cinema"); // true
```

이 함수는 불필요한 문자를 제거하기 위해 적절한 정규 표현식과 함께 `String.prototype.toLowerCase()` 및 `String.prototype.replace()`를 사용합니다. 또한 두 문자열 모두에서 `String.prototype.split()`, `Array.prototype.sort()`, 및 `Array.prototype.join()`을 사용하여 정규화하고 정규화된 형태가 같은지 확인합니다.
