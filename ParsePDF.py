from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure

def def_layout(outline):
    for obj in outline:
        print(obj.__class__.__name__)
        if isinstance(obj, LTTextBox) or isinstance(obj, LTTextLine):
            print(obj.get_text())
        elif isinstance(obj, LTFigure):
            def_layout(obj)

doc= open(r'/Users/jmlessoff/Documents/Lessoff_paper.pdf', 'rb')
parse= PDFParser(doc)
doc = PDFDocument(parse)
manager=PDFResourceManager()
laparams=LAParams()
device= PDFPageAggregator(manager, laparams=laparams)
interp=PDFPageInterpreter(manager,device)
for page in PDFPage.create_pages(doc):
    interp.process_page(page)
    outline=device.get_result()
    def_layout(outline)