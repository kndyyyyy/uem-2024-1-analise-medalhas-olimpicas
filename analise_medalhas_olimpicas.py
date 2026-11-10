'ARTHUR KENDY NISHIMUTA RA: 139099'
import sys
sys.setrecursionlimit(1500)

from enum import Enum

#Tipo Enumerado para os tipos de medalhas
class MedalType(Enum):

    OURO = 1
    PRATA = 2
    BRONZE = 3

from dataclasses import dataclass

@dataclass
#Tipo Estruturado com as informacoes relevantes dos atletas
class AthleteData:
    
    medal_code: MedalType
    country_code: str
    gender: str

@dataclass
#Tipo Estruturado com as informações de medalhas totais de cada pais
class CountryMedals:
### confusão aqui
    gold: MedalType
    silver: MedalType
    bronze: MedalType
    country: str

def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.
    Por exemplo, se o conteúdo do arquivo for
    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995
    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
            for i in range(1, len(linhas)):
                tabela.append(linhas[i].split(','))
            return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)

def reduz_matriz (tabela: list[list[str]]) -> list[AthleteData]:
    r'''
    Reduz a lista devolvida pela funcao *le_arquivo* com apenas as informações
    relevantes para o desenvolvimento.
    Exemplos:

    >>> tabela = [['Gold Medal', '1', '2024-07-27', 'Remco EVENEPOEL', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903136', 'BEL', 'Belgium', 'Belgium\n']]
    >>> reduz_matriz(tabela)
    [AthleteData(medal_code=1, country_code='BEL', gender='M')]

    >>> tabela = [['Gold Medal', '1', '2024-07-27', 'Remco EVENEPOEL', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903136', 'BEL', 'Belgium', 'Belgium\n'], ['Silver Medal', '2', '2024-07-27', 'Filippo GANNA', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1923520', 'ITA', 'Italy', 'Italy\n']]
    >>> reduz_matriz(tabela)
    [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M')]

    >>> tabela = [['Gold Medal', '1', '2024-07-27', 'Remco EVENEPOEL', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903136', 'BEL', 'Belgium', 'Belgium\n'], ['Silver Medal', '2', '2024-07-27', 'Filippo GANNA', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1923520', 'ITA', 'Italy', 'Italy\n'], ['Bronze Medal', '3', '2024-07-27', 'Wout van AERT', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903147', 'BEL', 'Belgium', 'Belgium\n']]
    >>> reduz_matriz(tabela)
    [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=3, country_code='BEL', gender='M')]
    
    >>> tabela = [['Gold Medal', '1', '2024-07-27', 'Remco EVENEPOEL', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903136', 'BEL', 'Belgium', 'Belgium\n'], ['Silver Medal', '2', '2024-07-27', 'Filippo GANNA', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1923520', 'ITA', 'Italy', 'Italy\n'], ['Bronze Medal', '3', '2024-07-27', 'Wout van AERT', 'M', 'Cycling Road', "Men's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/men-s-individual-time-trial/fnl-000100--', '1903147', 'BEL', 'Belgium', 'Belgium\n'], ['Gold Medal', '1', '2024-07-27', 'Grace BROWN', 'W', 'Cycling Road', "Women's Individual Time Trial", 'ATH', '/en/paris-2024/results/cycling-road/women-s-individual-time-trial/fnl-000100--', '1940173', 'AUS', 'Australia', 'Australia\n']]
    >>> reduz_matriz(tabela)
    [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=3, country_code='BEL', gender='M'), AthleteData(medal_code=1, country_code='AUS', gender='W')]
    '''
    lista_atletas = []
    for atleta in tabela:
        medal_code = int(atleta[1])
        country_code = atleta[10]
        gender = atleta[4]
        if medal_code == 1:
            medal_code = MedalType.OURO
        elif medal_code == 2:
            medal_code = MedalType.PRATA
        elif medal_code == 3:
            medal_code = MedalType.BRONZE
        lista_atletas.append(AthleteData(medal_code.value, country_code, gender))
    return lista_atletas

