from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt
from docx.dml.color import ColorFormat
from docx.shared import RGBColor





class Estilos:


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
