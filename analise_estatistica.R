# Análise Estatística - Projeto Agricultura Digital
# FarmTech Solutions

# Carregar pacotes necessários
if (!require("tidyverse")) install.packages("tidyverse")
library(tidyverse)

# Funções auxiliares para exibição de resultados
imprimir_separador <- function() {
  cat("\n", rep("-", 50), "\n", sep="")
}

# Carregar os dados do CSV gerado pelo Python
carregar_dados <- function() {
  cat("\nCarregando dados de agricultura digital...\n")
  
  # Verificar se o arquivo existe
  if (!file.exists("dados_agricultura.csv")) {
    stop("Arquivo 'dados_agricultura.csv' não encontrado. Execute o programa Python primeiro.")
  }
  
  # Carregar dados
  dados <- read.csv("dados_agricultura.csv", header = TRUE, stringsAsFactors = FALSE)
  
  cat("Dados carregados com sucesso!\n")
  imprimir_separador()
  
  return(dados)
}

# Análise descritiva básica
analise_descritiva <- function(dados) {
  cat("\nANÁLISE DESCRITIVA BÁSICA\n")
  imprimir_separador()
  
  # Número de registros por cultura
  cat("\n1. Número de registros por cultura:\n")
  print(table(dados$cultura))
  
  # Estatísticas da área
  cat("\n2. Estatísticas da área (em hectares):\n")
  resumo_area <- summary(dados$area_ha)
  print(resumo_area)
  cat("\nDesvio padrão:", sd(dados$area_ha), "\n")
  
  # Estatísticas por cultura
  cat("\n3. Estatísticas da área por cultura:\n")
  por_cultura <- dados %>%
    group_by(cultura) %>%
    summarise(
      media_area_ha = mean(area_ha),
      mediana_area_ha = median(area_ha),
      min_area_ha = min(area_ha),
      max_area_ha = max(area_ha),
      desvio_padrao = sd(area_ha),
      total_area_ha = sum(area_ha)
    )
  
  print(por_cultura)
  imprimir_separador()
}

# Análise de insumos
analise_insumos <- function(dados) {
  cat("\nANÁLISE DE INSUMOS\n")
  imprimir_separador()
  
  # Identificar colunas de insumos (exceto as colunas conhecidas)
  colunas_conhecidas <- c("id", "cultura", "area_m2", "area_ha", "irrigacao")
  colunas_insumos <- setdiff(names(dados), colunas_conhecidas)
  
  # Total de insumos
  cat("\n1. Total de cada insumo necessário:\n")
  totais_insumos <- dados %>%
    summarise(across(all_of(colunas_insumos), sum))
  
  for (insumo in colunas_insumos) {
    cat(insumo, ":", totais_insumos[[insumo]], "kg\n")
  }
  
  # Insumos por hectare (média)
  cat("\n2. Quantidade média de insumos por hectare:\n")
  
  total_area <- sum(dados$area_ha)
  
  for (insumo in colunas_insumos) {
    if (total_area > 0) {
      media_por_ha <- totais_insumos[[insumo]] / total_area
      cat(insumo, ":", round(media_por_ha, 2), "kg/ha\n")
    }
  }
  
  imprimir_separador()
}

# Análise de irrigação
analise_irrigacao <- function(dados) {
  cat("\nANÁLISE DE IRRIGAÇÃO\n")
  imprimir_separador()
  
  # Estatísticas de irrigação
  cat("\n1. Estatísticas de irrigação (mm/dia):\n")
  resumo_irrigacao <- summary(dados$irrigacao)
  print(resumo_irrigacao)
  cat("\nDesvio padrão:", sd(dados$irrigacao), "\n")
  
  # Irrigação por cultura
  cat("\n2. Irrigação média por cultura:\n")
  irrigacao_cultura <- dados %>%
    group_by(cultura) %>%
    summarise(
      media_irrigacao = mean(irrigacao),
      total_irrigacao = sum(irrigacao),
      area_total_ha = sum(area_ha),
      irrigacao_por_ha = sum(irrigacao) / sum(area_ha)
    )
  
  print(irrigacao_cultura)
  imprimir_separador()
}

# Visualizações
criar_visualizacoes <- function(dados) {
  cat("\nCRIANDO VISUALIZAÇÕES\n")
  imprimir_separador()
  
  cat("\nAs visualizações foram salvas na pasta atual:\n")
  
  # 1. Gráfico de barras - Área por cultura
  p1 <- ggplot(dados, aes(x = cultura, y = area_ha, fill = cultura)) +
    geom_bar(stat = "identity") +
    theme_minimal() +
    labs(title = "Área Total por Cultura (ha)",
         x = "Cultura",
         y = "Área (hectares)")
  
  # Salvar o gráfico
  ggsave("area_por_cultura.png", p1, width = 8, height = 6)
  cat("- area_por_cultura.png\n")
  
  # 2. Gráfico de dispersão - Área vs Irrigação
  p2 <- ggplot(dados, aes(x = area_ha, y = irrigacao, color = cultura)) +
    geom_point(size = 3) +
    theme_minimal() +
    labs(title = "Relação entre Área e Irrigação",
         x = "Área (hectares)",
         y = "Irrigação (mm/dia)")
  
  # Salvar o gráfico
  ggsave("area_vs_irrigacao.png", p2, width = 8, height = 6)
  cat("- area_vs_irrigacao.png\n")
  
  # 3. Boxplot - Distribuição de áreas por cultura
  p3 <- ggplot(dados, aes(x = cultura, y = area_ha, fill = cultura)) +
    geom_boxplot() +
    theme_minimal() +
    labs(title = "Distribuição de Áreas por Cultura",
         x = "Cultura",
         y = "Área (hectares)")
  
  # Salvar o gráfico
  ggsave("distribuicao_areas.png", p3, width = 8, height = 6)
  cat("- distribuicao_areas.png\n")
  
  imprimir_separador()
}

# Função principal
main <- function() {
  cat("\n", rep("=", 60), "\n", sep="")
  cat("    ANÁLISE ESTATÍSTICA - PROJETO AGRICULTURA DIGITAL\n")
  cat("             FarmTech Solutions\n")
  cat(rep("=", 60), "\n", sep="")
  
  # Carregar dados
  tryCatch({
    dados <- carregar_dados()
    
    # Realizar análises
    analise_descritiva(dados)
    analise_insumos(dados)
    analise_irrigacao(dados)
    
    # Criar visualizações
    criar_visualizacoes(dados)
    
    cat("\nAnálise estatística concluída com sucesso!\n")
    
  }, error = function(e) {
    cat("\nErro durante a análise:", e$message, "\n")
  })
}

# Executar o programa
main()