def lista_paises (lista_atletas: list[AthleteData]) -> list:
    '''
    função que recebe a lista reduzida com as informações relevantes e cria uma
    nova lista com todos os paises contemplados
    Exemplos:

    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M')]
    >>> lista_paises(lista_atletas)
    ['BEL']
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M')]
    >>> lista_paises(lista_atletas)
    ['BEL', 'ITA']
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=3, country_code='BEL', gender='M')]
    >>> lista_paises(lista_atletas)
    ['BEL', 'ITA', 'BEL']
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=3, country_code='BEL', gender='M'), AthleteData(medal_code=1, country_code='AUS', gender='W')]
    >>> lista_paises(lista_atletas)
    ['BEL', 'ITA', 'BEL', 'AUS']
    '''
    todos_paises = []
    for atleta in lista_atletas:
        pais = atleta.country_code
        todos_paises.append(pais)
    return todos_paises

def filtra_lista_paises (todos_paises: list) -> list:
    '''
    função que filtra a lista de países gerada pela função *lista_paises* para uma nova lista
    com apenas os países participantes da olimpíadas, sem nenhum repetido
    Exemplos:

    >>> todos_paises = ['BEL', 'BEL']
    >>> filtra_lista_paises(todos_paises)
    ['BEL']
    
    >>> todos_paises = ['BEL', 'BEL', 'ITA', 'ITA']
    >>> filtra_lista_paises(todos_paises)
    ['BEL', 'ITA']
    
    >>> todos_paises = ['BEL', 'BEL', 'ITA', 'ITA', 'AUS', 'AUS']
    >>> filtra_lista_paises(todos_paises)
    ['BEL', 'ITA', 'AUS']
    
    >>> todos_paises = ['BEL', 'BEL', 'ITA', 'ITA', 'AUS', 'AUS', 'BRA', 'BRA', 'BRA']
    >>> filtra_lista_paises(todos_paises)
    ['BEL', 'ITA', 'AUS', 'BRA']
    '''
    paises = []
    for pais in todos_paises:
        achou = False
        for pais_existe in paises:
            if pais == pais_existe:
                achou = True
        if achou == False:
            paises.append(pais)
    return paises

def conta_medalha (lista_atletas: list[AthleteData], paises: list) -> list[CountryMedals]:
    '''
    função que conta a quantia total de medalhas de ouro, prata, bronze de cada país, recebendo como parâmetro
    a *lista de atletas reduzida* e os *paises participantes das olimpíadas*
    Exemplos:
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M')]
    >>> paises = ['BEL']
    >>> conta_medalha(lista_atletas, paises)
    [CountryMedals(gold=1, silver=0, bronze=0, country='BEL')]
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M')]
    >>> paises = ['BEL', 'ITA']
    >>> conta_medalha(lista_atletas, paises)
    [CountryMedals(gold=1, silver=0, bronze=0, country='BEL'), CountryMedals(gold=0, silver=1, bronze=0, country='ITA')]
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=3, country_code='BEL', gender='M')]
    >>> paises = ['BEL', 'ITA']
    >>> conta_medalha(lista_atletas, paises)
    [CountryMedals(gold=1, silver=0, bronze=1, country='BEL'), CountryMedals(gold=0, silver=1, bronze=0, country='ITA')]
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=3, country_code='BEL', gender='M'), AthleteData(medal_code=1, country_code='AUS', gender='W')]
    >>> paises = ['BEL', 'ITA', 'AUS']
    >>> conta_medalha(lista_atletas, paises)
    [CountryMedals(gold=1, silver=0, bronze=1, country='BEL'), CountryMedals(gold=0, silver=1, bronze=0, country='ITA'), CountryMedals(gold=1, silver=0, bronze=0, country='AUS')]
    '''
    pais_medalhas = []
    for pais in paises:
        ouro = 0
        prata = 0
        bronze = 0
        for atleta in lista_atletas:
            if atleta.country_code == pais:
                if atleta.medal_code == 1:
                    ouro = ouro + 1
                elif atleta.medal_code == 2:
                    prata = prata + 1
                elif atleta.medal_code == 3:
                    bronze = bronze + 1
        pais_medalhas.append(CountryMedals(ouro, prata, bronze, pais))
    return pais_medalhas
                
