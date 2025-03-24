#!/usr/bin/env python3
"""
Projeto de Agricultura Digital - FarmTech Solutions
Programa principal com menu de opções para gerenciamento de culturas agrícolas.
"""

import os
import sys
from collections import defaultdict

# Definição das culturas
CULTURAS = {
    'Milho': {
        'figura': 'Retângulo',
        'formula': 'Base × Altura',
        'insumos': {
            'NPK': {'quantidade': 400, 'unidade': 'kg/ha'},
            'Ureia': {'quantidade': 200, 'unidade': 'kg/ha'},
        },
        'irrigacao': {'quantidade': 5, 'unidade': 'mm/dia'},
        'equipamentos': ['Trator com semeadora/adubadora', 'Pulverizador', 'Colheitadeira']
    },
    'Feijão': {
        'figura': 'Triângulo',
        'formula': '(Base × Altura) / 2',
        'insumos': {
            'NPK': {'quantidade': 300, 'unidade': 'kg/ha'},
            'Sulfato de Amônio': {'quantidade': 150, 'unidade': 'kg/ha'},
        },
        'irrigacao': {'quantidade': 4, 'unidade': 'mm/dia'},
        'equipamentos': ['Trator com semeadora', 'Pulverizador costal', 'Colheita manual/mecânica']
    },
    'Mandioca': {
        'figura': 'Quadrado',
        'formula': 'Lado²',
        'insumos': {
            'NPK': {'quantidade': 250, 'unidade': 'kg/ha'},
            'Calcário': {'quantidade': 100, 'unidade': 'kg/ha'},
        },
        'irrigacao': {'quantidade': 2, 'unidade': 'mm/dia'},
        'equipamentos': ['Enxada rotativa', 'Trator com plantadora', 'Facões para colheita']
    }
}

# Vetor para armazenar os registros
registros = []

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter():
    """Aguarda o usuário pressionar ENTER para continuar."""
    input("\nPressione ENTER para continuar...")

def calcular_area(cultura, **params):
    """Calcula a área plantada de acordo com a figura geométrica."""
    if CULTURAS[cultura]['figura'] == 'Retângulo':
        return params['base'] * params['altura']
    elif CULTURAS[cultura]['figura'] == 'Triângulo':
        return (params['base'] * params['altura']) / 2
    elif CULTURAS[cultura]['figura'] == 'Quadrado':
        return params['lado'] ** 2
    return 0

def calcular_insumos(cultura, area_ha):
    """Calcula a quantidade de insumos necessários para a área."""
    resultado = {}
    for insumo, info in CULTURAS[cultura]['insumos'].items():
        resultado[insumo] = info['quantidade'] * area_ha
    return resultado

