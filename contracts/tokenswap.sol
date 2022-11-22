pragma solidity ^0.5.0;

import "./bestbuy_token.sol";
import "./delta_token.sol";
import "./nike_token.sol";
import "./starbucks_token.sol";

contract TokenSwap {
    string public name = "Loyalty Tokens Exchange";
    Nike public token1;
    Starbucks public token2;
    Delta public token3;
    Bestbuy public token4;
    address public owner1;
    address public LoyaltyPool;

    constructor() public {

    }

}