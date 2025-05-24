# 정규 표현식 복제하기

정규 표현식을 복제하려면 `RegExp` 생성자, `RegExp.prototype.source`, 그리고 `RegExp.prototype.flags`를 사용합니다.

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

이 코드는 주어진 정규 표현식의 복제본을 생성합니다. 예를 들어:

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp !== regExp2
```
