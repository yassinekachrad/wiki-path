from typing import Dict, List
import requests


def getLinks(page: str) -> List[str]:
    """
    Get all links from a wikipedia page
    """
    response = requests.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "format": "json",
        "titles": page,
        "prop": "links",
        "pllimit": "max",
    })

    data = response.json()

    listOfDicts = list(data["query"]["pages"].values())[0]["links"]

    return [link["title"] for link in listOfDicts]

def shortestWikiPath(origin: str, target: str) -> List[str]:
    """
    Find the shortest path between two wikipedia pages
    """
    queue = [origin]

    prevPage: Dict[str, str] = {}

    while queue:
        page = queue.pop(0)
        print(page)
        if page == target:
            break
        try:
            links = getLinks(page)

            for link in links:
                if link not in prevPage:
                    prevPage[link] = page
                    queue.append(link)
        except Exception as e:
            print(f"Error: {e}")
    
    # build the path
    path = []
    current = target

    while current != origin:
        path.append(current)
        current = prevPage[current]

    path.append(origin)
    path.reverse()

    return path