function Check-MX {
    param([string]$domain)

    try {
        $answers = Resolve-DnsName -Type MX $domain
        $mx_records = $answers | ForEach-Object { $_.NameExchange }
        return $mx_records
    } catch {
        return $null
    }
}

function Check-DMARC {
    param([string]$domain)

    try {
        $result = Resolve-DnsName -Name "_dmarc.$domain" -Type TXT -ErrorAction Stop | Select-Object -ExpandProperty Strings
        $dmarc_record = $result -join " "
        return $dmarc_record
    } catch {
        return $null
    }
}

function Display-Banner {
    $banner_text = @"
╔╦╗╔╦╗╔═╗╦═╗╔═╗  ╦ ╦╦ ╦╔╗╔╔╦╗╔═╗╦═╗
 ║║║║║╠═╣╠╦╝║    ╠═╣║ ║║║║ ║ ║╣ ╠╦╝
═╩╝╩ ╩╩ ╩╩╚═╚═╝  ╩ ╩╚═╝╝╚╝ ╩ ╚═╝╩╚═
"@
    Write-Host $banner_text
}

function Main {
    Display-Banner

    $red_color = [System.ConsoleColor]::Red
    $green_color = [System.ConsoleColor]::Green
    $orange_color = [System.ConsoleColor]::DarkYellow
    $yellow_color = [System.ConsoleColor]::Yellow

    $file_path = 'domains.txt'

    $domains = Get-Content $file_path

    foreach ($domain in $domains) {
        Write-Host ("Domain: $domain") -ForegroundColor $green_color

        $mx_records = Check-MX $domain
        if ($mx_records) {
            Write-Host "MX Records:"
            foreach ($mx in $mx_records) {
                Write-Host ("  $mx")
            }
        } else {
            Write-Host "No MX records found."
        }

        $dmarc_record = Check-DMARC $domain
        if ($dmarc_record) {
            Write-Host "DMARC Record:"
            Write-Host ("  $dmarc_record")
            if ($dmarc_record -like "*p=none*") {
                Write-Host "DMARC existe, mas não há políticas definidas." -ForegroundColor $red_color
            } elseif ($dmarc_record -like "*p=quarantine*") {
                Write-Host "A política atual de DMARC para este domínio é QUARANTINE." -ForegroundColor $red_color
            } elseif ($dmarc_record -like "*p=reject*") {
                Write-Host "A política atual de DMARC para este domínio é REJECT." -ForegroundColor $red_color
            } else {
                Write-Host "DMARC encontrado, mas não no formato esperado." -ForegroundColor $red_color
            }
        } else {
            Write-Host "Nenhum registro DMARC encontrado para este domínio." -ForegroundColor $red_color
        }

        $whois_link = "https://who.is/whois/$domain"
        Write-Host ("Para mais informações sobre este domínio, acesse: $whois_link") -ForegroundColor $yellow_color

        Write-Host ("=" * 50)
    }
}

Main
