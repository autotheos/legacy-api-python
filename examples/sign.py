from legacyapi import Legacy
from legacyapi import HttpProvider

full_node = HttpProvider('https://apilg.lgcyscan.network/')
solidity_node = HttpProvider('https://apilg.lgcyscan.network/')
event_server = HttpProvider('https://apilg.lgcyscan.network/')

legacy = Legacy(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


legacy.private_key = 'private_key'
legacy.default_address = 'default address'

# create transaction
create_tx = legacy.transaction_builder.send_transaction('to', 1, 'from')

# offline sign
offline_sign = legacy.lgcy.sign(create_tx)


# online sign (Not recommended)
online_sign = legacy.lgcy.online_sign(create_tx)

