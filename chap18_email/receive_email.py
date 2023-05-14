import email
import getpass
import imaplib

with imaplib.IMAP4_SSL('imap.gmail.com') as imap:
    user = input('User: ')
    password = getpass.getpass('Password: ')

    print(f'Login: {imap.login(user, password)}')
    print(imap.list())

    print(f'\nINBOX:\n{imap.select("INBOX")}')
    search_criteria = 'SUBJECT "new python test"'
    print(f'Search {search_criteria}')
    typ, data = imap.search(None, search_criteria)
    print(typ)
    print(data[0])

    email_id = data[0]
    result, email_data = imap.fetch(email_id, '(RFC822)')
    print(result)
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    for part in email_message.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_payload(decode=True)
            print(body)
