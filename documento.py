from docx import Document
from docx.enum.text import WD_BREAK
from PIL import Image
from datetime import datetime
class Word:

    def abrirDocumento(self):
        informe = Document('./template-info/template.docx')
        return informe


    def insertarGraficoBarras(self, informe):
        informe.add_picture('./imagenes/graficoDeBarra.png')

    def crearDocx(self, informe):
        informe.save('./informe/informe.docx')

    def webFilter(self, informe):
        informe.add_heading('Top de bloqueos de Webfilter por usuario', level=2)
        informe.add_paragraph('En el siguiente gráfico se detallan los usuarios con mas urls bloqueadas por parte del webfilter del fortigate.')

    def titulo(self, informe):
        currentMonth = str(datetime.now().month)
        currentYear = str(datetime.now().year)
        informe.add_heading('Reporte Mensual OSSIM', level= 0)
        informe.add_heading(f'{currentMonth} {currentYear}', level=0)
        informe.add_page_break()
