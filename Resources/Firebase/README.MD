## Firebase Config
```
curl -v -X POST "https://firebaseremoteconfig.googleapis.com/v1/projects/[NOME/ID]/namespaces/firebase:fetch?key=[API KEY]" -H "Content-Type: application/json" --data '{"appId": "[ID]", "appInstanceId": "[NOME]"}'
```
