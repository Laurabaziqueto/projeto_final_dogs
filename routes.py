import pickle

import requests

base_url = "http://10.135.232.8:5000"

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

# editar
def put_usuario(nome, cpf, email, senha, telefone,id_usuario):
    try:
        url = f"{base_url}/editar_usuario/{id_usuario}"
        dados = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email,
            "senha": senha,
        }
        response = requests.post(url, json=dados)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }


def get_animais():
    try:
        url = f"{base_url}/listar_animais"
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


def get_voluntario():
    try:
        url = f"{base_url}/listar_voluntarios"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",

        }

def post_voluntario(nome, cpf, telefone, email, data_nascimneto ):
    try:
        url = f"{base_url}/cadastro_voluntario"
        dados = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email,
            "data_nascimneto": data_nascimneto,
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }


# ongs
def get_ongs():
    try:
        url = f"{base_url}/listar_ongs"
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
        return response.status_code
    except Exception as e:
        print(e)
        return {
            "error": f"{e}"
        }
