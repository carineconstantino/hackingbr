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
-n = componente

am startservices -n [nome-do-pacote/nome-do-serviço]
am stopservices -n [nome-do-pacote/nome-do-serviço]
am startservices -n [nome-do-pacote/nome-do-serviço] -a [nome-da-action]

Exemplo: am startservices -n com.android.music/com.android.music.MediaPlaybackService

am startservices -n org.owasp.android/.services.LocationService -a org.owasp.android.services.LocationServices
```
### Deep Links
Link: https://medium.com/mobis3c/deep-link-exploitation-introduction-open-unvalidated-redirection-b8344f00b17b<p>
Link: https://inesmartins.github.io/exploiting-deep-links-in-android-part1/index.html<p>
Link: https://redfoxsec.com/blog/protect-your-android-app-preventing-exploitation-of-deep-links/
```
./adb shell am start -W -a android.intent.action.VIEW -d [schema]://[host]/[path]
```

