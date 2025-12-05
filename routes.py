import pickle

import requests

base_url = "http://10.135.235.5:5001"

def post_login(cpf, senha):
    try:
        url = f"{base_url}/login"
        print(url)
        dados = {
            "cpf": cpf,
            "senha": senha,
        }
        response = requests.post(url, json=dados)
        return response
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def get_usuarios():
    try:
        url = f"{base_url}/listar_usuarios"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def get_usuario(id_usuario):
    try:
        url = f"{base_url}/get_usuario/{id_usuario}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def post_usuario(nome, cpf, telefone, email, senha ):
    try:
        url = f"{base_url}/usuario/cadastrar"
        dados = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email,
            "senha": senha,
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }

def put_usuario(usuario):
    try:
        url = f"{base_url}/editar_usuario/{usuario['id_usuario']}"
        dados = {
            "id": usuario['id_usuario'],
            "nome": usuario['nome'],
            "cpf": usuario['cpf'],
            "telefone": usuario['telefone'],
            "email": usuario['email'],
            "papel": usuario['papel'],
        }
        response = requests.put(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def get_adocoes(id_usuario):
    try:
        url = f"{base_url}/listar_adocoes/{id_usuario}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def post_voluntario(usuario_id, ong_id):
    try:
        url = f"{base_url}/cadastro_voluntario"
        dados = {
            "usuario_id": usuario_id,
            "ong_id": ong_id
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }

def get_voluntario(id_usuario):
    try:
        url = f"{base_url}/listar_voluntario/{id_usuario}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def post_adocoes(usuario_id, animal_id):
    try:
        url = f"{base_url}/cadastro_adocao"
        dados = {
            "usuario_id": usuario_id,
            "animal_id": animal_id
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }

def post_doacao(usuario_id, ong_id, valor):
    try:
        url = f"{base_url}/cadastro_pagamento"
        dados = {
            "usuario_id": usuario_id,
            "ong_id": ong_id,
            "valor": valor
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }

def get_animais(status):
    try:
        url = f"{base_url}/listar_animais/{status}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def post_animal(categoria, nome, raca, idade, sexo, imagem):
    try:
        url = f"{base_url}/cadastro/animal"
        dados = {
            "categoria": categoria,
            "nome": nome,
            "raca": raca,
            "idade": idade,
            "sexo": sexo,
            "imagem": imagem,
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def get_ongs():
    try:
        url = f"{base_url}/listar/ongs"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }

def get_ong(id_ong):
    try:
        url = f"{base_url}/get_ong/{id_ong}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }

def get_doacoes(id_usuario):
    try:
        url = f"{base_url}/listar_doacoes/{id_usuario}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def get_pagamentos(id_ong):
    try:
        url = f"{base_url}/listar_pagamentos/{id_ong}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def get_voluntarios(id_ong):
    try:
        url = f"{base_url}/listar_voluntarios/{id_ong}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def get_voluntariados(id_usuario):
    try:
        url = f"{base_url}/listar_voluntariados/{id_usuario}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def post_ongs(nome_ong, chave_pix, necessidades, imagem, descricao ):
    try:
        url = f"{base_url}/cadastro_ong"
        dados = {
            "nome_ong": nome_ong,
            "chave_pix": chave_pix,
            "necessidades": necessidades,
            "imagem": imagem,
            "descricao": descricao,
        }
        response = requests.post(url, json=dados)
        return response
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }
