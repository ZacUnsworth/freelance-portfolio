import csv
import smtplib
from email.message import EmailMessage

def generate_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Status", "Last Active"])
        for row in data:
            writer.writerow(row)

def send_email(filename, recipient):
    msg = EmailMessage()
    msg["Subject"] = "Inactive Users Report"
    msg["From"] = "your_email@example.com"
    msg["To"] = recipient
    msg.set_content("Please find the attached inactive user report.")
    
    with open(filename, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=filename)

    # Example using Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("your_email@example.com", "your_password")
        smtp.send_message(msg)

# Example usage
data = [["Alice", "Inactive", "2024-01-15"], ["Bob", "Inactive", "2024-01-20"]]
filename = "inactive_users.csv"
generate_csv(data, filename)
# send_email(filename, "recipient@example.com")  # Uncomment and configure to send