# ITEM 04_EJ_3
# Cambiar nombre HOST

from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.1.136",
    port=830,
    username="cisco",
    password="cisco123!",
)

netconf_host = """
    <config>
        <native xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-native'>
            <hostname>BRAVO-GATICA-JORQUERA-GONZALEZ</hostname>
        </native>
    </config>
                """

netconf_reply = m.edit_config(target='running', config=netconf_host)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
