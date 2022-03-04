import os
from PIL import Image

def valid_image(nome_arq):
    if nome_arq.endswith('png') or nome_arq.endswith('jpg'):
        return True
    return False


def resize(input_dir, output_dir, size):
    lista_arquivos = [nome for nome in os.listdir(input_dir) if valid_image(nome) == True]

    for nome in lista_arquivos:

        imagem = Image.open(os.path.join(input_dir, nome))
        size = size
        size_name = str(size).replace('(','').replace(')','').replace(',','x').replace(' ','')
        redimension = imagem.resize(size)
        nome1 = nome.split('.')
        nome_ = str(nome1[0])+'_'+size_name+'.'+str(nome1[1])
        redimension.save(os.path.join(output_dir, nome_))

    #print(lista_arquivos)

if __name__ == '__main__':
    dir = 'diretório onde estão os arquivos'
    output = 'diretório onde os novos arquivos serão salvos
    resize(dir, output, ((50,50)))