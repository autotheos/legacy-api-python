from legacyapi import Legacy
from legacyapi import HttpProvider

full_node = HttpProvider('https://apilg.lgcyscan.network/')
solidity_node = HttpProvider('https://apilg.lgcyscan.network/')
event_server = HttpProvider('https://apilg.lgcyscan.network/')
legacy = Legacy(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)



legacy.toSun(1)
# result: 1000000

legacy.fromSun(1000000)
# result: 1


