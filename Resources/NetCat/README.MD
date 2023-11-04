NETCAT é uma ferramenta que pode ser usada como cliente para conexão com o servidor web.

```
nc -V [site/IP] 80
GET / HTTP/1.0

Obs.: é necessário dar o espaço para ocorrer a divisão do header do body com \r\n

printf "HEAD / HTTP/1.0\r\n\r\n" | nc [IP] 80

echo -e "HEAD / HTTP/1.0\r\n\r\n" | nc [IP] 80

# mostra o header apenas
curl -I [site/IP]

# mostra toda a requisição e resposta
curl -v [site/IP]
```
Dessa forma, a conexão com o servidor web ocorre e retorna o código fonte HTML da página.
Também podemos usar o NetCat para fazer scan. 

```
# Ping Sweep
for i in $(seq 1 254); do nc -zv -w 1 172.16.1.$i 445; done

# TCP
nc -nvv -w 1 -z [IP] [port-range 3388-3390]

# UDP
nc -nv -u -z -w 1 [IP] [port-range 120-123]
```
