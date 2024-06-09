import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestSecurityEventsAPI:
    base_url = "https://api.example.com/security-events/{user_id}"

    @pytest.fixture(scope="class")
    def session(self):
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
        session.mount('https://', HTTPAdapter(max_retries=retries))
        logger.info("Setup: Created session with retry mechanism")
        yield session
        session.close()
        logger.info("Teardown: Session closed")

    def test_api_normal_behavior(self, session):
        user_id = "valid_user_id"
        response = session.get(self.base_url.format(user_id=user_id))
        logger.info(f"GET /security-events/{user_id} response status: {response.status_code}")
        logger.info(f"Response data: {response.json()}")

        assert response.status_code == 200, "Expected status code 200"
        response_json = response.json()
        assert "customer_email" in response_json, "Response should contain customer_email"
        assert "number_of_events" in response_json, "Response should contain number_of_events"
        assert "events" in response_json, "Response should contain events"
        for event in response_json["events"]:
            assert "ip" in event, "Event should contain ip"
            assert "time" in event, "Event should contain time"
            assert "event_type" in event, "Event should contain event_type"

    def test_api_invalid_user_id(self, session):
        user_id = "invalid_user_id"
        response = session.get(self.base_url.format(user_id=user_id))
        logger.info(f"GET /security-events/{user_id} response status: {response.status_code}")
        logger.info(f"Response data: {response.json()}")

        assert response.status_code == 404, "Expected status code 404 for invalid user ID"
        response_json = response.json()
        assert "error" in response_json, "Response should contain error message"

    def test_api_intermittent_issue(self, session):
        user_id = "valid_user_id"
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = session.get(self.base_url.format(user_id=user_id))
                if response.status_code == 200:
                    logger.info(f"GET /security-events/{user_id} response status: {response.status_code}")
                    logger.info(f"Response data: {response.json()}")
                    assert response.status_code == 200, "Expected status code 200"
                    break
            except requests.exceptions.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    pytest.fail(f"API call failed after {max_retries} attempts")
