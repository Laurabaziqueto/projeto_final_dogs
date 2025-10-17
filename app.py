from flask import Flask, request, jsonify, flash, url_for, render_template, redirect, session
from select import select

from routes import *

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

@app.route('/')
def index():
    return render_template('Pagina_inicial.html')

# ---------------------- LOGIN ----------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == 'teste@teste.com' and senha == '123456':
            session['usuario_id'] = 1
            session['usuario_nome'] = 'Usuário Teste'
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('listar_pagamento'))
        else:
            flash('Email ou senha inválidos.', 'danger')

    return render_template('Pagina_login.html')

# # ---------------------- CADASTRAR USUÁRIO ----------------------
@app.route('/usuario/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')

        if not nome or not email or not cpf or not telefone or not senha:
            flash('Todos os campos são obrigatórios.', 'danger')
            return redirect(url_for('login'))

        flash(f'Voluntário {nome} cadastrado com sucesso! (Simulado)', 'success')
        return redirect(url_for('login'))

    return render_template('Cadastro.html')

# # ---------------------- CADASTRAR ANIMAL ----------------------
# @app.route('/animal/cadastrar', methods=['GET', 'POST'])
# def cadastrar_animal():
#     if request.method == 'POST':
#         nome_animal = request.form.get('nome_animal')
#         raca = request.form.get('raca')
#         idade = request.form.get('idade')
#
#         if not nome_animal or not raca or not idade:
#             flash('Todos os campos são obrigatórios.', 'danger')
#             return redirect(url_for('cadastrar_animal'))
#
#         # Simula cadastro
#         flash(f'Animal {nome_animal} cadastrado com sucesso! (Simulado)', 'success')
#         return redirect(url_for('consultar_animal'))
#
#     return render_template('cadastro_animal.html')

# # ---------------------- CADASTRAR PAGAMENTO ----------------------
# @app.route('/pagamento/cadastrar', methods=['POST'])
# def cadastrar_pagamento():
#     dados_pagamento = request.get_json()
#     if not dados_pagamento:
#         return {"mensagem": "Nenhum dado recebido"}, 400
#
#     return {"mensagem": "Pagamento cadastrado! (Simulado)"}, 201

# # ---------------------- CADASTRAR VOLUNTARIO ----------------------
# @app.route('/cadastrar_voluntario/cadastrar', methods=['GET', 'POST'])
# def cadastrar_voluntario():
#     if request.method == 'POST':
#         nome = request.form.get('nome')
#         cpf = request.form.get('cpf')
#         telefone = request.form.get('telefone')
#         data_nascimento = request.form.get('data_nascimento')
#         email = request.form.get('email')
#
#         if not nome or not cpf or not telefone or not email or not data_nascimento:
#             flash('Todos os campos são obrigatórios.', 'danger')
#             return redirect(url_for('cadastrar_voluntario'))
#
#         flash(f'Voluntário {nome} cadastrado com sucesso! (Simulado)', 'success')
#         return redirect(url_for('login'))
#
#     return render_template('cadastroparaservoluntario.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5001)