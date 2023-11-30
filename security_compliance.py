# security_compliance.py
# Ensures compliance with security standards

import re

class SecurityCompliance:
    def __init__(self):
        # Initialize with any necessary compliance rules or standards
        self.compliance_rules = {
            "no_sensitive_data": re.compile(r"(?i)\b(ssn|password|credit\s*card|bank\s*account)\b"),
            "max_length": 1000  # Maximum length of data
        }

    def check_compliance(self, data):
        """ Check if the data complies with all the defined rules """
        return self.check_no_sensitive_data(data) and self.check_length(data)

    def check_no_sensitive_data(self, data):
        """ Check that the data does not contain sensitive information """
        if isinstance(data, str) and self.compliance_rules["no_sensitive_data"].search(data):
            print("Data contains sensitive information.")
            return False
        return True

    def check_length(self, data):
        """ Check that the data does not exceed the maximum length """
        if len(data) > self.compliance_rules["max_length"]:
            print("Data exceeds maximum allowed length.")
            return False
        return True

    # Additional compliance checking methods as needed

# Example usage
if __name__ == '__main__':
    compliance_checker = SecurityCompliance()

    # Example data checks
    print(compliance_checker.check_compliance("This is a test string without sensitive data."))
    print(compliance_checker.check_compliance("This is a test string with SSN 123-45-6789."))
