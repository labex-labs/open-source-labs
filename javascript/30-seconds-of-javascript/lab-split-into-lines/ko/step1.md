# 터미널/SSH 에서 코딩 연습을 시작하는 방법

터미널/SSH 에서 코딩 연습을 시작하려면 단순히 `node`를 입력하십시오.

# 여러 줄 문자열을 줄 배열로 분할하는 방법

여러 줄 문자열을 줄 배열로 분할하려면 다음을 수행하십시오.

- `String.prototype.split()`과 정규 표현식 (regular expression) 을 사용하여 줄 바꿈을 일치시키고 배열을 생성합니다.
- 정규 표현식 `/\r?\n/`은 `\r` 및 `\n` 줄 바꿈을 모두 일치시킵니다.
- 이렇게 하면 줄의 배열이 반환됩니다.

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a', 'multiline', 'string.' , '']
```
