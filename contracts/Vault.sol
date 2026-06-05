// SPDX-License-Identifier: MIT
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
}