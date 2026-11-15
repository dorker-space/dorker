"""BrighterMonday: the job board of Kenya and Uganda."""

from __future__ import annotations

from typing import ClassVar

from src.scraping.models import ATSType
from src.scraping.scrapers._listings_board import ListingsBoardScraper
from src.scraping.scrapers.base import ScraperRegistry


@ScraperRegistry.register(ATSType.BRIGHTERMONDAY)
class BrighterMondayScraper(ListingsBoardScraper):
    """BrighterMonday: ``ke``, ``ug``, or every site."""

    ats = ATSType.BRIGHTERMONDAY
    sites: ClassVar[dict[str, tuple[str, str]]] = {
        "ke": ("www.brightermonday.co.ke", "Kenya"),
        "ug": ("www.brightermonday.co.ug", "Uganda"),
    }
