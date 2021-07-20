## ERC20 Token demo ##

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract ERC20Token {
    string public name;
    mapping (address => uint256) public balances;
    
    function mint() public {
        balances[tx.origin] ++;
    }
}
contract MyContract  {
    address payable wallet;
    address public token;

    constructor(address payable _wallet, address _token)  {
       wallet = _wallet;
       token = _token;
    }
    
    fallback() external { 
        buyToken();
    }
    
    function buyToken() public payable {
      ERC20Token _token = ERC20Token(address(token));
      _token.mint();
      wallet.transfer(msg.value);

    }
        
}

# Inheritance

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract ERC20Token {
    string public name;
    mapping (address => uint256) public balances;
    
    constructor(string memory _name) {
        name = _name;
    }
    
    function mint() public virtual {
        balances[tx.origin] ++;
    }
}
contract MyToken is ERC20Token  {
    string public symbol;
    address[] public owners;
    uint256 ownerCount;
    
    constructor(string memory _name,string memory _symbol) ERC20Token(_name) {
        symbol = _symbol;
    }
    
    function mint() public override(ERC20Token) {
        super.mint();
        ownerCount ++;
        owners.push(msg.sender);
    }
        
}

## Activity: Deploy Hello Coin Token in Ganache ## 

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;
  
contract HelloCoin {
    string public name = 'HelloCoin'; 
    string public symbol = 'hc'; 
    
    mapping (address => uint) balances; 
    
    event Transfer(address _from, address _to, uint256 _value); 
    
    constructor() { 
        balances[msg.sender] = 10000; 
        
    }
    
    function mint() public virtual {
        balances[tx.origin] ++;
    }

    function sendCoin(address _receiver, uint _amount) public returns(bool sufficient) {
        if (balances[msg.sender] < _amount) return false;  
        balances[msg.sender] -= _amount;
        balances[_receiver] += _amount;
        
        emit Transfer(msg.sender, _receiver, _amount); 
        return true;
    }
    function getBalance(address _addr) public view returns(uint) { 
        //balance check
        return balances[_addr];  
    }
    
}
    

