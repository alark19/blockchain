import hashlib
import json
import time
 
 
class Block:
    def __init__(self, index, data, previous_hash, timestamp=None, nonce=0):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()
 
    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
 
 
class Blockchain:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]
 
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")
 
    def get_latest_block(self):
        return self.chain[-1]
 
    def proof_of_work(self, block):
        target = "0" * self.difficulty
        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block
 
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index + 1, data, previous_block.hash)
        new_block = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return new_block
 
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                print(f"Block {current.index} tampered (hash mismatch).")
                return False
            if current.previous_hash != previous.hash:
                print(f"Block {current.index} not linked correctly.")
                return False
            if not current.hash.startswith("0" * self.difficulty):
                print(f"Block {current.index} fails Proof-of-Work.")
                return False
        return True
 
 
# ---- Demonstration ----
my_chain = Blockchain(difficulty=3)
my_chain.add_block("Alice pays Bob 10 coins")
my_chain.add_block("Bob pays Charlie 5 coins")
my_chain.add_block("Charlie pays Dave 2 coins")
 
print("Chain valid before tampering?", my_chain.is_chain_valid())
 
my_chain.chain[1].data = "Alice pays Bob 1000 coins"  # tamper
print("Chain valid after tampering? ", my_chain.is_chain_valid())
