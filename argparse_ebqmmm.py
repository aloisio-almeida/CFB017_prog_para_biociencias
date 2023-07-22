#!/urs/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='O EBQMMM visa realizar cálculos de energia de ligação utilizando;teoria quântica/ab initio por meio de cálculos híbridos, com região de intersere sendo tratada com Mecânica Quântica (QM) e o restante do sistema com pontos de carga,derivados de campos de força clássicos')

# Adicionar os argumentos posicionais com o método add_argument():
parser.add_argument('pdb', type=argparse.FileType('r'), help='arquivo PDB')
parser.add_argument('-rqm', type=int, help='Raio da região QM')
parser.add_argument('n_resid', type=str, help='resíduo do PDB correspondente ao ligante/molécula de interesse')
parser.add_argument('name_lig', type=str, help='nome do resíduo do PDB correspondente ao ligante/molécula em estudo')
parser.add_argument('prefix', type=str, help='prefixo do sistema, uma pasta será criada com esse nome, contendo as pastas (apo), (complex) e (lig), caso não especificado, o prefixo será o nome do pdb')
parser.add_argument('-sofqm', type=str, help='programa QM utilizado, por padrão será utilizado o Orca (Orca e XTB implementados)')
parser.add_argument('-noapo', type=str, help='não prepara o sistema apo, útil quando a simulação apo já foi realizada anteriormente e/ou diminuir os cálculos, fazendo apenas Δe = Complex - Lig (não recomendado/testado) (Não implementado)')
parser.add_argument('-qmMethod', type=str, help='Método (palavras-chave) que serão utilizadas na região QM, por padrão será utilizado ("!B3LYP 6-31G* TightSCF") para programa Orca, por padrão no XTB será utilizado ("GFN2-xTB")')
parser.add_argument('-dir_work', type=str, help='Diretório que serão gerados arquivos intermediários, logs de programas (ex.: VMD), por padrão utiliza-se (/tmp);')
parser.add_argument('-dir_save', type=str, help='Diretório que serão salvos os sistemas preparados, por padrão será utilizado o diretório no qual foi executado o programa (""./"")')
parser.add_argument('-nprocs', type=str, help='Número de processadores que será usado pelo programa QM, padrão')
parser.add_argument('-maxram', type=str, help='Máximo de memória ram utilizado pelo programa QM, caso o programa aceite, padrão 2GB por núcleo (para o Orca)')
parser.add_argument('-charge', type=str, help='Carga do ligante/resídio de referência, a carga da proteína será calculada automaticamente. Só é necessário oferecer a carga do ligante, essa será somada a carga do restante da região QM. Atenção: Somente calculamos a carga de aminoácidos da região QM (em breve outras biomoléculas)')
parser.add_argument('-pointCharge', type=str, help='Adicionar automaticamente os pontos de carga, por padrão eles serão adicionados para proteínas. Para desativar basta -pointCharge off')
parser.add_argument('-ff', type=str, help='Campo de força de referência para adicionar os pontos de carga, por padrão será utilizado o CHARMM (top_all36_prot) presente em app.forcefild. Somente compatível com FFs CHARMM. Em breve adicionaremos outras biomoléculas e outros FFs')
parser.add_argument('-cutoff', type=str, help='Adiciona apenas os pontos de cargas dentro do cutoff ao redor da região QM. Padrão: todos os pontos de carga serão adicionados. Ex.: -cutoff 20')
parser.add_argument('-pathQMSof', type=str, help='Caminho do programa QM que será adicionado ao arquivo de execução dos cálculos QM, esse também pode ser modificado no arquivo .sh presente no diretório com os sistemas')
parser.add_argument('-pathQMExec', type=str, help='Local de execução dos cálculos QM, esse também pode ser modificado no arquivo .sh presente no diretório com os sistemas')


args = parser.parse_args()
