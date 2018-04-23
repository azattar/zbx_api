#!/usr/bin/python

from zabbix_functions import *

url = 'http://monitoracao/zabbix/api_jsonrpc.php'

login = 'zatta'
passwd = 'xyzpass'
token = zbx_get_auth(url, login, passwd)
# print(token)

# groupName = "ATI/DESET/GSUP/BD Oracle Instancias"
# trigg_group_dict = zbx_get_group_triggers(url, token, groupName)
# print(trigg_group_dict)

hostNames = ["srv0055.bndes.net", "srv0070.bndes.net", "srv0081.bndes.net", "srv0088.bndes.net", "ora_pasm",
             "ora_pacdir0a", "ora_pacdir0b", "ora_pinfra0a", "ora_pbnddw0a", "ora_ppacte0a", "ora_pbndes0a"]

# trigg_host_list = zbx_get_host_triggers(url, token, "ora_ppacte0a")
# print(trigg_host_list)

for y in hostNames:
    trigg_host_list = zbx_get_host_triggers(url, token, y)
    for x in trigg_host_list:
        print('"' + x['triggerid'] + '"' + ' ' + '"' + y + '"' + ' ' + '"' + x['description'] + '"')

# for y in hostNames:
#    print(y)
#    trigger_host_list = zbx_get_host_triggers(url, token, y)
#    for x in trigger_host_list:
#        print("    " + x['trigger_id'])
#        print("    " + x['description'])
#        print("    " + zbx_get_trigger_status(url, token, x['triggerid']))
#        print(' ')

# triggerID = 26497
# status = zbx_get_trigger_status(url, token, triggerID)
# print(status)