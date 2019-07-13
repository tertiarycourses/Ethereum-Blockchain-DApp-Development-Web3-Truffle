// import solidity
pragma solidity ^0.5.1;

contract Inheritance {
    address owner;
    bool deceased;
    uint money;
    
    constructor() public payable {
        owner = msg.sender;
        money = msg.value;
        deceased = false;
    }
    
    address[] wallets;

    mapping (address => uint) inheritance;

}