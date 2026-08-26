# 🏗️ Architettura e Execução dos Laboratórios

Guia completo de configuração e execução para cada laboratório da disciplina RC1.

---

## Pré-requisitos

### Instalação do ambiente (Windows)

O gestor de pacotes recomendado é o [Chocolatey](https://chocolatey.org/):

```powershell
# Instalar Chocolatey (PowerShell como administrador)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar ferramentas necessárias
choco install wget
choco install git -params " /GitAndUnixToolsOnPath "
choco install virtualbox
choco install vagrant
```

### Instalação do ambiente (macOS)

Usar [Homebrew](https://brew.sh):

```bash
brew install wget
brew install git
brew cask install virtualbox
brew cask install vagrant
```

### Instalação do ambiente (Linux/Ubuntu)

```bash
sudo apt-get update
sudo apt-get install git virtualbox vagrant
```

### Plugin Vagrant (recomendado)

```bash
vagrant plugin install vagrant-vbguest
```

---

## Lab #1 — Emulação de Rede com Mininet

### Objetivo

Configurar uma VM com Mininet para emular redes virtuais e experimentar comandos básicos de topologia de rede.

### Configuração

O `Vagrantfile` usa a box `ktr/mininet` com o provedor VirtualBox. Não há provisioning customizado — a box já vem com o Mininet pré-instalado.

### Execução

```bash
cd Lab#1/mininet

# Iniciar a VM
vagrant up --provider virtualbox

# Acessar a VM
vagrant ssh
```

### Comandos Mininet dentro da VM

```bash
# Criar topologia padrão: 2 hosts (h1, h2) + 1 switch (s1)
sudo mn

# Verificar conectividade entre hosts
mininet> pingall

# Verificar conexões dos nós
mininet> net

# Ver endereços IP dos hosts
mininet> dump

# Sair e limpar processos
mininet> exit
sudo mn -c
```

### Finalização

```bash
vagrant halt
vagrant global-status  # Confirmar que as VMs estão 'powered off'
```

---

## Lab #2 — Aplicações Web e HTTP

### Objetivo

Configurar um ambiente multinós (webserver + client) com Apache2 e experimentar o protocolo HTTP.

### Configuração

O `Vagrantfile` define duas VMs:

| VM | IP | Porta | Provisioning |
|----|----| -------|-------------|
| `webserver` | `192.168.56.21` | 80 → 8080 (host) | `bootstrap_web.sh` (Apache2) |
| `client` | `192.168.56.11` | — | Nenhum |

### Execução

```bash
cd Lab#2/multinode

# Iniciar ambas as VMs
vagrant up

# Verificar status
vagrant global-status
```

### Teste do servidor web

1. Acesse `http://localhost:8080` no browser da máquina host.
2. Deve aparecer uma página HTML com ASCII art.

### Experiência HTTP (telnet)

```bash
# Na VM client
vagrant ssh client

# Configurar DNS estático
sudo sh -c 'echo "192.168.56.21 webserver" >> /etc/hosts'

# Conectar ao servidor via telnet
telnet webserver 80
GET /index.html HTTP/1.1
Host: webserver
```

### Exercícios complementares (Lab 2.2)

Requer [Wireshark](https://www.wireshark.org/) instalado na máquina host:

1. Iniciar captura de pacotes no Wireshark
2. Aceder a `http://localhost:8080`
3. Analisar as respostas HTTP (código, cabeçalhos, tamanho)
4. Testar cache do browser (reload, espera de 2 minutos)
5. Transferir ficheiro grande (`jctest.docx`) e observar segmentação
6. Adicionar imagens ao `index.html` e analisar múltiplos pedidos
7. Testar códigos de erro (404, 301)

### Guardar saída (requisito de entrega)

```bash
vagrant halt
vagrant up > vagrant.out
```

### Finalização

```bash
vagrant halt
vagrant destroy
vagrant global-status
```

---

## Lab #3 — Servidor e Cliente Web em Python

### Objetivo

Desenvolver um servidor web e um cliente web em Python usando programação de sockets TCP, e analisar o tráfego HTTP com Wireshark.

### Configuração

O `Vagrantfile` define duas VMs:

| VM | IP | synced folder | Provisioning |
|----|----|---------------|-------------|
| `webserver` | `192.168.56.21` | `html/` → `/home/vagrant/html` | Nenhum (Apache comentado) |
| `client` | `192.168.56.11` | `html/` → `/home/vagrant/html` | `bootstrap-client.sh` (Wireshark, nmap) |

A pasta `html/` é partilhada entre host e VMs.

### Código do Servidor (`html/webserver.py`)

O servidor:
- Escuta na porta **6789**
- Recebe pedidos HTTP GET
- Retorna o ficheiro solicitado com cabeçalhos HTTP
- Retorna `404 Not Found` se o ficheiro não existir

### Código do Cliente (`html/webclient.py`)

Uso:
```bash
python webclient.py <server_ip> <server_port> <filename>
```

Exemplo:
```bash
python webclient.py 192.168.56.21 6789 /index.html
```

### Execução

```bash
cd Lab#3/multinode-webserver
vagrant up
```

**Terminal 1 — Servidor:**
```bash
vagrant ssh webserver
cd ~/html
python webserver.py
```

**Terminal 2 — Cliente:**
```bash
vagrant ssh client
cd ~/html
python webclient.py 192.168.56.21 6789 /index.html
```

**Teste via telnet:**
```bash
vagrant ssh client
telnet 192.168.56.21 6789
GET /index.html HTTP/1.1
```

### Análise com Wireshark

1. Iniciar captura na interface `eth1` da VM client
2. Executar o cliente ou telnet
3. Analisar os pacotes TCP trocados (syn, syn-ack, ack, data, fin)

### Finalização

```bash
vagrant halt
vagrant destroy
```

---

## Lab #4 — Ferramentas de Rede e E-mail (SMTP, POP3)

### Objetivo

Utilizar ferramentas de diagnóstico de rede e experimentar os protocolos de e-mail SMTP e POP3.

### Configuração

O `Vagrantfile` define duas VMs:

| VM | IP | synced folder | Provisioning |
|----|----|---------------|-------------|
| `webserver-email` | `192.168.56.21` | `html/` → `/home/vagrant/html` | Nenhum (comentado) |
| `client-email` | `192.168.56.11` | `html/` → `/home/vagrant/html` | `bootstrap-client.sh` (Wireshark, nmap) |

### Execução

```bash
cd Lab#4/multinode-email
vagrant up --provision
vagrant ssh client
```

### Ferramentas de rede

```bash
# Listar interfaces de rede
ifconfig
ifconfig eth1

# Testar conectividade
ping www.wustl.edu

# Definir TTL para descobrir saltos
ping -t 2 193.136.128.169

# Rastrear rota
traceroute www.wustl.edu

# Informação sobre entidades
whois 193.136.128.169

# Scan de rede
nmap -sP 192.168.1.0/24
nmap -v scanme.nmap.org
```

### Experiência SMTP (envio de e-mail)

Usar servidor externo de teste [Mailtrap](https://mailtrap.io/):

```bash
telnet smtp.mailtrap.io 2525
EHLO smtp.mailtrap.io
AUTH LOGIN
<utilizador_base64>
<password_base64>
MAIL FROM: <from@smtp.mailtrap.io>
RCPT TO: <to@smtp.mailtrap.io>
DATA
Subject: Teste RC1
Mensagem de teste.
.
QUIT
```

### Experiência POP3 (receção de e-mail)

```bash
telnet smtp.mailtrap.io 1100
USER <utilizador>
PASS <password>
STAT
LIST
RETR 1
QUIT
```

### Finalização

```bash
vagrant halt
vagrant destroy
```

---

## Lab #5 — Cisco Packet Tracer

### Objetivo

Configurar dispositivos de rede (routers, switches) usando o simulador Cisco Packet Tracer.

### Configuração

Abrir o ficheiro `PARTE 1 - Configuracoes.pkt` no [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer).

### Requisitos

- Cisco Packet Tracer 8.x ou superior
- Conta Cisco Networking Academy (para download)

---

## Notas gerais

- Todos os labs #1–#4 usam a box `ubuntu/trusty64` (Ubuntu 14.04)
- Os endereços IP das VMs seguem o esquema `192.168.56.x` (rede privada VirtualBox)
- Para reutilizar os labs, basta executar `vagrant up` novamente
- Os ficheiros `.pcap` (captures Wireshark) e `.pkt` (Packet Tracer) estão incluídos no repositório como referência
