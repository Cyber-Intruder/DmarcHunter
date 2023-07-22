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
Domain owner information not available
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

4 - Navigate to the Dmarc Hunter files directory;

5 - Run the following command: ".\DmarcHunter.ps1" or ".\ptbr-DmarcHunter.ps1" based on the language that you want to work; 

6 - The results will be shown.

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
Não é resposta autoritativa:
DMARC Record:
        ";p=reject;pct=100;rua=mailto:dmarc@github.com"
The current DMARC policy for this domain is REJECT
For more information about this domain, visit: https://who.is/whois/github.com
==================================================
Domain: google.com
MX Records:
  smtp.google.com
Non-authoritative answer:
DMARC Record:
        ";p=reject;rua=mailto:mailauth-reports@google.com"
The current DMARC policy for this domain is REJECT
For more information about this domain, visit: https://who.is/whois/google.com

Note that in PowerShell, domain ownership info is not shown.


*created by The Cyber-Intruder


