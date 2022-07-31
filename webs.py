import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()


#OUTPUT
.
/articles/CAIiELv02OIr_9gI10ZrRjxHaK8qGQgEKhAIACoHCAowyNj6CjDyiPICMJyFxQU?uo=CAUicWh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3Mvam9lLWJpZGVuLXRlc3RzLXBvc2l0aXZlLWZvci1jb3ZpZC0xOS1hZ2Fpbi13aWxsLWlzb2xhdGUtd2hpdGUtaG91c2UtcGh5c2ljaWFuLXNheXMv0gEA&hl=en-US&gl=US&ceid=US%3Aen

./articles/CAIiELv02OIr_9gI10ZrRjxHaK8qGQgEKhAIACoHCAowyNj6CjDyiPICMJyFxQU?uo=CAUicWh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3Mvam9lLWJpZGVuLXRlc3RzLXBvc2l0aXZlLWZvci1jb3ZpZC0xOS1hZ2Fpbi13aWxsLWlzb2xhdGUtd2hpdGUtaG91c2UtcGh5c2ljaWFuLXNheXMv0gEA&hl=en-US&gl=US&ceid=US%3Aen

./articles/CAIiELv02OIr_9gI10ZrRjxHaK8qGQgEKhAIACoHCAowyNj6CjDyiPICMJyFxQU?uo=CAUicWh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3Mvam9lLWJpZGVuLXRlc3RzLXBvc2l0aXZlLWZvci1jb3ZpZC0xOS1hZ2Fpbi13aWxsLWlzb2xhdGUtd2hpdGUtaG91c2UtcGh5c2ljaWFuLXNheXMv0gEA&hl=en-US&gl=US&ceid=US%3Aen

./articles/CCAiC2ZFYV9KTGg5OHpVmAEB?hl=en-US&gl=US&ceid=US%3Aen

./articles/CCAiC2ZFYV9KTGg5OHpVmAEB?hl=en-US&gl=US&ceid=US%3Aen

./articles/CBMiTmh0dHBzOi8vd3d3LmNubi5jb20vMjAyMi8wNy8zMC9wb2xpdGljcy9qb2UtYmlkZW4tY292aWQtMTktcG9zaXRpdmUvaW5kZXguaHRtbNIBUmh0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjIvMDcvMzAvcG9saXRpY3Mvam9lLWJpZGVuLWNvdmlkLTE5LXBvc2l0aXZlL2luZGV4Lmh0bWw?hl=en-US&gl=US&ceid=US%3Aen

./articles/CBMiTmh0dHBzOi8vd3d3LmNubi5jb20vMjAyMi8wNy8zMC9wb2xpdGljcy9qb2UtYmlkZW4tY292aWQtMTktcG9zaXRpdmUvaW5kZXguaHRtbNIBUmh0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjIvMDcvMzAvcG9saXRpY3Mvam9lLWJpZGVuLWNvdmlkLTE5LXBvc2l0aXZlL2luZGV4Lmh0bWw?hl=en-US&gl=US&ceid=US%3Aen

./articles/CAIiECvsEmiCyf1WytuDyMgv-NwqGQgEKhAIACoHCAowwL2ICzCckocDMMaPqQY?uo=CAUiVGh0dHBzOi8vd3d3LmZveG5ld3MuY29tL3BvbGl0aWNzL2JpZGVuLXRlc3RzLXBvc2l0aXZlLWNvdmlkLXJlYm91bmQtY2FzZS1kb2N0b3Itc2F5c9IBAA&hl=en-US&gl=US&ceid=US%3Aen

./articles/CAIiECvsEmiCyf1WytuDyMgv-NwqGQgEKhAIACoHCAowwL2ICzCckocDMMaPqQY?uo=CAUiVGh0dHBzOi8vd3d3LmZveG5ld3MuY29tL3BvbGl0aWNzL2JpZGVuLXRlc3RzLXBvc2l0aXZlLWNvdmlkLXJlYm91bmQtY2FzZS1kb2N0b3Itc2F5c9IBAA&hl=en-US&gl=US&ceid=US%3Aen
