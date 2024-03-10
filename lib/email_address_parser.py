import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the string into a list of email addresses
        addresses_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.email_addresses)

        # Remove duplicate email addresses and sort alphabetically
        unique_addresses = sorted(set(addresses_list))

        return unique_addresses