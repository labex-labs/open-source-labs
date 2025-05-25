# 글꼴 패밀리 정의

다음으로, 플롯에서 사용하려는 글꼴 패밀리를 정의해야 합니다. 이 예제에서는 `cmbright` 글꼴 패밀리를 사용합니다.

```python
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": "\n".join([
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
    ]),
})
```
