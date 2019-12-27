from web3 import Web3
web3 = Web3(Web3.HTTPProvider('http://192.168.0.24:8545'))
import json
import sys

ETH_SCALE = 1000000000000000000
ETH27_SCALE = 1000000000000000000000000000
ETH44_SCALE = 1000000000000000000000000000000000000000000000

START_BLOCK = 8957669
LAST_BLOCK = 9169457

ethAflip0x = '0xd8a04F5412223F513DC55F839574430f5EC15531'
cat0x = '0x78F2c2AF65126834c51822F56Be0d7469D7A523E'
ethAflipabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"},{"internalType":"bytes32","name":"ilk_","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lot","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"address","name":"gal","type":"address"}],"name":"Kick","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"beg","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bids","outputs":[{"internalType":"uint256","name":"bid","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"address","name":"guy","type":"address"},{"internalType":"uint48","name":"tic","type":"uint48"},{"internalType":"uint48","name":"end","type":"uint48"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"deal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"dent","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ilk","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"kick","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kicks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tau","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"tend","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tick","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ttl","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"yank","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
catabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"ilk","type":"bytes32"},{"indexed":true,"internalType":"address","name":"urn","type":"address"},{"indexed":false,"internalType":"uint256","name":"ink","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"art","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":false,"internalType":"address","name":"flip","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Bite","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"urn","type":"address"}],"name":"bite","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"cage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"address","name":"data","type":"address"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"address","name":"flip","type":"address"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"ilks","outputs":[{"internalType":"address","name":"flip","type":"address"},{"internalType":"uint256","name":"chop","type":"uint256"},{"internalType":"uint256","name":"lump","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"live","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vow","outputs":[{"internalType":"contract VowLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
ethAflip = web3.eth.contract(address=ethAflip0x, abi=ethAflipabi)
cat = web3.eth.contract(address=cat0x, abi=catabi)

TEND_TOPIC = ['0x4b43ed1200000000000000000000000000000000000000000000000000000000']
DENT_TOPIC = ['0x5ff3a38200000000000000000000000000000000000000000000000000000000']
DEAL_TOPIC = ['0xc959c42b00000000000000000000000000000000000000000000000000000000']
BITE_TOPIC = ['0xa716da86bc1fb6d43d1493373f34d7a418b619681cd7b90f7ea667ba1489be28']
KICK_TOPIC = ['0xc84ce3a1172f0dec3173f04caaa6005151a4bfe40d4c9f3ea28dba5f719b2a7a']

# go back to when the vault was created to find this contract
# ex: https://etherscan.io/tx/0xb80de95c4537cd54a2359e0053b1661ad35505f7484176a5924a8e5f1cf8e19d#internal
# answer - urn_to_find = '0xb0563B1B563952775C3ac676d0FB2014051B6c5f'
urn_to_find = '0xb0563B1B563952775C3ac676d0FB2014051B6c5f'
padded_urn = '0x000000000000000000000000' + urn_to_find[2:]
padded_urn = padded_urn.lower()

#cdpid_to_find = 2480


bite_filter = web3.eth.filter({"address":cat0x, "fromBlock":START_BLOCK, "toBlock":LAST_BLOCK, "topics":BITE_TOPIC})
bite_pre = bite_filter.get_all_entries()
kick_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":START_BLOCK, "toBlock":LAST_BLOCK, "topics":KICK_TOPIC})
kick_pre = kick_filter.get_all_entries()
tend_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":START_BLOCK, "toBlock":LAST_BLOCK, "topics":TEND_TOPIC})
tend_pre = tend_filter.get_all_entries()
dent_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":START_BLOCK, "toBlock":LAST_BLOCK, "topics":DENT_TOPIC})
dent_pre = dent_filter.get_all_entries()
deal_filter = web3.eth.filter({"address":ethAflip0x, "fromBlock":START_BLOCK, "toBlock":LAST_BLOCK, "topics":DEAL_TOPIC})
deal_pre = deal_filter.get_all_entries()
vault_liquidation_ids = []
vault_liquidation_id = 0
bite_hash = ''
bite_hashes = []
for j in range(0, len(bite_pre)):
	if ( web3.toHex(bite_pre[j]['topics'][2]) == padded_urn):
		vault_liquidation_id = web3.toInt(hexstr=bite_pre[j]['data'][280:].lstrip('0'))
		vault_liquidation_ids.append(vault_liquidation_id)
		bite_hash = web3.toHex(bite_pre[j]['transactionHash'])
		bite_hashes.append(bite_hash)

if(vault_liquidation_id == 0):
	print("couldn't find urn")
	sys.exit(0)
else:
	print("bite hashes: {0}".format(bite_hashes))

kick_hash = ''
kick_hashes = []
for j in range(0, len(kick_pre)):
	dd = web3.toInt(hexstr=kick_pre[j]['data'][2:66].lstrip('0'))
	if(dd in vault_liquidation_ids):
		kick_hash = web3.toHex(kick_pre[j]['transactionHash'])
		kick_hashes.append(kick_hash)
print("\nkick hashes: {0}".format(kick_hashes))

tend_hash = ''
tend_hashes = []
lot = 0
lots = []
bid = 0
bids = []
tends = []
for j in range(0, len(tend_pre)):
	dd = web3.toInt(hexstr=tend_pre[j]['data'][190:202].lstrip('0'))
	if(dd in vault_liquidation_ids):
		tend_hash = web3.toHex(tend_pre[j]['transactionHash'])
		lot = web3.toInt(hexstr=tend_pre[j]['data'][230:266].lstrip('0'))
		bid = web3.toInt(hexstr=tend_pre[j]['data'][269:330].lstrip('0'))

		bidder = web3.toHex(tend_pre[j]['topics'][1][12:])
		tt = [bidder, dd, lot, bid, tend_hash]
		tends.append(tt)

sorted_tends = sorted(tends, key=lambda x: x[1])
uniq_ids = []
for i in sorted_tends:
	if(i[1] not in uniq_ids):
		uniq_ids.append(i[1])

winning_tends = []
for i in uniq_ids:
	current_winning_bid = 0
	winning_index = 0
	for j in range(0, len(sorted_tends)):
		if(i == sorted_tends[j][1]):
			if(sorted_tends[j][3] > current_winning_bid):
				current_winning_bid = sorted_tends[j][3]
				winning_index = j
	winning_tends.append(sorted_tends[winning_index])
print("\nwinning tends")
print(winning_tends)

total_bids = 0
for i in winning_tends:
	total_bids += (i[3] / ETH44_SCALE)

print("\ntotal bids")
print(total_bids)





dent_hash = ''
dent_hashes = []
lot = 0
lots = []
bid = 0
bids = []
dents = []
for j in range(0, len(dent_pre)):
	dd = web3.toInt(hexstr=dent_pre[j]['data'][190:202].lstrip('0'))
	if(dd in vault_liquidation_ids):
		dent_hash = web3.toHex(dent_pre[j]['transactionHash'])
		lot = web3.toInt(hexstr=dent_pre[j]['data'][230:266].lstrip('0'))
		bid = web3.toInt(hexstr=dent_pre[j]['data'][269:330].lstrip('0'))

		bidder = web3.toHex(dent_pre[j]['topics'][1][12:])
		tt = [bidder, dd, lot, bid, dent_hash]
		dents.append(tt)

sorted_dents = sorted(dents, key=lambda x: x[1])
uniq_ids = []
for i in sorted_dents:
	if(i[1] not in uniq_ids):
		uniq_ids.append(i[1])

winning_dents = []
for i in uniq_ids:
	current_winning_lot = 999999999999999999999999999999999999999999
	winning_index = 0
	for j in range(0, len(sorted_dents)):
		if(i == sorted_dents[j][1]):
			if(sorted_dents[j][2] < current_winning_lot):
				current_winning_lot = sorted_dents[j][3]
				winning_index = j
	winning_dents.append(sorted_dents[winning_index])

print("\nwinning dents")
print(winning_dents)
total_returned = 0
for i in winning_dents:
	for j in winning_tends:
		if(i[1] == j[1]):
			returned = j[2] - i[2]
			total_returned += returned / ETH_SCALE


print("\ntotal lot returned")
print(total_returned)






