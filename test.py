from Email import MyEmail

temp = MyEmail('email_account', 'password', 'server_address')
email = temp.create_email('title_email', 'content_email')
temp.add_email_attachment(email, '/path/to/the/file', 'file_name')
temp.add_email_attachment(email, './path/to/the/file2', 'file_name2')
temp.send_email(email, ['receiver', 'receiver2'])

temp.quit()
