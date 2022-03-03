# Imports
import os
import pandas as pd
import yaml
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4, landscape

fields = {'Nome do Evento'}

def readYAML(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

# Convert date format to portuguese date
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


# Generate certificates
def certGen(event_name, df, background, date):

    for index, row in df.iterrows():
        name = row['NAME']
        hours = row['HOURS']
        filename = os.path.join(str(name) + '.pdf')
        c = canvas.Canvas(filename, pagesize = landscape(A4))
        c.setTitle(str(name))
        cW, cH = c._pagesize
        c.drawInlineImage(background, 0, 0, width = cW, height = cH)
        c.setFont('Helvetica', 40)
        i = "CERTIFICADO"
        c.drawCentredString(400, 440, i)
        dec = ['Declaramos para os devidos fins que',
                str(name),
                'participou do evento',
                '"' + str(event_name) + '"',
                'no dia ' + date + ' cumprindo carga horária de ' + str(hours) + ' horas.',
                ' ',
                'Bauru, ' + date2Text(datetime.now().strftime('%d/%m/%Y'))]
        y = 380
        for i in dec:
            c.setFont('Helvetica', 20)
            c.drawCentredString(400, y, i)
            y -= 30

        #fecha arquivo pdf e o salva
        c.showPage()
        c.save()

if __name__ == '__main__':
    config_file = readYAML('config.yaml')
    event_name = config_file['event_name']
    input_name = config_file['input_name']
    date = config_file['date']
    background_name = config_file['background_image']
    df = pd.read_csv(input_name, sep=',')
    background = str(background_name)
    certGen(event_name, df, background, date)
