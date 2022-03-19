
import banco
from flask import Flask, render_template, request
from enviaEmai import envia_email, envia_email_concluir
from datetime import datetime

base_dados = banco

app = Flask(__name__)

#abrir pagina de login
@app.route('/')
def abre_login():
    return render_template('login.html')

#validação de login
@app.route('/', methods=['POST'])
def login():
    nomeL = request.form['nomeLogin']
    senhaL = request.form['senhaLogin']
    res = base_dados.usuarios(nomeL, senhaL)
    if res > 0:
        return render_template('dados.html')
    else:
        return render_template('login.html', mensagem = 'Usuario ou senha invalido!!!')

#abrir pagina de adicionar usuario.
@app.route('/addUsuarios')
def abre_add_usuario():
    return render_template('addUsuarios.html')

#pagina de adicionar usuario
@app.route('/addUsuarios', methods=['POST'])
def add_usuario():
    nomeU = request.form['nomeUser']
    senhaU = request.form['senhaUser']
    senha02 = request.form['senhaUserRep']
    emailU = request.form['emailUser']
    if senhaU == senha02:
        addUser = base_dados.cadastro_usuarios(nomeU, senhaU, emailU)
        return render_template('addUsuarios.html', usuarios = addUser)
    else:
        return render_template('addUsuarios.html', sen = 'SENHAS NÃO CORRESPONDENTES!!!')

#abrir pagina do formulario de abrir chamado
@app.route('/dados')
def abre_dados():
    return render_template('dados.html')

#Adicionar dados no formulario de chamado, abrir chamado e enviar e-mail.
@app.route('/dados', methods=['POST'])
def add_dados():
    localS = request.form['localSoli']
    setorS = request.form['setorSoli']
    nomeS = request.form['nomeSoli']
    dataS = request.form['dataSoli']
    comentarioS = request.form['comentarioSoli']
    statusS=True
    dataFec = '0000-00-00 00:00:00'
    dados_add = base_dados.inserte_dados(localS, nomeS, dataS, setorS, comentarioS, statusS, dataFec)
    envio =  envia_email(localS, nomeS, dataS, setorS, comentarioS, statusS, dataFec)
    return render_template('dados.html', resultado = dados_add, envio_email = envio)

#@app.route('/filtroChamados')
#def abreFiltro():
    #return render_template('filtroChamados.html')

#lista de chamados
@app.route('/chamados')
def executar():
    listar = base_dados.chamados_lista()
    return render_template('chamados.html', lista = listar)

#listar por nome a lista de chamados
@app.route('/filtroChamados', methods=['POST'])
def filtrar():
    fil = request.form['pesquisar']
    pesquisa = base_dados.chamados_solicitante(fil)
    return render_template('filtroChamados.html', filtrar = pesquisa)

#Enviar o e-mail de fachamento do chamado com os dados.
@app.route('/concluir_chamado', methods=['POST'])
def atualizaChamado():
    idChamado = request.form['id_chamado']
    data_at = datetime.now()
    resul = base_dados.atualiza_chamado(idChamado, data_at)
    listar = base_dados.chamados_lista()
    conc = envia_email_concluir()
    return render_template('chamados.html', t = resul, lista = listar, c = conc)



#debug=True serve para atualizar sem reiniciar o servidor
if __name__=="__main__":
    app.run(debug=True)
