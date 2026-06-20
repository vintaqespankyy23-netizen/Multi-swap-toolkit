# CryptoSwap Toolkit - Private Tor-based Crypto Swaps

For educational and privacy-conscious use only.

## Features
- Tor integration for anonymous API calls
- CCXT support for CEX price/quotes
- Web3-ready for DEX swaps (extendable)
- Circuit renewal for IP rotation
- CLI interface

## Setup
1. Install Tor: apt install tor (Linux) or equivalent. Edit /etc/tor/torrc to enable ControlPort 9051.
2. pip install -e .
3. Set env vars: WALLET_PRIVATE_KEY=... (use .env, never commit!)
4. Run Tor: tor

## Usage
```bash
cryptoswap swap --from ETH --to USDC --amount 0.1
