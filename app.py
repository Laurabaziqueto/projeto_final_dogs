from flask import Flask, request, jsonify, flash, url_for, render_template, redirect, session
from routes import post_usuario, post_login, post_ongs, post_animal, get_animais, get_usuarios, post_voluntario, \
    get_ongs, get_adocoes, post_adocoes, get_voluntario, post_doacao, get_ong, get_doacoes, get_usuario, put_usuario, \
    get_pagamentos, get_voluntarios, get_voluntariados

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"


@app.route('/')
def index():
    return render_template('Pagina_inicial.html')


#  ---------------------- PAGÍNA INICIAL ----------------------
@app.route('/pagina_inicial/<papel>', methods=['GET'])
def pagina_inicial(papel):
    if papel == 'ong':
        session['usuario']['papel'] = papel
        print('usuario papel', session['usuario'])

        if put_usuario(session['usuario']) == 200:
            return redirect(url_for('cadastro_ong'))
        else:
            return redirect(url_for('escolher_papel'))
    elif papel == 'voluntario':
        session['usuario']['papel'] = papel
        print('usuario papel', session['usuario']['papel'])

        if put_usuario(session['usuario']) == 200:
            return redirect(url_for('listar_animais', status='d'))
        else:
            return redirect(url_for('escolher_papel'))
    else:
        return render_template('escolha.html')


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

            if not session['usuario']['papel']:
                flash('Login bem-sucedido!', 'success')
                return redirect(url_for('escolher_papel'))
            elif session['usuario']['papel'] == 'ong':
                print(resultado.json())
                session['id_ong'] = resultado.json()['id_ong']
                print('id_ong', session['id_ong'])
            return redirect(url_for('listar_animais', status='d'))
        else:
            flash('Usuario senha inválidos.', 'danger')
            return redirect(url_for('login'))

    return render_template('pagina_login.html')


@app.route('/escolha')
def escolher_papel():
    return render_template('escolha.html')


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


@app.route('/informacao', methods=['GET'])
def informacao():
    return render_template('informacao.html')


@app.route('/animais/<status>')
def listar_animais(status):
    papel = session['usuario']['papel']

    animais = get_animais(status)

    print(animais)
    print(papel)
    return render_template("lista_animais.html", animais=animais, papel=papel, status=status)


@app.route('/animal/', methods=['GET', 'POST'])
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
            return redirect(url_for('listar_animais', status='d'))
        else:
            flash('erro em cadastrar animal .', 'danger')
            return redirect(url_for('cadastro_animal'))
    return render_template('cadastro_animal.html')


@app.route('/animal/<id_animal>', methods=['GET', 'POST'])
def editar_animal(id_animal):
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
            return redirect(url_for('listar_animais', status='d'))
        else:
            flash('erro em cadastrar animal .', 'danger')
            return redirect(url_for('cadastro_animal'))

    return render_template('cadastro_animal.html')

@app.route('/cadastro_voluntario/<ong_id>', methods=['GET', 'POST'])
def cadastro_voluntario(ong_id):
    usuario_id = session['usuario']['id_usuario']

    print(ong_id)
    cadastro_adocoes = post_voluntario(usuario_id, ong_id)

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
    return render_template("lista_voluntariados.html", voluntarios=voluntarios, papel=session['usuario']['papel'])


@app.route('/ongs')
def listar_ongs():
    ongs = get_ongs()

    print(ongs)
    return render_template("pagina_voluntario.html", ongs=ongs['ongs'])


@app.route('/cadastro_ong', methods=['GET', 'POST'])
def cadastro_ong():
    if request.method == 'POST':
        nome_ong = request.form.get('nome_ong')
        chave_pix = request.form.get('chave_pix')
        necessidades = request.form.get('necessidades')
        imagem = request.form.get('imagem')
        descricao = request.form.get('descricao')

        resultado = post_ongs(nome_ong, chave_pix, necessidades, imagem, descricao)

        if resultado.status_code == 201:
            flash('Cadastro bem-sucedido!', 'success')
            return redirect(url_for('listar_animais', status='d'))
        else:
            flash(f'erro: {resultado}', 'danger')
            return redirect(url_for('cadastro_ong'))
    return render_template('casdastro_ong.html')


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

@app.route('/pagamentos')
def listar_pagamentos():
    id_ong = session['id_ong']
    print('ong paga', id_ong)
    pagamentos = get_pagamentos(id_ong)

    if "pagamentos" in pagamentos:
        pagamentos = pagamentos['pagamentos']
    else:
        pagamentos = []

    print(pagamentos)
    return render_template("pagamentos.html", pagamentos=pagamentos)

@app.route('/voluntarios')
def listar_voluntarios():
    id_ong = session['id_ong']
    print('ong volun', id_ong)
    print('papel', session['usuario']['papel'])
    voluntarios = get_voluntarios(id_ong)

    if "voluntarios" in voluntarios:
        voluntarios = voluntarios['voluntarios']
    else:
        voluntarios = []

    print(voluntarios)
    return render_template("lista_voluntariados.html", voluntarios=voluntarios, papel=session['usuario']['papel'])

@app.route('/voluntariados')
def listar_voluntariados():
    id_usuario = session['usuario']['id_usuario']
    print('id usu', id_usuario)
    print('papel', session['usuario']['papel'])
    voluntariados = get_voluntariados(id_usuario)

    if "voluntariados" in voluntariados:
        voluntariados = voluntariados['voluntariados']
    else:
        voluntariados = []

    print(voluntariados)
    return render_template("lista_voluntariados.html", voluntarios=voluntariados, papel=session['usuario']['papel'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
