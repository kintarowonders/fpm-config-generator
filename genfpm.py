import os

# PHP-FPM config generator by John Tate (johntate.org)
# licenced under the MIT licence.

# This script gets all the users from the group and makes a php-fpm config for
# that particular user. The config is based on a template where %USER% is repl-
# aced by the users name.

# This script runs on the production system Occulus Omega and works.
#   http://occuomegawqtkl6j.onion/

systemGroups = '/etc/group' #where the list of secondary groups are.
groupName = "users" #the group who get fpm configs
configTemplate = 'template.tpl' 
outputDir = '/etc/fpm.d/' #requires trailing slash

def getUsers():
    users = []
    f = open(systemGroups,'r')
    for line in f:
        splitted = line.split(':')
        if (splitted[0] == "users"):
            userline = splitted[3].split(',')
            for user in userline:
                users.append(user.strip('\n'))
    return users

def genConfig(user):
    tpl = open(configTemplate,'r')
    out = open(outputDir + user + ".conf",'w')
    for line in tpl:
        out.write(line.replace('%USER%',user))

listConfig = os.listdir(outputDir)
for configFile in listConfig:
    if (configFile.endswith(".conf")):
        print("Removing file: " + outputDir + configFile)
        os.remove(outputDir + configFile)

users = getUsers()
for user in users:
    print("Generating fpm config for user: " + user)
    genConfig(user)
