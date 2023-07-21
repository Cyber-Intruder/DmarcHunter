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
        print(f"Error resolving MX for {domain}: {e}")
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

    # Define ANSI escape sequences for red, green, blue, yellow, and reset colors
    red_color = "\033[91m"
    green_color = "\033[92m"
    blue_color = "\033[94m"
    yellow_color = "\033[93m"
    white_color = "\033[97m"
    reset_color = "\033[0m"

    file_path = 'domains.txt'  # Path to the file containing the list of domains

    with open(file_path, 'r') as file:
        domains = file.read().splitlines()

    for domain in domains:
        print(f"{green_color}Domain: {domain}{reset_color}")

        mx_records = check_mx(domain)
        if mx_records:
            print("MX Records:")
            for mx in mx_records:
                print(f"  {mx}")
        else:
            print("No MX records found.")

        dmarc_record = check_dmarc(domain)
        if dmarc_record:
            print(f"{white_color}DMARC Record: {dmarc_record}{reset_color}")
            if "p=none" in dmarc_record:
                print(f"{red_color}DMARC exists, but there are no defined policies{reset_color}")
            elif "p=quarantine" in dmarc_record:
                print(f"{red_color}The current DMARC policy for this domain is QUARANTINE{reset_color}")
            elif "p=reject" in dmarc_record:
                print(f"{red_color}The current DMARC policy for this domain is REJECT{reset_color}")
        else:
            print(f"{red_color}No DMARC record found for this domain{reset_color}")

        domain_owner = get_domain_owner(domain)
        if domain_owner:
            print(f"{blue_color}Domain Owner: {domain_owner}{reset_color}")
        else:
            print(f"{blue_color}Domain owner information not available{reset_color}")

        whois_link = f"{yellow_color}For more information about this domain, visit: https://who.is/whois/{domain}{reset_color}"
        print(whois_link)

        print("=" * 50)

if __name__ == "__main__":
    main()
