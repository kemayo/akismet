==========
Akismet.py
==========

Intro
-----

This was written back in 2005, the day the Akismet API docs were
released. So it has the distinction of being the first third-party
library for Akismet... which counts for little.

I wrote it more or less because I was learning Python at the time, and
it was a project that caught my interest.

It's a really simple wrapper around the API.

Usage
-----

>>> import akismet
>>> akismet.USERAGENT = "MyApplication/MyVersion"
>>> ak = akismet.Akismet(my_api_key, "http://www.example.com")
>>> ak.comment_check("127.0.0.1", "Mozilla/5.0 (...) Gecko/20051111 Firefox/1.5",
        comment_content="VIAGRA! LOTS OF VIAGRA!")
True

