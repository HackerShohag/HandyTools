import os

tag1 = '''  <static>
    <duration>1795.0</duration>
    <file>/usr/share/backgrounds/'''

tag2 = '''</file>
  </static>
  <transition>
    <duration>5.0</duration>
    <from>/usr/share/backgrounds/'''
tag3 = '''</from>
    <to>/usr/share/backgrounds/'''
tag4 = '''</to>
  </transition>'''

dir_path = os.getcwd()

# list to store files
files = []

# Iterate directory
for path in os.listdir(dir_path):
  # check if current path is a file
  if os.path.isfile(os.path.join(dir_path, path)):
    files.append(path)

with open("script_file.txt", 'w') as writeFile:
  for i in range(0, len(files) -1):
    writeFile.write(tag1 + files[i] + tag2 + files[i] + tag3 + files[i+1] + tag4)



  # <static>
  #   <duration>1795.0</duration>
  #   <file>/usr/share/backgrounds/Saffron_by_Rakesh_Yadav.png</file>
  # </static>
  # <transition>
  #   <duration>5.0</duration>
  #   <from>/usr/share/backgrounds/Saffron_by_Rakesh_Yadav.png</from>
  #   <to>/usr/share/backgrounds/Kinetic_Kudu_by_Joshua_T_dark.jpg</to>
  # </transition>
