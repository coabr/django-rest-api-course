import requests

header = {'Authorization': 'Token 2d696dc7ce5c630b353502cbd2ec788b09e3be19'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{ url_base_cursos }3/', headers=header)

assert resultado.status_code == 204

# testando se o tamanho do conteudo retornado é zero
assert len(resultado.text) == 0
assert len(resultado.content) == 0