def ordena_pais (pais_medalhas: list[CountryMedals]) -> list[CountryMedals]:
    '''
    função responsavel por organizar os paises por quantidade de medalha de ouro (maior prioridade), prata (media prioridade),
    bronze (baixa prioridade). Para que assim, caso haja empate entre medalhas de ouro por exemplo, o pais com mais medalhas de
    prata fique na frente do que tem menos.
    Exemplos:
    
    >>> pais_medalhas = [CountryMedals(gold=0, silver=1, bronze=0, country='ITA'), CountryMedals(gold=1, silver=0, bronze=0, country='BEL')]
    >>> ordena_pais(pais_medalhas)
    [CountryMedals(gold=1, silver=0, bronze=0, country='BEL'), CountryMedals(gold=0, silver=1, bronze=0, country='ITA')]
    
    >>> pais_medalhas = [CountryMedals(gold=0, silver=1, bronze=0, country='ITA'), CountryMedals(gold=1, silver=0, bronze=0, country='AUS'), CountryMedals(gold=2, silver=0, bronze=0, country='BEL')]
    >>> ordena_pais(pais_medalhas)
    [CountryMedals(gold=2, silver=0, bronze=0, country='BEL'), CountryMedals(gold=1, silver=0, bronze=0, country='AUS'), CountryMedals(gold=0, silver=1, bronze=0, country='ITA')]
    
    >>> pais_medalhas = [CountryMedals(gold=0, silver=1, bronze=0, country='ITA'), CountryMedals(gold=1, silver=0, bronze=0, country='BEL')]
    >>> ordena_pais(pais_medalhas)
    [CountryMedals(gold=1, silver=0, bronze=0, country='BEL'), CountryMedals(gold=0, silver=1, bronze=0, country='ITA')]
    
    >>> pais_medalhas = [CountryMedals(gold=2, silver=1, bronze=0, country='ITA'), CountryMedals(gold=2, silver=0, bronze=0, country='BEL')]
    >>> ordena_pais(pais_medalhas)
    [CountryMedals(gold=2, silver=1, bronze=0, country='ITA'), CountryMedals(gold=2, silver=0, bronze=0, country='BEL')]
    '''   
    for i in range(0, len(pais_medalhas)):
        for j in range(i+1, len(pais_medalhas)):
            if pais_medalhas[i].gold <= pais_medalhas[j].gold:
                pais_medalhas[i], pais_medalhas[j] = pais_medalhas[j], pais_medalhas[i]

    for i in range(0, len(pais_medalhas)):
        for j in range(i+1, len(pais_medalhas)):
            if pais_medalhas[i].gold == pais_medalhas[j].gold:
                if pais_medalhas[i].silver <= pais_medalhas[j].silver:
                    pais_medalhas[i], pais_medalhas[j] = pais_medalhas[j], pais_medalhas[i]
                    
    for i in range(0, len(pais_medalhas)):
        for j in range(i+1, len(pais_medalhas)):
            if pais_medalhas[i].gold == pais_medalhas[j].gold and pais_medalhas[i].silver == pais_medalhas[j].silver:
                    if pais_medalhas[i].bronze <= pais_medalhas[j].bronze:
                        pais_medalhas[i], pais_medalhas[j] = pais_medalhas[j], pais_medalhas[i]

    return pais_medalhas

def imprime_tabela (pais_medalhas: list[CountryMedals]):

    print("País" "   Ouro" "   Prata" "  Bronze" "  Total" )    
    for i in range(0, len(pais_medalhas)):
        total = str(pais_medalhas[i].gold + pais_medalhas[i].silver + pais_medalhas[i].bronze)
        gold = str(pais_medalhas[i].gold)
        silver = str(pais_medalhas[i].silver)
        bronze = str(pais_medalhas[i].bronze)
        pais = str(pais_medalhas[i].country)
        espaco = str(" " * 5)
        tabela_pais = pais + espaco + gold + espaco + silver + espaco + bronze + espaco + total

        print(tabela_pais)

