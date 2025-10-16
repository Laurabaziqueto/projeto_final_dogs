from flask import Flask, request, jsonify, flash, url_for, render_template, redirect
from select import select

from routes import *

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

@app.route("/usuarios", methods=['POST', 'GET'])
def get_usuarios():
    dados = get_usuarios()  # função precisa existir em routes.py

    if "usuarios" in dados:
        user = dados["usuarios"]
        return jsonify({"usuarios": user})
    else:
        flash("Erro ao buscar usuários.")
        return jsonify({"erro": "Não foi possível buscar os usuários"}), 400

@app.route('/usuario/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')
        cpf = request.form.get('cpf')

        if not nome or not email or not senha or not telefone:
            flash('Todos os campos são obrigatórios.', 'danger')
            return redirect(url_for('cadastrar_usuario'))


        cadastrar = post_usuario(nome, email, cpf, senha,telefone)
        print(cadastrar)

        flash(f'Usuário {nome} cadastrado com sucesso! (Simulado)', 'success')

        # return redirect(url_for('login'))
        print('deu certo')

    return render_template('Cadastro.html')

@app.route('/animal/cadastrar', methods=['GET', 'POST'])
def cadastrar_animal():
    if request.method == 'POST':
        nome = request.form.get('nome')
        raca = request.form.get('raca')
        idade = request.form.get('idade')
        sexo = request.form.get('sexo')

        if not nome or not raca or not idade or not sexo:
            flash('Todos os campos são obrigatórios.', 'danger')
            return redirect(url_for('cadastro_animal'))

        cadastro = post_usuario(nome, raca, idade, sexo)
        print(cadastro)

        flash(f'Animal {nome} cadastrado com sucesso! (Simulado)', 'success')
        # return redirect(url_for('login'))
        print('deu certo')

    return render_template('cadastro_animal.html')

@app.route('/editar_usuario', methods=['PUT'])
def editar_usuario():
    # busca de acordo com o id, usando o db_session
    # usuario_resultado = db_session.execute(select(Usuario).filter_by(id=int(id_usuario))).scalar()
    usuariro_editado = put_usuario()
    print(usuario_resultado)

    # verifica se existe
    if not usuario_resultado:
        flash("Usuario não encontrado", "error")
        return redirect(url_for('usuario'))
    if request.method == 'POST':
        # valida os dados recebidos
        if not request.form.get('form_nome'):
            flash("Preencher campo", "error")
        elif not request.form.get('form_email'):
            flash("Preencher campo", "error")
        elif not request.form.get('form_senha'):
            flash("Preencher campo", "error")
        elif not request.form.get('form_telefone'):
            flash("Preencher campo", "error")
        elif not request.form.get('form_cpf'):
            flash("Preencher campo", "error")
        else:
            try:
                # o ponto (.) busca a informaÃ§Ã£o
                # atualiza os dados
                usuario_resultado.nome = request.form.get('form_nome')
                usuario_resultado.email = request.form.get('form_email')
                usuario_resultado.senha = request.form.get('form_senha')
                usuario_resultado.telefone = request.form.get('form_telefone')
                usuario_resultado.cpf = request.form.get('form_cpf')

                # salva os dados alterados
                usuario_resultado.save()
                flash("Usuario atualizado com sucesso!", "sucess")
                return redirect(url_for('usuario'))
            except Exception:
                flash(f"Erro {Exception}", "error")
    return render_template('editar_usuario.html')



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)