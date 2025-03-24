# Análise Estatística (Versão Simplificada) - Projeto Agricultura Digital
# FarmTech Solutions - Usando apenas R base (sem tidyverse)

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
  
  # Função para calcular estatísticas por grupo
  estatisticas_por_grupo <- function(dados, grupo) {
    culturas_unicas <- unique(dados[[grupo]])
    resultado <- data.frame(
      cultura = character(),
      media_area_ha = numeric(),
      mediana_area_ha = numeric(),
      min_area_ha = numeric(),
      max_area_ha = numeric(), 
      desvio_padrao = numeric(),
      total_area_ha = numeric(),
      stringsAsFactors = FALSE
    )
    
    for (cultura in culturas_unicas) {
      subset_dados <- dados[dados[[grupo]] == cultura, ]
      
      row <- data.frame(
        cultura = cultura,
        media_area_ha = mean(subset_dados$area_ha),
        mediana_area_ha = median(subset_dados$area_ha),
        min_area_ha = min(subset_dados$area_ha),
        max_area_ha = max(subset_dados$area_ha),
        desvio_padrao = sd(subset_dados$area_ha),
        total_area_ha = sum(subset_dados$area_ha),
        stringsAsFactors = FALSE
      )
      
      resultado <- rbind(resultado, row)
    }
    
    return(resultado)
  }
  
  por_cultura <- estatisticas_por_grupo(dados, "cultura")
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
  totais_insumos <- sapply(dados[, colunas_insumos], sum)
  
  for (i in 1:length(colunas_insumos)) {
    insumo <- colunas_insumos[i]
    cat(insumo, ":", totais_insumos[i], "kg\n")
  }
  
  # Insumos por hectare (média)
  cat("\n2. Quantidade média de insumos por hectare:\n")
  
  total_area <- sum(dados$area_ha)
  
  for (i in 1:length(colunas_insumos)) {
    insumo <- colunas_insumos[i]
    if (total_area > 0) {
      media_por_ha <- totais_insumos[i] / total_area
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
  
  culturas_unicas <- unique(dados$cultura)
  irrigacao_cultura <- data.frame(
    cultura = character(),
    media_irrigacao = numeric(),
    total_irrigacao = numeric(),
    area_total_ha = numeric(),
    irrigacao_por_ha = numeric(),
    stringsAsFactors = FALSE
  )
  
  for (cultura in culturas_unicas) {
    subset_dados <- dados[dados$cultura == cultura, ]
    
    row <- data.frame(
      cultura = cultura,
      media_irrigacao = mean(subset_dados$irrigacao),
      total_irrigacao = sum(subset_dados$irrigacao),
      area_total_ha = sum(subset_dados$area_ha),
      irrigacao_por_ha = sum(subset_dados$irrigacao) / sum(subset_dados$area_ha),
      stringsAsFactors = FALSE
    )
    
    irrigacao_cultura <- rbind(irrigacao_cultura, row)
  }
  
  print(irrigacao_cultura)
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
    
    cat("\nAnálise estatística concluída com sucesso!\n")
    
  }, error = function(e) {
    cat("\nErro durante a análise:", e$message, "\n")
  })
}

# Executar o programa
main()