def entrada_dados():
    """Função para entrada de novos dados."""
    limpar_tela()
    print("\n" + "=" * 50)
    print("        ENTRADA DE DADOS")
    print("=" * 50)
    
    # Exibir culturas disponíveis
    print("\nCulturas disponíveis:")
    for i, cultura in enumerate(CULTURAS.keys(), 1):
        print(f"{i}. {cultura}")
    
    # Selecionar cultura
    try:
        opcao = int(input("\nSelecione a cultura (número): "))
        if opcao < 1 or opcao > len(CULTURAS):
            print("\nOpção inválida!")
            esperar_enter()
            return
        
        cultura_selecionada = list(CULTURAS.keys())[opcao-1]
    except ValueError:
        print("\nOpção inválida! Digite um número.")
        esperar_enter()
        return
    
    # Dados da figura geométrica
    print(f"\nÁrea de plantio ({CULTURAS[cultura_selecionada]['figura']}):")
    
    params = {}
    area = 0
    
    if CULTURAS[cultura_selecionada]['figura'] == 'Retângulo':
        try:
            params['base'] = float(input("Base (m): "))
            params['altura'] = float(input("Altura (m): "))
            area = calcular_area(cultura_selecionada, **params)
        except ValueError:
            print("\nValores inválidos! Use números.")
            esperar_enter()
            return
            
    elif CULTURAS[cultura_selecionada]['figura'] == 'Triângulo':
        try:
            params['base'] = float(input("Base (m): "))
            params['altura'] = float(input("Altura (m): "))
            area = calcular_area(cultura_selecionada, **params)
        except ValueError:
            print("\nValores inválidos! Use números.")
            esperar_enter()
            return
            
    elif CULTURAS[cultura_selecionada]['figura'] == 'Quadrado':
        try:
            params['lado'] = float(input("Lado (m): "))
            area = calcular_area(cultura_selecionada, **params)
        except ValueError:
            print("\nValor inválido! Use números.")
            esperar_enter()
            return
    
    # Converter área para hectares (1 ha = 10.000 m²)
    area_ha = area / 10000
    
    # Calcular insumos necessários
    insumos = calcular_insumos(cultura_selecionada, area_ha)
    
    # Adicionar registro ao vetor
    registro = {
        'id': len(registros) + 1,
        'cultura': cultura_selecionada,
        'parametros': params,
        'area_m2': area,
        'area_ha': area_ha,
        'insumos': insumos,
        'irrigacao': CULTURAS[cultura_selecionada]['irrigacao']['quantidade'] * area_ha
    }
    
    registros.append(registro)
    
    # Exibir resumo do registro
    print("\n" + "-" * 50)
    print(f"Registro #{registro['id']} - {registro['cultura']}")
    print(f"Área: {registro['area_m2']:.2f} m² ({registro['area_ha']:.4f} ha)")
    print("\nInsumos necessários:")
    for insumo, quantidade in registro['insumos'].items():
        unidade = CULTURAS[cultura_selecionada]['insumos'][insumo]['unidade'].replace('ha', 'total')
        print(f"- {insumo}: {quantidade:.2f} {unidade}")
    
    print(f"\nIrrigação: {registro['irrigacao']:.2f} mm/dia")
    print("-" * 50)
    
    esperar_enter()

def visualizar_dados():
    """Função para visualizar os dados armazenados."""
    limpar_tela()
    print("\n" + "=" * 50)
    print("        VISUALIZAÇÃO DE DADOS")
    print("=" * 50)
    
    if not registros:
        print("\nNenhum registro encontrado!")
        esperar_enter()
        return
    
    print(f"\nTotal de registros: {len(registros)}")
    
    for registro in registros:
        print("\n" + "-" * 50)
        print(f"Registro #{registro['id']} - {registro['cultura']}")
        
        # Exibir detalhes da figura
        if CULTURAS[registro['cultura']]['figura'] == 'Retângulo':
            print(f"Retângulo: Base = {registro['parametros']['base']}m, Altura = {registro['parametros']['altura']}m")
        elif CULTURAS[registro['cultura']]['figura'] == 'Triângulo':
            print(f"Triângulo: Base = {registro['parametros']['base']}m, Altura = {registro['parametros']['altura']}m")
        elif CULTURAS[registro['cultura']]['figura'] == 'Quadrado':
            print(f"Quadrado: Lado = {registro['parametros']['lado']}m")
        
        print(f"Área: {registro['area_m2']:.2f} m² ({registro['area_ha']:.4f} ha)")
        
        # Exibir insumos
        print("\nInsumos necessários:")
        for insumo, quantidade in registro['insumos'].items():
            unidade = CULTURAS[registro['cultura']]['insumos'][insumo]['unidade'].replace('ha', 'total')
            print(f"- {insumo}: {quantidade:.2f} {unidade}")
        
        print(f"\nIrrigação: {registro['irrigacao']:.2f} mm/dia")
        print("-" * 50)
    
    esperar_enter()

