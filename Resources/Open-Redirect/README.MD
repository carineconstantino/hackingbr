## Open Redirect
### Exemplo com o botão "Voltar"
+ Payload
```
https://exemplo-site-alvo.com.br/post?postId=1&url=https://exemplo-attack-server.net/
```
### Sink Open Redirect
```
location
location.host
location.hostname
location.href
location.pathname
location.search
location.protocol
location.assign()
location.replace()
open()
element.srcdoc
XMLHttpRequest.open()
XMLHttpRequest.send()
jQuery.ajax()
$.ajax()
```