def filtra_pais_atleta (lista_atletas: list[AthleteData], pais_sigla: str) -> list[AthleteData]:
    '''
    função que pega todos os atletas de determinado pais e retorna dentro de uma lista
    Exemplos:

    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='BEL', gender='M'), AthleteData(medal_code=1, country_code='ITA', gender='M')]
    >>> pais_sigla = 'BEL'
    >>> filtra_pais_atleta(lista_atletas, pais_sigla)
    [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='BEL', gender='M')]

    >>> lista_atletas = [AthleteData(medal_code=1, country_code='ITA', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=1, country_code='ITA', gender='M')]
    >>> pais_sigla = 'ITA'
    >>> filtra_pais_atleta(lista_atletas, pais_sigla)
    [AthleteData(medal_code=1, country_code='ITA', gender='M'), AthleteData(medal_code=2, country_code='ITA', gender='M'), AthleteData(medal_code=1, country_code='ITA', gender='M')]
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='AUS', gender='M'), AthleteData(medal_code=2, country_code='BEL', gender='M'), AthleteData(medal_code=1, country_code='ITA', gender='M')]
    >>> pais_sigla = 'AUS'
    >>> filtra_pais_atleta(lista_atletas, pais_sigla)
    [AthleteData(medal_code=1, country_code='AUS', gender='M')]

    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='BEL', gender='M'), AthleteData(medal_code=1, country_code='ITA', gender='M')]
    >>> pais_sigla = 'BRA'
    >>> filtra_pais_atleta(lista_atletas, pais_sigla)
    []
    '''
    atletas_certos = []
    if lista_atletas == []:
        return atletas_certos
    else:
        if lista_atletas[0].country_code == pais_sigla:
            atleta_pais = lista_atletas[0]
            atletas_certos.append(atleta_pais)
            atletas_certos = atletas_certos + filtra_pais_atleta(lista_atletas[1:], pais_sigla)
        else:
            atletas_certos = filtra_pais_atleta(lista_atletas[1:], pais_sigla)
    return atletas_certos

def filtra_genero_pais (lista_atletas: list[AthleteData], genero: str) -> list[AthleteData]:
    '''
    função que pega todos os atletas de um genero e retorna numa lista
    Exemplos:

    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='BEL', gender='W'), AthleteData(medal_code=1, country_code='ITA', gender='W')]
    >>> genero = 'W'
    >>> filtra_genero_pais(lista_atletas, genero)
    [AthleteData(medal_code=2, country_code='BEL', gender='W'), AthleteData(medal_code=1, country_code='ITA', gender='W')]
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BRA', gender='M'), AthleteData(medal_code=2, country_code='GER', gender='M'), AthleteData(medal_code=1, country_code='USA', gender='W')]
    >>> genero = 'M'
    >>> filtra_genero_pais(lista_atletas, genero)
    [AthleteData(medal_code=1, country_code='BRA', gender='M'), AthleteData(medal_code=2, country_code='GER', gender='M')]
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='TUN', gender='M'), AthleteData(medal_code=2, country_code='KOR', gender='M'), AthleteData(medal_code=1, country_code='USA', gender='W')]
    >>> genero = 'W'
    >>> filtra_genero_pais(lista_atletas, genero)
    [AthleteData(medal_code=1, country_code='USA', gender='W')]
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='TUN', gender='W'), AthleteData(medal_code=2, country_code='KOR', gender='W'), AthleteData(medal_code=1, country_code='USA', gender='W')]
    >>> genero = 'M'
    >>> filtra_genero_pais(lista_atletas, genero)
    []
    '''
    atletas_certos = []
    if lista_atletas == []:
        return atletas_certos
    else:
        if lista_atletas[0].gender == genero:
            atleta_pais = lista_atletas[0]
            atletas_certos.append(atleta_pais)
            atletas_certos = atletas_certos + filtra_genero_pais(lista_atletas[1:], genero)
        else:
            atletas_certos = filtra_genero_pais(lista_atletas[1:], genero)
    return atletas_certos

