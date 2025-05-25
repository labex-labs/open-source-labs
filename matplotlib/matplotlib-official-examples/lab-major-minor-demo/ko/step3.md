# 주요 및 보조 로케이터 설정

```python
# Set the major locator
ax.xaxis.set_major_locator(MultipleLocator(20))
# Set the major formatter
ax.xaxis.set_major_formatter('{x:.0f}')
# Set the minor locator
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

여기서는 주요 로케이터 (major locator) 를 20 의 배수에 눈금을 표시하도록 설정하고, 주요 포매터 (major formatter) 를 ".0f" 형식으로 주요 눈금에 레이블을 지정하도록 설정하며, 보조 로케이터 (minor locator) 를 5 의 배수에 눈금을 표시하도록 설정합니다.
