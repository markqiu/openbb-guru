import pytest
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.mark.record_http
def test_fmp_senate_trading_fetcher(credentials=test_credentials):
    """Test FMP senate trading fetcher."""
    params = {
        "symbol": "AAPL,MSFT",
    }

    fetcher = FMPSenateTradingFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_senate_trading_rss_feed_fetcher(credentials=test_credentials):
    """Test FMP senate trading rss feed fetcher."""
    params = {
        "page": 0,
    }

    fetcher = FMPSenateTradingRSSFeedFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_house_disclosure_fetcher(credentials=test_credentials):
    """Test FMP House Disclosure fetcher."""
    params = {
        "symbol": "AAPL,MSFT",
    }

    fetcher = FMPHouseDisclosureFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_house_disclosure_fetcher(credentials=test_credentials):
    """Test FMP House Disclosure rss feed fetcher."""
    params = {
        "page": 0,
    }

    fetcher = FMPHouseDisclosureRSSFeedFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
