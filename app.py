from flask import Flask, request, jsonify, flash, url_for, render_template, redirect, session
from select import select

from routes import post_usuario, post_login, post_ongs, post_animal, get_animais, get_usuarios, post_voluntario, \
    get_ongs, get_voluntario

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"
@app.route('/')
def index():
    flash("entrada, aplicacao", category="success")
    return render_template('Pagina_inicial.html')


#  ---------------------- PAGÍNA INICIAL ----------------------
@app.route('/pagina_inicial', methods=['GET'])
def pagina_inicial():
    return render_template('Paginainicial.html')

@app.route('/pagina_doacoes', methods=['GET'])
def pagina_doacoes():
    return render_template('pagina_doacao.html')

@app.route('/doacoes_realizada ',methods=['GET'])
def doacoes_realizada():
    return render_template('adoacoes_realizada.html')

@app.route('/voluntario', methods=['GET'])
def voluntario():
    return render_template('pagina_voluntario.html')

@app.route('/resgate', methods=['GET'])
def resgate():
    return render_template('resgate_denuncia.html')

# Rota para adicionar a ONG
@app.route('/ongs', methods=['GET'])
def ongs():
    return render_template('casdastro_ong.html')

@app.route('/pagamento', methods=['GET'])
def pagamento():
    return render_template('pagamento_pix.html')

# ---------------------- LOGIN ----------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obter os dados necessarios para enviar para a API
        cpf = request.form['cpf']
        senha = request.form['senha']

        # envio para a api
        resultado = post_login(cpf, senha)

        print(resultado.status_code)
        # verificar se deu sucesso
        if resultado.status_code == 200:
            # salvar na session id e nome do usuario
            session['id_usuario'] = resultado.json()['usuario']
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('pagina_inicial'))
        else:
            flash('Usuario senha inválidos.', 'danger')
            return redirect(url_for('login'))

    return render_template('pagina_login.html')


# listar usuario
@app.route('/usuarios', methods=['GET', 'POST'])
def listar_usuarios():

    usuarios = get_usuarios()

    print(usuarios)
    return render_template("tabela_usuario.html", usuarios=usuarios ['usuarios'])

# ---------------------- CADASTRAR USUARIO ----------------------
@app.route('/usuario/cadastrar', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        senha = request.form.get('senha')


        resultado = post_usuario(nome, cpf, telefone, email, senha)

        if resultado == 201:
            flash('Cadastro bem-sucedido!', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'erro: {resultado}', 'danger')
            return redirect(url_for('cadastro_usuario'))
    return render_template('cadastro_usuario.html')


# informações dos ongs
@app.route('/informacao', methods=['GET'])
def informacao():
    return render_template('informacao.html')

# listar animal/ adotar animal
@app.route('/animais')
def listar_animais():

    animais = get_animais()

    print(animais)
    return render_template("pagina_adotar.html", animais=animais ['animais'])

# cadastrar animal
@app.route('/animal/cadastrar', methods=['GET', 'POST'])
def cadastro_animal():
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        nome = request.form.get('nome')
        raca = request.form.get('raca')
        idade = request.form.get('idade')
        sexo = request.form.get('sexo')
        imagem = request.form.get('imagem')

        resultado = post_animal(categoria, nome, raca, idade, sexo, imagem)

        if resultado == 201:
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('listar_animais'))
        else:
            flash('erro em cadastrar animal .', 'danger')
            return redirect(url_for('cadastro_animal'))
    return render_template('cadastro_animal.html')

# listar voluntario
@app.route('/voluntario')
def listar_voluntario():

    voluntario = get_voluntario()

    print(voluntario)
    return render_template("tabela_usuario.html", voluntario=voluntario ['voluntario'])


# cadastro voluntario
@app.route('/cadastro_voluntario', methods=['GET', 'POST'])
def cadastro_voluntario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        data_nascimento = request.form.get('data_nascimneto')


        resultado = post_voluntario(nome, cpf, telefone, email, data_nascimento)

        if resultado == 201:
            flash('Cadastro bem-sucedido!', 'success')
            return redirect(url_for('voluntario'))
        else:
            flash(f'erro: {resultado}', 'danger')
            return redirect(url_for('cadastro_voluntario'))
    return render_template('cadastro_voluntario.html')

# listar ongs
@app.route('/ongs')
def listar_ongs():

    ongs = get_ongs()

    print(ongs)
    return render_template("pagina_voluntario.html", ongs=ongs ['ongs'])

# cadastrar ongs
@app.route('/cadastro_ong', methods=['GET', 'POST'])
def cadastro_ong():
    if request.method == 'POST':
        nome_ong = request.form.get('nome_ong')
        chave_pix = request.form.get('chave_pix')
        necessidades = request.form.get('necessidades')
        imagem = request.form.get('imagem')
        descricao = request.form.get('descricao')


        resultado = post_ongs(nome_ong, chave_pix, necessidades, imagem, descricao)

        if resultado == 201:
            flash('Cadastro bem-sucedido!', 'success')
            return redirect(url_for('voluntario'))
        else:
            flash(f'erro: {resultado}', 'danger')
            return redirect(url_for('cadastro_ong'))
    return render_template('casdastro_ong.html')

#
# # listar adocao
# @app.route('/adocoes')
# def listar_adocao():
#
#     adocoes = get_adocao()
#
#     print(adocao)
#     return render_template("pagina_voluntario.html", ongs=ongs ['ongs'])
#
# # cadastrar adocao
# @app.route('/cadastro_ong', methods=['GET', 'POST'])
# def cadastro_ong():
#     if request.method == 'POST':
#         nome_ong = request.form.get('nome_ong')
#         chave_pix = request.form.get('chave_pix')
#         necessidades = request.form.get('necessidades')
#         imagem = request.form.get('imagem')
#         descricao = request.form.get('descricao')
#
#
#         resultado = post_ongs(nome_ong, chave_pix, necessidades, imagem, descricao)
#
#         if resultado == 201:
#             flash('Cadastro bem-sucedido!', 'success')
#             return redirect(url_for('voluntario'))
#         else:
#             flash(f'erro: {resultado}', 'danger')
#             return redirect(url_for('cadastro_ong'))
#     return render_template('casdastro_ong.html')
#


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5001)