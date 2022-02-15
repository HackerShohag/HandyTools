import re

data = open("/home/shohag/Videos/ubuntu_contacts_20220203095752.vcf",'r').read()
data = re.sub(r"(FN:.+) [NPCH]\n", r"\1\n", data)
data = re.sub(r"(FN:.+) TL\n", r"\1\n", data)
open("removedtags.vcf",'w').write(data)
