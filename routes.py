import requests

base_url = "http://10.135.233.133:5000"

def get_pagina_inicial():
    url = base_url + "/pagina_inicial"
    response = requests.get(url)
    return response.text

def get_pagina_doacoes():
    url = base_url + "/pagina_doacoes"
    response = requests.get(url)
    return response.text

def get_doacoes_realizada():
    url = base_url + "/doacoes_realizada"
    response = requests.get(url)
    return response.text

def get_voluntario():
    url = base_url + "/voluntaria"
    response = requests.get(url)
    return response.text

def get_resgate():
    url = base_url + "/resgate"
    response = requests.get(url)
    return response.text

#--------------------- ONGS --------------------------
def get_ongs():
    try:
        url = f"{base_url}/listar_ongs"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {"error": str(e)}

def post_ongs(nome, chave_pix):
    try:
        url = f"{base_url}/animal/cadastrar"
        dados = {
            "nome": nome,
            "chave_pix": chave_pix,

        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}


# ---------------------- LOGIN ----------------------
def post_login(cpf, senha):
    try:
        url = f"{base_url}/login"
        dados = {
            "cpf": cpf,
            "senha": senha
        }
        response = requests.post(url, json=dados)
        return response
    except Exception as e:
        print(e)
        return {"error": str(e)}

# ---------------------- USUÁRIOS ----------------------
def get_usuarios():
    try:
        url = f"{base_url}/usuario"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {"error": str(e)}

def post_usuario(nome, telefone, email, senha, cpf):
    try:
        url = f"{base_url}/usuario/cadastrar"
        dados = {

            "nome": nome,
            "telefone": telefone,
            "email": email,
            "senha": senha,
            "cpf": cpf,
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}

def editar_usuario(id_usuario, nome, email, senha):
    try:
        url = f"{base_url}/editar_usuario/{id_usuario}"
        dados = {
            "form_nome": nome,
            "form_email": email,
            "form_senha": senha,
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}

# ---------------------- ANIMAIS ----------------------
def get_animais():
    try:
        url = f"{base_url}/animal"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {"error": str(e)}

def post_animal(nome_animal, raca, idade):
    try:
        url = f"{base_url}/animal/cadastrar"
        dados = {
            "nome_animal": nome_animal,
            "raca": raca,
            "idade": idade,
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}

def editar_animal(id_animal, nome_animal, raca, idade):
    try:
        url = f"{base_url}/editar_animal/{id_animal}"
        dados = {
            "form_nome": nome_animal,
            "form_raca": raca,
            "form_idade": idade,
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}

# ---------------------- PAGAMENTO ----------------------
def get_pagamentos():
    try:
        url = f"{base_url}/pagamento"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {"error": str(e)}

def post_pagamento(nome_completo, cpf, codigo_Banco, agencia_bancaria, id_usuario):
    try:
        url = f"{base_url}/pagamento/cadastrar"
        dados = {
            "nome_completo": nome_completo,
            "cpf": cpf,
            "codigo_Banco": codigo_Banco,
            "agencia_bancaria": agencia_bancaria,
            "id_usuario": id_usuario
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}

# ---------------------- VOLUNTÁRIO ----------------------
def get_voluntarios():
    try:
        url = f"{base_url}/voluntario"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(e)
        return {"error": str(e)}

def post_voluntario(nome, cpf, telefone, data_nascimento, email):
    try:
        url = f"{base_url}/cadastrar_voluntario/cadastrar"
        dados = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "data_nascimento": data_nascimento,
            "email": email
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}

def editar_voluntario(id_voluntario, nome, cpf, data_nascimento):
    try:
        url = f"{base_url}/editar_voluntario/{id_voluntario}"
        dados = {
            "form_nome": nome,
            "form_cpf": cpf,
            "form_data_nascimento": data_nascimento
        }
        response = requests.post(url, json=dados)
        return response.status_code
    except Exception as e:
        print(e)
        return {"error": str(e)}
