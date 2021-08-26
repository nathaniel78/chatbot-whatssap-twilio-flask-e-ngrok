## Chatbot com python ngrok e twilio

Esse pequeno projeto foi uma adaptação de um ótimo tutorial sobre a implantação de um chatbot com integração ao whatssap usando o twilio e ngrok do Miguel Grinberg,  https://www.twilio.com/blog/construa-chatbot-whatsapp-python-flask-twilio. Fiz alguns ajustes para receber e realizar a consulta ao dicionário do https://significado.herokuapp.com com api desenvolvida por Tiago Nelsi, https://github.com/ThiagoNelsi/dicio-api.

### Configurações necessárias

Realizei os teste criando uma VM no virtualbox com o ubuntu, instalei pip3, venv, screen, unzip, wget e download do executável do ngrok.

```markdown
# Versões instaladas

1. Ubuntu 20.04.2 LTS
2. Python 3.8.10 
3. ngrok version 2.3.40
4. Screen version 4.08.00 (GNU) 05-Feb-20
5. GNU Wget 1.20.3 built on linux-gnu.
6. UnZip 6.00 of 20 April 2009, by Debian. Original by Info-ZIP.

```

```markdown
# Comandos
- #apt-get update
- apt-get install python3-pip python3-venv
- apt-get install wget unzip

## Para realizar o download do ngrok basta realizar o cadastro no site https://ngrok.com/ e depois de descompactado ative o ngrok com a authtoken.
- wget versão_ngrok.zip
- unzip ngrok*

## Vamos criar um diretório para receber nosso virtual-env e instalar os pacotes python necessários e realizar a instalação e execução do script bot.py
- #screen -S sap
- #mkdir whatsapp-bot
- #cd whatsapp-bot
- python3 -m venv whatsapp-bot-venv
- source whatsapp-bot-venv/bin/activate
- whatsapp-bot-venv) $ pip3 install twilio requests
- (whatsapp-bot-venv) $ pip3 install Flask==1.1.0
- 
## Verificar os pacotes instalados
- (whatssap-bot-venv) root@ubuntu-whatssap:~# pip3 freeze

## pacontes pip
- certifi==2021.5.30
- charset-normalizer==2.0.4
- click==8.0.1
- Flask==1.1.0
- idna==3.2
- itsdangerous==2.0.1
- Jinja2==3.0.1
- MarkupSafe==2.0.1
- PyJWT==1.7.1
- pytz==2021.1
- requests==2.26.0
- six==1.16.0
- stdin==2020.12.3
- twilio==6.63.0
- twilio-stubs==0.1.0
- urllib3==1.26.6
- Werkzeug==2.0.1

## Cadastro no site twilio para integrar ao whatssap, basta realizar o cadastro no site https://www.twilio.com/ e realizar as configurações na aba Messaging -> Settings -> Whattsap sendobox setting, na opção WHEN A MESSAGE COMES IN HTTPS Post gerada no ngrok acrescido de /bot no final, gerando um link, algo como https://fc72-191-189-11-148.ngrok.io/bot, lembrando que a cada reinicio do serviço ngrok ele vai gerar nova url que deve ser alterada no twilio. Lembrando que você vai ter que validar seu telefone para no twilio para realizar o teste com o chatbot via whatssap.
- (whatssap-bot-venv) root@ubuntu-whatssap:~# python3 bot.py
### Sair do screen
- CTRL + A + D
### Vai executar o servidor python localhost na porta 5000. Fica aguardando a conexão, caso apareça 200 está ok
- Serving Flask app "bot" (lazy loading)
- Environment: production
- WARNING: This is a development server. Do not use it in a production deployment.
- Use a production WSGI server instead.
- Debug mode: off
- Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Executando o ngrok
- #./ngrok http 5000
### Vai gerar uma url estática que possibilita a conexão com o twilio, vai gerar uma tela com as informações abaixo
- ngrok by @inconshreveable                                                   (Ctrl+C to quit)
- Session Status                online
- Account                       email@gmail.com (Plan: Free)
- Version                       2.3.40
- Region                        United States (us)
- Web Interface                 http://127.0.0.1:4040
- Forwarding                    http://fc72-191-189-11-148.ngrok.io -> http://localhost:5000
- Forwarding                    https://fc72-191-189-11-148.ngrok.io -> http://localhost:5000
- Connections                   ttl     opn     rt1     rt5     p50     p90
-                               0       0       0.00    0.00    0.00    0.00
### Sair do screen
- CTRL + A + D

### Monitorar o terminais screen
- #screen -ls
### Monitorar o terminais screen
- #screen -r nome_ou_id_screen

# No final estiver tudo ok você pode realizar o teste com o chatbot do twilio que vai aparecer no seu whattsap. Fazendo alguns ajustes dá para conectar a outras api realizando consulta

# Dicas e sites:
- https://chatterbot.readthedocs.io/en/stable/setup.html
- https://www.twilio.com/blog/construa-chatbot-whatsapp-python-flask-twilio
- https://github.com/ThiagoNelsi/dicio-api
- https://www.twilio.com/
- https://ngrok.com/
- https://api.dicionario-aberto.net/index.html
- https://api.nasa.gov/
- https://openweathermap.org/api

```

