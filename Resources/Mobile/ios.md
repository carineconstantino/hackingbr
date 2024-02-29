# IOS
## Jailbreak IPHONE 7 - IOS 14.8
## CheckRa1n

Link: https://checkra.in/<br>
Vídeo: https://www.youtube.com/watch?v=ar4tq_6HYPk<br>
Ref.: https://aupsham98.medium.com/practical-ios-penetration-testing-a-step-by-step-guide-8214d35aaf3c<p>

O Checkra1n é compatível com versões do IOS até a 14.<br>
Ver a versão no dispositivo: Settings > Genral > About on your device<br>

- [ ] Inicie o checkra1n
- [ ] Pressione o botão de desligar junto com o botão de diminuir volume
- [ ] Quando a tela apagar, continue pressionando o botao de diminuir por 10 segundos
- [ ] O aparelho tem que entrar no modo DFU, no checkra1n click em Quit
- [ ] Em seguida na CLI digite **checkra1n -c**
- [ ] O APP do checkra1n vai aparecer no telefone
- [ ] Acesse o APP e instale o Cydia
- [ ] Instale o APP Filza Manager

## Cydia - Package Manager for Jailbroken IOS
Adicione os repositórios: Manage > Sources > Edit > Add

- [ ] https://cydia.akemi.ai (Karen's Repo)
- [ ] https://build.frida.re (Frida Repo)

Instale os seguintes pacotes:<br>
Search > [nome-do-pacote] > Install<br>

- HideJB
- Frida
- Appsync Unified (Permite a instalação de aplicativos auto-assinados, assinatura-fake, não-assinados, arquivos expirados)

## iDevice
Link: https://github.com/libimobiledevice/ideviceinstaller

### Ver o nome do device conectado
```
idevicename
```

### Instalar o arquivo IPA no dispositivo
```
ideviceinstaller - i [nome-do-arquivo].ipa
```

## Acesso o aparelho com o SSH
Link: https://blog.elcomsoft.com/2020/05/ios-jailbreaks-ssh-and-root-password/

O Cydia instalado com o checkra1n possui o pacote OpenSSH.

Para descobrir a senha do aparelho, acesse o arquivo localizado em /private/etc/master.password
A linha do usuário root possui o hash da senha **smx7MYTQIi2M** que é **alpine**
Em seguida, use o SSH para acessar o telefone. 

## SSL Kill Switch 2 
Instalação do SSL KILL Switch 2:

- Acesse o dispositivo com o SSH
- Acesse a pasta /tmp
- Download o SSL Kill Switch 2
  ```
  wget https://github.com/nabla-c0d3/ssl-kill-switch2/releases/download/0.14/com.nablac0d3.sslkillswitch2_0.14.deb .
  ```
- Instale o pacote
  ```
  dpkg -i com.nablac0d3.sslkillswitch2_0.14.deb
  ```
- Reinicie o SpringBoard
  ```
  killall -HUP SpringBoard
  ```

## Extrair o arquivo IPA do dispositivo

- [ ] Acessar o diretório do arquivo .app
```
cd /private/var/containers/Bundle/Application/
```
- [ ] Localizar o arquivo do aplicativo UUID
```
ls * | grep -B 2 -i 'nome-do-aplicativo'

Outra forma de localizar é acessar o caminho pelo Filza Manager
/var/containers/Bundle/Application/ e será possível ver o nome do aplicativo e o seu código UUID

Outra forma é buscar dentro da pasta /var
find /var/ -name "*.app"
```
- [ ] Copiar o diretório .app para um diretório com o nome Payload
```
cp -r [nome-do-aplicativo].app/ Payload/
```
- [ ] Compressão do diretório Payload usando .zip
```
Adicione a extensão .ipa diretamente na compressão

zip -r Payload/[nome-do-aplicativo].ipa Payload/

Se o ZIP não estiver instalado, usar o comando apt-get para instalar
```
- [ ] Transferir o arquivo para o computador local
```
scp root@[IP]:/private/var/containers/Bundle/Application/[UUID]/Payload/[nome-do-aplicativo].ipa
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

## OTOOL - Análise do binário do aplicativo 
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

- [ ] Execute a análise no dispositivo
```
./check-binary.sh /var/containers/Bundle/Application/[UUID]/arquivo.app
```

## Diretórios do Aplicativo 
```
## Arquivos do APP
/var/mobile/Containers/Data/Application/[UUID-do-Aplicartivo]/Library/Application Support/[nome-do-pacote-do-aplicativo]

## .plist
/var/mobile/Containers/Data/Application/[UUID-do-Aplicativo]/Library/Preferences
```
## Comandos Frida
```
## Ver os devices conectados 
frida-ls-devices

## Ver os aplicativos
frida-ps -Uai
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

Copia o executável keychain_dumper para o dispositivo móvel no diretório /tmp<p>
Atribui permissão de execução ```chmod +x keychain_dumper```<p>
Verfica se o arquivo keychain-2.db tem permissão de leitura<p>
```
ls -l /private/var/Keychains/keychain-2.db

## Atribui permissão de leitura
chmod +r /private/var/Keychains/keychain-2.db
```
## Memory Dump
### Objection
```
## Load APP
objection -g [app-nome-do-pacote] explore

## Lista os módulos em memória
memory list modules

## Lista os módulos exportados em memória do APP
memory list exports [app-nome-do-pacote]

## Procura por strings em memória
memory search [string-to-search] --string
```

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

## Ver arquivos de "auto screenshots" .ktx
Link: https://github.com/ydkhatri/MacForensics/tree/master<p>
Na máquina Windows, fazer o download do executável e arrastar o arquivo .ktx para cima do .exe, assim vai ser gerado um arquivo .png
```
## Local onde os arquivos .ktx ficam armazenados
/var/mobile/Containers/Data/Application/$APP_ID/Library/SplashBoard/Snapshots/sceneID:$APP_NAME-default/
```

(Testar essas tools)
## CyCript
Link: http://www.cycript.org/

## IDB 
Link: https://github.com/facebook/idb

## Snoop-IT
Instale a partir do Cydia adicionando o repositório ```http://repo.nesolabs.de```

Link: https://code.google.com/archive/p/snoop-it/<p>
Link: https://github.com/robdbirch/snoopit

## Hooper 
Link: https://www.hopperapp.com/

