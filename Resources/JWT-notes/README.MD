## JWE - JSON Web Encryption 
<p>É um padrão de segurança para os dados transmitidos pelo JWT. 
O JWE vai criptografar o JWT e proteger os dados do payload ao criptografá-los. 
Pode usar criptografia simétrica ou assimétrica (recomendada). 

O JWE adiciona confidencialidade e garante que apenas as partes autorizadas na comunicação tenham acesso aos dados transmitidos. 
</p>
<p>Um token JWE possui 5 partes:
<br></br>[+] Cabeçalho
<br></br>[+] Content Encryption Key
<br></br>[+] Vetor de Inicialização
<br></br>[+] Texto Cifrado
<br></br>[+] Tag de Autenticação
<p>
Suporta vários algoritmos de criptogradfia como RSA, AES-GCM e ECDH-ES.
</P>
<p>
Frameworks modernos como OAuth2 e OpenID Connect (OIDC) usam JWE como um token bearer. 
</p>


