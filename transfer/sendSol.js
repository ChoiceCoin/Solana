const web3 =  require("@solana/web3.js");

(async () => {
  // Connect to cluster
  console.log(web3.clusterApiUrl('devnet'))
  const connection = new web3.Connection(
    web3.clusterApiUrl('devnet'),
    'confirmed',
  );
  // Uncomment the below command to test your connection to your node
  //console.log(await connection.getEpochInfo())

  // Using the secretkey to generate the keypair
  const secretkey = Uint8Array.from()
  const from = web3.Keypair.fromSecretKey(secretkey);  
  
  //If you already have enough test sol in your account you can comment this out
  const airdropSignature = await connection.requestAirdrop(
    from.publicKey,
    web3.LAMPORTS_PER_SOL,
  );
  await connection.confirmTransaction(airdropSignature);

  // Add transfer instruction to transaction
  // Lamport is the value
  const transaction = new web3.Transaction().add(
    web3.SystemProgram.transfer({
      fromPubkey: from.publicKey,
      toPubkey: '',
      lamports: web3.LAMPORTS_PER_SOL / 100,
    }),
  );

  // Sign transaction, broadcast, and confirm
  const signature = await web3.sendAndConfirmTransaction(
    connection,
    transaction,
    [from],
  );
  console.log('SIGNATURE', signature);
})();
