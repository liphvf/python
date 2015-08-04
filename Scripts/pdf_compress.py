import os
import glob


def pdf_compress_convert(entrada=glob.glob('*.pdf')):
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

def pdf_compress_gs(entrada=glob.glob('*.pdf')):
    '''
    Esta função pega todos os pdfs presente na entrada,  comprime,
    e joga em uma pasta output
    '''
    if not os.path.exists('output'):
        os.mkdir('output')

    for pdf in entrada:

        output_folder = 'output/'
        command = 'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dBATCH  -dQUIET -sOutputFile=%s %s' % (output_folder + pdf, pdf)
        # print(command)
        os.system(command)

def pdf_compress_qpdf(entrada=glob.glob('*.pdf')):
    '''
    Esta função pega todos os pdfs presente na entrada,  comprime,
    e joga em uma pasta output
    '''
    if not os.path.exists('output'):
        os.mkdir('output')

    for pdf in entrada:

        output_folder = 'output/'
        command = 'qpdf --linearize %s %s' % (pdf,output_folder + pdf)
        # print(command)
        os.system(command)


# Another Method

'''

pdf2ps large.pdf very_large.ps
ps2pdf very_large.ps small.pdf
'''