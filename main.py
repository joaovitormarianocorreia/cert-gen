# Imports
import os
from re import T
import pandas as pd
import yaml
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph

def readYAML(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def date2Text(date):
    date = date.split('/')
    month = {
        '01': 'Janeiro',
        '02': 'Fevereiro',
        '03': 'Março',
        '04': 'Abril',
        '05': 'Maio',
        '06': 'Junho',
        '07': 'Julho',
        '08': 'Agosto',
        '09': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }.get(date[1])
    return (date[0] + " de " + month + " de " + date[2])


def createPDF(filename):
    directory = os.path.join(os.getcwd(), 'Certificados')
    if not os.path.exists(directory):
        os.makedirs(directory)

    return canvas.Canvas(os.path.join(directory, filename), pagesize=landscape(A4))


def drawBackground(canvas, background):
    cW, cH = canvas._pagesize
    canvas.drawInlineImage(background, 0, 0, width=cW, height=cH)


def drawParagraph(canvas, text, margin, x, y, style):
    cW, cH = canvas._pagesize

    message = Paragraph(text, style)
    message.wrapOn(canvas, cW - margin, cH)
    message.drawOn(canvas, x, y)


def drawLocalDate(canvas):
    cW, cH = canvas._pagesize
    canvas.setFillColor('white')
    canvas.setFont('Helvetica', 14)
    canvas.drawCentredString(
        cW/2, cH*0.39, f'Bauru, {date2Text(datetime.now().strftime("%d/%m/%Y"))}')


def certGen(event_name, df, background, date):

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER,
               fontSize=20, textColor='white', leading=24))

    for _index, row in df.iterrows():
        name = row['NAME'].title()
        ra = row['RA']
        hours = row['HOURS']

        # Create PDF
        filename = os.path.join(f'{ra}-{name}.pdf')
        c = createPDF(filename)
        c.setTitle(name)

        _cW, cH = c._pagesize
        drawBackground(c, background)

        text = f'''Declaramos para os devidos fins que \\n <strong><font size="24">{name}</font></strong> 
                \\n\\n Participou do evento <strong>\"{event_name}\"</strong> \\n Realizado no dia 
                <strong>{date2Text(date)}</strong> cumprindo carga horária de 
                <strong>{hours}</strong> horas.'''.replace('\\n', '<br/>')

        drawParagraph(c, text, 100, 50, cH*0.45, styles['centered'])
        drawLocalDate(c)

        c.showPage()
        c.save()
        print(f'Certificado gerado para "{name}"')


if __name__ == '__main__':
    config_file = readYAML('config.yaml')
    
    event_name = config_file['event_name']
    input_name = config_file['input_name']
    date = config_file['date']
    background = config_file['background_image']
    
    df = pd.read_csv(input_name, sep=';')
    
    certGen(event_name, df, background, date)
