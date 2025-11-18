"""
Lab3 - Servidor e Cliente Web
Docente: João Costa (joaojdacosta@gmail.com)
Discente: Jussana Paim (20230132@isptec.co.ao)
Novemebro, 2025.
"""

from socket import *  # importa o módulo socket
import sys            # importa ferramentas de argumentos

def run_client():      #função para executar o código
    # 1. Deve receber 3 argumentos (server_ip, server_port, filename)
    if len(sys.argv) != 4: # Verifica se as instruções foram dadas
        print("Uso: python webclient.py <server_ip> <server_port> <filename>") # Diz como usar
        sys.exit()  # termina o programa

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2]) 
    filename = sys.argv[3] # Deve ser '/index.html'

    # 2. Cria o socket do cliente (TCP)
    clientSocket = socket(AF_INET, SOCK_STREAM)

    try:
        # Conecta-se ao servidor
        print("A conectar a {}:{}...".format(server_ip, server_port))
        clientSocket.connect((server_ip, server_port))
        
        # 3. Constrói o pedido HTTP GET completo
        request = "GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(filename, server_ip)
        
        # Envia o pedido
        print("A enviar pedido: {}".format(request.splitlines()[0]))
        clientSocket.send(request.encode("latin-1"))

        # 4. Recebe a resposta completa até que o servidor feche
        response = b""
        while True:
            data = clientSocket.recv(1024)
            if not data:
                # O servidor fechou a conexão (Fim da Resposta HTTP)
                break
            response += data

        # 5. Exibe a resposta completa
        print("-" * 50)
        print("Resposta Completa do Servidor:")
        print(response.decode('latin-1')) 
        print("-" * 50)

    except Exception as e:
        print("Ocorreu um erro na conexão: {}".format(e))

    finally:
        # Fecha o socket de conexão do cliente (essencial)
        clientSocket.close()
        print("Conexão TCP encerrada.")

run_client()