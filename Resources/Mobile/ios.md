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
## Comandos Frida
```
## Ver os devices conectados 
frida-ls-devices

## Ver os aplicativos
frida-ps -Uai
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
## Extrair o arquivo IPA do dispositivo com Frida IOS Dump
Link: https://github.com/AloneMonkey/frida-ios-dump

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
## OTOOL - PIE (Position Independent Executable)
O binário do aplicativo não possui a flag fPIE-pie<br>
ASLR (Address Space Layout Randomization) protege o binário do aplicativo iOS contra vulnerabilidades de "memory corruption" (Buffer Overflow), randomizando a localização dos objetos do aplicativo na memória cada vez que o aplicativo é reiniciado. O ASLR é implementado compilando o binário do aplicativo iOS com a flag PIE.<br> 
Ref.: https://medium.com/cybersecurityservices/analyzing-the-ipa-file-of-an-ios-based-application-9c0a1749fe69<br>
Quando o ASLR é ativado, o aplicativo é carregado em um endereço de memória aleatório sempre que é iniciado, dificultando a previsão do endereço de memória inicial.
```
otool -hv [nome-do-app] | grep PIE   # It should include the PIE flag
```
```
otool -Vh [nome-do-app]
```
## OTOOL - Stack Canaries (fstack-protector flag)
"Stack Canary" é um valor adicionado antes da execução de uma função, ou seja, é adicionado na "pilha de execução" para checar a ocorrência de Buffer Overflow. A checagem ocorre no inicio e não final da "pilha". Se o aplicativo tiver a flag ```stack_chk_guard``` habilitada, a proteção está ativa. Aplicativo desenvolvidos em Swift possuem esssa proteção por padrão. No entanto, aplicativos desenvolvidos em Objective-C code e C/C++ podem estar vulneráveis caso a proteção não esteja habilitada. 
```
otool -I -v [nome-do-aplicativo] | grep stack_chk
```
## OTOOL - ARC (Automatic Reference Counting - fobjc-arc)
Previne falhas comuns de "memory corruption". O retorno deve mostrar a flag objc_release para indicar que o aplicativo encontra-se protegido. 
```
otool -I -v [nome-do-app] | grep objc_release
```
## OTOOL - Encrypted Binary
```
otool -arch all -Vl [nome-do-app] | grep -A5 LC_ENCRYPT
```
## OTOOL - Hash Algoritmos Inseguros
Algoritmos como MD5 e SHA1 usados em uma função Hash são considerados inseguros devido a vulnerabilidades de "colisão". Além disso, eles podem ser quebrados em sites com uma grande base ou por ferramentas como Hashcat. O impacto do uso desses algoritmos depende de onde está sendo usado. Se estiverem sendo usados para criar hash de informações confidenciais, um invasor pode tentar quebrar esses hashes. 
```
otool -I -v [nome-do-app] | grep -w "_CC_MD5" ou -w "_CC_SHA1"
```
## OTOOL - Insegure Random Functions
Ref.: https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator<br>
https://medium.com/cybersecurityservices/analyzing-the-ipa-file-of-an-ios-based-application-9c0a1749fe69<br>
Essas funções são consideradas inseguras pois geram números randônicos que podem ser previstos por um atacante. 
```
otool -I -v [nome-do-app] | grep -w "_random"
otool -I -v [nome-do-app] | grep -w "_srand"
otool -I -v [nome-do-app] | grep -w "_rand"
```
## OTOOL - Insecure 'Malloc' Fuction
Ref.: https://www.diffen.com/difference/Calloc_vs_Malloc<br>
A função "malloc" é considerada insegura mantém os valores alocados em memória quando a função é iniciada. Esse comportamento é considerado um risco de segurança porque o conteúdo da memória não é precisto e erros ao iniciar a função podem resultar no vazamento deste conteúdo. É recomendado usar a função "calloc" que ao ser iniciada, a região de alocação da memória inicia com zero. 
```
otool -I -v [nome-do-app] | grep -w "_malloc"
```
## OTOOL - Funções vulneráveis
Ref.: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/BufferOverflows.html<br>
Funções Obsoletas que são vulneráveis a buffer overflow. No IOS a exploração de buffer overflow com essas funções tem uma complexidade alta. A recomendação para não usar essas funções constituí boas práticas de segurança. 
```
otool -I -v [nome-do-app] | grep -w "_gets"
otool -I -v [nome-do-app] | grep -w "_memcpy"
otool -I -v [nome-do-app] | grep -w "_strncpy"
otool -I -v [nome-do-app] | grep -w "_strlen"
otool -I -v [nome-do-app] | grep -w "_vsnprintf"
otool -I -v [nome-do-app] | grep -w "_sscanf"
otool -I -v [nome-do-app] | grep -w "_strtok"
otool -I -v [nome-do-app] | grep -w "_alloca"
otool -I -v [nome-do-app] | grep -w "_sprintf"
otool -I -v [nome-do-app] | grep -w "_printf"
otool -I -v [nome-do-app] | grep -w "_vsprintf"
```

## Diretórios do Aplicativo 
```
## Arquivos do APP
private/var/mobile/Containers/Data/Application/[UUID-do-Aplicartivo]/Library/Application Support/[nome-do-pacote-do-aplicativo]

