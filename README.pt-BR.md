# Projeto de Layout de Armazém — Supply Chain

**Case de layout e fluxo operacional de armazém com foco em produtividade, segurança, giro de estoque e escalabilidade.**

[English version](README.md)

![Layout do armazém](assets/warehouse-layout.png)

## Visão geral

Este projeto de portfólio apresenta um layout conceitual de armazém organizado de acordo com a velocidade de movimentação dos produtos e com um fluxo claro desde o recebimento até a expedição. O desenho separa itens de baixo, médio e alto giro, aproxima os produtos de maior movimentação das áreas de picking e expedição e cria áreas específicas para preparação, embalagem e classificação.

O repositório também contém uma **análise de KPIs com dados sintéticos**, criada para demonstrar como o desempenho do layout poderia ser validado por dados. Nenhuma informação confidencial ou de empresa real foi utilizada.

## Problema de negócio

Layouts tradicionais podem gerar deslocamentos excessivos, cruzamento de fluxos, gargalos de picking e uso pouco eficiente do espaço. O projeto propõe uma estrutura que busca:

- reduzir a distância de movimentação interna;
- aumentar a produtividade do picking;
- separar fluxos de entrada e saída;
- organizar estoques conforme o giro dos produtos;
- melhorar a segurança operacional;
- permitir expansão futura;
- preparar a operação para uso de WMS e rastreabilidade.

## Fluxo proposto

```text
Recebimento
   ↓
Armazenagem (lento / principal)
   ↓
Movimentação rápida
   ↓
Picking / Preparação
   ↓
Embalagem
   ↓
Classificação
   ↓
Expedição
```

## Principais áreas

| Área | Objetivo |
|---|---|
| Recebimento | Conferência, identificação e registro no sistema |
| Armazenamento lento | Itens de menor giro em posições mais distantes |
| Armazenamento principal | Produtos de médio giro com boa acessibilidade |
| Movimentação rápida | Itens de alto giro próximos ao picking e expedição |
| Picking / Preparação | Separação e staging dos pedidos |
| Embalagem | Padronização e proteção dos pedidos |
| Classificação | Organização final por rota, destino ou transportadora |
| Expedição | Conferência final, carregamento e saída |
| Docas | Interface entre transporte e operação interna |

## Princípios aplicados

- Slotting baseado em giro de estoque
- Lógica de armazenamento orientada por classificação ABC
- Fluxo unidirecional de materiais
- Redução de cruzamentos de fluxo
- Menor distância de picking
- Áreas dedicadas de staging e packing
- Circulação segura de empilhadeiras e operadores
- Possibilidade de expansão modular
- Preparação para WMS, código de barras e RFID

## Benefícios esperados

- Menor tempo de deslocamento
- Maior produtividade na separação de pedidos
- Maior acuracidade dos pedidos
- Menos congestionamento e cruzamento de fluxos
- Melhor aproveitamento da área
- Maior segurança operacional
- Processos mais padronizados
- Maior escalabilidade

## Extensão analítica

A pasta [`analysis/`](analysis/) apresenta um cenário sintético comparando uma situação de referência com o layout proposto. Os indicadores demonstrados são:

- tempo médio de picking;
- distância interna percorrida;
- pedidos processados por hora;
- acuracidade dos pedidos;
- tempo de ciclo em doca.

Execute com:

```bash
python analysis/analyze_kpis.py
```

Não é necessário instalar bibliotecas externas.

## Estrutura do repositório

```text
supply-chain-warehouse-design/
├── README.md
├── README.pt-BR.md
├── LICENSE
├── .gitignore
├── assets/
│   ├── warehouse-layout.png
│   └── project-overview.png
├── docs/
│   ├── case-study.md
│   └── case-study.pt-BR.md
└── analysis/
    ├── README.md
    ├── synthetic_kpis.csv
    └── analyze_kpis.py
```

## Competências demonstradas

`Supply Chain Management` · `Warehouse Design` · `Gestão de Estoques` · `Otimização de Picking` · `Melhoria de Processos` · `Análise Operacional` · `KPIs` · `Python` · `Resolução de Problemas`

## Nota de portfólio

Este repositório é uma adaptação independente para portfólio de um projeto de aprendizagem sobre layout de armazém. A base de KPIs é totalmente sintética e serve apenas para demonstração analítica. Não há dados confidenciais de qualquer empresa.

## Autor

**Renan Henrique Carneiro**  
Ciência de Dados · Supply Chain Analytics · Python · SQL · Inteligência Artificial · Engenharia de Software
