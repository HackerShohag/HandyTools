import smtplib
from validate_email_address import validate_email

def email_validator(email):
    # Validate email format
    is_valid = validate_email(email)
    if not is_valid:
        return False, "Invalid email format."
    
    # Check if email exists using SMTP
    try:
        domain = email.split('@')[1]
        server = smtplib.SMTP(f'smtp.{domain}', 25)
        server.ehlo()
        server.quit()
        return True, "Email is valid and reachable."
    except Exception as e:
        return False, f"Unable to reach the email server: {str(e)}"

def process_emails(input_file, valid_file, invalid_file):
    with open(input_file, 'r') as infile, \
         open(valid_file, 'w') as valid_outfile, \
         open(invalid_file, 'w') as invalid_outfile:
        
        emails = infile.readlines()
        
        for email in emails:
            email = email.strip()
            status, message = email_validator(email)
            
            if status:
                print(f"Valid: {email}")
                valid_outfile.write(f"{email}\n")
            else:
                print(f"Invalid: {email} - {message}")
                invalid_outfile.write(f"{email} - {message}\n")

# Usage
input_file = 'emails.txt'
valid_file = 'valid_emails.txt'
invalid_file = 'invalid_emails.txt'

process_emails(input_file, valid_file, invalid_file)

