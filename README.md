# 📖 RC1-Laboratorios

Repositório contendo os **5 laboratórios** da disciplina **Redes de Computadores I (RC1)** — uma introdução prática a redes, protocolos de aplicação, programação de sockets e configuração de dispositivos de rede.

🧑‍💻 Desenvolvido ao longo do ano letivo **2024/2025** no **ISPTEC**.

## 📑 Índice

- [Objetivo](#-objetivo)
- [Contexto académico](#-contexto-académico)
- [Laboratórios](#-laboratórios)
- [Estrutura do repositório](#-estrutura-do-repositório)
- [Requisitos](#-requisitos)
- [Como executar](#-como-executar)
- [Integrantes](#-integrantes)
- [Licença](#-licença)

## 🎯 Objetivo

Fornecer um ambiente reproduzível para experimentar conceitos fundamentais de redes de computadores:

- Emulação de redes com **Mininet**
- Configuração de ambientes multi-nó com **Vagrant/VirtualBox**
- Serviços web e o protocolo **HTTP**
- Programação de **sockets TCP** em Python
- Ferramentas de diagnóstico de rede (**ifconfig**, **ping**, **traceroute**, **whois**, **nmap**)
- Protocolos de e-mail **SMTP** e **POP3**
- Configuração de dispositivos de rede com **Cisco Packet Tracer**

## 🏫 Contexto académico

| Campo | Valor |
|---|---|
| Instituição | Instituto Superior Politécnico de Tecnologias e Ciências (ISPTEC) |
| Departamento | Engenharia e Tecnologias |
| Curso | Licenciatura em Engenharia Informática |
| Cadeira | Redes de Computadores I (RC1) |
| Professor | João Costa |
| Ano letivo | 2024/2025 |

## 📂 Laboratórios

| Lab | Tema | Ferramentas | Camada |
|-----|------|-------------|--------|
| **#1** | Emulação de Rede com Mininet | Vagrant, VirtualBox, Mininet | Rede |
| **#2** | Aplicações Web e HTTP | Vagrant, Apache2, Telnet | Aplicação |
| **#3** | Servidor e Cliente Web em Python | Vagrant, Python, Wireshark | Aplicação |
| **#4** | Ferramentas de Rede e E-mail | Vagrant, nmap, Wireshark, Telnet | Aplicação |
| **#5** | Configuração de Dispositivos | Cisco Packet Tracer | Rede/Enlace |

## 📁 Estrutura do repositório

```
RC1-Laboratorios/
├── Lab#1/
│   └── mininet/                     # Lab#1 — Mininet (single node)
│       └── Vagrantfile
├── Lab#2/
│   └── multinode/                   # Lab#2 — Web Server multinós
│       ├── Vagrantfile
│       ├── bootstrap_web.sh
│       ├── vagrant.out              # Saída de vagrant up (requisito de entrega)
│       └── html/
│           ├── index.html
│           └── download/
├── Lab#3/
│   └── multinode-webserver/         # Lab#3 — Servidor/Cliente Python
│       ├── Vagrantfile
│       ├── bootstrap_web.sh
│       ├── bootstrap-client.sh
│       └── html/
│           ├── index.html
│           ├── webserver.py
│           └── webclient.py
├── Lab#4/
│   └── multinode-email/             # Lab#4 — Ferramentas de Rede + Email
│       ├── Vagrantfile
│       ├── bootstrap_web.sh
│       ├── bootstrap-client.sh
│       └── html/
│           └── index.html
├── Lab#5/
│   └── PARTE 1 - Configuracoes.pkt  # Lab#5 — Cisco Packet Tracer
├── ARCHITECTURE.md                   # Instruções detalhadas de execução
├── LICENSE
└── .gitignore
```

## 🧰 Requisitos

| Ferramenta | Versão mínima | Labs | Finalidade |
|------------|---------------|------|------------|
| [VirtualBox](https://www.virtualbox.org/) | 6.0+ | #1–#4 | Provedor de virtualização |
| [Vagrant](https://www.vagrantup.com/) | 2.2+ | #1–#4 | Gestão de VMs |
| [Python](https://www.python.org/) | 3.x | #3 | Servidor/Cliente web |
| [Wireshark](https://www.wireshark.org/) | 3.x | #2–#4 | Análise de tráfego |
| [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer) | 8.x | #5 | Simulação de rede |
| JDK | 24+ | — | Não requerido (apenas para referência) |

> **Nota:** Os labs #1–#4 usam a box `ubuntu/trusty64` (Ubuntu 14.04). Embora descontinuada, o Vagrant ainda consegue fazer o download da box.

## 🚀 Como executar

### Visão geral

Cada lab é um ambiente Vagrant independente. O fluxo geral é:

```bash
cd Lab#N/<pasta-do-lab>
vagrant up          # Cria e inicia as VMs
vagrant ssh <nome>  # Acessa uma VM
vagrant halt         # Desliga as VMs
vagrant destroy      # Destroi as VMs
```

### Lab #1 — Mininet

```bash
cd Lab#1/mininet
vagrant up --provider virtualbox
vagrant ssh
sudo mn              # Inicia topologia Mininet
```

### Lab #2 — Web Server Multinós

```bash
cd Lab#2/multinode
vagrant up
# Acessar http://localhost:8080 no browser da máquina host
```

### Lab #3 — Servidor/Cliente Python

```bash
cd Lab#3/multinode-webserver
vagrant up
vagrant ssh webserver
cd ~/html && python webserver.py

# Noutra janela:
vagrant ssh client
python webclient.py 192.168.56.21 6789 /index.html
```

### Lab #4 — Ferramentas de Rede e Email

```bash
cd Lab#4/multinode-email
vagrant up --provision
vagrant ssh client
# Usar ifconfig, ping, traceroute, whois, nmap
# Conectar ao mailtrap.io via telnet para SMTP/POP3
```

### Lab #5 — Cisco Packet Tracer

Abrir o ficheiro `.pkt` no Cisco Packet Tracer.

> Instruções completas passo a passo para cada lab estão em [ARCHITECTURE.md](ARCHITECTURE.md).

## 👥 Integrantes

| Nome | Número de estudante |
|---|---|
| Jussana Paim | 20230132 |

## 📄 Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE).
