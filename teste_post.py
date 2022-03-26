import requests

header = {'Authorization': 'Token 2afbce0a103e693bd35ef0089a551fd9ffba6857'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Introducao a programação com kotlin 2",
    "url": "http://www.udemy.com/introducao-a-programacao-com-kotlin2/",
}

resultado = requests.post(url=url_base_cursos, headers=header, data=novo_curso)

# Testando o código de status HTTP 201
assert resultado.status_code == 201

# testando se o titulo do curso criado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']