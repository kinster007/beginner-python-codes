"""
email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
"""

def email_list(domains):
	emails = []
	for key, users in domains.items():
	  for user in users:
	    emails.append("{}@{}".format(user, key))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))