import requests  # Used to call APIs / API call karnyasathi vaparto

import time  # Used for sleep (delay) / delay denyasathi vaparto

import json  # Used to save data in JSON file / data JSON madhe save karnyasathi

import os  # Used to create folders / folder create karnyasathi

from datetime import datetime  # Used to get current time / current time gheanyasathi


# headers define karto (server la sangto ki mi kon ahe)
headers = {"User-Agent": "TrendPulse/1.0"}  # API la identify karayla madat hote


# Step 1: Top story IDs gheto
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", headers=headers)  
# API call karto ani top stories che IDs gheto

data1 = response.json()  
# response la JSON format madhe convert karto (Python use sathi)


stories = []  
# saglya stories store karnyasathi empty list banavli


# categories ani tyache keywords define karto
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


# pratek category sathi count track karto (25 limit sathi)
category_count = {cat: 0 for cat in categories}  
# suruvatila sagle 0 thevto


# Step 2: category wise process karto
for cat in categories:  
# pratek category var loop chalel

    for story_Id in data1:  
    # pratek story ID var loop

        if category_count[cat] >= 25:  
        # jar 25 stories zalyat tar thambaycha
            break  

        try:
            URL = f"https://hacker-news.firebaseio.com/v0/item/{story_Id}.json"  
            # pratek story sathi detail API banavto

            response = requests.get(URL, headers=headers)  
            # story detail fetch karto

            data2 = response.json()  
            # JSON madhe convert karto

        except:
            print(f"Request failed for ID {story_Id}")  
            # jar request fail zali tar message print karto
            continue  

        if data2 is None:  
            # jar data nahi milala tar skip
            continue  

        if data2.get("type") != "story":  
            # jar type story nahi (comment/job) tar skip
            continue  

        title = data2.get("title", "")  
        # title gheto (nasel tar empty string)

        title_lower = title.lower()  
        # lowercase karto matching sathi


        # category match karto keywords sobat
        if not any(word in title_lower for word in categories[cat]):  
            continue  
        # jar keyword match nahi zala tar skip


        # ek story dictionary madhe store karto
        story = {
            "post_id": data2.get("id"),  # story ID
            "title": title,  # title
            "category": cat,  # assigned category
            "score": data2.get("score"),  # upvotes
            "num_comments": data2.get("descendants"),  # comments count
            "author": data2.get("by"),  # author
            "collected_at": datetime.now().isoformat()  # current time
        }

        stories.append(story)  
        # story list madhe add karto

        category_count[cat] += 1  
        # count increase karto


    time.sleep(2)  
    # pratek category nantar 2 second wait karto (API overload avoid)


# Step 3: data save karto

os.makedirs("data", exist_ok=True)  
# "data" folder create karto (aslyas error nahi)


filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"  
# file name dynamic banavto (date wise)


with open(filename, "w") as f:  
    # file write mode madhe open karto

    json.dump(stories, f, indent=2)  
    # stories JSON madhe save karto (pretty format)


print(f"Collected {len(stories)} stories. Saved to {filename}")  
# final output print karto