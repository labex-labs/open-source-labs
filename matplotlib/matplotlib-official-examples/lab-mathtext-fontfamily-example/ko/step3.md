# 플롯에 텍스트 설정

다음으로, `text()` 함수를 사용하여 플롯에 텍스트를 설정합니다. 각 개별 텍스트 요소에 대한 글꼴 패밀리를 변경하기 위해 `math_fontfamily` 매개변수를 사용합니다.

```python
# A text mixing normal text and math text.
msg = (r"Normal Text. $Text\ in\ math\ mode:\ "
       r"\int_{0}^{\infty } x^2 dx$")

# Set the text in the plot.
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# Set another font for the next text.
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
