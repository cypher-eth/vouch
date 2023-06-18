# Vouch

A public message attesting to anything. 

## Use Cases

#### Endorcements

A vouch can be from one address to another. It is one directional, with a public message attached. You can vouch for anyone, by writing something publicly.

#### Audits

An auditor could have a public address that vouches for smart contract addresses. Users can verify that contracts have been audited, and which addresses were covered in the audit.

#### Claims

A vouch can be from one address about itself. This can be used for recording general attestations, or to verify information.


## Testing
## Using Ape

#### Run Tests
Test suite is handed by [apeworx.io](https://apeworx.io)

```
ape test 
```

#### Gas usage

If you want to confirm the gas usage, you'll need hardhat configured, then run the following.

```
ape test --network=ethereum:local:hardhat --gas   
```


#### Deploy
Use ape to deploy to any network. If you've configured ape correctly, you can run the following example that deploys on Goerli.

```
ape run deploy --network=ethereum:goerli
```
## Using Woke

#### Run
```bash
woke init pytypes
```
to generate pytypes or
```bash
woke init pytypes -w
```
to generate pytypes and keep watching for filesystem changes and re-generate pytypes when needed.

Use
```bash
woke test -d tests/test_*.py
```
to run tests using a single process.

To run tests in parallel (makes sense only for fuzz tests), use
```bash
woke fuzz tests/test_*.py
```
