// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract LoyaltyExchange is ERC20 {
    using Address for address;
    using SafeERC20 for IERC20;
    
    // Brand loyalty points the dapp accepts
    IERC20 public bestbuy;
    IERC20 public starbucks;
    IERC20 public delta;
    IERC20 public nike;

    constructor(address _bestbuy, address _starbucks, address _delta, address _nike)
        ERC20("Loyalty Exchange Token", "LET")
    {
        bestbuy = IERC20(_bestbuy);
        starbucks = IERC20(_starbucks);
        delta = IERC20(_delta);
        nike = IERC20(_nike);
    }


    // Create Functions to view the dapp balance for each of the brand loyalty tokens

    function bestbuyBalance() public view returns (uint256) {
        return bestbuy.balanceOf(address(this));
    }
    function starbucksBalance() public view returns (uint256) {
        return starbucks.balanceOf(address(this));
    }
    function deltaBalance() public view returns (uint256) {
        return delta.balanceOf(address(this));
    }
    function nikeBalance() public view returns (uint256) {
        return nike.balanceOf(address(this));
    }


    /* Create Functions for a user to deposit brand loyalty tokens, the dapp then mints the same amount of LET
    tokens and deposits them into the user's wallet. */

    function depositbestbuy(uint256 _amount) public {
        // Amount must be greater than zero
        require(_amount > 0, "amount cannot be 0");

        // Transfer token to smart contract
        bestbuy.safeTransferFrom(msg.sender, address(this), _amount);

        // Mint Loyalty Exchange Token to msg sender
        _mint(msg.sender, _amount);
    }
    function depositstarbucks(uint256 _amount) public {
        // Amount must be greater than zero
        require(_amount > 0, "amount cannot be 0");

        // Transfer token to smart contract
        starbucks.safeTransferFrom(msg.sender, address(this), _amount);

        // Mint Loyalty Exchange Token to msg sender
        _mint(msg.sender, _amount);
    }
    function depositdelta(uint256 _amount) public {
        // Amount must be greater than zero
        require(_amount > 0, "amount cannot be 0");

        // Transfer token to smart contract
        delta.safeTransferFrom(msg.sender, address(this), _amount);

        // Mint Loyalty Exchange Token to msg sender
        _mint(msg.sender, _amount);
    }
     function depositnike(uint256 _amount) public {
        // Amount must be greater than zero
        require(_amount > 0, "amount cannot be 0");

        // Transfer token to smart contract
        nike.safeTransferFrom(msg.sender, address(this), _amount);

        // Mint Loyalty Exchange Token to msg sender
        _mint(msg.sender, _amount);
    }


    /* Create Functions for a user to withdraw brand loyalty tokens, the dapp burns the users LET tokens and sends them the
    same amount of brand loyalty tokens */

    function withdrawbestbuy(uint256 _amount) public {
        // Burn Loyalty Exchange Token from msg sender
        _burn(msg.sender, _amount);

        // Transfer tokens from this smart contract to msg sender
        bestbuy.safeTransfer(msg.sender, _amount);
    }
     function withdrawstarbucks(uint256 _amount) public {
        // Burn Loyalty Exchange Token from msg sender
        _burn(msg.sender, _amount);

        // Transfer tokens from this smart contract to msg sender
        starbucks.safeTransfer(msg.sender, _amount);
    }
    function withdrawdelta(uint256 _amount) public {
        // Burn Loyalty Exchange Token from msg sender
        _burn(msg.sender, _amount);

        // Transfer tokens from this smart contract to msg sender
        delta.safeTransfer(msg.sender, _amount);
    }
    function withdrawnike(uint256 _amount) public {
        // Burn Loyalty Exchange Token from msg sender
        _burn(msg.sender, _amount);

        // Transfer tokens from this smart contract to msg sender
        nike.safeTransfer(msg.sender, _amount);
    }
}
