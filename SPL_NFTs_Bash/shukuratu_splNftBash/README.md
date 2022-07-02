Go to requiremens file

Creating your SPL NFT
First, create the token
'spl-token create-token --decimals 0'

Using the unique token identifier, we can create an account to store our balance data
'spl-token create-account <token-identifier>'

Mint only one token into the account

spl-token mint <token-identifier> 1 <token-account>
Disable future minting

spl-token authorize <token-identifier> mint --disable