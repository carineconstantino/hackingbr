Kiterunner é uma excelente ferramenta desenvolvida e lançada pela Assetnote. 
Kiterunner é atualmente a melhor ferramenta disponível para descobrir endpoints e recursos de API. 
Embora ferramentas de força bruta de diretório como Gobuster/Dirbuster/ funcionem para descobrir caminhos de URL, normalmente elas dependem de solicitações HTTP GET padrão. 
O Kiterunner não apenas usará todos os métodos de solicitação HTTP comuns às APIs (GET, POST, PUT e DELETE), mas também imitará estruturas de caminho de API comuns. 
Em outras palavras, em vez de solicitar GET /api/v1/user/create, o Kiterunner tentará POST /api/v1/user/create, imitando uma solicitação mais realista.

## Instalação
```
git clone https://github.com/assetnote/kiterunner.git
cd kiterunner
make build
ln -s /opt/kiterunner/dist/kr /usr/bin/kr
```

## Scan
```
# wordlist routes-small.kite
kr scan [domain] -w routes-small.kite -x 20 -j 1 --fail-status-codes 400,401,404,403,501,502,426,411

# generic wordlist - brute-force option
kr brute [domain] -w /usr/share/dirb/wordlists/common.txt

# Replay request
kr kb replay "GET  414 [    183,    7,   8]://192.168.50.35:8888/api/privatisations/count 0cf6841b1e7ac8badc6e237ab300a90ca873d571" -w ~/api/wordlists/data/kiterunner/routes-large.kite
```

