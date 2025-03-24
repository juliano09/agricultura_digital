# Projeto de Agricultura Digital - FarmTech Solutions

Este projeto foi desenvolvido como parte do trabalho da disciplina de Programação para a FIAP.

## Visão Geral

O sistema de Agricultura Digital da FarmTech Solutions permite gerenciar culturas agrícolas, 
calculando áreas de plantio e os insumos necessários para cada cultura. O sistema suporta 
as seguintes operações:

- Cadastro de dados de plantio para culturas disponíveis
- Cálculo de área plantada baseado em figuras geométricas
- Cálculo de insumos necessários
- Visualização dos dados cadastrados
- Atualização e deleção de registros
- Exportação de dados para análise em R

## Culturas Suportadas

O sistema suporta 3 tipos de culturas:

1. **Milho** - Área calculada como um retângulo (Base × Altura)
2. **Feijão** - Área calculada como um triângulo ((Base × Altura) / 2)
3. **Mandioca** - Área calculada como um quadrado (Lado²)

## Estrutura do Projeto

```
fiap/agricultura_digital/
├── main.py                  # Programa principal em Python
├── analise_estatistica.R    # Script de análise estatística em R
├── dados_agricultura.csv    # Dados exportados (gerado automaticamente)
└── README.md                # Esta documentação
```

## Requisitos

### Python
- Python 3.6 ou superior
- Sistema operacional: Linux, macOS ou Windows

### R
- R 3.6 ou superior
- Pacotes: tidyverse

## Como Executar

### Instalação e Configuração

Para configurar o ambiente Python:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/macOS
```

### Executando o Programa Python

```bash
python3 main.py
```

### Executando a Análise em R

Após executar o programa Python e exportar os dados para CSV:

```bash
Rscript analise_estatistica.R
```

## Funcionalidades

### Entrada de Dados
- Seleção da cultura
- Entrada de dimensões para cálculo de área
- Cálculo automático de insumos necessários

### Visualização de Dados
- Lista todos os registros cadastrados
- Exibe detalhes de cada registro

### Atualização de Dados
- Permite modificar as dimensões de áreas já cadastradas
- Recalcula automaticamente área e insumos

### Deleção de Dados
- Remove registros do sistema
- Solicita confirmação antes de deletar

### Exportação de Dados
- Exporta todos os registros para um arquivo CSV
- Prepara os dados para análise estatística em R

## Análise Estatística (R)

O script em R realiza as seguintes análises:

1. **Análise Descritiva Básica**
   - Contagem de registros por cultura
   - Estatísticas de área (média, mediana, desvio padrão)
   - Estatísticas por cultura

2. **Análise de Insumos**
   - Total de cada insumo necessário
   - Quantidade média de insumos por hectare

3. **Análise de Irrigação**
   - Estatísticas de irrigação
   - Irrigação média por cultura

4. **Visualizações**
   - Gráfico de barras: Área por cultura
   - Gráfico de dispersão: Área vs Irrigação
   - Boxplot: Distribuição de áreas por cultura

## Exemplos de Uso

### Calculando Área e Insumos para Milho
1. Selecione a opção "1" no menu principal (Entrada de dados)
2. Escolha a cultura "Milho"
3. Informe a base e altura do retângulo (ex: 100m x 50m)
4. O sistema calculará automaticamente:
   - Área: 5000 m² (0.5 ha)
   - NPK necessário: 200 kg
   - Ureia necessária: 100 kg
   - Irrigação: 2.5 mm/dia

## Autores

Desenvolvido pelo grupo: Juliano, Daniel, Larrisa, Davi e Brenda da turma: 1TIAOB ( Turma B )

## Licença

Este projeto é aberto para fins educacionais.