from flask import Flask, request, jsonify, flash, url_for, render_template, redirect, session
from select import select

from routes import post_usuario, post_login, post_voluntario, post_ongs, post_animal

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"


@app.route('/')
def index():
    return render_template('Pagina_inicial.html')


# ---------------------- LOGIN ----------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obter os dados necessarios para enviar para a API
        cpf = request.form['cpf']
        senha = request.form['senha']

        # envio para a api
        resultado = post_login(cpf, senha)

        # verificar se deu sucesso
        if resultado.status_code == 200:
            # salvar na session id e nome do usuario
            session['usuario_id'] = resultado.json()['usuario']['id_usuario']
            session['usuario_nome'] = resultado.json()['usuario']['nome']
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('pagina_inicial'))
        else:
            flash('Usuario senha inválidos.', 'danger')
            return redirect(url_for('login'))

    return render_template('Pagina_login.html')


#  ---------------------- CADASTRAR USUÁRIO ----------------------
@app.route('/usuario/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')
        # enviar os dados para a API
        resultado = post_usuario(nome, telefone, email, senha, cpf)

        # verificar se deu sucesso
        if resultado == 201:
            flash('cadastro bem-sucedido!', 'success')
        else:
            flash('erro no cadastro.', 'danger')
            return redirect(url_for('cadastrar_usuario'))

    return render_template('Cadastro.html')


#  ---------------------- PAGÍNA INICIAL ----------------------
@app.route('/pagina_inicial', methods=['GET'])
def pagina_inicial():
    return render_template('Paginainicial.html')


@app.route('/pagina_doacoes', methods=['GET'])
def pagina_doacoes():
    return render_template('pagina_doacao.html')


@app.route('/doacoes_realizada ', methods=['GET'])
def doacoes_realizada():
    return render_template('adoacoes_realizada.html')


@app.route('/voluntario/cadastrar', methods=['GET', 'POST'])
def cadastrar_voluntario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        data_nascimento = request.form.get('data_nascimento')
        email = request.form.get('email')
        senha = request.form.get('senha')
        cpf = request.form.get('cpf')

        # enviar os dados para a API
        resultado = post_voluntario(nome, telefone, data_nascimento, email, senha, cpf)

        # verificar se deu sucesso
        if resultado.status_code == 200:
            flash('Login bem-sucedido!', 'success')
        else:
            flash('erro usuario.', 'danger')
            return redirect(url_for('cadastrar_voluntario'))

    return render_template('cadastro_voluntario.html')


@app.route('/voluntario', methods=['GET'])
def voluntario():
    return render_template('Pagina_Voluntario.html')


@app.route('/resgate', methods=['GET'])
def resgate():
    return render_template('resgate_denuncia.html')


# Rota para adicionar a ONG
@app.route('/ongs', methods=['GET'])
def cadastrar_ongs():
    if request.method == 'POST':
        nome = request.form.get('nome')
        chave_pix = request.form.get('chave_pix')

        # enviar os dados para a API
        resultado = post_ongs(nome, chave_pix)

        # verificar se deu sucesso
        if resultado == 201:
            flash('ong cadastrada!', 'success')
        else:
            flash('erro pra cadastrar ong.', 'danger')
            return redirect(url_for('cadastrar_usuario'))

    return render_template('ongs.html')



@app.route('/pagamento', methods=['GET'])
def pagamento():
    return render_template('pagamento_pix.html')


# ----------------------PAGINA ADOTAR --------------------------
@app.route('/pagina_adotar', methods=['GET'])
def pagina_adotar():
    return render_template('Pagina_Adotar.html')


# ----------------------INFORMAÇÃO DE ADOÇÃO--------------------------
@app.route('/informacao', methods=['GET'])
def informacao():
    return render_template('informacao.html')

@app.route('/animais', methods=['GET'])
def animais():
    return render_template('Pagina_Adotar.html')


# ---------------------- CADASTRAR ANIMAL ----------------------
@app.route('/animal/cadastrar', methods=['GET', 'POST'])
def cadastro_animal():
    if request.method == 'POST':
        nome_animal = request.form.get('nome_animal')
        raca = request.form.get('raca')
        idade = request.form.get('idade')

        resultado = post_animal(nome_animal, raca, idade)

        if resultado.status_code == 200:
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('pagina_adotar'))
        else:
            flash('erro em cadastrar animal .', 'danger')
            return redirect(url_for('cadastro_animal'))
    return render_template('cadastro_animal.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
