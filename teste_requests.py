from tokenize import Token
import requests

# GET avaliacoes
#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#acessa o codigo de status HTTP
#print(avaliacoes.status_code)

# acessando os dados da resposta
#print(avaliacoes.json())
# print(type(avaliacoes.json()))

#acessando a quantidade de registros
#print(avaliacoes.json()['count'])

#acessando a proxima pagina de resultados
#print(avaliacoes.json()['next'])

# acessando os resultados dessa pagina
#print(avaliacoes.json()['results'])
#print(type(avaliacoes.json()['results']))

#acessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])

#acessando o ultimo elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])

#acessando somente o nome da pessoa que criou a ultima avaliacao
#print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliacao
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/2/')
# print(avaliacao.json())

#GET cursos
headers = {'Authorization': 'Token 2afbce0a103e693bd35ef0089a551fd9ffba6857' }

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())
