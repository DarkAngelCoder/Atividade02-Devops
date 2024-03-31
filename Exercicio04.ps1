$nome_servico = "Spooler"

$status_servico = Get-Service -Name $nome_servico | Select-Object -ExpandProperty Status

if ($status_servico -ne "Running") {
    # Iniciar o serviço se não estiver em execução
    Start-Service -Name $nome_servico
    Write-Host "O serviço foi iniciado com sucesso."
} else {
    Write-Host "O serviço já está em execução."
}
