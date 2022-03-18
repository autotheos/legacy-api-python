from legacyapi import Legacy
from legacyapi import HttpProvider

full_node = HttpProvider('https://apilg.lgcyscan.network/')
solidity_node = HttpProvider('https://apilg.lgcyscan.network/')
event_server = HttpProvider('https://apilg.lgcyscan.network/')

# option 1
legacy = Legacy(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)

# option 2
legacy_v2 = Legacy()

# option 3
legacy_v3 = Legacy(
    default_address='TRWBqiqoFZysoAeyR1J35ibuyc8EvhUAoY',
    private_key='...'
)
