
# Run Step
You must have Nodejs installed on your system.
- Step 1: Create a file or copy the file `sendSol.js`into your machine and open it with vscode
- Step 2: Inside that directory integrated terminal innstall the solana web3.js library using `npm i @solana/web3.js`
- Step 3: Install the solana cli tool using `sh -c "$(curl -sSfL https://release.solana.com/v1.10.24/install)"` if you are propmted with this message `Please update your PATH environment variable to include the solana programs:` copy and paste the content of the line below it and press enter
- Step 4:If you have an already generated public address you want to use you will have to generate the keypair using the 12 word seed phrase given when you created your address using `solana-keygen recover -o file.json`, this is a solana cli command that would prompt you to input your seed phrase in your terminal and a `file.json` file would be generated with the contetnts being the secretkey which would be used to generate the keypair
- The content if the file should be like this `[4,141,211,222,196,83,15,186,225,14,235,178,208,60,129,66,100,109,184,177,43,108,204,141,249,255,156,217,179,89,98,126,140,172,25,113,234,250,227,231,101,75,76,156,217,227,190,122,24,210,58,103,224,130,83,98,147,101,82,111,100,103,187,214]` once you are able to get that you are good to go.
- Step 5: In the sendSol file on line 14 `const secretkey = Uint8Array.from([4,141,211,222,196,83,15,186,225,14,235,178,208,60,129,66,100,109,184,177,43,108,204,141,249,255,156,217,179,89,98,126,140,172,25,113,234,250,227,231,101,75,76,156,217,227,190,122,24,210,58,103,224,130,83,98,147,101,82,111,100,103,187,214])` inside the parenthesises replace the content with your keypair
- Step 6: For the `toPubkey` you can use input the address directly without using the secretkey and keypair like I did in line 29 `toPubkey: '5cG115Uv89fkAGMVSrLYBgnEX7MEiE7BJkd7pK9YdQJ4',` WHY you may ask - that's because you dont need to sign any transaction to recieve any token but you will have to sign a transaction using your keypair to send any token out of your account
- Step 7: So once all that is set up you can go ahead to make your first transaction using `node sendSol.js` in your terminal, the output would be a signature which is like the transaction id in algorand and pasting it on the solscan search engine you can see the full contents of the transaction (remeber to change it to devnet just like we do on algoexplorer)


