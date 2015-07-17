from PIL import Image
import os
# Tirar limiute para quantidade de pixels
Image.MAX_IMAGE_PIXELS = None


# OBS: Caso você tente abrir ou mover aquivo como ./arquivo.png, percebe que ele toma como referencia aonde você executou o script se o script tiver na pasta A e você tiver chamando ele na pasta B
# Ele irá associar o ./ na pasta A ainda. então lembre de usar
# os.path.joing(root, nome_do_arquivo)

# OBS2: desconfio que os.walk não verifica pastas vazias


# Melhorias
# se já havia alguma pasta sem imagem, deletar
# criar uma pasta chamada fail e colocar o failverbose.md nela

def imgQuality(path, w=1800, h=900):

    try:
        os.mkdir('fail')
    except:
        pass

    with open('./fail/failverbose.md', 'w') as failverbose:

        failImgs = 0
        for root, dirs, files in os.walk(path):

            # print(root, dirs, files, len(dirs), len(files))

            if len(dirs) == len(files):
                print(root, 'Pasta Vazia')
                failverbose.write(
                    '\n' + '- ***PASTA VAZIA***' + root + '\n' + '\n')

            for imgname in files:
                isImage = imgname.lower()
                if isImage.endswith(('.png', '.gif', '.jpg', '.tif')):
                    caminho = os.path.join(root, imgname)

                    # problema, se o diretório for exept não faça nada continue

                    try:
                        img = Image.open(caminho)

                        # PROBLEMA, NÃO FUNCIONA
                        # verificar se o pasta ta vazia
                        # print(len(files), root)
                        # if len(files) == 0:
                        #     failverbose.write('- Pasta:' + root + 'VAZIA')

                        if img.size[0] < w or img.size[1] < h:

                            # verificar se o pasta ta vazia, nesse caso ele só tem
                            # 1 imagem, que será removida
                            if len(files) == 1:
                                failverbose.write(
                                    '- ***NOVA PASTA VAZIA***' + root + '\n')

                            failImgs += 1
                            print(failImgs)
                            failverbose.write(
                                '- Pasta:' + root + 'IMAGEM: --->' + imgname + '\n')
                            os.rename(
                                os.path.join(root, imgname), './fail/' + imgname)

                    except:
                        print(caminho, '--->', imgname, 'ERRO')

        failverbose.write('\n' + 'Fails = ' + str(failImgs))


imgQuality('/home/liphvf/Downloads/4chan2/')
