from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    msg_recebida = request.values.get('Body', '').lower()
    resposta = MessagingResponse()
    msg_enviada = resposta.message()
    valida = False

    # valida o msg_recebida 
    if msg_recebida:
        # faz a consulta no api do site dicionario online com o valor recebido em msg_recebida
        requisicao = requests.get('https://significado.herokuapp.com/'+msg_recebida)
        # valida requisicao com status, se for 200 está ok 
        if requisicao.status_code == 200:
            # recebe o valor da api json
            data = requisicao.json()
            # filtra a pesquisa, mais orientações https://github.com/ThiagoNelsi/dicio-api
            filtro = data[0]["meanings"][0]
            filtro += data[0]["meanings"][1]
            filtro += data[4]["etymology"]

            msg_enviada.body(filtro)
            valida = True
        else:
            filtro = 'Não consegui realizar a pesquisa, desculpe.'
            msg_enviada.body(filtro)
            valida = True
    else:
        msg_enviada.body('Apenas palavras para consulta no dicionário, desculpe!')
        valida = True

    return str(resposta)
if __name__ == '__main__':
   app.run()