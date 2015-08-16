
import contact

def start():
    print('1 - Add a new contact')
    print('2 - Show all contacts')
    print('3 - Edit a contact')
    print('4 - Fina a contact')
    print('5 - Delete a contact')
    print('6 - Exit')
    print("--->")
    userchoice = input("enter number> ")
    return(userchoice)

def contactString():
    conString = "Should this contact be Simple (%s),"%ContactType[0]+" Friend (%s),"%ContactType[1]+\
                " Professional (%s)"%ContactType[2]+" or Both (%s)"%ContactType[3]+"? "
    # conString = conString.format(ContactType[0],ContactType[1] ,ContactType[2], ContactType[3])
    return conString



def createContact(ch, olderContact=None):
    if ch == ContactType[0]:
        directory.append(contact.Contact(olderContact))
    elif ch == ContactType[1]:
        directory.append(contact.FriendContact(olderContact))
    elif ch == ContactType[2]:
        directory.append(contact.ProfessionalContact(olderContact))
    elif ch == ContactType[3]:
        directory.append(contact.ProfessionalFriendContact(olderContact))
    else:
        print("you have entered an invalid choice")
        start()

    directory.sort()

def editContact():
    contactChoice = input("Enter a valid number of the contact you wish to edit: ")
    while True:
        if contactChoice < "1" or contactChoice > str(len(directory)):
            contactChoice  = input("Enter a valid number of the contact you wish to edit: ")
        else:
            break

    typecontact = typeOfContact()
    print("For the following fields click enter if there's no change, " +
          "a new value if you want to replace the field, " +
          "or x if you want to delete the field (the name field cannot be deleted).")
    temp = directory[int(contactChoice)-1]
    del directory[int(contactChoice)-1]

    createContact(typecontact,temp)




def printContacts():
    print("Phone book numbers are:")
    for i in range(len(directory)):
        print("Contact Number",str(i+1) +":",directory[i])
    print("")



def removeContact():
    contactChoice = input("Enter a valid number of the contact you wish to delete: ")
    while True:
        if contactChoice < "1" or contactChoice > str(len(directory)):
            contactChoice  = input("Enter a valid number of the contact you wish to delete: ")
        else:
            break
    del directory[int(contactChoice)-1]

    # if name in numbers:
    #     del numbers[name]
    # else:
    #     print(name, " was not found")

def lookupContact():
    match = input("Type contact details (name, phone, email): ")
    for i in range(len(directory)):
        if directory[i].Match(match):
           print("Contact Number",str(i+1) +":",directory[i])

    # if name in numbers:
    #     return "The number is " + numbers[name]
    # else:
    #     return name + "Was Not Found"
def typeOfContact():
    typeContact = input(contactString())
    while True:
        if typeContact not in ContactType:
            typeContact = input(contactString())
        else:
            break
    return typeContact


#main
directory = []
ContactType = ["S", "F", "P", "B"]

while True:
    ch = start()
    if ch =='1':
        ch =typeOfContact()
        createContact(ch)

    elif ch == '2':
        print('you chose to print all the contacts')
        printContacts()

    elif ch == '3':
        print('you chose to edit a contact')
        editContact()
    elif ch == '4':
        print("you chose to find a contact")
        lookupContact()

    elif ch =='5':
        print('you chose to delete a contact')
        removeContact()

    elif ch == '6':
        print('Bye Bye')
        break
    else:
        print("You have Entered an invalid key")
        start()
