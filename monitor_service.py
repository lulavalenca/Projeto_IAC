#!/usr/bin/env python3
"""
Sistema de Monitoramento de Serviços - Versão 1.1
Monitora serviços, recursos do sistema e gera relatórios
"""

import subprocess
import sys
import json
import psutil
from datetime import datetime
import socket


class ServiceMonitor:
    def __init__(self):
        # ✅ CORRIGIDO: self.services_to_check (não self_services_to_check)
        self.services_to_check = [
            "nginx",
            "mysql",
            "ssh",
            "docker",
            "apache2",
            "systemd",
        ]
        self.results = {}

    def check_service(self, service_name):
        """Verifica se um serviço está rodando"""
        try:
            result = subprocess.run(
                ["systemctl", "is-active", service_name],
                capture_output=True,
                text=True,
                timeout=10,
            )

            status = result.stdout.strip()
            is_running = status == "active"

            return {
                "service": service_name,
                "status": status,
                "is_running": is_running,
                "timestamp": datetime.now().isoformat(),
            }

        except subprocess.TimeoutExpired:
            return {
                "service": service_name,
                "status": "timeout",
                "is_running": False,
                "timestamp": datetime.now().isoformat(),
            }
        except Exception as e:
            return {
                "service": service_name,
                "status": f"error: {str(e)}",
                "is_running": False,
                "timestamp": datetime.now().isoformat(),
            }

    def check_system_resources(self):
        """Verifica recursos do sistema"""
        try:
            # Uso de CPU
            cpu_percent = psutil.cpu_percent(interval=1)

            # Memória
            memory = psutil.virtual_memory()

            # Disco
            disk = psutil.disk_usage("/")

            # Load average
            load_avg = psutil.getloadavg()

            return {
                "cpu_percent": cpu_percent,
                "memory_total_gb": round(memory.total / (1024**3), 2),
                "memory_used_gb": round(memory.used / (1024**3), 2),
                "memory_percent": memory.percent,
                "disk_total_gb": round(disk.total / (1024**3), 2),
                "disk_used_gb": round(disk.used / (1024**3), 2),
                "disk_percent": disk.percent,
                "load_avg_1min": load_avg[0],
                "load_avg_5min": load_avg[1],
                "load_avg_15min": load_avg[2],
            }
        except Exception as e:
            return {"error": f"Failed to get system resources: {str(e)}"}

    def check_all_services(self):
        """Verifica todos os serviços configurados"""
        print("🔍 Verificando status dos serviços...")

        for service in self.services_to_check:
            result = self.check_service(service)
            self.results[service] = result

            emoji = "✅" if result["is_running"] else "❌"
            print(f"{emoji} {service}: {result['status']}")

        return self.results

    def generate_report(self):
        """Gera um relatório completo"""
        services_report = self.check_all_services()
        system_report = self.check_system_resources()

        report = {
            "timestamp": datetime.now().isoformat(),
            "hostname": socket.gethostname(),
            "services": services_report,
            "system_resources": system_report,
            "summary": {
                "total_services": len(services_report),
                "running_services": sum(
                    1 for r in services_report.values() if r["is_running"]
                ),
                "failed_services": sum(
                    1 for r in services_report.values() if not r["is_running"]
                ),
            },
        }

        return report


def main():
    monitor = ServiceMonitor()

    if len(sys.argv) > 1:
        if sys.argv[1] == "--json":
            report = monitor.generate_report()
            print(json.dumps(report, indent=2))
        elif sys.argv[1] == "--service":
            service = sys.argv[2]
            result = monitor.check_service(service)
            print(json.dumps(result, indent=2))
        elif sys.argv[1] == "--resources":
            resources = monitor.check_system_resources()
            print(json.dumps(resources, indent=2))
        else:
            print(
                "Uso: python3 monitor_service.py [--json | --service <name> | --resources]"
            )
    else:
        # Modo interativo
        report = monitor.generate_report()

        print(f"\n📊 RESUMO DO SISTEMA - {report['hostname']}")
        print(f"🕐 {report['timestamp']}")
        print(
            f"📦 Serviços: {report['summary']['running_services']}/{report['summary']['total_services']} rodando"
        )

        if "system_resources" in report and "error" not in report["system_resources"]:
            sys_info = report["system_resources"]
            print(f"🖥️  CPU: {sys_info['cpu_percent']}%")
            print(
                f"💾 Memória: {sys_info['memory_percent']}% ({sys_info['memory_used_gb']:.1f}/{sys_info['memory_total_gb']:.1f} GB)"
            )
            print(
                f"💿 Disco: {sys_info['disk_percent']}% ({sys_info['disk_used_gb']:.1f}/{sys_info['disk_total_gb']:.1f} GB)"
            )
            print(
                f"📈 Load: {sys_info['load_avg_1min']:.2f}, {sys_info['load_avg_5min']:.2f}, {sys_info['load_avg_15min']:.2f}"
            )


if __name__ == "__main__":
    main()
