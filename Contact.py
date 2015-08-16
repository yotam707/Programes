
import re

class Contact:
    def __init__(self, olderContact = None):
        data = Contact.ReadValues(olderContact)
        self.name = data[0]
        if data[1] != "":
            self.number = data[1]
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        nameStr = "Name:" +self.name
        if hasattr(self, "number"):
            nameStr+= ", Cell Phone: "+str(self.number)
        return nameStr

    def ReadValues(olderContact):
        if olderContact is None:
            name = input("Name: ")
            while name == "":
                print("Name cannot be empty.")
                name = input("Name: ")

        else:
            name = input("Name (%s):" %olderContact.name)
        number = Contact.getNumber(0,olderContact)

        if name != "":
            data = [name]
        else:
            data = [olderContact.name]

        if number =='x':
            number =""

        data.append(number)

        return data

    def Match(self, matchString):
        if matchString in self.name:
            return True
        if hasattr(self, "number"):
            return matchString in self.number
        return False


    def getNumber(numberAction, olderContact):
        numberTypes = {0: "Cell Phone: %s ", 1:"Home Phone: %s", 2:"Work Phone: %s"}
        numberAttr = ["number","homeNumber", "workNumber"]
        prevNumber = ""
        if olderContact != None and hasattr(olderContact, numberAttr[numberAction]):
            if numberAction ==0:
                prevNumber += "%s" %olderContact.number
            elif numberAction ==1:
                prevNumber += "%s" %olderContact.homeNumber
            elif numberAction ==2:
                prevNumber += "%s" %olderContact.workNumber
            else:
                print("please enter a valid number selection")

        number = input(numberTypes[numberAction] %prevNumber)
        while not(number.isdigit() or number == "" or (number == 'x' if olderContact is not None else False)):
                print("Cell phone can be digits only or empty")
                number = input(numberTypes[numberAction] %prevNumber)

        if number == "":
            number = str(prevNumber[2:-1])
        return str(number)


    def getEmail(emailAction, olderContact):
        emailTypes = {0: "Personal Email: %s", 1: "Work Email: %s"}
        emailAttr = ["personalEmail","workEmail"]
        prevEmail = ""
        if olderContact != None and hasattr(olderContact,emailAttr[emailAction]):
            if emailAction == 0:
                prevEmail += "%s" %olderContact.personalEmail
            elif emailAction ==1:
                prevEmail += "%s" %olderContact.workEmail
            else:
                print("You have enters an invalid selection")
        email = input(emailTypes[emailAction] %prevEmail)
        emailValid = re.match(r'[\w\.-]+@[\w\.-]+',email)

        while(emailValid is None and email != "" ):
            if olderContact is not None and email == 'x':
                email ==""
            else:
                print("Please enter a valid email address or an empty line:")
                email = input(emailTypes[emailAction] %prevEmail)
                emailValid = re.match(r'[\w\.-]+@[\w\.-]+',email)

        if email == "":
            email = prevEmail[:-1]
        elif email == 'x':
            email = ""
        return email

        # def getName(self):
    #     return self.name
    # def getNumber(self):
    #     return self.number

class FriendContact(Contact):
    def __init__(self,olderContact = None):
        super().__init__(olderContact)
        data = FriendContact.ReadValues(olderContact)
        if data[0] != "":
            self.homeNumber = data[0]
        if data[1] !="":
            self.personalEmail = data[1]

    def __str__(self):
        friendString = super().__str__()
        if hasattr(self, "homeNumber"):
            friendString += " ,Home Phone: %s" %self.homeNumber
        if hasattr(self,"personalEmail"):
            friendString += ", Personal Email: %s" %self.personalEmail

        return friendString

    def ReadValues(olderContact):
        return [Contact.getNumber(1,olderContact), Contact.getEmail(0, olderContact)]


    def Match(self, matchString):
        if not isinstance(self,ProfessionalFriendContact):
            if super(FriendContact,self).Match(matchString):
                return True
        if hasattr(self,"homeNumber"):
            if matchString in self.homeNumber:
                return True
        if hasattr(self, "personalEmail"):
            if matchString in self.personalEmail:
                return True

        return False


    # def getHomeNumber(self):
    #     return self.homeNumber
    # def getPersonalEmail(self):
    #     return self.personalEmail

class ProfessionalContact(Contact):
    def __init__(self,olderContact=None):
        super().__init__(olderContact)
        data = ProfessionalContact.ReadValues(olderContact)

        if data[0] != "":
            self.workPhone = data[0]
        if data[1] != "":
            self.workEmail = data[1]


    def __str__(self):
        professionalString = super().__str__()
        if hasattr(self,"workPhone"):
            professionalString += ", Work Phone: %s " %self.workPhone
        if hasattr(self,"workEmail"):
            professionalString += ", Work Email: %s " %self.workEmail
        return professionalString



    def ReadValues(olderContact):
        return [Contact.getNumber(2,olderContact), Contact.getEmail(1,olderContact)]


    def Match(self, matchString):
        if super().Match(matchString):
            return True
        if hasattr(self,"workPhone"):
            if self.workPhone in matchString:
                return True
        if hasattr(self,"workEmail"):
            if self.workEmail in matchString:
                return True
        return False

    # def getWorkPhone(self):
    #     return self.workPhone
    # def getWorkEmail(self):
    #     return self.workEmail

class ProfessionalFriendContact(FriendContact,ProfessionalContact):
    def __init__(self,olderContact=None):
        super().__init__(olderContact)

    def __str__(self):
        PFString = super().__str__()
        return PFString

    def Match(self, matchString):
        return super().Match(matchString)

