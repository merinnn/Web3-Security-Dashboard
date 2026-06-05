import json
import time
import random
import os

def run_arena_loop():
    print("[*] Launching Autonomous Attack & Defense Simulation Arena...")
    output_path = "Web3-Security-Dashboard/public/telemetry.json"
    contract_path = "Web3-Security-Dashboard/contracts/Vault.sol"
    
    tvl = 2500.00
    exploit_count = 0
    
    while True:
        # --- PHASE 1: NORMAL TRAFFIC ---
        tvl += random.uniform(1.2, 5.5)
        telemetry = {
            "tvl": f"{round(tvl, 2)} ETH",
            "gas": f"{random.randint(22, 26)} Gwei",
            "exploitCount": exploit_count,
            "zkp": random.randint(145, 155),
            "latestEvent": {"type": "info", "text": "Mempool state stable. Block #194825 verified via ZK-Rollup."},
            "latestTx": {"hash": f"0x{random.randint(1000,9999)}...3a", "method": "deposit", "value": f"{round(random.uniform(0.5, 10), 2)} ETH"},
            "timestamp": time.time()
        }
        with open(output_path, "w") as f: json.dump(telemetry, f, indent=2)
        time.sleep(4)

        # --- PHASE 2: AGENT 1 (THE ADVERSARY) ATTACKS ---
        print("\n[!] AGENT 1 (Adversary) scanning workspace contracts...")
        time.sleep(2)
        print("[!] Vulnerability Found in Vault.sol: State Sequencing Flaw.")
        
        tvl -= 650.00  # Drain the pool balance
        exploit_count += 1
        telemetry = {
            "tvl": f"{round(tvl, 2)} ETH",
            "gas": "85 Gwei",  # Gas spikes during exploits!
            "exploitCount": exploit_count,
            "zkp": random.randint(110, 130),
            "latestEvent": {"type": "alert", "text": "[CRITICAL] Reentrancy attack signature detected on Vault.withdraw()!"},
            "latestTx": {"hash": "0xDEAD...BF", "method": "exploitWithdraw", "value": "650.00 ETH"},
            "timestamp": time.time()
        }
        with open(output_path, "w") as f: json.dump(telemetry, f, indent=2)
        print("[WARNING] Attack Transaction dispatched to ledger pool. Dashboard alerted.")
        time.sleep(5)

        # --- PHASE 3: AGENT 2 (THE GUARDIAN) PATCHES THE HOLE ---
        print("\n[OK] AGENT 2 (Guardian) intercepting threat telemetry...")
        time.sleep(2)
        print("[OK] Restructuring source code parameters in Vault.sol...")
        
        # Simulate an atomic secure code patch (Checks-Effects-Interactions pattern)
        patched_code = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CryptoVault {
    mapping(address => uint256) public balances;

    function withdraw(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        
        // SECURE REFACTOR: State is updated BEFORE the external call
        balances[msg.sender] -= _amount;
        
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");
    }
}"""
        with open(contract_path, "w") as f:
            f.write(patched_code)
        print("[OK] Source code patched securely. Reentrancy vulnerability eliminated.")
        
        # Reset dashboard state showing protection is active
        telemetry["latestEvent"] = {"type": "info", "text": "[MITIGATION SUCCESS] Guardian Agent refactored Vault.sol using Checks-Effects-Interactions pattern."}
        telemetry["gas"] = "23 Gwei"
        telemetry["timestamp"] = time.time()
        with open(output_path, "w") as f: json.dump(telemetry, f, indent=2)
        
        time.sleep(6)

if __name__ == "__main__":
    run_arena_loop()
