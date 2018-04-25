import PyPDF2, pprint
file1=open(r'c:\users\bruce\desktop\code\tax\2016\1095.pdf','rb')
file2=open(r'c:\users\bruce\desktop\code\tax\2016\f8843.pdf','rb')
reader1=PyPDF2.PdfFileReader(file1)
reader2=PyPDF2.PdfFileReader(file2)
writer=PyPDF2.PdfFileWriter()
for numPage in range(reader1.numPages):
    page=reader1.getPage(numPage)
    writer.addPage(page)
for numPage in range(reader2.numPages):
    page=reader2.getPage(numPage)
    writer.addPage(page)
writer.encrypt('chenggang')
pdfOutFile=open('combinationfile.pdf','wb')
writer.write(pdfOutFile)
pdfOutFile.close()
file1.close()
file2.close()