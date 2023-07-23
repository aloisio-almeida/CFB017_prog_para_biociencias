#!/urs/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='O EBQMMM visa realizar cálculos de energia de ligação utilizando teoria quântica/ab initio por meio de cálculos híbridos, com região de interesse sendo tratada com Mecânica Quântica (QM) e o restante do sistema com pontos de carga derivados de campos de força clássicos.')

# Argumentos posicionais
parser.add_argument('pdb', type=argparse.FileType('r'), help='Caminho para o arquivo PDB contendo a estrutura molecular.')
parser.add_argument('n_resid', type=str, help='Resíduo do PDB correspondente ao ligante/molécula de interesse.')
parser.add_argument('name_lig', type=str, help='Nome do resíduo do PDB correspondente ao ligante/molécula em estudo.')
parser.add_argument('prefix', type=str, help='Prefixo do sistema. Será criada uma pasta com esse nome contendo as pastas (apo), (complex) e (lig). Caso não especificado, o prefixo será o nome do arquivo PDB.')

# Argumentos opcionais
parser.add_argument('-rqm', type=int, default=5, help='Raio da região QM (Mecânica Quântica).')
parser.add_argument('-sofqm', type=str, default='Orca', help='Programa QM utilizado. Opções: "Orca" ou "XTB".')
parser.add_argument('-noapo', action='store_true', help='Não preparar o sistema apo. Útil quando a simulação apo já foi realizada anteriormente e/ou para diminuir os cálculos, fazendo apenas Δe = Complex - Lig (não recomendado/testado).')
parser.add_argument('-qmMethod', type=str, default='!B3LYP 6-31G* TightSCF', help='Método (palavras-chave) a ser utilizado na região QM. Por padrão, usa-se "!B3LYP 6-31G* TightSCF" para o programa Orca e "GFN2-xTB" para o XTB.')
parser.add_argument('-dir_work', type=str, default='/tmp', help='Diretório onde serão gerados arquivos intermediários e logs de programas (ex.: VMD). Por padrão, utiliza-se o diretório /tmp.')
parser.add_argument('-dir_save', type=str, default='./', help='Diretório onde serão salvos os sistemas preparados. Por padrão, utiliza-se o diretório atual.')
parser.add_argument('-nprocs', type=int, default=1, help='Número de processadores que será usado pelo programa QM. Padrão: 1.')
parser.add_argument('-maxram', type=str, default='2GB', help='Máximo de memória RAM utilizado pelo programa QM. Padrão: "2GB".')
parser.add_argument('-charge', type=int, help='Carga do ligante/resíduo de referência. A carga da proteína será calculada automaticamente. Só é necessário oferecer a carga do ligante, essa será somada à carga do restante da região QM.')
parser.add_argument('-pointCharge', type=str, default='on', help='Adicionar automaticamente os pontos de carga. Opções: "on" (para proteínas) ou "off".')
parser.add_argument('-ff', type=str, default='CHARMM', help='Campo de força de referência para adicionar os pontos de carga. Padrão: CHARMM (top_all36_prot) presente em app.forcefild. Somente compatível com FFs CHARMM.')
parser.add_argument('-cutoff', type=int, help='Adiciona apenas os pontos de carga dentro do cutoff ao redor da região QM. Exemplo: -cutoff 20.')
parser.add_argument('-optGeo', type=str, default='AM1', help='Realizar otimização da geometria da região QM. Método pode ser indicado (por padrão, usa-se AM1).')
parser.add_argument('-pathQMSof', type=str, default='', help='Caminho do programa QM que será adicionado ao arquivo de execução dos cálculos QM. Pode ser modificado também no arquivo .sh presente no diretório com os sistemas.')
parser.add_argument('-pathQMExec', type=str, default='', help='Local de execução dos cálculos QM. Pode ser modificado também no arquivo .sh presente no diretório com os sistemas.')
parser.add_argument('-multiPrepare', type=str, default='AM1', help='Realizar otimização da geometria da região QM. Método pode ser indicado (por padrão, usa-se AM1).')

args = parser.parse_args()

