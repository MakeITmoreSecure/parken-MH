import requests
import argparse

parken_url = "https://8s5zm653e0.execute-api.eu-central-1.amazonaws.com/production/v2/payment/plate/search?plate="

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plate",
                        "-p",
                        dest="plate",
                        required=True,
                        help="plate to track. Format: M-AS123")

    return parser.parse_args()


def track_plate(plate):
    try:

        t_req = requests.request(method="GET", url=f"{parken_url}{plate}")
        print(t_req.status_code)
        print(t_req.text)
    except Exception as e:
        print(e)
def main():
    myargs = args()
    track_plate(myargs.plate)



if __name__ == '__main__':
    main()