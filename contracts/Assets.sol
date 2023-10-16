// SPDX-License-Identifier: MIT

//Додати p2p платформу (DApp)  daps: mapping(address -> bool);
//Передати в керування (DApp) allowed: maping(uint256->address);
//Трансфер квартири до іншого власника. Перевірити allowed -> 


pragma solidity ^0.8.14;

/**
 * @dev Assets tokenization contract
 */
contract Assets {
    // Structs.
    struct Token {
        address owner;
        address grantedAccess;
        string governmentRegistryId;
        string name;
        string description;
    }

    // Vars.
    address _admin;
    address _state_admin;
    string _name;
    string _symbol;
    address _tokenizer; // Allow tokenize only by this address
    address _withdrawAddress; // Allow withdraw only to this address
    mapping(uint256 => Token) private _tokens;
    mapping(address => uint256) private _balances;
    uint256 _nextTokenId = 1;

    mapping(address => bool) private _p2p_platforms;
    address _selected_p2p_platform;

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

    modifier onlyP2P_selected() {
        require(msg.sender == _selected_p2p_platform, "Only selected P2P Platform can call this method.");
        _;
    }

    modifier onlyStateAdmin_selected() {
        require(msg.sender == _state_admin, "Only state (goverment) admin can call this method.");
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
        _state_admin = address(0);
        _name = contractName;
        _symbol = contractSymbol;
        _tokenizer = tokenizer;
        _withdrawAddress = withdrawAddress;
        _selected_p2p_platform = address(0);

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
     * @dev Grant permission to transfer token
     */
    function grantPermission(address to, uint256 tokenId) public {
        require(msg.sender == _tokens[tokenId].owner, "Only owner can grant permission.");
        _tokens[tokenId].grantedAccess = to;
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
            grantedAccess: address(0),
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


    /**
    * @dev addP2PPlatform to list
    */
    function AddP2pPplatform(address p2p_address) public{

        _p2p_platforms[p2p_address] = true;

    }

    /**
    * @dev Allow P2P platform
    */
    function AllowP2Pplatform(address p2p_address)  public onlyAdmin {

        require( _p2p_platforms[msg.sender], "Only alloweded P2P Platform can selected by this method.");

        _selected_p2p_platform = p2p_address;

    }

       /**
    * @dev Deny P2P platform
    */
    function DenyP2Pplatform()  public onlyAdmin {

        require(_p2p_platforms[msg.sender], "Only alloweded P2P Platform can selected by this method.");

        _selected_p2p_platform = address(0);

    }

    /**
    * @dev TransferTokenByP2pPlatform
    */
    function TransferTokenByP2pPlatform( address newOwner) public onlyP2P_selected {

        _admin = newOwner;
        _selected_p2p_platform = address(0);

    }
}
