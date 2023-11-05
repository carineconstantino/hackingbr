## GoBuster
```
gobuster dir -u [IP] -w /usr/share/wordlists/dirb/common.txt -t 5
```

## WMAP 
```
load wmap

# Adiciona o IP do site
  
wmap_sites -a [IP]
  
# Adiciona o target

wmap_targets -t [IP]

# Lista os sites disponíveis  
  
wmap_sites -l

# Lista os targets disponíveis 
  
wmap_targets -l 
  
# Mostra os módulo disponíveis para scan

wmap_run -t 
  
# Executa o scan

wmap_run -e 
```

## HTTP Scan
```
Módulos:

[+] auxiliary/scanner/http/apache_userdir_enum

[+] auxiliary/scanner/http/brute_dirs

[+] auxiliary/scanner/http/dir_scanner

[+] auxiliary/scanner/http/dir_listing

[+] auxiliary/scanner/http/http_put

[+] auxiliary/scanner/http/files_dir

[+] auxiliary/scanner/http/http_login

[+] auxiliary/scanner/http/http_header

[+] auxiliary/scanner/http/http_version

[+] auxiliary/scanner/http/robots_txt
```

## Recon
```
theharvester
sublist3r
subfinder
truffleHog
Social Mapper
metagoofil
spiderfoot
recon-ng
maltego
Photon
gitrob
linkedin2username
sherlock
twint
Amass
aquatone
discover scripts
tinfoleak
Sn1per
JS-Scan
ReconPi

Shodan.io
Censys.io
Hunter.io
ZoomEye.org
WiGLE.net
PublicWWW.com
Pulsedive.com
Intelx.io
reposify.com
viz.greynoise.io

Grep App
Binary Edge
ONYPHE
GreyNoise
Fofa
LeakIX
IntelligenceX
Netlas
URL Scan
PublicWWW
FullHunt
CRT sh
Vulners
Pulsedive
Packet Storm ecurity
GrayHatWarefare
```
