## Demo: Web3.py ##

from web3 import Web3

Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/95408920a948489c99c5bcb436235bd2"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

# Activity: Web3.py ** 

from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/95408920a948489c99c5bcb436235bd2"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.eth.gasPrice)


## Demo: Check Wallet balnace ##

from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/95408920a948489c99c5bcb436235bd2"
web3 = Web3(Web3.HTTPProvider(infura_url))

# # Fill in your account here
balance = web3.eth.getBalance("0xec914D5a21EeC7692a985E80207Df05CdD1E2CE5")
print(web3.fromWei(balance, "ether"))


## Demo: Get info from OMG Token ##

import json
from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/95408920a948489c99c5bcb436235bd2"
web3 = Web3(Web3.HTTPProvider(infura_url))

# OMG Address
abi = json.loads('[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
# OMG ABI
address = '0xd26114cd6EE289AccF82350c8d8487fedB8A0C07'

contract = web3.eth.contract(address=address, abi=abi)

totalSupply = contract.functions.totalSupply().call()
print(web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())
balance = contract.functions.balanceOf('0xd26114cd6EE289AccF82350c8d8487fedB8A0C07').call()
print(web3.fromWei(balance, 'ether'))

## Activity: Get info from Bancor Token ##

import json
from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/95408920a948489c99c5bcb436235bd2"
web3 = Web3(Web3.HTTPProvider(infura_url))

# OMG Address
abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_disable","type":"bool"}],"name":"disableTransfers","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"withdrawTokens","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_amount","type":"uint256"}],"name":"destroy","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"transfersEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"newOwner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint8"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_token","type":"address"}],"name":"NewSmartToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Issuance","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Destruction","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_prevOwner","type":"address"},{"indexed":false,"name":"_newOwner","type":"address"}],"name":"OwnerUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')
# OMG ABI
address = '0x1F573D6Fb3F13d689FF844B4cE37794d79a7FF1C'

contract = web3.eth.contract(address=address, abi=abi)

totalSupply = contract.functions.totalSupply().call()
print(web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())


## Demo: Transactions between 2 accounts on Ganache ##

from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0xf5D4e9649A28D0546d8361eDFc1DFc165b999DE7' # Fill me in
account_2 = '0xa14041B8E24CAd210D93e07Fe29D10Ba85982CCa' # Fill me in
private_key = '20870a2923a4c47b2e67db318b0b95147c88e290f33ec0795b4d7f0862fa8b9b' # Fill me in

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))

## Activity: Transactions between 2 accounts on Ganache ## 

from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0xa14041B8E24CAd210D93e07Fe29D10Ba85982CCa' # Fill me in
account_2 = '0xbd12Dc89638ED324d781109848F658D7231cC3eC' # Fill me in
private_key = '39bd329782326ef4622ddaa6ef43fc1d283f6298b6e972195c9414fc0ac698f4' # Fill me in

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(5, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))


## Demo: Compile Hello World Smart Contract on Ganache blockchain ##

import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org

# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]

