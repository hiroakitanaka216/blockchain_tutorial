# https://www.sejuku.net/blog/75079 
import hashlib
import json
import datetime
import csv
import time

class Block:
    def __init__(self, index, timestamp, transaction, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.difficulty = 5  # 難易度を追加, ハッシュの頭n(=4)桁が全部0
        self.property_dict = {str(i): j for i, j in self.__dict__.items()}
        # ハッシュ計算に必要な要素を辞書化
        self.now_hash = self.calc_hash()
        self.proof = None # プルーフを追加
        self.proof_hash = None  # プルーフを追加して計算したハッシュ
 
    def calc_hash(self):
        # ハッシュ関数: 
        # 同じファイルからは同じ値を得られる
        # 少しでもファイルのデータが異なると全く違う値になる
        # ハッシュは簡単に生成できるが、ハッシュから元のファイルを復元するのはすごく大変
        block_string = json.dumps(self.property_dict, sort_keys=True).encode('ascii')
        # ハッシュ計算関数に代入するための形を整える用にjson
        return hashlib.sha256(block_string).hexdigest()
 
    # プルーフの検証用関数
    def check_proof(self, proof):
        proof_string = self.now_hash + str(proof)
        calced = hashlib.sha256(proof_string.encode("ascii")).hexdigest()
        if calced[:self.difficulty:].count('0') == self.difficulty:
            self.proof_hash = calced
            return True
        else:
            return False
 
    # プルーフを採掘するための関数
    def mining(self):
        proof = 0
        while True:
            if self.check_proof(proof):
                break
            else:
                proof += 1
        return proof
 
# トランザクションの生成
'''
def new_transaction(sender, recipient, amount):
    transaction = {
        "差出人": sender,
        "あて先": recipient,
        "金額": amount,
    }
    return transaction
'''

print("please input the number of the new blocks")
num = int(input())

t1 = time.time()
block_chain = []
 
block = Block(0, 0, [], '-') #最初のブロックを作成
 
block.proof = block.mining()
 
block_chain.append(block)

f = open('blockchain_info.csv', 'a')
 
for i in range(num):
    block = Block(i+1, str(datetime.datetime.now()), ["とあるトランザクション"], block_chain[i].now_hash)
    block.proof = block.mining()
    block_chain.append(block)
 
for block in block_chain:
    for key, value in block.__dict__.items():
        print(key, ':', value)
    print("")

    for key, value in block.__dict__.items():
        f.write(f'{key}:{value}\n')

t2 = time.time()
elapse_time = t2-t1
print(f"経過時間:{elapse_time}[s]")
f.write(f"経過時間:{elapse_time}[s]")
print(f'difficulty:{block.difficulty}')
f.write(f'difficulty:{block.difficulty}')
