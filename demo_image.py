#!/usr/bin/env python3
"""Demo script to send demo image to iDotMatrix device."""
import asyncio
import os
import sys
from idotmatrix import ConnectionManager, Image as DMImage

async def main():
    address = os.environ.get('IDOTMATRIX_ADDRESS')
    if not address:
        print('Please set the IDOTMATRIX_ADDRESS environment variable (or use "auto").')
        sys.exit(1)
    conn = ConnectionManager()
    if address.lower() == 'auto':
        await conn.connectBySearch()
    else:
        await conn.connectByAddress(address)
    img = DMImage()
    await img.setMode(1)
    await img.uploadUnprocessed('images/demo_32.png')

if __name__ == '__main__':
    asyncio.run(main())