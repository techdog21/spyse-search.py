from spyse import Client
import argparse

client = Client("API Here")

#Argument Parser
parser = argparse.ArgumentParser(description='Options')
parser.add_argument("domain", type=str, help='domain name to be searched')
args = parser.parse_args()

if args.domain:

        d = client.get_domain_details(args.domain)

        print(f"Domain details:")
        print(f"Website title: {d.http_extract.title}")
        print(f"Alexa rank: {d.alexa.rank}")
        print(f"Certificate subject org: {d.cert_summary.subject.organization}")
        print(f"Certificate issuer org: {d.cert_summary.issuer.organization}")
        print(f"Updated at: {d.updated_at}")
        print(f"DNS Records: {d.dns_records}")
        print(f"Technologies: {d.technologies}")
        print(f"Vulnerabilities: {d.cve_list}")
        print(f"Trackers: {d.trackers}")

