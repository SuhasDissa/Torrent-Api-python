<h2 align='center'>Torrents Api ✨</h2>
<p align="center">
<a href="https://github.com/Ryuk-me"><img title="Original Author" src="https://img.shields.io/badge/OriginalAuthor-Ryuk--me-red.svg?style=for-the-badge&logo=github"></a>
</p>

<p align="center">
<a href="https://github.com/Suhasdissa"><img title="Followers" src="https://img.shields.io/github/followers/Suhasdissa?color=teal&style=flat-square"></a>
<a href="https://github.com/Suhasdissa/Torrent-Api-python/stargazers/"><img title="Stars" src="https://img.shields.io/github/stars/Suhasdissa/Torrent-Api-python?color=brown&style=flat-square"></a>
<a href="https://github.com/Suhasdissa/Torrent-Api-python/network/members"><img title="Forks" src="https://img.shields.io/github/forks/Suhasdissa/Torrent-Api-python?color=lightgrey&style=flat-square"></a>
<a href="https://github.com/Suhasdissa/Torrent-Api-python/issues"><img title="issues" src="https://img.shields.io/github/issues/Suhasdissa/Torrent-Api-python?style=flat-square">
</a>
<img src='https://visitor-badge.glitch.me/badge?page_id=Suhasdissa.Torrent-Api-python'>
</p>

<p align="center">
<span style='font-size: 19px'>
An Unofficial API for <span style='font-weight:600;'>1337x</span>, <span style='font-weight:600;'>Piratebay</span>, <span style='font-weight:bold;'>Nyaasi</span>, <span style='font-weight:bold;'>Torlock</span>, <span style='font-weight:bold;'>Torrent Galaxy</span>, <span style='font-weight:600;'>Zooqle</span>, <span style='font-weight:600;'>Kickass</span>, <span style='font-weight:600;'>Bitsearch</span>, <span style='font-weight:600;'>MagnetDL, </span>Libgen, YTS, Limetorrent, TorrentFunk, Glodls, TorrentProject and YourBittorrent
</span>
</p>

---

## Installation

```sh

# Clone the repo
$ git clone https://github.com/Suhasdissa/Torrent-Api-python

# Install Depedencies
$ pip install -r requirements.txt

# Start
$ python main.py

```

## Supported Sites

|    Website     |     Keyword      |             Url              | Cloudfare |
|:--------------:|:----------------:|:----------------------------:|:---------:|
|     1337x      |     `1337x`      |      https://1337xx.to       |     ❌     |
| Torrent Galaxy |      `tgx`       |   https://torrentgalaxy.to   |     ❌     |
|    Torlock     |    `torlock`     |   https://www.torlock.com    |     ❌     |
|   PirateBay    |   `piratebay`    |  https://thepiratebay10.org  |     ❌     |
|     Nyaasi     |     `nyaasi`     |       https://nyaa.si        |     ❌     |
|     Zooqle     |     `zooqle`     |      https://zooqle.com      |     ❌     |
|    KickAss     |    `kickass`     |  https://kickasstorrents.to  |     ❌     |
|   Bitsearch    |   `bitsearch`    |     https://bitsearch.to     |     ❌     |
|    MagnetDL    |    `magnetdl`    |   https://www.magnetdl.com   |     ✅     |
|     Libgen     |     `libgen`     |      https://libgen.is       |     ❌     |
|      YTS       |      `yts`       |        https://yts.mx        |     ❌     |
|  Limetorrent   |  `limetorrent`   | https://www.limetorrents.pro |     ❌     |
|  TorrentFunk   |  `torrentfunk`   | https://www.torrentfunk.com  |     ❌     |
|     Glodls     |     `glodls`     |      https://glodls.to       |     ❌     |
| TorrentProject | `torrentproject` | https://torrentproject2.com  |     ❌     |
| YourBittorrent |      `ybt`       |  https://yourbittorrent.com  |     ❌     |

---

<details>
<summary style='font-size: 20px'><span style='font-size: 25px;font-weight:bold;'>Supported Methods and categories</span></summary>

<p>

