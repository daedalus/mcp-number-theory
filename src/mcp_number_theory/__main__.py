"""CLI entry point for the MCP number theory server."""

from mcp_number_theory.server import mcp


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    raise SystemExit(main())
