#!/bin/bash

echo "🚀 Configurando Projeto Ansible IAC"

# Criar diretórios
mkdir -p monitor_results
mkdir -p .github/workflows

# Configurar permissões
chmod +x monitor_service.py
chmod +x scripts/setup_project.sh

# Testar Ansible
echo "🔍 Testando conectividade..."
ansible all -m ping

echo "✅ Projeto configurado com sucesso!"
echo "📁 Estrutura:"
tree -a -I '.git|.venv' .