```json

{
  "1337x": {
    "trending_available": true,
    "trending_category": true,
    "search_by_category": true,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "anime",
      "music",
      "games",
      "tv",
      "apps",
      "documentaries",
      "other",
      "xxx",
      "movies"
    ],
    "limit": 20
  },
  "torlock": {
    "trending_available": true,
    "trending_category": true,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "anime",
      "music",
      "games",
      "tv",
      "apps",
      "documentaries",
      "other",
      "xxx",
      "movies",
      "books",
      "images"
    ],
    "limit": 50
  },
  "zooqle": {
    "trending_available": false,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": false,
    "recent_category_available": false,
    "categories": [],
    "limit": 30
  },
  "magnetdl": {
    "trending_available": false,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "apps",
      "movies",
      "music",
      "games",
      "tv",
      "books"
    ],
    "limit": 40
  },
  "tgx": {
    "trending_available": true,
    "trending_category": true,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "anime",
      "music",
      "games",
      "tv",
      "apps",
      "documentaries",
      "other",
      "xxx",
      "movies",
      "books"
    ],
    "limit": 50
  },
  "nyaasi": {
    "trending_available": false,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": false,
    "categories": [],
    "limit": 50
  },
  "piratebay": {
    "trending_available": true,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "tv"
    ],
    "limit": 50
  },
  "bitsearch": {
    "trending_available": true,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": false,
    "recent_category_available": false,
    "categories": [],
    "limit": 50
  },
  "kickass": {
    "trending_available": true,
    "trending_category": true,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "anime",
      "music",
      "games",
      "tv",
      "apps",
      "documentaries",
      "other",
      "xxx",
      "movies",
      "books"
    ],
    "limit": 50
  },
  "libgen'": {
    "trending_available": false,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": false,
    "recent_category_available": false,
    "categories": [],
    "limit": 25
  },
  "yts": {
    "trending_available": true,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": false,
    "categories": [],
    "limit": 20
  },
  "limetorrent": {
    "trending_available": true,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "anime",
      "music",
      "games",
      "tv",
      "apps",
      "other",
      "movies",
      "books"
    ],
    "limit": 50
  },
  "torrentfunk": {
    "trending_available": true,
    "trending_category": true,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "anime",
      "music",
      "games",
      "tv",
      "apps",
      "xxx",
      "movies",
      "books"
    ],
    "limit": 50
  },
  "glodls": {
    "trending_available": true,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": false,
    "categories": [],
    "limit": 45
  },
  "torrentproject": {
    "trending_available": false,
    "trending_category": false,
    "search_by_category": false,
    "recent_available": false,
    "recent_category_available": false,
    "categories": [],
    "limit": 20
  },
  "ybt": {
    "trending_available": true,
    "trending_category": true,
    "search_by_category": false,
    "recent_available": true,
    "recent_category_available": true,
    "categories": [
      "anime",
      "music",
      "games",
      "tv",
      "apps",
      "xxx",
      "movies",
      "books",
      "pictures",
      "other"
    ],
    "limit": 20
  }
}
```

</p>
</details>

---

## API Endpoints

<details>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Supported sites list</span></summary>
<p>

> `api/sites`

</p>
</details>
<br>

<details>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search</span></summary>
<p>

> `api/search`

| Parameter | Required |  Type   | Default |                        Example                        |
|:---------:|:--------:|:-------:|:-------:|:-----------------------------------------------------:|
|   site    |    ✅     | string  |  None   |                `api/search?site=1337x`                |
|   query   |    ✅     | string  |  None   |        `api/search?site=1337x&query=avengers`         |
|   limit   |    ❌     | integer | Default |    `api/search?site=1337x&query=avengers&limit=20`    |
|   page    |    ❌     | integer |    1    | `api/search?site=1337x&query=avengers&limit=0&page=2` |

</p>
</details>
<br>

<details>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Trending</span></summary>
<p>

> `api/trending`

| Parameter | Required |  Type   | Default |                       Example                        |
|:---------:|:--------:|:-------:|:-------:|:----------------------------------------------------:|
|   site    |    ✅     | string  |  None   |              `api/trending?site=1337x`               |
|   limit   |    ❌     | integer | Default |          `api/trending?site=1337x&limit=10`          |
| category  |    ❌     | string  |  None   |    `api/trending?site=1337x&limit=0&category=tv`     |
|   page    |    ❌     | integer |    1    | `api/trending?site=1337x&limit=6&category=tv&page=2` |

