from docx import Document
from docx.enum.text import WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from PIL import Image
from datetime import datetime
from docx.shared import Pt
from docx.dml.color import ColorFormat
from docx.shared import RGBColor
class Word:

    def abrirDocumento(self):
        informe = Document('./template-info/template.docx')
        self.styleHeading1(informe)
        return informe


    def crearDocx(self, informe):
        informe.save('./informe/informe.docx')

    def webFilter(self, informe):
        informe.add_paragraph('Top de bloqueos de Webfilter por usuario', style = 'Heading 1')
        informe.add_paragraph('En el siguiente gráfico se detallan los usuarios con mas urls bloqueadas por parte del webfilter del fortigate.', style='Body Text')
        informe.add_picture('./imagenes/graficoDeBarra.png')
        informe.add_page_break()

    #def titulo(self, informe):
    #    currentMonth = str(datetime.now().month)
    #    currentYear = str(datetime.now().year)
    #    informe.add_heading('Reporte Mensual OSSIM', level=0)
    #    informe.add_heading(f'{currentMonth} {currentYear}', level=1)
    #    informe.add_page_break()

    def styleHeading1 (self, informe):
        styles = informe.styles
        style = styles.add_style('Heading 1', WD_STYLE_TYPE.PARAGRAPH)
        font = style.font
        font.name = 'Lato Light'
        font.size = Pt(20)
        color = font.color
        color.rgb = RGBColor(223, 125, 14)
