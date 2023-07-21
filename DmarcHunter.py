import dns.resolver
import subprocess

def check_mx(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        mx_records = [str(r.exchange)[:-1] for r in answers]
        return mx_records
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return None
    except dns.exception.DNSException as e:
        print(f"Error while resolving MX for {domain}: {e}")
        return None

def check_dmarc(domain):
    try:
        result = subprocess.run(['dig', '+short', 'TXT', f'_dmarc.{domain}'], capture_output=True, text=True)
        dmarc_record = result.stdout.strip()
        return dmarc_record
    except subprocess.CalledProcessError:
        return None


