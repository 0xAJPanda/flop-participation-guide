# FLOP: Simple Devnet, Validator, and Miner Guide

This guide is for beginners. Start with the wallet test. Do not run a validator or miner unless the official public Testnet instructions are available and you understand the operating requirements.

## Important

**FLOP Devnet does not provide rewards, airdrop weight, scoring, or guaranteed Testnet priority.** It is only for testing.[1][2]

There is no official FLOP token, mint, presale, Discord, or Telegram. Do not buy an unofficial token or share a recovery phrase or private key.[1]

## Part 1: Test the wallet

### Step 1: Install Talisman

Go to <https://talisman.xyz/download> and install Talisman.[8]

Create a wallet, set a password, and save the recovery phrase offline. Never send that phrase to anyone.

### Step 2: Create two test accounts

In Talisman, create two new **Substrate** accounts:

- `FLOP Devnet A`
- `FLOP Devnet B`

When copying an address, choose **Substrate (Generic)**. Use only these disposable accounts for this test.

### Step 3: Add FLOP Devnet

In Talisman:

1. Open **More**.
2. Select **Manage Networks**.
3. Select **Add Network**.
4. Choose **Substrate**.
5. Enter the following values.

| Field | Value |
|---|---|
| Network name | `FLOP Devnet` |
| RPC | `wss://rpc.devnet.flop.network` |
| Symbol | `FLOP` |
| Decimals | `18` |
| SS58 prefix | `42` |
| Explorer | `https://explorer.devnet.flop.network` |
| Testnet | Enabled |
| CheckMetadataHash | Disabled |

Save the network.

`CheckMetadataHash` is disabled because enabling it caused Talisman to reject a live test transaction with `1011: Unknown Transaction Validity`.

### Step 4: Request test FLOP

1. Copy the **Substrate (Generic)** address for `FLOP Devnet A`.
2. Open <https://faucet.flop.network>.[6]
3. Paste the address.
4. Request the displayed Devnet grant.
5. Wait for the balance to appear in Talisman.

Devnet FLOP has no monetary value.

### Step 5: Send FLOP to your second wallet

Do not copy a recipient address from a social post or public guide. Send only to your own `FLOP Devnet B` account.

1. Copy the **Substrate (Generic)** address for `FLOP Devnet B`.
2. Open `FLOP Devnet A` in Talisman.
3. Select FLOP and choose **Send**.
4. Paste the address for `FLOP Devnet B`.
5. Enter `0.1 FLOP`.
6. Confirm the network says `FLOP Devnet`.
7. Check the first and last six characters of the address.
8. Review the fee and sign inside Talisman.
9. Check both accounts at <https://explorer.devnet.flop.network>.[7]

One transaction is enough. You may send `0.05 FLOP` back from B to A as a return test, then stop. Extra transactions do not improve eligibility.

### If Talisman says `Unknown Transaction Validity`

1. Open the FLOP Devnet network settings.
2. Disable `CheckMetadataHash`.
3. Save the network.
4. Create the transfer again.

A rejected transaction does not count as completed. Confirm it in the explorer.

## Part 2: Validator

A validator does not need a GPU, but it is not a beginner wallet task. Validators must run continuously and participate in block production, finality, and data availability.[4]

The current Devnet validator process is administrator-assisted. It requires FLOP operations coordination, network access, funding, and promotion. Public self-service onboarding is not ready.[4]

The current planning profile is:[4]

- 8 dedicated CPU cores
- 32 GB RAM
- 4 TB NVMe storage
- Reliable low-latency 1 Gbps internet
- Continuous monitoring, backups, and uptime

**What to do now:** read the official validator guide and wait for public Testnet onboarding. Do not copy development keys, expose RPC ports, or attempt to bypass admission.

Official validator guide: <https://docs.flop.network/docs/run-validator>

## Part 3: Miner

A miner uses an NVIDIA GPU to serve AI inference. It also runs a worker for registration, calibration, evidence, and sessions.[5]

The current official guide says Devnet sponsorship, registration, and calibration can be available, but paid public mining sessions are not open yet.[5]

The documented starting requirements include:[5]

- Linux host or full virtual machine
- NVIDIA GPU with at least 16 GB VRAM
- Docker and NVIDIA Container Toolkit
- Persistent model storage
- Public HTTPS hostname or controlled HTTPS tunnel

We tested the official backend on an RTX 5060 Ti 16 GB. The container detected the GPU and loaded the registered Qwen 0.5B model using about 12 GB VRAM. This proves only basic GPU and model-loading compatibility. It does not prove calibration, settlement, admission, or earnings.

**What to do now:** prepare the hardware and wait for the public Testnet release, current miner package, open sponsorship capacity, and published reward rules. Do not create multiple identities or assume Devnet mining will count later.

Official miner guide: <https://docs.flop.network/docs/run-miner>

## Part 4: Wait for Testnet

Devnet earns nothing and does not qualify an account for future rewards.[1][2]

The draft Testnet design focuses on verified compute served, not wallet balance, transfer count, completed-job count, or active days. The official page also says these rules were not fully built when published.[3]

Before spending money or deploying equipment, wait for FLOP to publish:

- A live Testnet announcement
- Testnet genesis and network settings
- Final validator and miner releases
- Public onboarding rules
- Final scoring, reward, snapshot, and vesting rules

Follow only:

- X: <https://x.com/flop_labs>
- Documentation: <https://docs.flop.network>
- GitHub: <https://github.com/flop-labs>
- Website: <https://flop.finance>

## Optional technical checks

The `scripts/` directory contains read-only checks for experienced operators. Beginners do not need them for the wallet tutorial.

## Sources

[1] https://docs.flop.network/docs/official-links — Official links & verification
[2] https://docs.flop.network/docs/testnet-and-timeline — FAQ: Testnet & Launch Timeline
[3] https://docs.flop.network/docs/airdrop-and-testnet-conversion — The airdrop and testnet conversion
[4] https://docs.flop.network/docs/run-validator — Run a FLOP validator
[5] https://docs.flop.network/docs/run-miner — Run a FLOP miner on a GPU host
[6] https://faucet.flop.network — FLOP Devnet faucet
[7] https://explorer.devnet.flop.network — FLOP Devnet explorer
[8] https://talisman.xyz/download — Talisman wallet download
