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
- [ ] Localizar o arquivo do aplicativo UUID
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
./check-binary.sh /var/containers/Bundle/Application/[UUID]/arquivo.app
```

## Notas Teóricas

- [ ] O sistema operacional iOS é baseado no Darwin OS, no qual é originalmente da Apple e escrito em C, C++ e Objective-C
Link: https://developer.apple.com/library/ios/documentation/Miscellaneous/Conceptual/iPhoneOSTechOverview/Introduction/Introduction.html
- [ ] iOS Security Guide: https://www.apple.com/business/docs/iOS_Security_Guide.pdf
- [ ] Boot ROM contém o Apple Root CA public-key que é usada para verificar que os softwares carregados são confiáveis pela Apple
- [ ] Dispositivos que tem o processador A7 ou anteriores, possuem um processador chamado Secure Enclave
- [ ] O Secure Enclave é um processador separado que possui o próprio processo de boot e seu hardware gera um número randômico (key)
- [ ] Esse processador facilita as operações de criptografia no iOS
- [ ] As chaves do TouchID, FaceID e a senha definida pelo usuário (passcode) ficam no Secure Enclave, que possui uma chave randômica

## Prevenir Captura de tela
Função ```ApplicationDidEnterBackground()```
Link: https://developer.apple.com/library/archive/qa/qa1838/_index.html

A captura de tela fica armazenada no local ```/Library/Caches/Snapshots/```

## Keychain
Container criptografado que armazena senhas para aplicativos e serviços do IOS.
Usa criptogradia simétrica AES Key (passcode do usuário + salt (256 bit UID))
```
kSecAttrAccessibleAlways - itens marcados com esse atributo não são armazenados de forma segura na Kaychain. (Deprecated)
kSecAttrAccessibleAfterFirstUnlock - itens não podem ser acessados após o reboot até o dispositivo ser desbloqueado pelo usuário.
kSecAttrAccessibleWhenUnlocked - itens podem ser acessados apenas enquanto o dispositivo está desbloqueado.
"thisDeviceOnly" - pode ser habilitado nos 3 métodos citados. Quando habilitado, criptografa os itens da Keychain com o UID do device. Os itens da keychain no backup ficam inválidos.
```
Para manter a separação dos dados armazenados na Keychain, IOS usa o AppIdentifierPrefix (ID Apple) e o BundleIdentifier (User ID). 
Nas versões anteriores ao IOS 10.3 quando um aplicativo é deletado, IOS não deleta os itens desse aplicativo da Keychain. 

### Keychain Dump
Link: https://github.com/ptoomey3/Keychain-Dumper

## Cookies
IOS armazena os cookies dos aplicativos no diretório ```/private/var/mobile/Library/Cookies```, no arquivo cookies.binarycookies.

### Binary Cookie Parser
Link: https://github.com/mdegrazia/Safari-Binary-Cookie-Parser

### Keyboard Cache 
Localizado no diretório /private/var/mobile/Library/Keyboard

## Damm Vulnerable iOS App
Link: https://github.com/prateek147/DVIA-v2

## SSL Kill Switch
Disable SSL certification validation (Certificate Pinning)
Link: https://github.com/nabla-c0d3/ssl-kill-switch2

(Testar essas tools)
## CyCript
Link: http://www.cycript.org/

## IDB 
Link: https://github.com/facebook/idb

## Snoop-IT
Instale a partir do Cydia adicionando o repositório ```http://repo.nesolabs.de```

Link: https://code.google.com/archive/p/snoop-it/
Link: https://github.com/robdbirch/snoopit



