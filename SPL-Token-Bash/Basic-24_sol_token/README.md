## SPL TOKEN CREATION
In this folder there is a file `SPLTokenBash.js` which is responsible for the creation of a spl token and also the minting of the token, initially when a token is created the total supply is zero but after writing the minting script you can mint any amount of that token.
This file alone isn't enough to do these transactions so follow these steps and you'll be able to create your first spl token on solana.

Ensure you have solana and npm installed in your system

## Install

```shell
npm add @solana/spl-token
```

## Build from Source

### Ref.
## Clone the project: 
```shell
git clone https://github.com/solana-labs/solana-program-library.git
```

## Install the dependencies:
```shell
npm i || npm install
```
# note
If you've followed the steps above you'll get a mint id and a transfer id of your token should look like >

`int tx: d7tdN8dXsXjEBt8cHrJekAgAnSziTuRXh56psqvr4y9d2UJgu9DHmkZEGaoG7H2e7Dp7fDq3ihLMx8vQaAGZYLL`

`transfer tx: 4fp5YuZrhjP9yG7jXCuNRUVjvfLuCChFwfW3WjTJ1rthGUTa2NZi2M2SWfeW6HGXHg1spQpnhJffSCb9nUoiqU65`

## Screen-shots
[screen-shot](img/spl-ss.png)

Here's the [screen-shot](img/spl.png) showing the token address and the owner address and the supply.