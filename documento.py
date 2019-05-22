from docx import Document
from docx.enum.text import WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from datetime import datetime
from docx.shared import Pt
from docx.dml.color import ColorFormat
from docx.shared import RGBColor
from auxiliares import devolverMes

class Word:

    def abrirDocumento(self):
        informe = Document('./template-info/template.docx')
        self.styleTitle(informe)
        self.styleBodyText(informe)
        self.styleHeading1(informe)
        self.styleSubtitle(informe)
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

    def styleHeading1 (self, documento):
        styles = documento.styles
        style = styles.add_style('Heading 1', WD_STYLE_TYPE.PARAGRAPH)
        font = style.font
        font.name = 'Lato Light'
        font.size = Pt(20)
        color = font.color
        color.rgb = RGBColor(223, 125, 14)


    def styleBodyText (self, documento):
        styles = documento.styles
        styles['Body Text'].delete()
        style = styles.add_style('Body Text', WD_STYLE_TYPE.PARAGRAPH)
        font = style.font
        font.name = 'Lato Light'
        font.size = Pt(14)
        color = font.color
        color.rgb = RGBColor(41,39,39)

    def styleTitle(self, documento):
        styles = documento.styles
        styles['Title'].delete()
        style = styles.add_style('Title', WD_STYLE_TYPE.PARAGRAPH)
        font = style.font
        font.name = 'Lato Light'
        font.size = Pt(26)
        font.bold= True
        color = font.color
        color.rgb = RGBColor(255,255,255)

    def styleSubtitle (self, documento):
        styles = documento.styles
        styles['Subtitle'].delete()
        style = styles.add_style('Subtitle', WD_STYLE_TYPE.PARAGRAPH)
        font = style.font
        font.name = 'Lato Light'
        font.size = Pt(24)
        font.bold= True
        color = font.color
        color.rgb = RGBColor(255,255,255)
