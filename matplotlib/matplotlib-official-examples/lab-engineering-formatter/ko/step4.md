# 공학 표기법을 사용하여 눈금 레이블 지정

이제 공학 표기법을 사용하여 x 축의 눈금에 레이블을 지정합니다. 첫 번째 subplot 에서는 기본 설정을 사용하고, 두 번째 subplot 에서는 `places` 및 `sep` 옵션을 사용하여 소수점 이하 자릿수와 숫자와 접두사/단위 사이의 구분 기호를 지정합니다.

```python
# Demo of the default settings, with a user-defined unit label.
ax0.set_title('Full unit ticklabels, w/ default precision & space separator')
formatter0 = EngFormatter(unit='Hz')
ax0.xaxis.set_major_formatter(formatter0)
ax0.plot(xs, ys)
ax0.set_xlabel('Frequency')

# Demo of the options `places` (number of digit after decimal point) and
# `sep` (separator between the number and the prefix/unit).
ax1.set_title('SI-prefix only ticklabels, 1-digit precision & '
              'thin space separator')
formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
ax1.xaxis.set_major_formatter(formatter1)
ax1.plot(xs, ys)
ax1.set_xlabel('Frequency [Hz]')
```
