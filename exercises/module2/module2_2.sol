// import solidity
pragma solidity ^0.5.1;

contract DataTypes {
    // string
    string name = "manny";
    // integers
    uint storedata = 34;
    // boolean
    bool atrueorfalsevalue = false;
    // address
    address walletAddress = address(0x72ba773893b);
    // bytes
    bytes32 code;

    // arrays
    string[] names;
    // Struct to define 
    struct User {
        string firstName;
        string lastName;
    }
    // enums
    enum userType {buyer, seller}
    // mappings
    mapping(address => uint) public balances;
}