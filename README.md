██████╗ ███╗   ███╗ █████╗ ██████╗  ██████╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██╔████╔██║███████║██████╔╝██║         ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║  ██║██║╚██╔╝██║██╔══██║██╔══██╗██║         ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╗    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                   


Python usage:

If you don't have python-whois installed, you will need to install it, in order to DMARC HUNTER work properly.
Run the following command to python-whois installation:"pip install python-whois".

After that, follow these steps:

1 - Make sure that all files are in the same directory;

2 - Add all the domains that you want to check in the included "domains.txt" file (add a domain per line and do not leave blank spaces or empty lines) and save the file;

3 - Navigate to the Dmarc Hunter files directory;

4 - Run the following command: python3 DmarcHunter.py;

5 - The results will be shown.

Output example:

python3 DmarcHunter.py

╔╦╗╔╦╗╔═╗╦═╗╔═╗  ╦ ╦╦ ╦╔╗╔╔╦╗╔═╗╦═╗
 ║║║║║╠═╣╠╦╝║    ╠═╣║ ║║║║ ║ ║╣ ╠╦╝
═╩╝╩ ╩╩ ╩╩╚═╚═╝  ╩ ╩╚═╝╝╚╝ ╩ ╚═╝╩╚═

Domain: github.com
MX Records:
  aspmx.l.google.com
  alt3.aspmx.l.google.com
  alt4.aspmx.l.google.com
  alt1.aspmx.l.google.com
  alt2.aspmx.l.google.com
DMARC Record: "v=DMARC1; p=reject; pct=100; rua=mailto:dmarc@github.com"
The current DMARC policy for this domain is REJECT
Domain owner GitHub Inc
For more information about this domain, visit: https://who.is/whois/github.com
==================================================
Domain: google.com
MX Records:
  smtp.google.com
DMARC Record: "v=DMARC1; p=reject; rua=mailto:mailauth-reports@google.com"
The current DMARC policy for this domain is REJECT
Domain owner information not available
For more information about this domain, visit: https://who.is/whois/google.com
==================================================
Domain: example.com.br
MX Records:
  mx.example.com.br

*** example.example.example.com did not find _dmarc.example.com.br: Non-existent domain
No DMARC record found for this domain
Domain owner Example Corp
For more information about this domain, visit: https://who.is/whois/example.com.br
==================================================

You can save the output to a separate file, as in the following example:
python3 DmarcHunter.py | grep "github.com" > results.txt

_________________________________________________
Language PTBR
If you want to use the brazilian portuguese version, you must use the "ptbr-DmarcHunter.py" or "ptbr-DmarcHunter.ps1" it depends on which platform you want to use (Python(.py) or PowerShell(.ps1)) in this case, the sintaxe are the same for both cases.

_________________________________________________

PowerShell usage:

1 - Make sure that all files are in the same directory;

2 - Add all the domains that you want to check in the included "domains.txt" file (add a domain per line and do not leave blank spaces or empty lines) and save the file;

3 - Open PowerShell as administrator;

4 - Allow that scripts can be executed by changing the default execution policy(only for the current user) with the command: "Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser" ;

5 - Navigate to the Dmarc Hunter files directory;

6 - Run the following command: ".\DmarcHunter.ps1" or ".\ptbr-DmarcHunter.ps1" based on the language that you want to work; 

7 - The results will be shown.

8 - If you want to return the default execution policy(recommended), run the following command: "Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser"

Output example:

DmarcHunter> .\DmarcHunter.ps1
╔╦╗╔╦╗╔═╗╦═╗╔═╗  ╦ ╦╦ ╦╔╗╔╔╦╗╔═╗╦═╗
 ║║║║║╠═╣╠╦╝║    ╠═╣║ ║║║║ ║ ║╣ ╠╦╝
═╩╝╩ ╩╩ ╩╩╚═╚═╝  ╩ ╩╚═╝╝╚╝ ╩ ╚═╝╩╚═
Domain: github.com
MX Records:
  aspmx.l.google.com
  alt4.aspmx.l.google.com
  alt3.aspmx.l.google.com
  alt2.aspmx.l.google.com
  alt1.aspmx.l.google.com
Non-authoritative answer:
DMARC Record:
        ";p=reject;pct=100;rua=mailto:dmarc@github.com"
The current DMARC policy for this domain is REJECT
For more information about this domain, visit: https://who.is/whois/github.com
==================================================
Domain: example.com
MX Records:
  mxl.example.com
  mx2.aspmx.l.example.com
    Non-authoritative answer:
DMARC Record:
        ";p=none;rua=mailto:example@example.com.br"
DMARC exists, but no policies defined
For more information about this domain, visit: https://who.is/whois/example.com
==================================================
Domain: example.com
MX Records:
  mx.example1.com
  mx.example1.com

Non-authoritative answer:
DMARC Record:
        ";p=quarantine;rua=mailto:dmarc-ab@service.alibaba.com;ruf=mailto:dmarc-ab@service.alibaba.com"
The current DMARC policy for this domain is QUARANTINE
For more information about this domain, visit: https://who.is/whois/example.com


Note that in PowerShell, domain ownership info is not shown. The reason is because PowerShell needs to use paid API in order to retrieve info about domain owners. That is why this function in PowerShell was removed from the DMARC HUNTER project.

*created by The Cyber-Intruder.
