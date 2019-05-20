from docx import Document

class Word:

    def crearDocumento(self):
        informe = Document()
        informe.add_picture('./grafico.png')
        informe.save('./informe.docx')



