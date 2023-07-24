# Assets Tokenization EVM Contracts

## Description

This repository contains the smart contracts for the Assets Tokenization project.

## Dependencies

- [Python](https://www.python.org/downloads/).
- [Blownie](https://eth-brownie.readthedocs.io/en/stable/install.html).
- [Ganache](https://www.trufflesuite.com/ganache).

## Scripts

```sh
# Add local Ganache to use in tests.
brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337

# Run tests on defined network.
brownie test --network development

# Run one defined test.
brownie test -k mint --network development

# Deploy.
brownie run scripts/deploy.py --network development
brownie run scripts/deploy.py --network polygon-test
brownie run scripts/deploy.py --network polygon-main
brownie run scripts/deploy.py --network mainnet

# Tokenize.
brownie run scripts/tokenize.py --network development
brownie run scripts/tokenize.py --network polygon-test
brownie run scripts/tokenize.py --network polygon-main
brownie run scripts/tokenize.py --network mainnet
```
