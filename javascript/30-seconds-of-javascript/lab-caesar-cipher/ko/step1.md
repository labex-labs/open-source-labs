# 시저 암호 (Caesar Cipher)

시저 암호를 사용하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 암호화 또는 해독할 문자열, 이동 값, 그리고 해독 여부를 나타내는 부울 값을 사용하여 `caesarCipher` 함수를 호출합니다.
3. `caesarCipher` 함수는 모듈로 연산자 (`%`) 와 삼항 연산자 (`?`) 를 사용하여 올바른 암호화 또는 해독 키를 계산합니다.
4. 스프레드 연산자 (`...`) 와 `Array.prototype.map()`을 사용하여 주어진 문자열의 문자를 반복합니다.
5. `String.prototype.charCodeAt()` 및 `String.fromCharCode()`를 사용하여 특수 문자, 공백 등을 무시하고 각 문자를 적절하게 변환합니다.
6. `Array.prototype.join()`을 사용하여 모든 문자를 문자열로 결합합니다.
7. 암호화된 문자열을 해독하려면 `caesarCipher` 함수를 호출할 때 마지막 매개변수인 `decrypt`에 `true`를 전달합니다.

다음은 `caesarCipher` 함수의 코드입니다.

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

다음은 `caesarCipher` 함수를 사용하는 몇 가지 예입니다.

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
