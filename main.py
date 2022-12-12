import asyncio
import time
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from helper.supported_sites import supported_sites

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/search")
async def call_api(
        site: str, query: str, limit: Optional[int] = 0, page: Optional[int] = 1
):
    site = site.lower()
    query = query.lower()

    if site in supported_sites.keys():
        limit = (
            supported_sites[site]["limit"]
            if limit == 0 or limit > supported_sites[site]["limit"]
            else limit
        )

        resp = await supported_sites[site]["website"]().search(query, page, limit)
        if resp is None:
            return {"error": "website blocked change ip or domain"}
        elif len(resp["data"]) > 0:
            return resp
        else:
            return {"error": "no results found"}

    return {"error": "invalid site"}


@app.get("/api/trending")
async def get_trending(
        site: str,
        limit: Optional[int] = 0,
        category: Optional[str] = None,
        page: Optional[int] = 1,
):
    site = site.lower()
    category = category.lower() if category else None
    if site in supported_sites.keys():
        limit = (
            supported_sites[site]["limit"]
            if limit == 0 or limit > supported_sites[site]["limit"]
            else limit
        )
        if supported_sites[site]["trending_available"]:
            if category is not None and not supported_sites[site]["trending_category"]:
                return {
                    "error": "search by trending category not available for {}".format(
                        site
                    )
                }
            if category is not None and category not in supported_sites[site]["categories"]:
                return {
                    "error": "selected category not available",
                    "available_categories": supported_sites[site]["categories"],
                }
            resp = await supported_sites[site]["website"]().trending(category, page, limit)
            if not resp:
                return {"error": "website blocked change ip or domain"}
            elif len(resp["data"]) > 0:
                return resp
            else:
                return {"error": "no results found"}

        else:
            return {"error": "trending search not availabe for {}".format(site)}
    return {"error": "invalid site"}


@app.get("/api/category")
async def get_category(
        site: str,
        query: str,
        category: str,
        limit: Optional[int] = 0,
        page: Optional[int] = 1,
):
    site = site.lower()
    query = query.lower()
    category = category.lower()

    if site in supported_sites:
        limit = (
            supported_sites[site]["limit"]
            if limit == 0 or limit > supported_sites[site]["limit"]
            else limit
        )
        if supported_sites[site]["search_by_category"]:
            if category not in supported_sites[site]["categories"]:
                return {
                    "error": "selected category not available",
                    "available_categories": supported_sites[site]["categories"],
                }

            resp = await supported_sites[site]["website"]().search_by_category(
                query, category, page, limit
            )
            if resp is None:
                return {"error": "website blocked change ip or domain"}
            elif len(resp["data"]) > 0:
                return resp
            else:
                return {"error": "no results found"}
        else:
            return {"error": "search by category not available for {}".format(site)}
    return {"error": "invalid site"}


@app.get("/api/recent")
async def get_recent(
        site: str,
        limit: Optional[int] = 0,
        category: Optional[str] = None,
        page: Optional[int] = 1,
):
    site = site.lower()
    category = category.lower() if category else None

    if site in supported_sites:
        limit = (
            supported_sites[site]["limit"]
            if limit == 0 or limit > supported_sites[site]["limit"]
            else limit
        )
        if supported_sites[site]["recent_available"]:
            if category is not None and not supported_sites[site]["recent_category_available"]:
                return {
                    "error": "search by recent category not available for {}".format(
                        site
                    )
                }
            if category is not None and category not in supported_sites[site]["categories"]:
                return {
                    "error": "selected category not available",
                    "available_categories": supported_sites[site]["categories"],
                }
            resp = await supported_sites[site]["website"]().recent(category, page, limit)
            if not resp:
                return {"error": "website blocked change ip or domain"}
            elif len(resp["data"]) > 0:
                return resp
            else:
                return {"error": "no results found"}
        else:
            return {"error": "recent search not available for {}".format(site)}
    else:
        return {"error": "invalid site"}


@app.get("/")
async def home():
    return {"info": "torrent api python"}


@app.get("/api/all/search")
async def get_search_combo(query: str, limit: Optional[int] = 0):
    start_time = time.time()
    query = query.lower()
    sites_list = list(supported_sites.keys())
    tasks = []
    combo = {"data": []}
    total_torrents_overall = 0
    for site in sites_list:
        limit = (
            supported_sites[site]["limit"]
            if limit == 0 or limit > supported_sites[site]["limit"]
            else limit
        )
        tasks.append(
            asyncio.create_task(
                supported_sites[site]["website"]().search(query, page=1, limit=limit)
            )
        )
    results = await asyncio.gather(*tasks)
    for res in results:
        if res and len(res["data"]) > 0:
            for torrent in res["data"]:
                combo["data"].append(torrent)
            total_torrents_overall = total_torrents_overall + res["total"]
    combo["time"] = time.time() - start_time
    combo["total"] = total_torrents_overall
    return combo


@app.get("/api/all/trending")
async def get_all_trending(limit: Optional[int] = 0):
    start_time = time.time()
    sites_list = [
        site
        for site in supported_sites.keys()
        if supported_sites[site]["trending_available"] and supported_sites[site]["website"]
    ]
    tasks = []
    combo = {"data": []}
    total_torrents_overall = 0
    for site in sites_list:
        limit = (
            supported_sites[site]["limit"]
            if limit == 0 or limit > supported_sites[site]["limit"]
            else limit
        )
        tasks.append(
            asyncio.create_task(
                supported_sites[site]["website"]().trending(
                    category=None, page=1, limit=limit
                )
            )
        )
    results = await asyncio.gather(*tasks)
    for res in results:
        if res and len(res["data"]) > 0:
            for torrent in res["data"]:
                combo["data"].append(torrent)
            total_torrents_overall = total_torrents_overall + res["total"]
    combo["time"] = time.time() - start_time
    combo["total"] = total_torrents_overall
    return combo


@app.get("/api/sites")
async def get_all_supported_sites():
    sites_list = [
        site
        for site in supported_sites.keys()
        if supported_sites[site]["website"]
    ]
    return {"supported_sites": sites_list}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
