import docx
def getText(filename):
    try:
        doc=docx.Document(filename)
        fulltext=[]
        for para in doc.paragraphs:
            fulltext.append(para.text)
        return '\n'.join(fulltext)
    except Exception as ex:
        print(ex)