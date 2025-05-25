# PDF 파일의 메타데이터 설정

이 단계에서는 PDF 파일의 메타데이터를 설정합니다. PDF 파일의 제목, 작성자, 주제, 키워드 및 생성/수정 날짜를 설정할 수 있습니다.

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
