import json
import time
import random
import os

# Define mock network events
EVENTS_POOL = [
    {"type": "info", "text": "New block mined (#194822) - 142 txs included safely."},
    {"type": "info", "text": "Mempool processing signature verification checks."},
    {"type": "info", "text": "Zero-Knowledge succinct proof aggregate validated."},
    {"type": "alert", "text": "[CRITICAL] Flash Loan manipulation signatures matched on DEX routing path!"},
    {"type": "alert", "text": "[WARNING] High gas congestion sequence detected from arbitrage bots."},
    {"type": "info", "text": "Inbound balance sync finalized on escrow node checkpoint."}
]

METHODS_POOL = ["transfer", "approve", "swapExactTokens", "mint", "flashLoan", "delegateCall"]

def generate_live_telemetry():
    print("[*] Web3 SecOps Background Telemetry Agent Active.")
    print("[-] Generating live block traffic into public/telemetry.json...")
    
    # Initialize base values
    tvl = 1420.50
    exploit_count = 0
    
    output_path = "Web3-Security-Dashboard/public/telemetry.json"
    
    while True:
        # Randomly adjust variables to make dashboard metrics dance
        tvl += random.uniform(-2.5, 3.1)
        gas = random.randint(21, 32)
        
        # Decide if an event happens
        current_event = random.choice(EVENTS_POOL)
        if current_event["type"] == "alert" and "Flash Loan" in current_event["text"]:
            exploit_count += 1
            
        # Generate a dummy incoming transaction
        mock_tx = {
            "hash": f"0x{random.randint(1000, 9999)}...{random.randint(1000, 9999)}",
            "method": random.choice(METHODS_POOL),
            "value": f"{round(random.uniform(0.1, 50.0), 2)} ETH"
        }
        
        # Compile structure
        telemetry_data = {
            "tvl": f"{round(tvl, 2)} ETH",
            "gas": f"{gas} Gwei",
            "exploitCount": exploit_count,
            "zkp": random.randint(140, 165),
            "latestEvent": current_event,
            "latestTx": mock_tx,
            "timestamp": time.time()
        }
        
        # Atomically write data out for frontend polling consumption
        with open(output_path, "w") as f:
            json.dump(telemetry_data, f, indent=2)
            
        # Wait a random interval between 2 to 4 seconds to simulate dynamic network spacing
        time.sleep(random.uniform(2.0, 4.0))

if __name__ == "__main__":
    generate_live_telemetry()