</p>
</details>
<br>

<details>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Recent</span></summary>
<p>

> `api/recent`

| Parameter | Required |  Type   | Default |                       Example                       |
|:---------:|:--------:|:-------:|:-------:|:---------------------------------------------------:|
|   site    |    ✅     | string  |  None   |               `api/recent?site=1337x`               |
|   limit   |    ❌     | integer | Default |           `api/recent?site=1337x&limit=7`           |
| category  |    ❌     | string  |  None   |     `api/recent?site=1337x&limit=0&category=tv`     |
|   page    |    ❌     | integer |    1    | `api/recent?site=1337x&limit=15&category=tv&page=2` |

</p>
</details>
<br>

<details>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search By Category</span></summary>
<p>

> `api/category`

| Parameter | Required |  Type   | Default |                               Example                               |
|:---------:|:--------:|:-------:|:-------:|:-------------------------------------------------------------------:|
|   site    |    ✅     | string  |  None   |                      `api/category?site=1337x`                      |
|   query   |    ✅     | string  |  None   |              `api/category?site=1337x&query=avengers`               |
| category  |    ✅     | string  |  None   |      `api/category?site=1337x&query=avengers&category=movies`       |
|   limit   |    ❌     | integer | Default |  `api/category?site=1337x&query=avengers&category=movies&limit=10`  |
|   page    |    ❌     | integer |    1    | `api/category?site=1337x&query=avengers&category=tv&limit=0&page=2` |

</p>
</details>

<br>

<details>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Search from all sites</span></summary>
<p>

> `api/all/search`

| Parameter | Required |  Type   | Default |                 Example                 |
|:---------:|:--------:|:-------:|:-------:|:---------------------------------------:|
|   query   |    ✅     | string  |  None   |     `api/all/search?query=avengers`     |
|   limit   |    ❌     | integer | Default | `api/all/search?query=avengers&limit=5` |

<pre>Here <b>limit = 5</b> will get 5 results from each site.</pre>

> http://0.0.0.0:8080/api/all/search?query=avengers

> http://0.0.0.0:8080/api/all/search?query=avengers&limit=5

</details>

<br>

<details>
<summary style='font-size: 15px'><span style='font-size: 20px;font-weight:bold;'>Get trending from all sites</span></summary>
<p>

> `api/all/trending`

| Parameter | Required |  Type   | Default |          Example           |
|:---------:|:--------:|:-------:|:-------:|:--------------------------:|
|   limit   |    ❌     | integer | Default | `api/all/trending?limit=2` |

> http://0.0.0.0:8080/api/all/trending

> http://0.0.0.0:8080/api/all/trending?limit=2

</p>
</details>

---

<details>
<summary> See response</summary>
<p>

```json
{
  "data": [
    {
      "name": "Eternals.2021.1080p.WEBRip.DDP5.1.x264-NOGRP",
      "size": "5.6 GB",
      "date": "Jan. 11th '22",
      "seeders": "10872",
      "leechers": "6820",
      "url": "https://1337xx.to/torrent/5110260/Eternals-2021-1080p-WEBRip-DDP5-1-x264-NOGRP/",
      "uploader": "TheMorozko",
      "screenshot": [
        "https://checkmy.pictures/images/2022/01/11/32162343474810151667.jpg",
        "https://checkmy.pictures/images/2022/01/11/38515612831471833686.jpg",
        "https://checkmy.pictures/images/2022/01/11/71518482909886223945.jpg"
      ],
      "category": "Movies",
      "poster": "https://1337xx.to/img/movie/Eternals-2021.jpg",
      "magnet": "magnet:?xt=urn:btih:A2AD2A669250A014BED19919E6C386DD4F82A883&dn=Eternals.2021.1080p.WEBRip.DDP5.1.x264-NOGRP&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2950%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2870%2Fannounce&tr=udp%3A%2F%2Ftracker.tallpenguin.org%3A15720%2Fannounce&tr=udp%3A%2F%2Ftracker.thinelephant.org%3A12780%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce",
      "hash": "A2AD2A669250A014BED19919E6C386DD4F82A883"
    }
  ],
  "current_page": 1,
  "total_pages": 7,
  "time": 1.276763677597046,
  "total": 20
}
```

</p>
</details>