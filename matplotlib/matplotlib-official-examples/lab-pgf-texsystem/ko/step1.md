# Matplotlib 임포트 및 pgf.texsystem 매개변수 설정

먼저, Matplotlib 라이브러리를 임포트하고 `pgf.texsystem` 매개변수를 `pdflatex`로 설정해야 합니다. 이 매개변수를 사용하면 LaTeX 를 사용하여 플롯의 글꼴 패밀리를 사용자 정의할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
