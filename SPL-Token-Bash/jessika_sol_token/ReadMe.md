## SPL TOKEN CREATION
In this folder there is a file `create_mint_and_transfer_token.ts` which is resposible for the creation of a spl token and also the minting of the token, initially when a token is createdthe total suooly is zero but after writing the minting script you can mint any amount of that token.
This file alone isnt enough to do these transactions so follow these steps and youll be able to create your first spl token on solana.

Ensure you have solana and yarn installed in your system

## Install

```shell
yarn add @solana/spl-token
```

## Build from Source

1. Clone the project:
```shell
git clone https://github.com/solana-labs/solana-program-library.git
```

2. Navigate to the library:
```shell
cd solana-program-library/token/js
```

3. Install the dependencies:
```shell
yarn install
```

4. Build the library:
```shell
yarn build
```

5. Run the tests:
```shell
yarn test
```

6. Run the example:
```shell
yarn example
```

## Adjustments
To adjust the total supply being minted you can play around with the decimal in my code the decimal is 5 on line19 `const mint = await createMint(connection, fromWallet, fromWallet.publicKey, null, 5);` so my total supply is 1000000000 / 10^5 = 10k, so to make it 1billion you can change the decimal to 0 making it have no decimal place.

If you've followed the steps above you'll get a mint id and a transfer id transfering a fraction of my token to another address

`Mint tx : 31gv56UpjavvZnZ1vYneGoows2EXhiUnntVEkkJC3n154TWeYFQW4ciUEeuU7dTVucx2bCDGpoG8nxSA4ZkGa7SA`

Transfer tx : `3VgvnEQVqVm7yrMyBPF3tYFDsEv75CUsK8htlerikYB79SZc8BaVyLhJ15cTqjerg3TSe72RH45zWRXv96rYkLkP`

Here's the [demo video](https://youtu.be/cUyBsDTB_us) showing the token address and the owner and the supply.

In Solana naming a token is a bit lengthier and time taking because you will have to clone a repo edit some files, commit the file and make a pr for after some checks to ensure no other changes apart from the right ones took place ,here is a link for a detailed [video](https://www.youtube.com/watch?v=kVxueRjcm6A)  to edit the name of your spl token and also the logo with the symbols using this [repo](https://github.com/solana-labs/token-list)