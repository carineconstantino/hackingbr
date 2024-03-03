## Firebase Config
É um serviço que armazena configurações que podem ser facilmente modificada pelos desenvolvedores. As informações podem ser publicas, no entanto, é importante não armazenar dados como credenciais, chaves de API e outras informações úteis na formulação de um ataque.<br>
Para acessar as configurações do Firebase são necessários os seguintes dados:<br>
- Google API Key
- Google APP ID
- Google Project ID<br>
No IOS essas informações podem ser localizadas no arquivo GoogleService-Info.plist. 
```
curl -v -X POST "https://firebaseremoteconfig.googleapis.com/v1/projects/[NOME/ID]/namespaces/firebase:fetch?key=[API KEY]" -H "Content-Type: application/json" --data '{"appId": "[ID]", "appInstanceId": "[NOME]"}'
```
Se o retorno do comando for "state: NO_TEMPLATE" indica que a aplicação não usa o Firebase Remote Config ou não há configuração habilitada.<br>
Se o retorno do comando for "state: UPDATE" as configurações serão retornadas. 
