import os
import config

# PHP-FPM config generator by John Tate (johntate.org)
# licenced under the MIT licence.

# This script gets all the users from the group and makes a php-fpm config for
# that particular user. The config is based on a template where %USER% is repl-
# aced by the users name.

# This script runs on the production system Occulus Omega and works.
#   http://occuomegawqtkl6j.onion/

def getUsers():
    users = []
    f = open(config.systemGroups,'r')
    for line in f:
        splitted = line.split(':')
        if (splitted[0] == "users"):
            userline = splitted[3].split(',')
            for user in userline:
                users.append(user.strip('\n'))
    return users

def customConfig(user):
    # checks if there is a custom configuration for a user.
    if (os.path.isfile(config.customConfigs + user + ".tpl")):
        return config.customConfigs + user + ".tpl"
    return config.configTemplate

def genConfig(user):
    tpl = open(customConfig(user),'r')
    out = open(config.outputDir + user + ".conf",'w')
    for line in tpl:
        out.write(line.replace('%USER%',user))

listConfig = os.listdir(config.outputDir)
for configFile in listConfig:
    if (configFile.endswith(".conf")):
        print("Removing file: " + config.outputDir + configFile)
        os.remove(config.outputDir + configFile)

users = getUsers()
for user in users:
    print("Generating fpm config for user: " + user)
    genConfig(user)
