import json
import time
from selenium.common import WebDriverException

def retrieve_phone_code(driver) -> str:
    """Returns a phone confirmation code as a string."""
    code = None
    for _ in range(10):
        try:
            logs = [
                log["message"] for log in driver.get_log('performance')
                if log.get("message") and 'api/v1/number?number' in log.get("message")
            ]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue

        if code:
            return code

    raise Exception("No phone confirmation code was found.\n"
                    "Use 'retrieve_phone_code' only after requesting the code in your application.")
