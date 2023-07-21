import dns.resolver
import subprocess
import whois

def check_mx(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        mx_records = [str(r.exchange)[:-1] for r in answers]
        return mx_records
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return None
    except dns.exception.DNSException as e:
        print(f"Erro ao resolver MX para {domain}: {e}")
        return None

def check_dmarc(domain):
    try:
        result = subprocess.run(['dig', '+short', 'TXT', f'_dmarc.{domain}'], capture_output=True, text=True)
        dmarc_record = result.stdout.strip()
        return dmarc_record
    except subprocess.CalledProcessError:
        return None

def get_domain_owner(domain):
    try:
        domain_info = whois.whois(domain)
        if isinstance(domain_info.registrant_name, list):
            owner = domain_info.registrant_name[0]
        else:
            owner = domain_info.registrant_name
        return owner
    except Exception:
        return None

def display_banner():
    banner_text = r"""
╔╦╗╔╦╗╔═╗╦═╗╔═╗  ╦ ╦╦ ╦╔╗╔╔╦╗╔═╗╦═╗
 ║║║║║╠═╣╠╦╝║    ╠═╣║ ║║║║ ║ ║╣ ╠╦╝
═╩╝╩ ╩╩ ╩╩╚═╚═╝  ╩ ╩╚═╝╝╚╝ ╩ ╚═╝╩╚═
"""
    print(banner_text)

def main():
    display_banner()

    # Define ANSI escape sequences for red, green, blue, and reset colors
    red_color = "\033[91m"
    green_color = "\033[92m"
    blue_color = "\033[94m"
    reset_color = "\033[0m"

    file_path = 'domains.txt'  # Caminho para o arquivo contendo a lista de domínios

    with open(file_path, 'r') as file:
        domains = file.read().splitlines()

    for domain in domains:
        print(f"{green_color}Domínio: {domain}{reset_color}")

        mx_records = check_mx(domain)
        if mx_records:
            print("Registros MX:")
            for mx in mx_records:
                print(f"  {mx}")
        else:
            print("Nenhum registro MX encontrado.")

        dmarc_record = check_dmarc(domain)
        if dmarc_record:
            print("Registro DMARC:")
            print(f"  {dmarc_record}")
            if "p=none" in dmarc_record:
                print(f"{red_color}DMARC existe, mas não há políticas definidas{reset_color}")
            elif "p=quarantine" in dmarc_record:
                print(f"{red_color}A política atual de DMARC para este domínio é QUARENTENA{reset_color}")
            elif "p=reject" in dmarc_record:
                print(f"{red_color}A política atual de DMARC para este domínio é REJEITAR{reset_color}")
        else:
            print(f"{red_color}Nenhum registro DMARC encontrado para este domínio{reset_color}")

        domain_owner = get_domain_owner(domain)
        if domain_owner:
            print(f"{blue_color}Proprietário do Domínio: {domain_owner}{reset_color}")
        else:
            print(f"{blue_color}Informações do proprietário do domínio não disponíveis{reset_color}")

        print("=" * 50)

if __name__ == "__main__":
    main()

