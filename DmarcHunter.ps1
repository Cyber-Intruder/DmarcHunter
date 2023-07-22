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
        $result = & nslookup -type=TXT "_dmarc.$domain" | Select-String "v=DMARC1"
        $dmarc_record = $result -replace "v=DMARC1", "" -replace " ", ""
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
                Write-Host "DMARC exists, but no policies defined" -ForegroundColor $red_color
            } elseif ($dmarc_record -like "*p=quarantine*") {
                Write-Host "The current DMARC policy for this domain is QUARANTINE" -ForegroundColor $red_color
            } elseif ($dmarc_record -like "*p=reject*") {
                Write-Host "The current DMARC policy for this domain is REJECT" -ForegroundColor $red_color
            }
        } else {
            Write-Host "No DMARC record found for this domain" -ForegroundColor $red_color
        }

        $whois_link = "https://who.is/whois/$domain"
        Write-Host ("For more information about this domain, visit: $whois_link") -ForegroundColor $yellow_color

        Write-Host ("=" * 50)
    }
}

Main
