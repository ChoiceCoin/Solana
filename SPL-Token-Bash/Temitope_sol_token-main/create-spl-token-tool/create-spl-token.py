import sys
import subprocess

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print("\nPlease provide, with the following order, the network, the number of tokens to mint, the path to your private key, your public key, the number of decimals of your token and if you want disable or enable future token mint!")
        exit()

    ### Create the needed variables from the user inputs ### 
    network = sys.argv[1]
    quantity = sys.argv[2]
    path_keypair = sys.argv[3]
    pubkey = sys.argv[4]
    decimals = sys.argv[5]
    mint = sys.argv[6]


    token_address = ""
    token_account = ""


    if (network == "mainnet-beta" or network == "devnet") and (mint == "disable" or mint == "enable"):
        if mint == "disable" or mint == "enable":
            try:
                quantity = int(quantity)
                try:
                    decimals = int(decimals)
                    ### Set the command to create a token ###
                    create_token_cmd = f'spl-token create-token --url {network} --fee-payer {path_keypair} --mint-authority {pubkey} --decimals {decimals}'

                    ### Execute the command and get the output ###
                    create_token_result = subprocess.check_output(create_token_cmd, shell=True, universal_newlines=True)

                    ### Verify if the transaction succeed ###
                    if "Signature:" in create_token_result:
                        print("\nToken created!")

                        ### Get the address of the token created from the output ###
                        for i in range(15, 59):
                            token_address += create_token_result[i]

                        ### Set the command to create the associated token account ###
                        create_token_account_cmd = f'spl-token create-account --url {network} --fee-payer {path_keypair} --owner {pubkey} {token_address}'

                        ### Execute the command and get the output ###
                        create_token_account_result = subprocess.check_output(create_token_account_cmd, shell=True, universal_newlines=True)
                
                        ### Verify if the transaction succeed ###
                        if "Signature:" in create_token_account_result:
                            print("\nToken account created!")

                            ### Get the address of the associated token account from the output ###
                            for i in range(17, 61):
                                token_account += create_token_account_result[i]

                            ### Set the command to mint token ###
                            mint_token_cmd = f'spl-token mint --url {network} --fee-payer {path_keypair} --mint-authority {path_keypair} {token_address} {quantity} {token_account}'

                            ### Execute the command and get the output ###
                            mint_token_result = subprocess.check_output(mint_token_cmd, shell=True, universal_newlines=True)

                            ### Verify if the transaction succeed ###
                            if "Signature:" in mint_token_result:
                                print("\nToken minted!")

                                if network == "mainnet-beta":
                                    url = f'https://solscan.io/token/{token_address}'

                                else:
                                    url = f'https://solscan.io/token/{token_address}?cluster=devnet'

                                print(f'\nSee your token at this url : {url}')

                                if mint == "disable":

                                    ### Set the command to disable mint authority ###
                                    disable_mint_cmd = f'spl-token authorize --url {network} --fee-payer {path_keypair} --authority {path_keypair} {token_address} mint --disable'
                                    
                                    ### Execute the command and get the output ###
                                    disable_mint_result = subprocess.check_output(disable_mint_cmd, shell=True, universal_newlines=True)

                                    ### Verify if the transaction succeed ###
                                    if "Signature:" in disable_mint_result:
                                        print("\nMint authority correctly disabled!")

                except ValueError:
                    print("\nOops! It's not a valid number of decimals. Try again...")

            except ValueError:
                print("\nOops! It's not a valid number of tokens to mint. Try again...")
        else:
            print(f"\nOops! It's not a valid input for the mint authority")
    else:
        print("\nOops! It's not a valid network. Only mainnet-beta and devnet are allowed")
