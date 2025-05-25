# 바이트를 사람이 읽을 수 있는 문자열로 변환하기

바이트 단위의 숫자를 사람이 읽을 수 있는 문자열로 변환하려면 `prettyBytes()` 함수를 사용하십시오. 다음 사항에 유의하십시오.

- 이 함수는 지수를 기반으로 접근할 수 있는 단위 배열 사전 (array dictionary) 을 사용합니다.
- 두 번째 인수 `precision`을 사용하여 숫자를 특정 자릿수로 자를 수 있습니다. 기본값은 `3`입니다.
- 세 번째 인수 `addSpace`를 사용하여 숫자와 단위 사이에 공백을 추가할 수 있습니다. 기본값은 `true`입니다.
- 이 함수는 제공된 옵션과 음수 여부를 고려하여 예쁘게 꾸며진 문자열을 구성하여 반환합니다.

다음은 `prettyBytes()` 함수의 코드입니다.

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision)
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

다음은 `prettyBytes()` 함수 사용의 몇 가지 예입니다.

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