def atualizar_dados():
    """Função para atualizar um registro existente."""
    limpar_tela()
    print("\n" + "=" * 50)
    print("        ATUALIZAÇÃO DE DADOS")
    print("=" * 50)
    
    if not registros:
        print("\nNenhum registro encontrado!")
        esperar_enter()
        return
    
    # Listar registros para escolha
    print("\nRegistros disponíveis:")
    for registro in registros:
        print(f"{registro['id']}. {registro['cultura']} - {registro['area_m2']:.2f} m²")
    
    # Selecionar registro
    try:
        id_registro = int(input("\nDigite o ID do registro a atualizar: "))
        registro_idx = next((i for i, r in enumerate(registros) if r['id'] == id_registro), None)
        
        if registro_idx is None:
            print("\nRegistro não encontrado!")
            esperar_enter()
            return
        
    except ValueError:
        print("\nID inválido! Digite um número.")
        esperar_enter()
        return
    
    # Exibir dados atuais
    registro = registros[registro_idx]
    print("\nDados atuais:")
    print(f"Cultura: {registro['cultura']}")
    
    if CULTURAS[registro['cultura']]['figura'] == 'Retângulo':
        print(f"Base: {registro['parametros']['base']}m, Altura: {registro['parametros']['altura']}m")
    elif CULTURAS[registro['cultura']]['figura'] == 'Triângulo':
        print(f"Base: {registro['parametros']['base']}m, Altura: {registro['parametros']['altura']}m")
    elif CULTURAS[registro['cultura']]['figura'] == 'Quadrado':
        print(f"Lado: {registro['parametros']['lado']}m")
    
    # Atualizar dados
    print("\nDigite os novos valores (deixe em branco para manter o valor atual):")
    
    params = registro['parametros'].copy()
    
    if CULTURAS[registro['cultura']]['figura'] == 'Retângulo':
        base_input = input(f"Base (atual: {params['base']}m): ")
        if base_input:
            try:
                params['base'] = float(base_input)
            except ValueError:
                print("\nValor inválido! Mantendo o valor atual.")
        
        altura_input = input(f"Altura (atual: {params['altura']}m): ")
        if altura_input:
            try:
                params['altura'] = float(altura_input)
            except ValueError:
                print("\nValor inválido! Mantendo o valor atual.")
                
    elif CULTURAS[registro['cultura']]['figura'] == 'Triângulo':
        base_input = input(f"Base (atual: {params['base']}m): ")
        if base_input:
            try:
                params['base'] = float(base_input)
            except ValueError:
                print("\nValor inválido! Mantendo o valor atual.")
        
        altura_input = input(f"Altura (atual: {params['altura']}m): ")
        if altura_input:
            try:
                params['altura'] = float(altura_input)
            except ValueError:
                print("\nValor inválido! Mantendo o valor atual.")
                
    elif CULTURAS[registro['cultura']]['figura'] == 'Quadrado':
        lado_input = input(f"Lado (atual: {params['lado']}m): ")
        if lado_input:
            try:
                params['lado'] = float(lado_input)
            except ValueError:
                print("\nValor inválido! Mantendo o valor atual.")
    
    # Recalcular área e insumos
    area = calcular_area(registro['cultura'], **params)
    area_ha = area / 10000
    insumos = calcular_insumos(registro['cultura'], area_ha)
    
    # Atualizar registro
    registros[registro_idx] = {
        'id': registro['id'],
        'cultura': registro['cultura'],
        'parametros': params,
        'area_m2': area,
        'area_ha': area_ha,
        'insumos': insumos,
        'irrigacao': CULTURAS[registro['cultura']]['irrigacao']['quantidade'] * area_ha
    }
    
    # Exibir dados atualizados
    print("\n" + "-" * 50)
    print("Registro atualizado com sucesso!")
    print(f"Nova área: {area:.2f} m² ({area_ha:.4f} ha)")
    print("-" * 50)
    
    esperar_enter()

