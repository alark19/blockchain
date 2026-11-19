// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
contract SimpleToken {
 string public name = "SimpleToken";
 string public symbol = "STK";
 uint8 public decimals = 18;
 uint256 public totalSupply;
 address public owner;
 mapping(address => uint256) public balanceOf;
 event Transfer(address indexed from, address indexed to, uint256 value);
 constructor(uint256 _initialSupply) {
 owner = msg.sender;
 totalSupply = _initialSupply * (10 ** uint256(decimals));
 balanceOf[owner] = totalSupply;
 emit Transfer(address(0), owner, totalSupply);
 }
 // Transfer tokens from caller to another address
 function transfer(address _to, uint256 _value) public returns (bool success) {
 require(_to != address(0), "Invalid address");
 require(balanceOf[msg.sender] >= _value, "Insufficient balance");
 balanceOf[msg.sender] -= _value;
 balanceOf[_to] += _value;
 emit Transfer(msg.sender, _to, _value);
 return true;
 }
 // Helper to check balance of any account
 function getBalance(address _account) public view returns (uint256) {
 return balanceOf[_account];
 }
}
