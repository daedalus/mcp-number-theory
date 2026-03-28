# mcp-number-theory

> MCP server exposing number theory functions and factorization algorithms.

[![PyPI](https://img.shields.io/pypi/v/mcp-number-theory.svg)](https://pypi.org/project/mcp-number-theory/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-number-theory.svg)](https://pypi.org/project/mcp-number-theory/)

## Install

```bash
pip install mcp-number-theory
```

## Usage

```python
from mcp_number_theory import number_theory as nt

# Compute GCD
result = nt.gcd(48, 18)  # Returns 6

# Factorize
from mcp_number_theory import algos
p, q = algos.fermat(1234567890123456789)
```

## MCP Server

This package provides an MCP server that exposes number theory functions. Run with:

```bash
mcp-number-theory
```

mcp-name: io.github.daedalus/mcp-number-theory
