import requests
import jsonpath


avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(resultados)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')

# print(primeira)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

# print(nome)

# comentario = jsonpath.jsonpath(avaliacoes.json(), 'results[1].comentario')

# print(comentario)

# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')

# print(curso_id)

# todos os nomes de pessoas que avaliaram o curso
#nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
#print(nomes)

notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao') # .json() retorna um dicionário python
print(notas) 