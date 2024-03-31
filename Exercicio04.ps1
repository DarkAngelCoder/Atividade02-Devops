import subprocess

nome_servico = "Spooler"

comando_ps_status = f"Get-Service '{nome_servico}' | Select-Object -ExpandProperty Status"

status_servico = subprocess.run(["powershell", "-Command", comando_ps_status], capture_output=True, text=True).stdout.strip()

if status_servico != "Running":
    comando_ps_start = f"Start-Service '{nome_servico}'"
    
    subprocess.run(["powershell", "-Command", comando_ps_start])
    
    print("O serviço foi iniciado com sucesso.")
else:
    print("O serviço já está em execução.")
