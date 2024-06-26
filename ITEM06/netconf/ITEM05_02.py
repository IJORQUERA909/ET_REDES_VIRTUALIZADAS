#ITEM 05_EJ_2
#Crear INT LOOPBACK SHUTDOWN


from ncclient import manager

#Conexión con RT


m=manager.connect(
    host="192.168.1.136",
    port=830,
    username="cisco",
    password="cisco123!",
    )

#Creacion de Loopback con estao SHUTDOWN

netconf_loopback_sh = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>22</name>
                <ip>
                    <address>
                        <primary>
                            <address>22.22.22.22</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
                <shutdown/>
            </Loopback>
        </interface>
    </native>
</config>
"""


#imprimir confirmación de acción
netconf_reply = m.edit_config(target='running', config=netconf_loopback_sh)
print(netconf_reply)