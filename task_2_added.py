"""
----------------------
PROBLEM STATEMENT
----------------------


The Star Wars API lists 82 main characters in the Star Wars saga.

For the first task, we would like you to use a random number generator
that picks a number between 1-82.

Using these random numbers you will be pulling 15 characters
from the API using Python.

"""

import sys
import random
import requests
import argparse


def generate_random_numbers(n: int = 15) -> list:
    """produces n random numbers (default 15)"""

    i = 1
    result = []
    while i <= n:
        result.append(random.randint(1, 83))
        i += 1
    return result


def get_url(resource_id: int) -> str:
    """

   Args:
       resource_id:

   Returns:

   """

    home_url = "https://swapi.dev"
    relative_url = "/api/people/{}"
    absolute_url = home_url + relative_url.format(resource_id)
    return absolute_url


if __name__ == "__main__":
    """
   HOME-URL :: https://swapi.dev
   relative-URL:: /api/people/1

   URL
   https://swapi.dev/api/people/1/

   """

    parser = argparse.ArgumentParser(
        prog="starwarsAPI",
        usage="Fetches resources from swapi.dev based "
              "on whatever arguments we provide",
        description="It uses random number generator and uses requests library "
                    "to get values from the swapi.dev"
    )

    # we are creating an option to provide count
    parser.add_argument('-c', '--count')
    arguments = parser.parse_args()

    print(f"parsed arguments are - {arguments}")

    resources = generate_random_numbers(int(arguments.count))
    print(f"[ INFO ] produced {len(resources)}"
          f" random resource ids in range(1, 83).")

    data = []
    for resource_id in resources:
        print(f"[ INFO ] fetching data for resource_id {resource_id}...")
        url_ = get_url(resource_id)

        # `requests.get()` returns a HttpResponse
        res = requests.get(url_)

        # gettign dict value from response object
        result = res.json()

        # capturing name from dict object
        data.append(result.get("name"))

    print(data)