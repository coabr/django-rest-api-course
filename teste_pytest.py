import requests

class TestCursos:
    header = {'Authorization': 'Token 2d696dc7ce5c630b353502cbd2ec788b09e3be19'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.header)
        assert cursos.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}6/', headers=self.header)
        assert resposta.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Introducao a programação com ruby",
            "url": "http://www.udemy.com/introducao-a-programacao-com-ruby/",
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.header, data=novo_curso)
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        curso_atualizado = {
            "titulo": "Introducao a programação com ruby 2",
            "url": "http://www.udemy.com/introducao-a-programacao-com-ruby2/",
        }
        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.header, data=curso_atualizado)
        assert resposta.status_code == 200
    
    def test_put_titulo_curso(self):
        curso_atualizado = {
            "titulo": "Introducao a programação com ruby 3",
            "url": "http://www.udemy.com/introducao-a-programacao-com-ruby3/",
        }
        resposta = requests.put(url=f'{self.url_base_cursos}5/', headers=self.header, data=curso_atualizado)
        assert resposta.json()['titulo'] == curso_atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}5/', headers=self.header)
        assert resposta.status_code == 204 and len(resposta.text) == 0
