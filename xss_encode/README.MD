<p align="center">
    <img width="500" src="html_scan.png" alt="HTML SCAN"><p></p>
    <a href="https://github.com/carineconstantino/hackingbr">@hackingbr></a>
</p>

## XSS Encode Tool
XSS Encode é uma ferramenta em python para testar se uma página é vulnerável ao ataque de XSS do tipo refletido. A partir de uma lista de payloads, a ferramenta executa teste no parametro da URL e consegue identificar quando a página é vulnerável. No código do payload é aplicado o formato url-encode para o bypass de filtros em WAF - Web Application Firewall. 

## Exemplo
```
python3 xss_encode.py --url exemplo.com --p cat
```
### XSS Refletido identificado
<p align="left">
    <img width="500" src="xss_encode_exemplo.png"><p></p>
</p>

### Resultado no HTML
<p align="left">
    <img width="500" src="html_scan_report.png"><p></p>
</p>

#

