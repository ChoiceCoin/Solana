from theblockchainapi import \
    SolanaAPIResource, SolanaCurrencyUnit, SolanaNFTUploadMethod, SolanaNetwork, DerivationPath, SolanaWallet
import time

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
# I will delete my keys after the dead-line
MY_API_KEY_ID = "IfgA0hcJPVX4lVD"
MY_API_SECRET_KEY = "ZB1SjavyJ5j6Qj3"

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def solnft():
 
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key(API,SECRET) ID pair!")

    # Create a wallet
    secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    wallet = SolanaWallet(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=DerivationPath.CLI_PATH,
      	
    )
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)

    print(f"Public Key: {public_key}")
    print(f"Secret Recovery Phrase: {secret_recovery_phrase}")

    # Get an airdrop on the devnet in order to be able to mint an NFT
    BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)

    # We need to make sure the airdrops have time to process before minting the NFT!
    time.sleep(15)

    def get_balance():
        balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(
            public_key,
            unit=SolanaCurrencyUnit.SOL,
            network=SolanaNetwork.DEVNET
        )
        print(f"Balance: {balance_result['balance']}")
    get_balance()

    # Mint an NFT
    nft = BLOCKCHAIN_API_RESOURCE.create_nft(
        wallet=wallet,
        mint_to_public_key="8CAuSKvvpmpe7LmgEjC4np1AQ51MtX4QaukQmeh7HSCp",
        name="Solana NFT ZeeBabe",
        symbol="ZeeBabe",
        network=SolanaNetwork.DEVNET,

        # ---- S3 upload method...
        image_url="https://drive.google.com/file/d/104hRvGFBzyjpEJSdMYBoo4gp4mCLCiy5/view?usp=sharing",
        upload_method=SolanaNFTUploadMethod.S3,
        description="ZeeBabe SPL_NFT_SOLANA",
        uri_metadata={
            "attributes": [
                {
                    "trait_type": "fruit",
                    "value": "yes"
                },
                {
                    "trait_type": "speed",
                    "value": 100
                },
                {
                    "trait_type": "dead",
                    "value": "no"
                }
            ],
            "collection": {
                "name": "BlockchainAPI NFT (Very Rare)",
                "family": "BlockchainAPI NFTs"
            }
        },

        # ---- OR (instead of S3)
        # uri='',
        # upload_method=SolanaNFTUploadMethod.URI,

        creators=[
            public_key,
            "769UKc8ddKNYjsV74RsaCG7GSePxKE7PC2h6zTncLjE4",
            "44C7VssifqLmzHu2rnLy9VpT57pjm4T2p31CUTpAFhkp"
        ],
        share=[10, 70, 20],
        seller_fee_basis_points=100,
        is_mutable=False,
        is_master_edition=True
    )
    print("NFT: ", nft)
    print(f"View Explorer: {nft['explorer_url']}")


if __name__ == '__main__':
    solnft()
