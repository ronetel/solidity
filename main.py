from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_adress

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

print(w3.from_wei(w3.eth.get_balance("0x308F1D0c65AeA4A4193587DE2234E664eA54C8f3"), 'ether'))

print(w3.from_wei(w3.eth.get_balance("0xf73df88c38b3875fB22331a22aEEE49ACed8D51c"), 'ether'))

print(w3.from_wei(w3.eth.get_balance("0x92aC26E60B2e8414736acCCaEC1B6db823ddf04B"), 'ether'))

print(w3.from_wei(w3.eth.get_balance("0x8A8D8D60CbbeEcA2b641f9bA443dA346b26F9468"), 'ether'))

print(w3.from_wei(w3.eth.get_balance("0x64f680493BD99609AA55916ECc598D349970C94B"), 'ether'))