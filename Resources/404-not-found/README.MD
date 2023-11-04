## 404 Not Found

Correção para não mostrar informações do servidor web ao retornar o código 404 Not Found. 

## Correção no Apache
404 Not Found mostra a versão do servidor web e para corrigir essa falha, no Apache, acesse o arquivo /etc/apache2/conf-enabled/security.conf 
e altere o parâmetro ServerTokens para o valor Prod e altere o parâmetro ServerSignature para Off, removendo assim toda a informação sobre o servidor web 
quando um recurso retorna o status 404 Not Found. 
