import math

#Calcula media dos alunos
def post_grades(lista_dados_estudantes: list) -> list:
    if not lista_dados_estudantes:
        return []
    
    resultados = tratar_dados(lista_dados_estudantes)
    resultados.sort(key=lambda x: x['media'], reverse=True)
    
    resultados_finais = verificar_resultados(resultados)
    return resultados_finais

def tratar_dados(lista_dados_estudantes: list) -> list:
    lista_resultados = []
    for estudante in lista_dados_estudantes:
        resultados = organizar_dados(estudante, lista_resultados)

    return resultados

def organizar_dados(estudante: str, lista_resultados: list) -> list:
    estudante_um = estudante.strip().split(' - ')
    id_estudante = estudante_um[0]
    notas = estudante_um[2].strip().split(' ')
    media = calcular_media(notas)

    lista_resultados.append({
        'id_estudante': id_estudante,
        'media': media
    })
    return lista_resultados

def calcular_media(notas: list) -> float:
    notas_tratadas = [float(nota_convertida) for nota_convertida in notas]
    media_aluno = sum(notas_tratadas) / len(notas_tratadas)
    return media_aluno

def verificar_resultados(resultados: list) -> list:
    resultados_tratados = []
    
    for resultado in resultados:
        media_arredondada = round(resultado['media'], 2)
        if comparar_media(resultado['media'], media_arredondada):
            resultados_tratados.append((resultado['id_estudante'], media_arredondada))
        else:
            resultados_tratados.append((resultado['id_estudante'], resultado['media']))
    return resultados_tratados

def comparar_media(media_calculada, media_esperada, margem=1e-9):
    return math.isclose(media_calculada, media_esperada, abs_tol=margem)

lista_dados_estudantes = [
    'S01 - Student Name A - 95 98.4 92.15', 
    'S02 - Student Name B - 100 96.4 90', 
    'S03 - Student Name C - 84.2 90.5 92.8', 
    'S04 - Student Name D - 80 96.4 88.4'
]

iniciar = post_grades(lista_dados_estudantes)
print(iniciar)