## Firefox Config
Como desabilitar o redirecionamento para HTTPS? 
```
about:config 

network.stricttransportsecurity.preloadlist set to false

browser.fixup.fallback-to-https set to false

dom.security.https_first set to false

dom.security.https_first_pbm set to false
```
