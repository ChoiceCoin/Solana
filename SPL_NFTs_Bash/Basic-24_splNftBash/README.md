# Transfer SOL nft between wallets

Transaction script to send Solana nft form one wallet to another using NodeJs and web3js official library

MAKE SURE TO TEST THAT EVERYTHING WORKS FINE USING DEVNET FIRST, IF YOU MAKE SOME MISTAKE IN MAINNET YOU MIGHT LOSE SOL

You can first check functionality in devnet script using demo accounts

Change the devnet.js to mainnet.js in package.json


# Quick Start

``` shell
 npm init
 npm install @solana/web3.js
 npm install @solana/spl-token
 npm install @solana/buffer-layout

```
	
## Requirements
	@solana/web3.js
	@solana/spl-token
	@solana/buffer-layout

## Side notes

- [Solana official library - ](https://docs.solana.com/ "Solana official library") 

## shell Output

```
Solana public address: 2atoc2pBaesstEB6Kvx26i3NnjYsiKkieuBxEEcgTMSJ
PublicKey {
  _bn: <BN: cfc2a8402d8a25b175d628fbdbf9467cb7a41ec887daa5599d83f6976d4c10d3>
}
Mint public address: Ez1YrmXKae6jS318ybNCG3KYqqsAVBEJH5xQE3NKMXdL

Token public address: 8Ss53RK4QnLPDeZMpXAvN1y1s58LBe7piYintFBWsaZa

QvRy8JVWnkqB79cuPUEvFuUkjaCtqZw5FGQHfcdud3b7BaSRedRPVmgMrvfUcYHHkWZ19wmKR88o8GuoLwpftLg
EosJmt2dKbygabDpQwkc2rfn3dvn6rizKzJpJhhkzYw1 Receiver addr

Transaction signature 4Bc5EsDZWqYrbzZeUFgwmjHT6KLCPLMh2oZge8to4ot3Mi8At5ef2f8zTntnhB9A4TgFxUGb71ozJHJakdX75qEW

Success!
Done

```

## Explorer | Solana

https://explorer.solana.com/tx/4Bc5EsDZWqYrbzZeUFgwmjHT6KLCPLMh2oZge8to4ot3Mi8At5ef2f8zTntnhB9A4TgFxUGb71ozJHJakdX75qEW?cluster=devnet

## Screen-shots
[Explorer | Solana](screenshot/explorersol.png)
