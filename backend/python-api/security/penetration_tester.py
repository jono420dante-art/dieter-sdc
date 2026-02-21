# Penetration Tester Module
# This module includes security testing and vulnerability scanning tools.

import subprocess

class PenetrationTester:
    def __init__(self, target):
        self.target = target

    def run_nmap(self):
        """Run nmap for network scanning"""
        print(f"Running nmap on {self.target}")
        subprocess.run(['nmap', self.target])

    def run_nessus(self):
        """Run Nessus for vulnerability scanning"""
        print(f"Running Nessus scan on {self.target}")
        subprocess.run(['nessus', '-T', self.target])

    def run_metaspoloit(self):
        """Run Metasploit for penetration testing"""
        print(f"Running Metasploit on {self.target}")
        subprocess.run(['msfconsole', '-x', f'search {self.target}'])

if __name__ == '__main__':
    tester = PenetrationTester('target_ip_or_domain')
    tester.run_nmap()
    tester.run_nessus()
    tester.run_metaspoloit()