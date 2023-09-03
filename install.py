import os
import subprocess
import urllib.request

# URLs dos arquivos que precisam ser baixados
agent_url = "https://raw.githubusercontent.com/coderealmhub/polarease-raspberry-pi-agent/main/agent.py"
requirements_url = "https://raw.githubusercontent.com/coderealmhub/polarease-raspberry-pi-agent/main/requirements.txt"

# Diretório de instalação
installation_dir = "/opt/polarease-agent"

# Verifica se o script está sendo executado como root
if os.geteuid() != 0:
    print("Este script deve ser executado como root.")
    exit(1)

# Cria o diretório de instalação, se ele não existir
if not os.path.exists(installation_dir):
    os.makedirs(installation_dir)

# Baixa o arquivo agent.py
urllib.request.urlretrieve(agent_url, os.path.join(installation_dir, "agent.py"))

# Baixa o arquivo requirements.txt
urllib.request.urlretrieve(requirements_url, os.path.join(installation_dir, "requirements.txt"))

# Cria um ambiente virtual
subprocess.run(["python3", "-m", "venv", os.path.join(installation_dir, ".venv")])

# Ativa o ambiente virtual e instala as dependências
subprocess.run(
    [
        os.path.join(installation_dir, ".venv", "bin", "pip"),
        "install",
        "-r",
        os.path.join(installation_dir, "requirements.txt"),
    ]
)

# Cria um arquivo de serviço systemd para iniciar o agente com o sistema
service_file_content = f"""[Unit]
Description=Polarease Raspberry Pi Agent
After=network.target

[Service]
ExecStart={os.path.join(installation_dir, ".venv", "bin", "uvicorn")} agent:app --reload --port 8000
WorkingDirectory={installation_dir}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""

service_file_path = "/etc/systemd/system/polarease-agent.service"

with open(service_file_path, "w") as service_file:
    service_file.write(service_file_content)

# Recarrega o systemd para atualizar a lista de serviços e inicia o agente
subprocess.run(["systemctl", "daemon-reload"])
subprocess.run(["systemctl", "enable", "polarease-agent"])
subprocess.run(["systemctl", "start", "polarease-agent"])

print("A instalação foi concluída com sucesso.")
