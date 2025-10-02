# 🚀 Sistema de Monitoramento com Ansible IaC

![Ansible](https://img.shields.io/badge/Ansible-8.0+-red.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> Sistema completo de monitoramento automatizado para infraestrutura, utilizando Ansible para deploy e gerenciamento de múltiplos servidores com automação CI/CD.

## 📋 Índice

- [📊 Demonstração](#-demonstração)
- [🏗️ Arquitetura](#️-arquitetura)
- [⚡ Funcionalidades](#-funcionalidades)
- [🛠️ Instalação](#️-instalação)
- [⚙️ Configuração](#️-configuração)
- [🎯 Uso](#-uso)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🔧 Customização](#-customização)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## 📊 Demonstração

### Execução do Monitoramento

```bash
# Executar monitoramento em todos os servidores
ansible-playbook run_monitor_simple.yml
```

**Saída do Sistema:**
```
🖥️ SERVER1 - 1/6 serviços rodando | CPU: 12.5% | Mem: 13.9%
🖥️ SERVER2 - 3/6 serviços rodando | CPU: 19.6% | Mem: 23.3%  
🖥️ SERVER3 - 2/6 serviços rodando | CPU: 13.5% | Mem: 26.9%
```

---

## 🏗️ Arquitetura

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Control   │    │    VM 1     │    │    VM 2     │
│   Node      │◄──►│ 10.0.0.5    │◄──►│ 10.0.0.61   │
│ (Ansible)   │    │ Web Server  │    │Load Balance │
└─────────────┘    └─────────────┘    └─────────────┘
                           ▲
                           │
                   ┌─────────────┐
                   │    VM 3     │
                   │ 10.0.0.114  │
                   │ Monitoring  │
                   └─────────────┘
```

### Componentes

| Componente | Descrição | Tecnologia |
|------------|-----------|------------|
| **Control Node** | Servidor central de automação | Ansible + Python |
| **VM 1** | Servidor web principal | Apache/Nginx + MySQL |
| **VM 2** | Load balancer | Nginx |
| **VM 3** | Servidor de monitoramento | Prometheus + Grafana |

---

## ⚡ Funcionalidades

### 🔍 Monitoramento de Serviços
- **Serviços Suportados**: nginx, mysql, ssh, docker, apache2, systemd
- **Status em Tempo Real**: Verificação ativo/inativo
- **Verificação Automática**: Execução programada
- **Alertas Personalizados**: Notificações configuráveis

### 📈 Métricas do Sistema
- **🖥️ CPU**: Percentual de uso em tempo real
- **💾 Memória**: GB usado/total disponível
- **💿 Disco**: Percentual de utilização
- **📊 Load Average**: Médias de 1, 5 e 15 minutos
- **🌐 Rede**: Tráfego de entrada/saída

### 🚀 Automação Ansible
- **Deploy Automatizado**: Implantação em múltiplos servidores
- **Execução Remota**: Comandos distribuídos
- **Segurança SSH**: Autenticação por chaves
- **Playbooks Modulares**: Código reutilizável e escalável

### 🔄 CI/CD Integration
- **GitHub Actions**: Pipeline automatizado
- **Testes Automáticos**: Validação de código
- **Deploy Contínuo**: Implantação automatizada

---

## 🛠️ Instalação

### Pré-requisitos

#### Ubuntu/Debian
```bash
sudo apt update && sudo apt install -y ansible python3-pip sshpass
```

#### Via pip
```bash
pip install ansible psutil requests pyyaml
```

#### Dependências Python
```bash
pip install -r requirements.txt
```

### Instalação do Projeto

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/projetoIac.git
cd projetoIac

# Configurar automaticamente
chmod +x scripts/setup_project.sh
./scripts/setup_project.sh

# Instalar dependências
pip install -r requirements.txt
```

---

## ⚙️ Configuração

### 1. Configuração do Inventário

Edite o arquivo `inventory.ini` com suas informações:

```ini
[servers]
server1 ansible_host=10.0.0.5   ansible_user=usuario
server2 ansible_host=10.0.0.61  ansible_user=usuario  
server3 ansible_host=10.0.0.114 ansible_user=usuario

[webservers]
server1 ansible_host=10.0.0.5

[loadbalancers]
server2 ansible_host=10.0.0.61

[monitoring]
server3 ansible_host=10.0.0.114

[servers:vars]
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
ansible_python_interpreter=/usr/bin/python3
```

### 2. Configuração SSH

```bash
# Gerar chave SSH (se não existir)
ssh-keygen -t rsa -b 4096

# Copiar chave para os servidores
ssh-copy-id -i ~/.ssh/id_rsa.pub usuario@10.0.0.5
ssh-copy-id -i ~/.ssh/id_rsa.pub usuario@10.0.0.61
ssh-copy-id -i ~/.ssh/id_rsa.pub usuario@10.0.0.114
```

### 3. Configuração do Ansible

```bash
# Testar conectividade
ansible all -m ping

# Verificar configuração
ansible all -m setup --limit server1
```

---

## 🎯 Uso

### Deploy Inicial do Sistema

```bash
# Implantar o sistema em todos os servidores
ansible-playbook deploy_monitor.yml -v

# Deploy com tags específicas
ansible-playbook deploy_monitor.yml --tags "install,configure"
```

### Executar Monitoramento

#### Execução Simples
```bash
# Executar monitoramento uma vez
ansible-playbook run_monitor_simple.yml

# Executar apenas em um servidor
ansible-playbook run_monitor_simple.yml --limit server1
```

#### Execução Detalhada
```bash
# Ver resultados detalhados
ansible all -m command -a "python3 /opt/service-monitor/monitor_service.py"

# Formato JSON para integração
ansible server1 -m command -a "python3 /opt/service-monitor/monitor_service.py --json"

# Salvar resultados em arquivo
ansible all -m command -a "python3 /opt/service-monitor/monitor_service.py --output /tmp/metrics.json"
```

### Comandos Úteis de Manutenção

#### Testes e Diagnósticos
```bash
# Testar conectividade
ansible all -m ping

# Informações do sistema
ansible all -m setup -a "filter=ansible_distribution*"

# Verificar uptime
ansible all -m command -a "uptime"

# Verificar espaço em disco
ansible all -m command -a "df -h"
```

#### Gerenciamento de Serviços
```bash
# Reiniciar serviços
ansible all -m systemd -a "name=nginx state=restarted" --become

# Verificar status de serviços
ansible all -m systemd -a "name=apache2 state=started" --become

# Atualizar sistema
ansible all -m apt -a "upgrade=yes update_cache=yes" --become
```

#### Execução de Scripts Personalizados
```bash
# Executar script local em servidores remotos
ansible all -m copy -a "src=./meu_script.sh dest=/tmp/script.sh mode=0755"
ansible all -m command -a "/tmp/script.sh"
```

---

## 📁 Estrutura do Projeto

```
projetoIac/
├── .github/
│   └── workflows/              # CI/CD com GitHub Actions
│       ├── ci.yml              # Pipeline de integração
│       └── deploy.yml          # Pipeline de deploy
├── scripts/
│   ├── setup_project.sh        # Script de configuração automática
│   └── backup.sh               # Script de backup
├── playbooks/
│   ├── deploy_monitor.yml      # Deploy do sistema de monitoramento
│   ├── run_monitor_simple.yml  # Execução do monitoramento
│   ├── setup_sudo.yml          # Configuração de privilégios
│   └── backup.yml              # Playbook de backup
├── roles/                      # Roles do Ansible (futuro)
├── group_vars/                 # Variáveis por grupo
├── host_vars/                  # Variáveis por host
├── files/
│   └── monitor_service.py      # Script principal de monitoramento
├── templates/                  # Templates Jinja2
├── tests/                      # Testes automatizados
├── docs/                       # Documentação adicional
├── ansible.cfg                 # Configuração do Ansible
├── inventory.ini               # Inventário de servidores
├── requirements.txt            # Dependências Python
├── .gitignore                  # Arquivos ignorados pelo Git
├── LICENSE                     # Licença do projeto
└── README.md                   # Este arquivo
```

### Descrição dos Arquivos Principais

| Arquivo | Função |
|---------|--------|
| `deploy_monitor.yml` | Playbook principal para deploy do sistema |
| `run_monitor_simple.yml` | Execução do monitoramento |
| `monitor_service.py` | Script Python de monitoramento |
| `setup_project.sh` | Automatização da configuração inicial |
| `ansible.cfg` | Configurações globais do Ansible |
| `inventory.ini` | Definição dos servidores gerenciados |

---

## 🔧 Customização

### Adicionar Novos Serviços

Edite o arquivo `monitor_service.py`:

```python
class ServiceMonitor:
    def __init__(self):
        self.services_to_check = [
            'nginx', 'mysql', 'ssh', 'docker', 
            'apache2', 'systemd', 'postgresql',  # ← Novo serviço
            'redis', 'mongodb'                   # ← Mais serviços
        ]
```

### Adicionar Novas Métricas

```python
def check_system_resources(self):
    """Adicione novas métricas de sistema"""
    return {
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'network_io': psutil.net_io_counters()._asdict(),  # ← Nova métrica
        'process_count': len(psutil.pids()),               # ← Nova métrica
        'boot_time': psutil.boot_time()                    # ← Nova métrica
    }
```

### Personalizar Alertas

Crie um arquivo `group_vars/all.yml`:

```yaml
# Thresholds de alertas
alert_thresholds:
  cpu_warning: 70
  cpu_critical: 85
  memory_warning: 80
  memory_critical: 90
  disk_warning: 85
  disk_critical: 95

# Configurações de notificação
notifications:
  slack_webhook: "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
  email_enabled: true
  email_to: "admin@empresa.com"
```

### Configurar Monitoramento Contínuo

Adicione ao crontab dos servidores:

```bash
# Executar a cada 5 minutos
*/5 * * * * /usr/bin/python3 /opt/service-monitor/monitor_service.py --json > /var/log/monitor.log
```

---

## 🧪 Testes

### Executar Testes Locais

```bash
# Validar sintaxe dos playbooks
ansible-playbook deploy_monitor.yml --syntax-check

# Dry run (simulação)
ansible-playbook deploy_monitor.yml --check

# Teste de conectividade
ansible all -m ping
```

### Testes Automatizados

```bash
# Executar suite de testes
python -m pytest tests/

# Testes com cobertura
python -m pytest tests/ --cov=monitor_service
```

---

## 🚀 Deploy e CI/CD

### Pipeline GitHub Actions

O projeto inclui workflows automatizados:

- **CI**: Testes e validação de código
- **CD**: Deploy automatizado em diferentes ambientes
- **Monitoramento**: Verificações de saúde pós-deploy

### Ambientes de Deploy

```bash
# Deploy para desenvolvimento
ansible-playbook deploy_monitor.yml -e "env=development"

# Deploy para produção
ansible-playbook deploy_monitor.yml -e "env=production"
```

---

## 📊 Monitoramento e Logs

### Localização dos Logs

```bash
# Logs do sistema de monitoramento
/var/log/service-monitor.log

# Logs do Ansible
/var/log/ansible.log

# Métricas em JSON
/tmp/system-metrics.json
```

### Visualização de Métricas

```bash
# Ver métricas em tempo real
tail -f /var/log/service-monitor.log

# Analisar métricas JSON
cat /tmp/system-metrics.json | jq '.'
```

---

## 🔒 Segurança

### Práticas Implementadas

- **Autenticação SSH**: Uso de chaves em vez de senhas
- **Usuários Limitados**: Princípio do menor privilégio
- **Logs de Auditoria**: Registro de todas as operações
- **Validação de Input**: Sanitização de dados

### Configurações de Segurança

```yaml
# ansible.cfg
[defaults]
host_key_checking = False
timeout = 30
gather_timeout = 30

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
pipelining = True
```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Clone** seu fork: `git clone https://github.com/SEU-USUARIO/projetoIac.git`
3. **Crie uma branch**: `git checkout -b feature/nova-funcionalidade`
4. **Faça suas alterações** e teste localmente
5. **Commit**: `git commit -am 'Adiciona nova funcionalidade'`
6. **Push**: `git push origin feature/nova-funcionalidade`
7. **Abra um Pull Request**

### Padrões de Código

- Use `yamllint` para validar YAML
- Siga PEP 8 para código Python
- Documente novas funcionalidades
- Inclua testes para novas features

### Issues e Suporte

- 🐛 [Reportar bugs](https://github.com/seu-usuario/projetoIac/issues)
- 💡 [Sugerir melhorias](https://github.com/seu-usuario/projetoIac/issues)
- 📚 [Documentação](https://github.com/seu-usuario/projetoIac/wiki)

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Luiz Valença Filho**
- GitHub: [@lulavalenca](https://github.com/lulavalenca)
- LinkedIn: [Luiz Valença Filho](https://linkedin.com/in/lulavalenca)
- Email: contato@lulavalenca.dev

---

## 🙏 Agradecimentos

- Comunidade Ansible
- Contribuidores do projeto
- Stack Overflow pela ajuda em dúvidas técnicas

---

## 📈 Roadmap

### Versão Atual (v1.0)
- [x] Monitoramento básico de serviços
- [x] Deploy automatizado com Ansible
- [x] CI/CD com GitHub Actions

### Próximas Versões

#### v1.1 (Em Desenvolvimento)
- [ ] Interface web para visualização
- [ ] Alertas por email/Slack
- [ ] Métricas históricas

#### v1.2 (Planejado)
- [ ] Integração com Prometheus/Grafana
- [ ] API REST para integração
- [ ] Dashboard interativo

#### v2.0 (Futuro)
- [ ] Suporte a Kubernetes
- [ ] Multi-cloud support
- [ ] Machine Learning para predições

---

*Feito com ❤️ e ☕ por [Luiz Valença Filho](https://github.com/lulavalenca)*
