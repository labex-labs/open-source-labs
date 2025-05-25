# PdfPages 객체 생성

다음으로, PDF 파일의 페이지를 저장할 PdfPages 객체를 생성해야 합니다. 'with' 문을 사용하여 예외가 발생하더라도 블록이 끝날 때 PdfPages 객체가 제대로 닫히도록 할 수 있습니다.

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
