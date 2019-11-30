class Contact:
    all_contacts = []

    def __init__(self):
        Contact.all_contacts.append(1)

Contact()
print(Contact().all_contacts)
print(Contact.all_contacts)
