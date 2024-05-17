from typing import List
import src.wiki.search as wikisearch

origin = input("Input a wikipedia link to go from :")
target = input("Input a wikipedia link to go to :")

result: List[str] = wikisearch.shortestWikiPath(origin, target)

print(f"The shortest path from {origin} to {target} is : {' -> '.join(result)}")