def retorna_pais_unico_genero (lista_atletas: list[AthleteData], paises: list[str]) -> list[str]:
    '''
    função que retorna uma lista de todos os paises que contemplam apenas um genero medalista
    Exemplos:
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='M'), AthleteData(medal_code=2, country_code='BEL', gender='W'), AthleteData(medal_code=1, country_code='ITA', gender='W')]
    >>> paises = ['BEL', 'ITA']
    >>> retorna_pais_unico_genero(lista_atletas, paises)
    ['ITA']
    
    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='W'), AthleteData(medal_code=2, country_code='BEL', gender='W'), AthleteData(medal_code=1, country_code='ITA', gender='W')]
    >>> paises = ['BEL', 'ITA']
    >>> retorna_pais_unico_genero(lista_atletas, paises)
    ['BEL', 'ITA']

    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='W'), AthleteData(medal_code=2, country_code='BRA', gender='W'), AthleteData(medal_code=1, country_code='ITA', gender='W')]
    >>> paises = ['BEL', 'ITA', 'BRA']
    >>> retorna_pais_unico_genero(lista_atletas, paises)
    ['BEL', 'ITA', 'BRA']

    >>> lista_atletas = [AthleteData(medal_code=1, country_code='BEL', gender='W'), AthleteData(medal_code=2, country_code='BEL', gender='M'), AthleteData(medal_code=1, country_code='ITA', gender='W'), AthleteData(medal_code=1, country_code='ITA', gender='M')]
    >>> paises = ['BEL', 'ITA']
    >>> retorna_pais_unico_genero(lista_atletas, paises)
    []
    '''
    paises_unico_genero = []
    if paises == []:
        return paises_unico_genero
    
    atletas_pais = filtra_pais_atleta(lista_atletas, paises[0])
    atletas_genero_m = filtra_genero_pais(atletas_pais, 'M') 
    atletas_genero_w = filtra_genero_pais(atletas_pais, 'W')
    
    if atletas_genero_m == []:
        pais_codigo = paises[0]
        paises_unico_genero.append(pais_codigo)
        paises_unico_genero = paises_unico_genero + retorna_pais_unico_genero(lista_atletas, paises[1:])

    elif atletas_genero_w == []:
        pais_codigo = paises[0]
        paises_unico_genero.append(pais_codigo)
        paises_unico_genero = paises_unico_genero + retorna_pais_unico_genero(lista_atletas, paises[1:])
    else:
        paises_unico_genero = retorna_pais_unico_genero(lista_atletas, paises[1:])
    
    return paises_unico_genero

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])

    tabela_reduzida = reduz_matriz(tabela)

    paises = lista_paises(tabela_reduzida)

    paises_org = filtra_lista_paises(paises)

    infos = conta_medalha(tabela_reduzida, paises_org)

    impressao = ordena_pais(infos)

    #atletas_por_pais = filtra_pais_atleta(tabela_reduzida, "GEO")

    #genero_por_pais = filtra_genero_pais(atletas_por_pais_filtrados, "M")

    paises_um_genero = retorna_pais_unico_genero(tabela_reduzida, paises_org)

    imprime_tabela(impressao)

    print("Estes são os países que contemplam apenas um gênero como medalistas:")
    print(paises_um_genero)

    # linha 471 estava vazio o cod da medalha
    # a partir da linha 1037 os numeros do cod da medalha do csv estavam como float.
    # renomeei as modalidades que haviam virgula no nome. EX:
    # Women's 10,000m para Women's 10.000m

    # print(len(linhas[i].split(',')), i) 47
    # count = count + 1
    # print(atleta[1], count)

    # TODO: computar e exibir o quadro de medalhas
    "OK" 
    # TODO: computar e exibir os países que tiverem apenas
    # atletas de um único gênero premiados
    "OK"

if __name__ == '__main__':
    main()