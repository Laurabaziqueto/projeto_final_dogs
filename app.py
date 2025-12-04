from flask import Flask, request, jsonify, flash, url_for, render_template, redirect, session
from select import select

from routes import post_usuario, post_login, post_ongs, post_animal, get_animais, get_usuarios, post_voluntario, \
    get_ongs, get_adocoes, post_adocoes, get_voluntario, post_doacao, get_ong, get_doacoes, get_usuario

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

@app.route('/')
def index():
    return render_template('Pagina_inicial.html')

#  ---------------------- PAGÍNA INICIAL ----------------------
@app.route('/pagina_inicial', methods=['GET'])
def pagina_inicial():
     ongs = get_ongs()
     return render_template('Paginainicial.html', ongs=ongs)


@app.route('/resgate', methods=['GET'])
def resgate():
    return render_template('resgate_denuncia.html')


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
            session['usuario'] = resultado.json()['usuario']
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('listar_animais'))
        else:
            flash('Usuario senha inválidos.', 'danger')
            return redirect(url_for('login'))

    return render_template('pagina_login.html')


# listar usuario
@app.route('/usuarios', methods=['GET', 'POST'])
def listar_usuarios():

    usuarios = get_usuarios()

    print(usuarios)
    return render_template("tabela_usuario.html", usuarios=usuarios['usuarios'])

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
    return render_template("Paginainicial.html", animais=animais ['animais'])

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

''
# cadastro voluntario
@app.route('/cadastro_voluntario/<ong_id>', methods=['GET', 'POST'])
def cadastro_voluntario(ong_id):
    usuario_id = session['usuario']['id_usuario']

    print(ong_id)
    cadastro_adocoes = post_adocoes(usuario_id, ong_id)

    return redirect(url_for('listar_voluntario'))

@app.route('/listar_voluntario')
def listar_voluntario():
    id_usuario = session['usuario']['id_usuario']
    print(id_usuario)
    voluntarios = get_voluntario(id_usuario)

    if "voluntarios" in voluntarios:
        voluntarios = voluntarios['voluntarios']
    else:
        voluntarios = []

    print(voluntarios)
    return render_template("lista_voluntariados.html", voluntarios=voluntarios)


# ongs
@app.route('/ongs')
def listar_ongs():

    ongs = get_ongs()

    print(ongs)
    return render_template("pagina_voluntario.html", ongs=ongs['ongs'])

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
            return redirect(url_for('listar_ongs'))
        else:
            flash(f'erro: {resultado}', 'danger')
            return redirect(url_for('cadastro_ong'))
    return render_template('casdastro_ong.html')

#
# listar adocao
@app.route('/adocoes')
def listar_adocoes():
    id_usuario = session['usuario']['id_usuario']
    print(id_usuario)
    adocoes = get_adocoes(id_usuario)

    if "adocoes" in adocoes:
        adocoes = adocoes['adocoes']
    else:
        adocoes = []

    print(adocoes)
    return render_template("adoacoes_realizada.html", adocoes=adocoes)


# cadastrar adocao
@app.route('/cadastro_adocoes/<id_animal>', methods=['GET', 'POST'])
def cadastro_adocao(id_animal):

    usuario_id = session['usuario']['id_usuario']

    print(id_animal)
    cadastro_adocoes = post_adocoes(usuario_id, id_animal)
    # if "adocao" in cadastro_adocoes:
    #     cadastro_adocoes = cadastro_adocoes['cadastro_adocoes']
    # else:
    #     cadastro_adocoes = []
    #     print(cadastro_adocoes)

    return redirect(url_for('listar_adocoes'))

@app.route('/cadastro_doacao/<ong_id>', methods=['GET', 'POST'])
def cadastro_doacao(ong_id):
    usuario_id = session['usuario']['id_usuario']

    if request.method == 'POST':
        valor = request.form.get('form_valor')
        cadastro_adocoes = post_doacao(usuario_id, ong_id, int(valor))

        print(cadastro_adocoes)
        if cadastro_adocoes:
            flash('Cadastro de doacao', 'success')
            return redirect(url_for('listar_doacoes'))
        else:
            flash(f'erro: {cadastro_adocoes}', 'danger')
            return redirect(url_for('cadastro_doacao'))

    ong = get_ong(ong_id)
    usuario = get_usuario(usuario_id)
    print('ong', ong)
    print('usuario', usuario)
    return render_template("cadastro_doacao.html", ong=ong['ong'], usuario=usuario['usuario'])

@app.route('/doacoes')
def listar_doacoes():
    id_usuario = session['usuario']['id_usuario']
    print(id_usuario)
    doacoes = get_doacoes(id_usuario)

    if "doacoes" in doacoes:
        doacoes = doacoes['doacoes']
    else:
        doacoes = []

    print(doacoes)
    return render_template("doacoes.html", doacoes=doacoes)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5001)