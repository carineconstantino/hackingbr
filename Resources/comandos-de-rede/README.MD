```
ifconfig 
ifconfig [interface] 

# cálculo do IP
ipcalc [IP]/[Mascara]

# ver as portas abertas em um host
netstat -nlpt | grep 80

# altera o endereço MAC para um aleatório
macchanger -r [interface]

# volta o endereço original
macchanger -p [interface]

# define um endereço MAC específico
macchanger -m 00:00:00:00:00:00 [interface]

# ver as rotas da máquina
route -n 

# deleta o endereço do gateway
route del default gw [endereço-gateway]

# adiciona o endereço do gateway
route add default gw [endereço-gateway]

# deleta uma rota 
ip route del default dev [interface]

# adiciona uma rota
ip route add default via [endereço-gateway] dev [interface] metric [priority-number]
```
