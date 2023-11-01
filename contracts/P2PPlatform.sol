// SPDX-License-Identifier: MIT

pragma solidity ^0.8.14;

contract Asset {
    function TransferTokenByP2pPlatform( address newOwner) public {}
}

contract P2PPlatform {

    struct ControlledObject {
        address Owner;
        uint DateFrom;
        bool Status;
    }

    struct Deals {
        address Shopper;
        uint Price;
        uint DateDeal;
        uint DateTransaction;
        bool Status;
    }

    //Vars
    address _Administrator;
    address _Control;
    mapping(address=>ControlledObject) _controlledObjects;
    mapping(address=>Deals) _deals;

    // Modifiers.
    modifier onlyAdmin() {
        require(msg.sender == _Administrator, "Only administrator can call this method.");
        _;
    }

    modifier onlyOwner(address controbject) {
        require( msg.sender == _controlledObjects[controbject].Owner , "Only owner can call this method.");
        _;
    }


    constructor (
        address admin,
        address control
    ) {
        _Administrator = admin;
        _Control = control;
    }

    function getObject( address object, address owner) public {

        _controlledObjects[object] = ControlledObject(owner, block.timestamp, true);

    }

    function setDeal(uint price, address object) public onlyOwner(object) {
        _deals[object] = Deals(address(0), price, block.timestamp, 0, false);
    }

    function acceptDeal(address object) public {
        _deals[object].Shopper = msg.sender;
    }

    function finishDeal(address object) public onlyAdmin {
        _deals[object].DateTransaction = block.timestamp;
        _deals[object].Status = true;
        Asset _asset;
        _asset = Asset(object);
        _asset.TransferTokenByP2pPlatform(_deals[object].Shopper);
        _controlledObjects[object].Status = false;
    }

}