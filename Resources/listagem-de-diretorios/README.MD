## Correção no Apache

Listagem de diretórios acessível ocorre quando um diretório do servidor web fica acessível pois não possui um arquivo index.html para apresentar uma página ao acessar o servidor. 
Ao acessar um servidor que não tem o arquivo index.html, todos os arquivos naquele diretório ficam acessíveis. 
No Apache, no arquivo de configuração /etc/apache2/apache2.conf, para bloquear o acesso aos diretórios do servidor web, basta remover o parâmetro Indexes na configuração de `/var/www`. 
