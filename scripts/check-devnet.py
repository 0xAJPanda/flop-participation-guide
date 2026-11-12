#!/usr/bin/env python3
"""Read-only FLOP Devnet identity and availability check."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

RPC_URL = "https://rpc.devnet.flop.network"
FAUCET_CHAIN_URL = "https://faucet.flop.network/chain"
FAUCET_LIMITS_URL = "https://faucet.flop.network/limits"
EXPECTED_GENESIS = "0x99c172c095340ace980631f9123544c6bebd4839f3437e463533422d8be2d631"
USER_AGENT = "flop-participation-guide/1.0"


def get_json(url: str) -> object:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"{url} returned HTTP {response.status}")
        return json.load(response)


def rpc(method: str, params: list[object] | None = None) -> object:
    body = json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or []}
    ).encode("utf-8")
    request = urllib.request.Request(
        RPC_URL,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        payload = json.load(response)
    if "error" in payload:
        raise RuntimeError(f"RPC {method} failed: {payload['error']}")
    return payload.get("result")


def main() -> int:
    try:
        chain_name = rpc("system_chain")
        rpc_genesis = rpc("chain_getBlockHash", [0])
        faucet_chain = get_json(FAUCET_CHAIN_URL)
        limits = get_json(FAUCET_LIMITS_URL)
    except (OSError, ValueError, RuntimeError, urllib.error.URLError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    if not isinstance(faucet_chain, dict):
        print("FAIL: faucet chain response is not an object", file=sys.stderr)
        return 1
    faucet_genesis = faucet_chain.get("genesisHash")

    print(f"chain: {chain_name}")
    print(f"expected genesis: {EXPECTED_GENESIS}")
    print(f"RPC genesis:      {rpc_genesis}")
    print(f"faucet genesis:   {faucet_genesis}")

    if rpc_genesis != EXPECTED_GENESIS or faucet_genesis != EXPECTED_GENESIS:
        print("FAIL: network identity mismatch; do not sign or request funds", file=sys.stderr)
        return 1

    if isinstance(limits, dict):
        faucet = limits.get("faucet", {})
        sponsor = limits.get("sponsor", {})
        miner = sponsor.get("miner", {}) if isinstance(sponsor, dict) else {}
        print(f"faucet status: {faucet.get('status', 'unknown') if isinstance(faucet, dict) else 'unknown'}")
        print(f"miner sponsor status: {miner.get('status', 'unknown') if isinstance(miner, dict) else 'unknown'}")
        print(f"limits stale: {limits.get('stale', 'unknown')}")

    print("PASS: RPC and faucet agree on the expected FLOP Devnet genesis")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