# Greeter contract ABI
abi = json.loads('[{"inputs":[],"name":"Greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
# Greeter contract address - convert to checksum address
address = web3.toChecksumAddress('0x69375acdC39D9fD1ca3F31795a6744bf3f4f5d0D') # FILL ME IN
# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)
# Read the default greeting
print(contract.functions.greet().call())
# Set a new greeting
tx_hash = contract.functions.setGreeting('HEELLLLOOOOOO!!!').transact()
# Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)
# Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))

## Acitivty: Compile Conctractor Contract on Ganache blockchain ##

import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org

# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]

# Greeter contract ABI
abi = json.loads('[{"inputs":[],"name":"Greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
# Greeter contract address - convert to checksum address
address = web3.toChecksumAddress('0x69375acdC39D9fD1ca3F31795a6744bf3f4f5d0D') # FILL ME IN
# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)
# Read the default greeting
print(contract.functions.greet().call())
# Set a new greeting
tx_hash = contract.functions.setGreeting('HEELLLLOOOOOO!!!').transact()
# Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)
# Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))


## Demo: Deploy Hello World Contract  Smart Contract on Ganache ## 

import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi = json.loads('[{"inputs":[],"name":"Greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
bytecode = "608060405234801561001057600080fd5b506105c2806100206000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c8063777256c414610051578063a41368621461005b578063cfae321714610077578063ef690cc014610095575b600080fd5b6100596100b3565b005b6100756004803603810190610070919061034e565b610101565b005b61007f61011b565b60405161008c91906103d0565b60405180910390f35b61009d6101ad565b6040516100aa91906103d0565b60405180910390f35b6040518060400160405280600581526020017f48656c6c6f000000000000000000000000000000000000000000000000000000815250600090805190602001906100fe92919061023b565b50565b806000908051906020019061011792919061023b565b5050565b60606000805461012a906104a6565b80601f0160208091040260200160405190810160405280929190818152602001828054610156906104a6565b80156101a35780601f10610178576101008083540402835291602001916101a3565b820191906000526020600020905b81548152906001019060200180831161018657829003601f168201915b5050505050905090565b600080546101ba906104a6565b80601f01602080910402602001604051908101604052809291908181526020018280546101e6906104a6565b80156102335780601f1061020857610100808354040283529160200191610233565b820191906000526020600020905b81548152906001019060200180831161021657829003601f168201915b505050505081565b828054610247906104a6565b90600052602060002090601f01602090048101928261026957600085556102b0565b82601f1061028257805160ff19168380011785556102b0565b828001600101855582156102b0579182015b828111156102af578251825591602001919060010190610294565b5b5090506102bd91906102c1565b5090565b5b808211156102da5760008160009055506001016102c2565b5090565b60006102f16102ec84610417565b6103f2565b90508281526020810184848401111561030d5761030c61056c565b5b610318848285610464565b509392505050565b600082601f83011261033557610334610567565b5b81356103458482602086016102de565b91505092915050565b60006020828403121561036457610363610576565b5b600082013567ffffffffffffffff81111561038257610381610571565b5b61038e84828501610320565b91505092915050565b60006103a282610448565b6103ac8185610453565b93506103bc818560208601610473565b6103c58161057b565b840191505092915050565b600060208201905081810360008301526103ea8184610397565b905092915050565b60006103fc61040d565b905061040882826104d8565b919050565b6000604051905090565b600067ffffffffffffffff82111561043257610431610538565b5b61043b8261057b565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b82818337600083830152505050565b60005b83811015610491578082015181840152602081019050610476565b838111156104a0576000848401525b50505050565b600060028204905060018216806104be57607f821691505b602082108114156104d2576104d1610509565b5b50919050565b6104e18261057b565b810181811067ffffffffffffffff82111715610500576104ff610538565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f830116905091905056fea26469706673582212207b999a2b66e23ec9d74295c9a423016fc59362ac5f8bbbaa7d4529868ae5baec64736f6c63430008060033"

# # set pre-funded account as sender
web3.eth.defaultAccount = web3.eth.accounts[0]

# # Instantiate and deploy contract
Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

# # Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# # Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# # Create the contract instance with the newly-deployed address
contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi,
)

print(tx_receipt.contractAddress)

# # # Display the default greeting from the contract
print('Default contract greeting: {}'.format(
    contract.functions.greet().call()
))

# # update the greeting
tx_hash = contract.functions.setGreeting('HELLOOOOOOOOOOOOO!!!!').transact()

# # Wait for transaction to be mined...
web3.eth.waitForTransactionReceipt(tx_hash)

# # Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))


## Activity: Deploy Smart Contract on Ganache ## 

import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"get","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_value","type":"string"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
bytecode = "608060405234801561001057600080fd5b506040518060400160405280600781526020017f6d7956616c7565000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610166565b82805461006e90610105565b90600052602060002090601f01602090048101928261009057600085556100d7565b82601f106100a957805160ff19168380011785556100d7565b828001600101855582156100d7579182015b828111156100d65782518255916020019190600101906100bb565b5b5090506100e491906100e8565b5090565b5b808211156101015760008160009055506001016100e9565b5090565b6000600282049050600182168061011d57607f821691505b6020821081141561013157610130610137565b5b50919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b6104a8806101756000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c80634ed3885e1461003b5780636d4ce63c14610057575b600080fd5b61005560048036038101906100509190610234565b610075565b005b61005f61008f565b60405161006c91906102b6565b60405180910390f35b806000908051906020019061008b929190610121565b5050565b60606000805461009e9061038c565b80601f01602080910402602001604051908101604052809291908181526020018280546100ca9061038c565b80156101175780601f106100ec57610100808354040283529160200191610117565b820191906000526020600020905b8154815290600101906020018083116100fa57829003601f168201915b5050505050905090565b82805461012d9061038c565b90600052602060002090601f01602090048101928261014f5760008555610196565b82601f1061016857805160ff1916838001178555610196565b82800160010185558215610196579182015b8281111561019557825182559160200191906001019061017a565b5b5090506101a391906101a7565b5090565b5b808211156101c05760008160009055506001016101a8565b5090565b60006101d76101d2846102fd565b6102d8565b9050828152602081018484840111156101f3576101f2610452565b5b6101fe84828561034a565b509392505050565b600082601f83011261021b5761021a61044d565b5b813561022b8482602086016101c4565b91505092915050565b60006020828403121561024a5761024961045c565b5b600082013567ffffffffffffffff81111561026857610267610457565b5b61027484828501610206565b91505092915050565b60006102888261032e565b6102928185610339565b93506102a2818560208601610359565b6102ab81610461565b840191505092915050565b600060208201905081810360008301526102d0818461027d565b905092915050565b60006102e26102f3565b90506102ee82826103be565b919050565b6000604051905090565b600067ffffffffffffffff8211156103185761031761041e565b5b61032182610461565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b82818337600083830152505050565b60005b8381101561037757808201518184015260208101905061035c565b83811115610386576000848401525b50505050565b600060028204905060018216806103a457607f821691505b602082108114156103b8576103b76103ef565b5b50919050565b6103c782610461565b810181811067ffffffffffffffff821117156103e6576103e561041e565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f830116905091905056fea2646970667358221220c315b43c924f8e4d72ead78e24adfc0f1739f6f313e2087ab2418a8d162e03d764736f6c63430008060033"

# # set pre-funded account as sender
web3.eth.defaultAccount = web3.eth.accounts[0]

# # Instantiate and deploy contract
MyContract = web3.eth.contract(abi=abi, bytecode=bytecode)

# # Submit the transaction that deploys the contract
tx_hash = MyContract.constructor().transact()

# # Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# # Create the contract instance with the newly-deployed address
contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi,
)

print(tx_receipt.contractAddress)

# # # Display the default greeting from the contract
print('Default contract value: {}'.format(
    contract.functions.get().call()
))

# # update the greeting
tx_hash = contract.functions.set('New_value').transact()

# # Wait for transaction to be mined...
web3.eth.waitForTransactionReceipt(tx_hash)

# # Display the new greeting value
print('Updated contract value: {}'.format(
    contract.functions.get().call()
))


