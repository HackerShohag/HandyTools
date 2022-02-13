'''
<no-license>
A tool to make with VObject module to merge the duplicate contacts. It became handy. The sortNumber function can perform the task to sort only the Bangladeshi numbers
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

def sortNumber(number):
    number = ''.join(str(v) for v in [int(word) for word in number if word.isdigit()])
    if len(number) == 11:
        number = number.replace("0",'',1)
        number = "+880 " + number[:4] + "-" + number[4:]
    if len(number) == 13:
        number = "+" + number[:3] + " " + number[3:7] + "-" + number[7:]
    return number


data = open("/home/shohag/Videos/removedtags.vcf",'r').read()
newVObject = vobject.vCard()

nameList = []
sortedContactsList = []

for vcard in vobject.readComponents(data):
    if vcard.fn.value.lower() in nameList:
        index = nameList.index(vcard.fn.value.lower())
        singleOldVObjectData = vobject.readOne(sortedContactsList[index])
        print(f"{bcolors.WARNING}{bcolors.BOLD}Dup: {bcolors.ENDC}{bcolors.WARNING}Duplicate contact, index: {index}, name: {vcard.fn.value}")
        newPhoneNumbers = vcard.contents['tel']
        for number in newPhoneNumbers:
            tel = singleOldVObjectData.add('tel')
            tel.type_param = "cell"
            tel.value = sortNumber(number.value)
            print(f"\t{bcolors.WARNING}{bcolors.OKBLUE}DupInfo: {bcolors.ENDC}{bcolors.OKBLUE}added duplicate number {tel.value}")
        sortedContactsList[index] = singleOldVObjectData.serialize()
    else:
        vcard.tel.value = sortNumber(vcard.tel.value)
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}AddInfo: {bcolors.ENDC}{bcolors.OKGREEN}added new contact {vcard.fn.value}, {vcard.tel.value}")
        nameList.append(vcard.fn.value.lower())
        sortedContactsList.append(vcard.serialize())


file = open("sortedContactsWithRemovedTags.vcf",'w')
print(f"{bcolors.BOLD}{bcolors.HEADER}Info: {bcolors.ENDC}{bcolors.HEADER}Writting all the sorted data to the 'sortedContactsWithRemovedTags.vcf' file")
file.write(''.join(sortedContactsList))
print(f"{bcolors.BOLD}{bcolors.HEADER}Info: {bcolors.ENDC}{bcolors.HEADER}write successful, closing now")
file.close()
