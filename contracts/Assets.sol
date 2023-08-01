// SPDX-License-Identifier: MIT

pragma solidity ^0.8.14;

/**
 * @dev Assets tokenization contract
 */
contract Assets {
    // Structs.
    struct Token {
        address owner;
        string governmentRegistryId;
        string name;
        string description;
    }

    // Vars.
    address _admin;
    string _name;
    string _symbol;
    address _tokenizer; // Allow tokenize only by this address
    address _withdrawAddress; // Allow withdraw only to this address
    mapping(uint256 => Token) private _tokens;
    mapping(address => uint256) private _balances;
    uint256 _nextTokenId = 1;

    // Modifiers.
    modifier onlyAdmin() {
        require(msg.sender == _admin, "Only owner can call this method.");
        _;
    }
    modifier onlyTokenizer() {
        require(
            msg.sender == _tokenizer,
            "Only tokenizer can call this method."
        );
        _;
    }

    /**
     * @dev Constructor
     */
    constructor(
        string memory contractName,
        string memory contractSymbol,
        address tokenizer,
        address withdrawAddress
    ) {
        _admin = msg.sender;
        _name = contractName;
        _symbol = contractSymbol;
        _tokenizer = tokenizer;
        _withdrawAddress = withdrawAddress;
    }

    /**
     * @dev Returns the token name
     */
    function name() public view returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the token symbol
     */
    function symbol() public view returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns token owner
     */
    function getTokenOwner(uint256 tokenId) public view returns (address) {
        return _tokens[tokenId].owner;
    }

    /**
     * @dev Returns token government registry id
     */
    function getTokenGovernmentRegistryId(uint256 tokenId) public view returns (string memory) {
        return _tokens[tokenId].governmentRegistryId;
    }

    /**
     * @dev Tokenize asset
     */
    function tokenize(
        address to,
        string memory tokenGovernmentRegistryId,
        string memory tokenName,
        string memory tokenDescription
    ) public onlyTokenizer returns (uint256) {
        _tokens[_nextTokenId] = Token({
            owner: to,
            governmentRegistryId: tokenGovernmentRegistryId,
            name: tokenName,
            description: tokenDescription
        });
        _balances[to] += 1;
        _nextTokenId += 1;
        return _nextTokenId - 1;
    }

    /**
     * @dev Withdraw (if someone accidentally sends ETH to this contract)
     */
    function withdraw() public onlyAdmin {
        payable(_withdrawAddress).transfer(address(this).balance);
    }
}
