// import solidity
pragma solidity ^0.5.1;

// your first contract
contract SimpleContract {
    // state variable
    uint storedData;
    
    // modifier is a conditional
    modifier onlyData() {
        require(
            storedData >= 0);
            _;
    }
    
    // function
    function set(uint x) public {
        storedData = x;
    }
    
    // event
    event Sent(address from, address to, uint storedData);
    
}