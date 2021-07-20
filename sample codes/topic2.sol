# Your first smart contract
# set and get values

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    string value;
    
    constructor() {
        value = "myValue";
    }
    function get() public view returns(string memory) {
        return value;
        
    }
    
    function set(string memory _value) public {
        value = _value;
    }
    
}

#  Make the value public and remove the get function

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    string public value;
    
    constructor()  {
        value = "myValue";
    }
 
    
    function set(string memory _value) public {
        value = _value;
    }
    
}

# Set the default value and remove the constructor

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    string public value = "myValue"; 
    
    
    function set(string memory _value) public {
        value = _value;
    }
    
}


# use constant 

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    string public constant value = "myValue"; 
}

# data types

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    string public myString = "myString";
    bool public myBool = true;
    int public myInt = 1;
    uint public myUint = 1;
    uint8 public mUint8 = 8;
    uint256 public myUint265 = 9999;
        
}

# enum

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    enum State {Waiting, Ready, Active}
    State public state;
    
    constructor() {
        state = State.Waiting;
    }
    
    function activate() public {
        state = State.Active;
    }
    
    function isActive() public view returns(bool) {
        return state == State.Active;
    }

        
}


# struct
// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    Person[] public person;
    
    struct Person {
        string _firstname;
        string _lastname;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public {
        person.push(Person(_firstName, _lastName));

    }
        
}

# count no of people
// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    Person[] public person;
    
    uint256 public peopleCount;
    
    struct Person {
        string _firstname;
        string _lastname;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public {
        person.push(Person(_firstName, _lastName));
        peopleCount += 1;
    }
  
        
}

# mapping

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    uint256 public peopleCount = 0;
    mapping(uint => Person) public people;
    
    struct Person {
        uint _id;
        string _firstname;
        string _lastname;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public {
         people[peopleCount] = Person(peopleCount,_firstName, _lastName);
         peopleCount += 1;
    }
  
        
}


# internal 

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    uint256 public peopleCount = 0;
    mapping(uint => Person) public people;
    
    struct Person {
        uint _id;
        string _firstname;
        string _lastname;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public {
         people[peopleCount] = Person(peopleCount,_firstName, _lastName);
         incrementCount();
        
    }
    
    function incrementCount() internal {
         peopleCount += 1;
    }
  
        
}


# modifier, address and msg

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    uint256 public peopleCount = 0;
    mapping(uint => Person) public people;
    
    address owner;
    
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
    
    constructor() {
        owner = msg.sender;
    }
    
    
    struct Person {
        uint _id;
        string _firstname;
        string _lastname;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public  onlyOwner {
         people[peopleCount] = Person(peopleCount,_firstName, _lastName);
         incrementCount();
        
    }
    
    function incrementCount() internal {
         peopleCount += 1;
    }
  
        
}

# modifier, epoch time, timestamp

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract {
    uint256 public peopleCount = 0;
    mapping(uint => Person) public people;
    
   uint256 openingTime = 1625245800;
   
   modifier onlyWhileOpen() {
       require(block.timestamp >= openingTime);
       _;
   }
    
    struct Person {
        uint _id;
        string _firstname;
        string _lastname;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public  onlyWhileOpen{
         people[peopleCount] = Person(peopleCount,_firstName, _lastName);
         incrementCount();
        
    }
    
    function incrementCount() internal {
         peopleCount += 1;
    }
  
        
}

# wallet transfer 

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract  {
    mapping(address => uint256) public balances;
    address payable wallet;
    
    constructor(address payable _wallet)  {
       wallet = _wallet;
    }
    
    function buyToken() public payable {
      //buy a token 
      balances[msg.sender] += 1;
      // send ether to the wallet
      wallet.transfer(msg.value);
    }
  
        
}

# fallback function

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract  {
    mapping(address => uint256) public balances;
    address payable wallet;
    
    constructor(address payable _wallet)  {
       wallet = _wallet;
    }
    
    fallback() external { 
        buyToken();
    }
    
    function buyToken() public payable {
      //buy a token 
      balances[msg.sender] += 1;
      // send ether to the wallet
      wallet.transfer(msg.value);
    }
  
        
}
    
# event

// SPDX-License-Identifier: MIT
pragma solidity 0.8.6;

contract MyContract  {
    mapping(address => uint256) public balances;
    address payable wallet;
    
    event Purchase(
        address _buyer,
        uint256 _amount
    );
    
    constructor(address payable _wallet)  {
       wallet = _wallet;
    }
    
    fallback() external { 
        buyToken();
    }
    
    function buyToken() public payable {
      //buy a token 
      balances[msg.sender] += 1;
      // send ether to the wallet
      wallet.transfer(msg.value);
      emit Purchase(msg.sender,1);
    }
        
}


pragma solidity 0.8.6;

contract MyContract  {
    mapping(address => uint256) public balances;
    address payable wallet;
    
    event Purchase(
        address indexed _buyer,
        uint256 _amount
    );
    
    constructor(address payable _wallet)  {
       wallet = _wallet;
    }
    
    fallback() external { 
        buyToken();
    }
    
    function buyToken() public payable {
      //buy a token 
      balances[msg.sender] += 1;
      // send ether to the wallet
      wallet.transfer(msg.value);
      emit Purchase(msg.sender,1);
    }
       


