"""Minimal reproducible example script.

This script is for you to use to reproduce a bug or demonstrate a feature.
"""

import asyncio
from os import getenv
import logging

from acapy_controller import Controller
from acapy_controller.logging import logging_to_stdout
from acapy_controller.protocols import didexchange

ALICE = getenv("ALICE", "http://alice:3001")
BOB = getenv("BOB", "http://bob:3001")

LOGGER = logging.getLogger(__name__)


async def main():
    """Test Controller protocols."""
    async with Controller(base_url=ALICE) as alice, Controller(base_url=BOB) as bob:
        await didexchange(alice, bob)

    LOGGER.debug("Done")


if __name__ == "__main__":
    logging_to_stdout()
    asyncio.run(main())
