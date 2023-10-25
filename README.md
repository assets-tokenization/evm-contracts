# Assets Tokenization EVM Contracts

## Description

This repository contains the smart contracts for the Assets Tokenization project.

## Dependencies

- [Python](https://www.python.org/downloads/).
- [Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html).
- [Ganache](https://www.trufflesuite.com/ganache).
- [Infura](https://app.infura.io/dashboard).

## Configs

```sh
# Create environment file.
cp .env.example .env
# Edit environment file.
```

## Test

```sh
# Add local Ganache to use in tests.
brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337

#add ganash npm packet
npm install -g ganache-cli

# Run tests on defined network.
brownie test --network development

# Run one defined test.
brownie test -k tokenize --network development
```

## Deploy

```sh
# Deploy on defined network.
brownie run scripts/deploy.py --network development
brownie run scripts/deploy.py --network polygon-test
brownie run scripts/deploy.py --network polygon-main
brownie run scripts/deploy.py --network mainnet
```

## Tokenize

```sh
# Tokenize on defined network.
brownie run scripts/tokenize.py --network development
brownie run scripts/tokenize.py --network polygon-test
brownie run scripts/tokenize.py --network polygon-main
brownie run scripts/tokenize.py --network mainnet
```
