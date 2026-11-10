# Análise de Medalhas Olímpicas (Paris 2024)

Trabalho da disciplina **Fundamentos de Algoritmos** da Universidade Estadual de Maringá (UEM).

## Descrição

O programa lê um arquivo CSV com os dados das medalhas das Olimpíadas de Paris 2024 e gera:

1. O **quadro de classificação de medalhas** por país, com a quantidade de ouros, pratas, bronzes e o total. A ordenação considera ouro, depois prata e depois bronze.
2. A lista de **países que tiveram atletas de apenas um gênero** premiados (ignorando os gêneros `X` e `O`).

O trabalho utiliza listas de listas, tipos estruturados (`dataclass`), funções com passagem de parâmetros por referência e funções recursivas.

## Arquivos

- `analise_medalhas_olimpicas.py` - código-fonte do programa.
- `medals.csv` - base de dados (não inclusa no repositório).

A base de dados pode ser obtida em:
<https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games>

## Como executar

É necessário ter o Python 3.9 ou superior instalado.

No terminal do VS Code, execute:

```bash
python analise_medalhas_olimpicas.py medals.csv
```

O arquivo `medals.csv` deve estar na mesma pasta do script (ou informe o caminho completo dele).
