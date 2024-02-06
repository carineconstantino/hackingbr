## Android Pentest
### Checklist 
```
[1] Análise estática do código - Tools
  - apktools
  - dex2jar
  - jd-gui
  - jadx
  - MOBSF - Mobile Security Framework

[2] Log Inseguro
  - logcat
  - pidcat

[3] Hardcoded
  - jd-gui
  - jadx
  - MOBSF
  - JNI (Biblioteca vulnerável)
      - comando strings [nome-da-biblioteca]
      - objdump -s [nome-da-biblioteca
      - rodata (constantes)

[4] Armazenamento inseguro
  - shared_prefs
  - SQLite databases
  - Armazenamento interno
  - Armazemaneto externo (/mnt/sd-card)

[5] Validação da entrada de dados (usa o logcat ou pidcat durante a validação) 
  - SQL Injection
  - XSS

[6] Validação da entrada de dados
  - URL externa
  - Arquivo interno

[7] Activities
  - exported=true

[8] Content Provider
  - exported=true

[9] Broadcast 

[10] Memory Corruption
```
## unzip APK 
```
Apenas mostra os arquivos mas não é possível ler
unzip [app.apk] -d [app-name]
```
## APKTools 
```
### Decompilhando
java -jar apktools.jar d [app.apk] -o [nome-output]

### Compilando (APK alterado)
java -jar apktools.jar b [diretorio-do-app]

### Script para fazer a compilação e assinatura do APK
Link: https://github.com/carineconstantino/pentest-scripts/blob/main/CVE/mobile/android/compile_sign.zip
```
## Dex2Jar
```
dex2jar.sh [app.apk] -o [app.jar]
```
## D2j-dex2jar
Link: https://github.com/pxb1988/dex2jar/releases
```
./d2j-dex2jar [base.apk] -o [base.jar]
```
## JD-GUI
```
java -jar jd-gui.jar [app.jar]
```
## JADX
```
### CLI 
jadx [app].apk -d [output-nome]

### GUI
jadx-gui [app].apk
```
### ADB - Android Debug Bridge
Link: https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8
```
adb devices = lista devides (-d devices / -e emuladores / -s serial)
adb shell = acessa shell do device
adb shell su = acessa shell como root
adb shell [command] = executa um comando no device
adb push teste.txt /data/local/tmp = copia dados para o android
adb pull /data/local/tmp/teste.txt = pega dados do android
adb install file.apk = instala o app manualmente
adb uninstall package = desinstala o app
adb kill-server = encerra o serviço do adb
adb start-server = inicia o serviço do adb
```

## APKSigner (ver as assinaturas do APK)
```
apt install -y apksigner
```

## Activities
Guia para Activities: https://developer.android.com/guide/appendix/app-intents?hl=pt-br<p>
Referências:<p>
https://developer.android.com/topic/security/risks/android-exported<p>
https://developer.android.com/guide/components/activities/background-starts<p>
https://developer.android.com/guide/components/activities/intro-activities<p>
https://aupsham98.medium.com/exploiting-android-activity-activity-android-exported-true-93ffeb263682<p>
https://book.hacktricks.xyz/mobile-pentesting/android-app-pentesting#exploiting-exported-activities-authorisation-bypass<p>

```
### Start Activity pelo ADB

./adb shell am start [package-name]/[activity-name]
./adb shell am start -n [package-name]/[activity-name]
./adb shell am start -a android.intent.action.VIEW https://[site] = realiza a ação de abrir o site
./adb shell am start -a android.intent.action.CALL -d tel:[numero-do-telefone] = realiza a ação de ligar para um número
./adb shell am start -a android.intent.action.VIEW geo:0,0?=[palavra-para-buscar] = realiza a ação de fazer uma busca no Google Maps
./adb shell am start -a android.intent.action.VIEW content://contacts/people = realiza a ação de abrir a lista de contatos

### Start Activity dentro do dispositivo

am start [package-name]/[activity-name]
am start -n [package-name]/[activity-name]
am start -a android.intent.action.VIEW https://[site] = realiza a ação de abrir o site
am start -a android.intent.action.CALL -d tel:[numero-do-telefone] = realiza a ação de ligar para um número
am start -a android.intent.action.VIEW geo:0,0?=[palavra-para-buscar] = realiza a ação de fazer uma busca no Google Maps
am start -a android.intent.action.VIEW content://contacts/people = realiza a ação de abrir a lista de contatos
```
### Start Services in Background
```
### Dentro do dispositivo
-n = componente

am start-service -n [nome-do-pacote/nome-do-serviço]
am stopservices -n [nome-do-pacote/nome-do-serviço]
am start-service -n [nome-do-pacote/nome-do-serviço] -a [nome-da-action]

Exemplo: am start-service -n com.android.music/com.android.music.MediaPlaybackService

am start-service -n org.owasp.android/.services.LocationService -a org.owasp.android.services.LocationServices
```
### Deep Links
Link: https://medium.com/mobis3c/deep-link-exploitation-introduction-open-unvalidated-redirection-b8344f00b17b<p>
Link: https://inesmartins.github.io/exploiting-deep-links-in-android-part1/index.html<p>
Link: https://redfoxsec.com/blog/protect-your-android-app-preventing-exploitation-of-deep-links/
```
./adb shell am start -W -a android.intent.action.VIEW -d [schema]://[host]/[path]
```
### PendingIntent
Link: https://www.youtube.com/watch?v=pc8ZKl5XG24<p>
Link: https://valsamaras.medium.com/pending-intents-a-pentesters-view-92f305960f03

### Memory DUMP 
#### Frida Dump
Link: https://github.com/Nightbringer21/fridump

## JAD Decompiler
Link: https://varaneckas.com/jad/<p>
Para o Ubuntu 22.04 usei o Jad 1.5.8e for Linux (statically linked)

### Alterar uma classe java para testar
[1] Unzip os arquivos do .apk<p>
[2] Converter o arquivo classes.dex to .jar com dex2jar<p>
[3] Unzip o arquivo .jar<p>

[4] Converter os arquivos .java para .jad<p>
```./jad [nome-do-arquivo].class```

[5] Compilar o arquivo .jad para .java apenas fazendo uma cópia .java<p>
[6] Modifica o código<p>
[7] Compilar o arquivo .java<p> 
```javac [nome-do-arquivo].java```<p>
[8] Executa o código modificado<p> 
```java [nome-do-arquivo].java```

## Arquivo Default.realm
Para ler esse arquivo é necessário instalar a ferramenta Realm Studio.<p>
Copiar o arquivo arquivo para a máquina local e abri-lo na ferramenta.
Links de referência para criptografar o arquivo default.realm: 

[1] https://www.mongodb.com/docs/realm/sdk/kotlin/realm-database/realm-files/encrypt-a-realm/#:~:text=You%20encrypt%20the%20realm%20file,given%20512%2Dbit%20encryption%20key.
[2] https://github.com/julkar-nain/secure-realm-database