## .plist
/var/mobile/Containers/Data/Application/[UUID-do-Aplicativo]/Library/Preferences
```
## Info.plist
```
## Objection
ios plist cat Info.plist

## Linux
plistutil -i Info.plist -o Infoxml.plist
```
## Arquivos e Diretórios para analisar

Bundle directories = private/var/containers/Bundle/Application<br>

- [ ] Info.plist = configurações do aplicativo
- [ ] _CodeSignature = contém arquivos plist com assinatura para todos os arquivos do Bundle
- [ ] Assets.car = formato .zip que contém os ativos usados pelo aplicativo, como icones
- [ ] Frameworks = diretórios com bibliotecas nativas (.dylib ou .framework)
- [ ] PlugIns = diretório contém extensão de plugIns
- [ ] Core Data = armazena dados para uso offline, cache, dados temporários
- [ ] PkgInfo = arquivo que é uma alternativa para especificar tipos e códigos para o aplicativo
- [ ] en.lproj, Base.lproj = arquivos com a definição de linguagem

Data directories = /var/mobile/Containers/Data/Application

- [ ] Documents
- [ ] Library
- [ ] StoreKit
- [ ] SystemData
- [ ] tmp


## Objection - Cookies
```
ios cookies get --json
```
## Cookies
IOS armazena os cookies dos aplicativos no diretório ```/private/var/mobile/Library/Cookies```, no arquivo cookies.binarycookies.

## idevice
Ref.: https://github.com/libimobiledevice/libimobiledevice<br>

#### Ver o ID do dispositivo
```
idevice_id
```

#### Ver os logs
```
idevicesyslog -u idevice_id | grep "[nome-do-app]"
```

## Prevenir captura de tela
Função ```ApplicationDidEnterBackground()```<br>
Link: https://developer.apple.com/library/archive/qa/qa1838/_index.html

A captura de tela fica armazenada no local ```/Library/Caches/Snapshots/```

## Ver arquivos de "auto screenshots" .ktx
Link: https://github.com/ydkhatri/MacForensics/tree/master<br>
Na máquina Windows, fazer o download do executável e arrastar o arquivo .ktx para cima do .exe, assim vai ser gerado um arquivo .png
```
## Local onde os arquivos .ktx ficam armazenados
/var/mobile/Containers/Data/Application/$APP_ID/Library/SplashBoard/Snapshots/sceneID:$APP_NAME-default/
```

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
Link: https://github.com/ptoomey3/Keychain-Dumper<br>

Copia o executável keychain_dumper para o dispositivo no diretório /tmp<br>
Atribui permissão de execução ```chmod +x keychain_dumper```<br>
Verfica se o arquivo keychain-2.db tem permissão de leitura<br>
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

