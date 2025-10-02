# 🚀 Sistema de Monitoramento com Ansible IAC

![Ansible](https://img.shields.io/badge/Ansible-8.0+-red.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-green.svg)

Sistema completo de monitoramento automatizado para infraestrutura, utilizando Ansible para deploy e gerenciamento de múltiplos servidores.

## 📊 Demonstração

```bash
# Executar monitoramento em todos os servidores
ansible-playbook run_monitor_simple.yml


🖥️ SERVER1 - 1/6 serviços rodando | CPU: 12.5% | Mem: 13.9%
🖥️ SERVER2 - 3/6 serviços rodando | CPU: 19.6% | Mem: 23.3%  
🖥️ SERVER3 - 2/6 serviços rodando | CPU: 13.5% | Mem: 26.9%


┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Control   │    │    VM 1     │    │    VM 2     │
│   Node      │◄──►│ 10.0.0.5    │◄──►│ 10.0.0.61   │
│ (Ansible)   │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
                           ▲
                           │
                   ┌─────────────┐
                   │    VM 3     │
                   │ 10.0.0.114  │
                   │             │
                   └─────────────┘


 ⚡ Funcionalidades
🔍 Monitoramento de Serviços
✅ nginx, mysql, ssh, docker, apache2, systemd

📊 Status em tempo real (ativo/inativo)

🔄 Verificação automática

📈 Métricas do Sistema
🖥️ Uso de CPU (percentual)

💾 Memória (GB usado/total)

💿 Disco (percentual usado)

📊 Load Average (1, 5, 15 min)

🚀 Automação Ansible
🔄 Deploy automatizado em múltiplos servidores

⚡ Execução remota de comandos

🔒 SSH com chaves para segurança

📋 Playbooks modulares e reutilizáveis                  

🛠️ Instalação Rápida
Pré-requisitos
bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y ansible python3-pip sshpass

# Ou via pip
pip install ansible psutil
Configuração
bash
git clone https://github.com/seu-usuario/projetoIac.git
cd projetoIac

# Configurar automaticamente
./scripts/setup_project.sh

# Configurar inventory com seus servidores
nano inventory.ini
Exemplo de Inventory
ini
[servers]
server1 ansible_host=192.168.1.10 ansible_user=admin
server2 ansible_host=192.168.1.11 ansible_user=admin

[servers:vars]
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
🎯 Uso
Deploy do Sistema
bash
# Implantar em todos os servidores
ansible-playbook deploy_monitor.yml
Executar Monitoramento
bash
# Executar uma vez
ansible-playbook run_monitor_simple.yml

# Ver resultados detalhados
ansible all -m command -a "python3 /opt/service-monitor/monitor_service.py"

# Modo JSON para integração
ansible server1 -m command -a "python3 /opt/service-monitor/monitor_service.py --json"
Comandos Úteis
bash
# Testar conectividade
ansible all -m ping

# Ver informações do sistema
ansible all -m setup -a "filter=ansible_distribution*"

# Reiniciar serviços
ansible all -m systemd -a "name=nginx state=restarted" --become
📁 Estrutura do Projeto
text
projetoIac/
├── .github/workflows/          # CI/CD Automático
├── scripts/setup_project.sh    # Setup automático
├── ansible.cfg                 # Configuração Ansible
├── inventory.ini               # Inventário de servidores
├── deploy_monitor.yml          # Playbook de deploy
├── run_monitor_simple.yml      # Playbook de execução
├── setup_sudo.yml              # Configuração de sudo
├── monitor_service.py          # Script de monitoramento
├── requirements.txt            # Dependências
└── README.md                   # Este arquivo
🔧 Customização
Adicionar Novos Serviços
Edite monitor_service.py:

python
self.services_to_check = [
    'nginx', 'mysql', 'ssh', 'docker', 
    'apache2', 'systemd', 'postgresql'  # ← Novo serviço
]
Adicionar Novas Métricas
python
def check_system_resources(self):
    # Adicione novas métricas aqui
    return {
        'cpu_percent': ...,
        'memory_percent': ...,
        'your_metric': ...  # ← Nova métrica
    }
🤝 Contribuição
Fork o projeto

Crie uma branch: git checkout -b feature/nova-funcionalidade

Commit: git commit -am 'Adiciona nova funcionalidade'

Push: git push origin feature/nova-funcionalidade

Abra um Pull Request

📄 Licença
Este projeto está sob licença MIT. Veja o arquivo LICENSE para detalhes.

👨‍💻 Autor
Seu Luiz Valença Filho - lulavalenca

