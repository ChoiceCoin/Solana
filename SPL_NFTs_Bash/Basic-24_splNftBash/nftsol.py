import requests
import json

NFT_URI = "https://cdn.pixabay.com/photo/2017/08/24/11/04/brain-2676370_1280.jpg"
NFT_NAME = "Basic-24"
NFT_SYMBOL = "Brain"  
NFT_DESCRIPTION = "Solana NFT Creation Bash - Ahmed"
NFT_METADATA = {
    "cleverness": 100,
    "intelligence": 100,
    "musk": 99,
    "warioness": 98
}

KEY_ID = "xm9MSoRvlaLzPJO"
SECRET_KEY = "WB01dLnOnhVRLyc"
HEADERS = {
    "APIKeyID": KEY_ID,
    "APISecretKey": SECRET_KEY
}


SECRET_PHRASE_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/wallet/secret_recovery_phrase"
PUBLIC_KEY_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/wallet/public_key"
BALANCE_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/wallet/balance"
NFT_MINT_FEE_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/nft/mint/fee"
NFT_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/nft"

SECRET_PHRASE = "critic summer impact weasel muscle couch into nuclear sibling clip dignity multiply"

PUBLIC_KEY = "DMjPKvEjRSA8rbCemvvojactQVuBPXwTVeifQad3h7yC"

DERIVATION_PATH = ''

if __name__ == '__main__':
 
  ## Here the NFT will be created.

  mint_nft_response = requests.post(
        NFT_ENDPOINT,
        params={
            "derivation_path": DERIVATION_PATH,
            "secret_recovery_phrase": SECRET_PHRASE,
            "nft_name": NFT_NAME,
            "nft_symbol": NFT_SYMBOL,
            "nft_description": NFT_DESCRIPTION,
            "nft_url": NFT_URI,
            "nft_metadata": json.dumps(NFT_METADATA),
            "network": "devnet",
            "nft_upload_method": "S3"
        },
        headers=HEADERS
    )
  print(mint_nft_response.json())
