# 문자열을 뒤집는 함수:

문자열을 뒤집으려면 스프레드 연산자 (`...`) 와 `Array.prototype.reverse()`를 사용합니다. `Array.prototype.join()`을 사용하여 문자를 결합하여 문자열을 얻습니다. 코드는 다음과 같습니다.

```js
const reverseString = (str) => [...str].reverse().join("");
```

사용 예시:

```js
reverseString("foobar"); // 'raboof'
```
