OWASP Amass é uma ferramenta de linha de comando que faz o mapeamento através de OSINT, coletando informações a partir de um domínio ou endereço IP.<P> 
Link: https://github.com/owasp-amass/amass/tree/master

```
# Enumeração de Subdomínios

amass enum -d [domain]

# Enumeração Passiva

amass enum -passive -d [domain]

# Enumeração Ativa

amass enum -active -d [domain]

# Enumeração de registros do IP
(ASN ID, SSL Certificate, Reverse Whois)

amass intel -addr [IP]

# Whois

amass intel -d [domain] -whois

# Brute-Force

amass enum -active -brute -w /usr/share/wordlists/API_superlist -d [domain] -dir [nome-do-diretório]
```

