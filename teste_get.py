import requests

header = {'Authorization': 'Token 2afbce0a103e693bd35ef0089a551fd9ffba6857'}

url_bases_cursos = 'http://localhost:8000/api/v2/cursos/'
url_bases_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_bases_cursos, headers=header)

#print(resultado.json())
# print(resultado.status_code)

# testando se o endpoint está correto
assert resultado.status_code == 200
# testando a quantidade de registros
assert resultado.json()['count'] == 9
#testando se o titulo do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Introducao a programacao com python'

# ao rodar esse teste no console nao aparece nenhum erro