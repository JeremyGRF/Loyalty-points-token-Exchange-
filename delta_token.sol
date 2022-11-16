pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Delta is ERC20 {

    constructor(uint256 initialSupply) ERC20("Delta", "DLTA") {
        _mint(msg.sender, initialSupply);
    }

   function decimals() public view virtual override returns (uint8) {
     return 18;  // eg. return 12;
   }
}