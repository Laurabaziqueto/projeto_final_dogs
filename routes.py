import requests

base_url = "http://10.135.233.139:5000"

def post_login(email, senha):
    try:
        url = f"{base_url}/login"
        dados = {
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
def post_usuario(nome, cpf, email, senha, telefone):
    try:
        url = f"{base_url}/cadastro_usuario"
        dados = {
            "nome": nome,
            "cpf": cpf,
            "email": email,
            "senha": senha,
            "telefone": telefone,
        }
        response = requests.post(url, json=dados)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

def post_animal(nome, raca, idade, sexo):
    try:
        url = f"{base_url}/cadastro_animal"
        dados = {
            "nome": nome,
            "raca": raca,
            "idade": idade,
            "sexo": sexo,
        }
        response = requests.post(url, json=dados)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }

# editar
def put_usuario(nome, cpf, email, senha, telefone,id_usuario):
    try:
        url = f"{base_url}/editar_usuario/{id_usuario}"
        dados = {
            "nome": nome,
            "cpf": cpf,
            "email": email,
            "senha": senha,
            "telefone": telefone,
        }
        response = requests.post(url, json=dados)
        return response.json()
    except Exception as e:
        print(e)
        return {
            "error": f"{e}",
        }


def post_voluntario():
    return None


def post_ongs():
    return None