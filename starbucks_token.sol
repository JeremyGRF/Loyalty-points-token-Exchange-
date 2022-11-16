pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Starbucks is ERC20 {

    constructor(uint256 initialSupply) ERC20("Starbucks", "STRB") {
        _mint(msg.sender, initialSupply);
    }

   function decimals() public view virtual override returns (uint8) {
     return 18;  // eg. return 12;
   }
}