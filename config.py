# This is the configuration for fpm-config-generator. It exists in its own file
# because then a script can automatically update it easier.

global systemGroups
global groupName
global configTemplate
global outputDir
global customConfigs
systemGroups = "group" #where the list of secondary groups are.
groupName = "users" #the group who get fpm configs
configTemplate = "templates/template.tpl"
outputDir = "fpm-out/" #requires trailing slash
customConfigs = "templates/custom/"
