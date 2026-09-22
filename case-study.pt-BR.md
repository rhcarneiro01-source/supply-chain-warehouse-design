# Estudo de Caso — Otimização de Layout de Armazém

## 1. Contexto

O desempenho de um armazém é fortemente influenciado pelo layout físico. Posicionamento do estoque, giro dos produtos, organização dos corredores e sequência das áreas operacionais afetam diretamente deslocamentos, produtividade do picking, segurança e tempo de processamento dos pedidos.

Este case parte de um princípio simples: **quanto maior o giro do item, mais próximo ele deve ficar das áreas que o movimentam com maior frequência**.

## 2. Objetivo

Criar um layout conceitual capaz de melhorar o fluxo desde o recebimento até a expedição, mantendo uma operação compreensível, escalável e compatível com tecnologias comuns de armazenagem.

## 3. Estratégia do layout

### Recebimento
Entrada de mercadorias por docas dedicadas, com descarga, conferência, identificação e registro no sistema.

### Armazenamento lento
Produtos de menor giro ficam em posições mais distantes do picking e expedição, preservando áreas nobres para itens de maior movimentação.

### Armazenamento principal
Produtos de médio giro ocupam a região central, equilibrando capacidade e acessibilidade.

### Movimentação rápida
Itens de alto giro ficam próximos ao picking e expedição para reduzir deslocamentos e tempo de reposição.

### Picking / Preparação
Área dedicada à separação e staging dos pedidos antes da embalagem.

### Embalagem
Padronização, proteção e preparação dos pedidos.

### Classificação
Organização por rota, destino ou transportadora.

### Expedição
Conferência final e carregamento próximos da classificação, evitando movimentações de retorno.

## 4. Filosofia de fluxo

O layout prioriza um fluxo predominantemente unidirecional, reduzindo cruzamentos entre operações de entrada e saída e melhorando segurança e visibilidade operacional.

## 5. Preparação tecnológica

O conceito é compatível com:

- WMS (Warehouse Management System)
- Código de barras
- RFID
- Endereçamento de posições
- Picking por zonas
- Instruções digitais de trabalho
- Dashboards operacionais

## 6. KPIs para validação

Uma implantação real deveria avaliar o redesenho por indicadores como:

- tempo de picking por pedido;
- distância percorrida por pedido;
- linhas separadas por hora;
- pedidos processados por hora;
- acuracidade de pedidos;
- dock-to-stock;
- tempo de ciclo em doca;
- acuracidade de estoque;
- utilização do espaço;
- incidentes e quase-acidentes.

## 7. Limitações

Este é um projeto conceitual e não um desenho executivo de engenharia. Uma aplicação real exigiria dimensões detalhadas, perfil de SKUs, histórico de demanda, frequência de pedidos, posições-palete, raio de giro dos equipamentos, requisitos de segurança contra incêndio, restrições de mão de obra e simulação dos fluxos.

## 8. Próximas evoluções

1. Classificação ABC/XYZ;
2. Modelo de slotting de SKUs;
3. Simulação de distância percorrida;
4. Cálculo de capacidade por posição-palete;
5. Simulação de eventos discretos;
6. Dashboard em Power BI ou aplicação web;
7. Mapeamento de processos WMS;
8. Estudo de custo-benefício e ROI.
