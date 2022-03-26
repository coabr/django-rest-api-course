import requests

header = {'Authorization': 'Token 2d696dc7ce5c630b353502cbd2ec788b09e3be19'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo curso de scrum: Agilidade, produtividade e gestao",
    "url": "http://www.udemy.com/novo-curso-de-scrum-3-agilidade-produtividade-e-gestao/",
}

# buscando o curso com o id 2 que sera atualizado
#curso = requests.get(f'{url_base_cursos}3/', headers=header)
#print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}3/', headers=header, data=curso_atualizado)

#curso = requests.get(f'{url_base_cursos}3/', headers=header)
#print(curso.json())

# testando o código de status HTTP 200
assert resultado.status_code == 200

# testando se o titulo colocado é o mesmo do alterado
assert resultado.json()['titulo'] == curso_atualizado['titulo']