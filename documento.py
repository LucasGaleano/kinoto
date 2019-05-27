from docx import Document
from docx.enum.text import WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from datetime import datetime
from docx.shared import Pt
from docx.dml.color import ColorFormat
from docx.shared import RGBColor
from auxiliares import devolverMes
from estilo import Estilos

class Word:

    def abrirDocumento(self):
        informe = Document('./template-info/template.docx')
        estilos = Estilos()
        estilos.styleTitle(informe)
        estilos.styleBodyText(informe)
        estilos.styleHeading1(informe)
        estilos.styleSubtitle(informe)


        return informe


    def crearDocx(self, informe):
        informe.save('./informe/informe.docx')

    def webFilter(self, informe):
        informe.add_paragraph('Top de bloqueos de Webfilter por usuario', style = 'Heading 1')
        informe.add_paragraph('En el siguiente gráfico se detallan los usuarios con mas urls bloqueadas por parte del webfilter del fortigate.', style='Body Text')
        informe.add_picture('./imagenes/graficoDeBarra.png')
        informe.add_page_break()

    def titulo(self, informe):
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        mesActual = devolverMes(currentMonth)
        informe.add_paragraph('Reporte Mensual OSSIM', style = 'Title')
        informe.add_paragraph(f'{mesActual} {currentYear}', style = 'Subtitle')
        informe.add_page_break()

    