def deletar_dados():
    """Função para deletar um registro."""
    limpar_tela()
    print("\n" + "=" * 50)
    print("        DELEÇÃO DE DADOS")
    print("=" * 50)
    
    if not registros:
        print("\nNenhum registro encontrado!")
        esperar_enter()
        return
    
    # Listar registros para escolha
    print("\nRegistros disponíveis:")
    for registro in registros:
        print(f"{registro['id']}. {registro['cultura']} - {registro['area_m2']:.2f} m²")
    
    # Selecionar registro
    try:
        id_registro = int(input("\nDigite o ID do registro a deletar: "))
        registro_idx = next((i for i, r in enumerate(registros) if r['id'] == id_registro), None)
        
        if registro_idx is None:
            print("\nRegistro não encontrado!")
            esperar_enter()
            return
        
    except ValueError:
        print("\nID inválido! Digite um número.")
        esperar_enter()
        return
    
    # Confirmar deleção
    confirma = input(f"\nConfirma a deleção do registro #{id_registro}? (S/N): ").strip().upper()
    
    if confirma == 'S':
        del registros[registro_idx]
        print("\nRegistro deletado com sucesso!")
    else:
        print("\nOperação cancelada.")
    
    esperar_enter()

def exportar_dados():
    """Função para exportar dados para um arquivo CSV (para uso posterior no R)."""
    if not registros:
        print("\nNenhum registro para exportar!")
        esperar_enter()
        return
    
    try:
        with open('dados_agricultura.csv', 'w') as arquivo:
            # Cabeçalho
            arquivo.write("id,cultura,area_m2,area_ha,")
            # Adicionar todos os insumos possíveis
            todos_insumos = set()
            for cultura in CULTURAS.values():
                for insumo in cultura['insumos'].keys():
                    todos_insumos.add(insumo)
            
            arquivo.write(",".join(todos_insumos))
            arquivo.write(",irrigacao\n")
            
            # Dados
            for registro in registros:
                linha = f"{registro['id']},{registro['cultura']},{registro['area_m2']},{registro['area_ha']},"
                
                # Adicionar valores dos insumos
                valores_insumos = []
                for insumo in todos_insumos:
                    if insumo in registro['insumos']:
                        valores_insumos.append(str(registro['insumos'][insumo]))
                    else:
                        valores_insumos.append("0")
                
                linha += ",".join(valores_insumos)
                linha += f",{registro['irrigacao']}\n"
                
                arquivo.write(linha)
        
        print("\nDados exportados com sucesso para 'dados_agricultura.csv'!")
    except Exception as e:
        print(f"\nErro ao exportar dados: {e}")
    
    esperar_enter()

def menu_principal():
    """Exibe o menu principal e gerencia as opções."""
    while True:
        limpar_tela()
        print("\n" + "=" * 50)
        print("        FARMTECH SOLUTIONS - AGRICULTURA DIGITAL")
        print("=" * 50)
        print("\nFazenda FOF (Future Of Food)")
        print("Tamanho da Fazenda: 20 mil metros quadrados (2 ha)")
        print("\nMENU PRINCIPAL:")
        print("1. Entrada de dados (novo registro)")
        print("2. Visualizar dados")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Exportar dados para CSV (para R)")
        print("0. Sair do programa")
        print("=" * 50)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                entrada_dados()
            elif opcao == 2:
                visualizar_dados()
            elif opcao == 3:
                atualizar_dados()
            elif opcao == 4:
                deletar_dados()
            elif opcao == 5:
                exportar_dados()
            elif opcao == 0:
                limpar_tela()
                print("\nObrigado por usar o sistema FarmTech Solutions!")
                print("Saindo do programa...\n")
                sys.exit(0)
            else:
                print("\nOpção inválida!")
                esperar_enter()
        
        except ValueError:
            print("\nOpção inválida! Digite um número.")
            esperar_enter()

if __name__ == "__main__":
    print("Iniciando o sistema FarmTech Solutions...")
    menu_principal()