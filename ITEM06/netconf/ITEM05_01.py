#ITEM 05_EJ_1
#Eliminar INT LOOPBACK


from ncclient import manager

#Conexión con RT


m=manager.connect(
    host="192.168.1.136",
    port=830,
    username="cisco",
    password="cisco123!",
    )

#Eliminar Loopback

netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback operation="delete">
                <name>11</name>
            </Loopback>
        </interface>
    </native>
</config>
"""

#imprimir confirmación de acción
netconf_reply = m.edit_config(target='running', config=netconf_loopback)
print(netconf_reply)