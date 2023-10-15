# IOS
## Jailbreak IPHONE 7 - IOS 14.8
## CheckRa1n

Link: https://checkra.in/<br>
Vídeo: https://www.youtube.com/watch?v=ar4tq_6HYPk

- [ ] Inicie o checkra1n
- [ ] Pressione o botão de desligar junto com o botão de diminuir volume
- [ ] Quando a tela apagar, continue pressionando o botao de diminuir por 10 segundos
- [ ] O aparelho tem que entrar no modo DFU, no checkra1n click em Quit
- [ ] Em seguida na CLI digite **checkra1n -c**
- [ ] O APP do checkra1n vai aparece no telefone
- [ ] Acesse o APP e instale o Cydia
- [ ] Instale o APP Filza Manager

## Acesso o aparelho com o SSH
Link: https://blog.elcomsoft.com/2020/05/ios-jailbreaks-ssh-and-root-password/

O Cydia instalado com o checkra1n possui o pacote OpenSSH.

Para descobrir a senha do aparelho, acesse o arquivo localizado em /private/etc/master.password
A linha do usuário root possui o hash da senha **smx7MYTQIi2M** que é **alpine**
Em seguida, use o SSH para acessar o telefone. 

## Extrair o arquivo IPA do dispositivo

- [ ] Acessar o diretório do arquivo .app
```
cd /var/containers/Bundle/Application/
ls -l
```
- [ ] Localizar o arquivo do aplicativo
```
ls * | grep -B 2 -i 'nome-do-aplicativo'

Outra forma de localizar é acessar no dispositivo o Filza Manager o caminho
/var/containers/Bundle/Application/ e será possível ver o nome do aplicativo e o seu código
```
- [ ] Copiar o diretório .app para um diretório com o nome Payload
```
cp -r [nome-do-aplicativo].app/ Payload/
```
- [ ] Compressão do diretório Payload usando .zip
```
Adicione a extensão .ipa diretamente na compressão

zip -r /[caminho]/[nome-do-aplicativo].ipa Payload/

Se o ZIP não estiver instalado, usar o comando apt-get para instalar
```
- [ ] Transferir o arquivo para o computador local
```
scp root@[IP]:/Payload/[nome-do-aplicativo].ipa
```
## MOBSF - Mobile Security Framework
Use o MOBSF para fazer a análise estática do arquivo .ipa <br>
Link: https://github.com/MobSF/Mobile-Security-Framework-MobSF <br>
Link: https://mobsf.github.io/docs/#/installation?id=linuxmac (Instalação) <br>
Link: https://github.com/carineconstantino/hackingbr/blob/main/Resources/Mobile/docker.zip

## Aplicativos para bypass da detecção do Jailbreak

- [ ] Shadow <br>
Link: https://www.youtube.com/watch?v=C-CpVJwRnhI <br>
Link: https://github.com/jjolano/shadow
```
Adicionar a fonte no Cydia.

https://ios.jjolano.me/

Dentro do aplicativo habilitar o bypass no aplicativo-alvo 
```
- [ ] FlyJB <br>
Link: https://mrepo.org/package/4125 <br>
Link: https://yalujailbreak.net/flyjb/ <br>

- [ ] A-Bypass <br>
Link: https://onejailbreak.com/blog/a-bypass-tweak/ <br>

## Análise do binário do aplicativo 
Link: https://github.com/saladandonionrings/iOS-Binary-Security-Analyzer

- [ ] Instalar no Cydia o pacote Big Boss
Link: http://apt.thebigboss.org/repofiles/cydia/
 
- [ ] Instalar no Cydia do pacote optool_ios
    
- [ ] Instalar no dispositivo a ferramenta oTool
```
apt install otool
```
- [ ] Download o respositório do script para análise do binário
```
git clone https://github.com/saladandonionrings/ios-binary-checks.git
```

- [ ] Transfira o arquivo check-binary.sh para o dispositivo
```
scp check-binary.sh root@[IP]:/var/root
```

- [ ] Execute o análise no dispositivo
```
./check-binary.sh /var/containers/Bundle/Application/[HASH]/arquivo.app
```




