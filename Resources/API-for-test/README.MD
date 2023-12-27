## API para Teste (externo)

Ambas são aplicações desenvolvidas para testar as ferramentas e as técnicas de hacking em API. 
APISec.ia disponibiliza um laboratório hacking para API que você pode usar para praticar. 

crAPI é localizada em [crapi](http://crapi.apisec.ai/login)<p>
vAPI é localizada em [vapi](http://vapi.apisec.ai/)

Você também pode configurar localmente as APIs de teste. 


## The Completely Ridiculous API (crAPI)

Link: https://github.com/OWASP/crAPI
```
$mkdir ~/lab
$cd ~/lab
curl -o docker-compose.yml https://raw.githubusercontent.com/OWASP/crAPI/main/deploy/docker/docker-compose.yml
docker-compose pull
docker-compose -f docker-compose.yml --compatibility up -d
```

Após a instalação, você pode acessar localmente a API no endereço http://127.0.0.1:8888 para ter acesso a crAPI landing page ou http://127.0.0.1:8025 a aplicação crAPI Mailhog Server. 

O comando para para a execução da API é: 
```
docker-compose stop
```

Caso você tenha problemas durante a instalação local, existe a opção da versão de desenvolvimento que pode ser acessada no link abaixo:
https://github.com/OWASP/crAPI

## vAPI

vAPI é outra aplicação disponível para instalação local. Eu recomendo a instalação dessa aplicação pois durante o curso ela será usada para prática das técnicas que vamos aprender. 

Link: https://github.com/roottusk/vapi

cd ~/lab
git clone https://github.com/roottusk/vapi.git
cd /vapi
docker-compose up -d

Após a instalação, a aplicação você acessar a aplicação localmente no endereço http://127.0.0.1/vapi

Depois de validar o funcionamento da API, veja que os arquivos .json com a estrutura da API são disponibilizados no diretório vapi/postman



Faça a importação dos dois arquivos .json para o Postman



No diretório Resources, você encontra as Secrets necessárias para completar a execução dos ataques. 



## Outros laboratórios disponíveis 

Portswigger
https://portswigger.net/web-security


Try Hack Me
https://tryhackme.com/room/bookstoreoc -- free

https://tryhackme.com/room/idor -- pago

https://tryhackme.com/room/carpediem1 -- pago


Hack The Box Lab 
https://www.hackthebox.com/hacker/hacking-labs

• Craft
• Postman
• JSON
• Node
• Help

Github Vulnerable App

Pixi
https://github.com/DevSlop/Pixi

RestApiGoat
https://github.com/optiv/rest-api-goat

DVWS Node
https://github.com/snoopysecurity/dvws-node

Web Sheep
https://github.com/marmicode/websheep
