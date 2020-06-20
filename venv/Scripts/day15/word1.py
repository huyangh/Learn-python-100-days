"""
Time   : 2020/6/19 20:38
Author : huyangh
演示读取word文档
"""
from docx import Document

doc = Document('docs/test1.docx')
print(len(doc.paragraphs))
print(doc.paragraphs[0].text)
# print(doc.paragraphs[1].runs[0].text)

content = []
for para in doc.paragraphs:
    content.append(para.text)
print(''.join(content))