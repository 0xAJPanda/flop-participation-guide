#!/usr/bin/env bash
# Read-only host preflight for the documented FLOP miner path.
set -u

failures=0
warnings=0

pass() { printf 'PASS: %s\n' "$1"; }
warn() { printf 'WARN: %s\n' "$1"; warnings=$((warnings + 1)); }
fail() { printf 'FAIL: %s\n' "$1"; failures=$((failures + 1)); }

if command -v nvidia-smi >/dev/null 2>&1; then
  pass "nvidia-smi is installed"
  nvidia-smi --query-gpu=name,memory.total,driver_version,compute_cap,temperature.gpu \
    --format=csv,noheader || fail "nvidia-smi query failed"
else
  fail "nvidia-smi is not installed"
fi

if command -v docker >/dev/null 2>&1; then
  pass "Docker is installed"
  if docker info >/dev/null 2>&1; then
    pass "Docker daemon is reachable"
    if docker info --format '{{json .Runtimes}}' | grep -qi nvidia; then
      pass "Docker reports an NVIDIA runtime"
    else
      fail "Docker does not report an NVIDIA runtime"
    fi
    if docker compose version >/dev/null 2>&1; then
      pass "Docker Compose plugin is available"
    else
      fail "Docker Compose plugin is unavailable"
    fi
    printf '\nCurrent containers:\n'
    docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
  else
    fail "Docker daemon is not reachable"
  fi
else
  fail "Docker is not installed"
fi

printf '\nMemory:\n'
free -h || warn "could not read memory"

printf '\nFilesystems:\n'
df -hT -x tmpfs -x devtmpfs || warn "could not read filesystems"

printf '\nGPU processes:\n'
if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia-smi --query-compute-apps=pid,process_name,used_gpu_memory --format=csv,noheader \
    || warn "could not read GPU processes"
fi

printf '\nSummary: failures=%d warnings=%d\n' "$failures" "$warnings"
if [ "$failures" -ne 0 ]; then
  exit 1
fi

printf '%s\n' "Preflight passed. This does not prove model inference, registration, calibration, admission, settlement, or earnings."
