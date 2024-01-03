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

