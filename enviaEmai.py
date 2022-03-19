#Codigo para transferir dados voa smtp
from email import message
import smtplib

from email.message import EmailMessage

EMAIL_LOGIN = 'misterlarry06@gmail.com'
SENHA_LOGIN = 'Iagooliver14##'

def envia_email(localSol, nomeSol, dataSol, setorSol, comentarioSol, statusSol, dataFec):
    #cria um objeto do tipo EmailMessagem
    mensagem = EmailMessage()
    mensagem['Subject'] = 'ABERTURA DE CHAMADO'
    #rementente
    mensagem['From'] = 'misterlarry06@gmail.com'
    #destinatario
    mensagem['To'] = 'misterlarry06@gmail.com'
    #mensagem do email
    mensagem.set_content(f'{localSol} - {nomeSol} - {dataSol} - {setorSol} - {comentarioSol} - {statusSol} - {dataFec}')

    #classe que nos retorna uma conexão
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(EMAIL_LOGIN, SENHA_LOGIN)
        servidor.send_message(mensagem)

    return 'enviado com sucesso'

def envia_email_concluir():
    #cria um objeto do tipo EmailMessagem
    mensagem = EmailMessage()
    mensagem['Subject'] = 'Conclusão de Chamado'
    #rementente
    mensagem['From'] = 'misterlarry06@gmail.com'
    #destinatario
    mensagem['To'] = 'misterlarry06@gmail.com'
    #mensagem do email
    mensagem.set_content('Chamado concluido com sucesso!!!')

    #classe que nos retorna uma conexão
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(EMAIL_LOGIN, SENHA_LOGIN)
        servidor.send_message(mensagem)

    return 'enviado com sucesso'
