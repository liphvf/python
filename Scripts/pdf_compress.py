import os
import glob


def pdf_compress(entrada=glob.glob('*.pdf')):
    '''
    Esta função pega todos os pdfs presente na entrada,  comprime,
    e joga em uma pasta output
    '''
    if not os.path.exists('output'):
        os.mkdir('output')

    for pdf in entrada:

        output_folder = 'output/'
        command = 'convert %s -compress Zip %s' % (pdf, output_folder + pdf)
        # print(command)
        os.system(command)
