'''
<no-license>
A tool to make with VObject module to merge the duplicate contacts. It became handy.
<feel free to use it>
'''


import vobject

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

data = open("/home/shohag/Videos/ubuntu_contacts_20220203095752.vcf",'r').read()
newVObject = vobject.vCard()

nameList = []
sortedContactsList = []

for vcard in vobject.readComponents(data):
    if vcard.fn.value in nameList:
        index = nameList.index(vcard.fn.value)
        singleOldVObjectData = vobject.readOne(sortedContactsList[index])
        print(f"{bcolors.WARNING}{bcolors.BOLD}Dup: {bcolors.ENDC}{bcolors.WARNING}Duplicate contact, index: {index}, name: {vcard.fn.value}")
        newPhoneNumbers = vcard.contents['tel']
        for number in newPhoneNumbers:
            tel = singleOldVObjectData.add('tel')
            tel.type_param = "cell"
            tel.value = number.value
            print(f"\t{bcolors.WARNING}{bcolors.OKBLUE}DupInfo: {bcolors.ENDC}{bcolors.OKBLUE}added duplicate number {number.value}")
        sortedContactsList[index] = singleOldVObjectData.serialize()
    else:
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}AddInfo: {bcolors.ENDC}{bcolors.OKGREEN}added new contact {vcard.fn.value}, {vcard.tel.value}")
        nameList.append(vcard.fn.value)
        sortedContactsList.append(vcard.serialize())


file = open("sortedContacts.vcf",'w')
print(f"{bcolors.BOLD}{bcolors.HEADER}Info: {bcolors.ENDC}{bcolors.HEADER}Writting all the sorted data to the 'sortedContacts.vcf' file")
file.write(''.join(sortedContactsList))
print(f"{bcolors.BOLD}{bcolors.HEADER}Info: {bcolors.ENDC}{bcolors.HEADER}write successful, closing now")
file.close()
