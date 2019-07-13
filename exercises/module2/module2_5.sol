pragma solidity ^0.5.1;

contract C {
 function test(uint a, uint b) pure public returns(string memory ){
     if(a >= b){
        return "a is larger than b";
     } else {
     	return "a is smaller than b";
     }
   }
   
 function test(uint a) public pure returns (uint){
 	while (a<10) {
 		a++;
 	}
 	return a;
   }
   
 uint[] public b;
 function test() public returns (uint[] memory){
 	for (uint i=0;i<10;i++) {
 		b.push(i);
 	}
 	return b;
   }
  
 }
