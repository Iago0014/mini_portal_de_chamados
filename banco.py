import mysql.connector as mc


banco = mc.connect(host='localhost', user='root', password='admin',database='db_manutencao')

#função de inserção de dados na tabela.
def inserte_dados(localSol, nomeSol, dataSol, setorSol, comentarioSol, statusSoli, dataF):
    if banco.is_connected():
        comando = 'insert into solicitante(localidade, nome, dataSolicitacao, setor, comentario, status, dataFecha) values (%s, %s, %s, %s, %s, %s, %s)'
        cursor = banco.cursor()
        valores = (localSol, nomeSol, dataSol, setorSol, comentarioSol, statusSoli, dataF)
        cursor.execute(comando, valores)
        banco.commit()
        return 'Salvo com sucesso!!'
    else:
        return 'Erro ao salvar!!!'

#Mostra a lista de chamados em ordem decrescente.
def chamados_lista():
    if banco.is_connected():
        cursor = banco.cursor()
        comandoSel = 'select * from solicitante order by idSolicitente desc'
        cursor.execute(comandoSel)
        return cursor.fetchall()

#Faz uma pesquisa na lista por solicitante.
def chamados_solicitante(nomeSolicitante):
    nomeDoSol = f'%{nomeSolicitante}%'
    if banco.is_connected():
        cursor = banco.cursor()
        comandoSql = 'select * from solicitante where nome like %s'
        valor = (nomeDoSol,)
        cursor.execute(comandoSql, valor)
        return cursor.fetchall()

#Modifica o campo status da tabela solicitante, mudando de True para false. 
# Ai através desse campo sabemos se o chamado esta aberto ou fechado. 
def atualiza_chamado(id_chamado, dataF):
    cursor = banco.cursor()
    sql = 'update solicitante set status = false, dataFecha = %s  where idSolicitente = %s'
    valor = (dataF, id_chamado,)
    cursor.execute(sql, valor)
    banco.commit()
    return 'chamado concluido com sucesso!!!'

#verirfica se usuario e senha estão corretos.
def usuarios(nomeLog, senhaLog):
    comandoSelect = 'select nomeUser, senhaUser from usuarios where nomeUser like %s and senhaUser like %s'
    valorA = (nomeLog, senhaLog)
    cursor = banco.cursor()
    cursor.execute(comandoSelect, valorA)
    return len(cursor.fetchall())


#Cadastra usuário e senha na tabela usuarios, para fazer o login no sistema.  
def cadastro_usuarios(nome_user, senha_user, email_user):
    comdInsert = 'insert into usuarios(nomeUser, senhaUser, emailUser) values( %s, %s, %s)'
    cursor = banco.cursor()
    valores = (nome_user, senha_user, email_user)
    cursor.execute(comdInsert, valores)
    banco.commit()