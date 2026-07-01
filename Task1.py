import re

# Read input file
with open("emails.txt", "r") as file:
    content = file.read()

# Find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save emails to output file
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("Found Emails:")
for email in emails:
    print(email)