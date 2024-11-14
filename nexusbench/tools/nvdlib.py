# pylint: disable=unused-argument


def searchCVE(
    cpeName=None,
    cveId=None,
    cvssV2Metrics=None,
    cvssV2Severity=None,
    cvssV3Metrics=None,
    cvssV3Severity=None,
    cweId=None,
    hasCertAlerts=None,
    hasCertNotes=None,
    hasOval=None,
    isVulnerable=None,
    keywordExactMatch=None,
    keywordSearch=None,
    lastModStartDate=None,
    lastModEndDate=None,
    noRejected=None,
    pubStartDate=None,
    pubEndDate=None,
    sourceIdentifier=None,
    versionEnd=None,
    versionEndType=None,
    versionStart=None,
    versionStartType=None,
    virtualMatchString=None,
    limit=None,
    delay=None,
    key=None,
    verbose=None,
):
    """
    Build and send GET request then return list of objects containing a collection of CVEs. For more information on the parameters available, please visit https://nvd.nist.gov/developers/vulnerabilities

    When providing ANY date time strings, please also specify the time. Such as: "00:00" suffix to the end of every datetime string. So, if you're generating a date, make sure to say "2023-03-01 00:00".

    cpeName (str): Please do not confuse this with keywordSearch; this requires the argument to start with "cpe", whereas the keywordSearch argument allows for arbitrary keywords. This value will be compared agains the CPE Match Criteria within a CVE applicability statement. (i.e. find the vulnerabilities attached to that CPE). Partial match strings are allowed.
    cveId (str): Please pass in a string integer, like "1" or "30". Returns a single CVE that already exists in the NVD.
    cvssV2Metrics (str): This parameter returns only the CVEs that match the provided CVSSv2 vector string. Either full or partial vector strings may be used. This parameter cannot be used in requests that include cvssV3Metrics.
    cvssV2Severity (str): Find vulnerabilities having a LOW, MEDIUM, or HIGH version 2 severity.
    cvssV3Metrics (str): This parameter returns only the CVEs that match the provided CVSSv3 vector string. Either full or partial vector strings may be used. This parameter cannot be used in requests that include cvssV2Metrics.
    cvssV3Severity (str): Find vulnerabilities having a LOW, MEDIUM, HIGH, or CRITICAL version 3 severity.
    cweId (str): Filter collection by CWE (Common Weakness Enumeration) ID. You can find a list at https://cwe.mitre.org/. A CVE can have multiple CWE IDs assigned to it. Examples include "CVE-34".
    hasCertAlerts (bool): Returns CVE that contain a Technical Alert from US-CERT.
    hasCertNotes (bool): Returns CVE that contain a Vulnerability Note from CERT/CC.
    hasOval (bool): Returns CVE that contain information from MITRE's Open Vulnerability and Assessment Language (OVAL) before this transitioned to the Center for Internet Security (CIS).
    isVulnerable (bool): Returns CVE associated with a specific CPE, where the CPE is also considered vulnerable. REQUIRES cpeName parameter. isVulnerable is not compatible with virtualMatchString parameter.
    keywordExactMatch (bool): When keywordSearch is used along with keywordExactmatch, it will search the NVD for CVEs containing exactly what was passed to keywordSearch. REQUIRES keywordSearch.
    keywordSearch (str): Searches CVEs where a word or phrase is found in the current description. If passing multiple keywords with a space character in between then each word must exist somewhere in the description, not necessarily together unless keywordExactMatch=True is passedto searchCVE.
    lastModStartDate (str): Include the time, such as "2023-03-01 00:00". These parameters return only the CVEs that were last modified during the specified period. If a CVE has been modified more recently than the specified period, it will not be included in the response. If filtering by the last modified date, both lastModStartDate and lastModEndDate are REQUIRED. The maximum allowable range when using any date range parameters is 120 consecutive days. Example includes "2023-03-01 00:00".
    lastModEndDate (str, datetime obj): Include the time, such as "2023-03-01 00:00". Required if using lastModStartDate. Example includes "2023-03-01 00:00".
    noRejected (bool): Filters out all CVEs that are in a reject or rejected status. Searches without this parameter include rejected CVEs.
    pubStartDate (str,datetime obj): Include the time, such as "2023-03-01 00:00". These parameters return only the CVEs that were added to the NVD (i.e., published) during the specified period. If filtering by the published date, both pubStartDate and pubEndDate are REQUIRED. The maximum allowable range when using any date range parameters is 120 consecutive days. Example includes "2023-03-01 00:00".
    pubEndDate (str, datetime obj): Include the time, such as "2023-03-01 00:00". Required if using pubStartDate. Examples include "2023-03-01 00:00".
    sourceIdentifier (str): Returns CVE where the data source of the CVE is the value that is passed to sourceIdentifier.
    versionEnd (str): Must be combined with versionEndType and virtualMatchString. Returns only the CVEs associated with CPEs in specific version ranges.
    versionEndType (str): Must be combined with versionEnd and virtualMatchString. Valid values are including or excluding. Denotes to include the specified version in versionEnd, or exclude it.
    versionStart (str): Must be combined with versionStartType and virtualMatchString. Returns only CVEs with specific versions. Requests that include versionStart cannot include a version component in the virtualMatchString.
    versionStartType (str): Must be combined with versionStart and virtualMatchString. Valid values are including or excluding. Denotes to include the specified version in versionStart, or exclude it.
    virtualMatchString (str): A more broad filter compared to cpeName. The cpe match string that is passed to virtualMatchString is compared against the CPE Match Criteria present on CVE applicability statements.
    limit (int): Custom argument to limit the number of results of the search. Allowed any number between 1 and 2000.
    delay (int): Can only be used if an API key is provided. This allows the user to define a delay. The delay must be greater than 0.6 seconds. The NVD API recommends scripts sleep for atleast 6 seconds in between requests.
    key (str): NVD API Key. Allows for the user to define a delay. NVD recommends scripts sleep 6 seconds in between requests. If no valid API key is provided, requests are sent with a 6 second delay.
    verbose (bool): Prints the URL request for debugging purposes.
    """


def searchCPE(
    cpeNameId=None,
    cpeMatchString=None,
    keywordExactMatch=None,
    keywordSearch=None,
    lastModStartDate=None,
    lastModEndDate=None,
    limit=None,
    key=None,
    delay=None,
    verbose=None,
):
    """
    Build and send GET request then return list of objects containing a collection of CPEs.

    When providing ANY date time strings, please also specify the time. Such as: "00:00" suffix to the end of every datetime string. So, if you're generating a date, make sure to say "2023-03-01 00:00".

    cpeNameId (str) – Returns a specific CPE record using its UUID. If a correctly formatted UUID is passed but it does not exist, it will return empty results. The UUID is the cpeNameId value when searching CPE.
    cpeMatchString (str) – Use a partial CPE name to search for other CPE names.
    keywordExactMatch (bool) – Searches metadata within CPE title and reference links for an exact match of the phrase or word passed to it. Must be included with keywordSearch.
    keywordSearch (str) – Returns CPE records where a word or phrase is found in the metadata title or reference links. Space characters act as an AND statement.
    lastModStartDate (str) - Include the time!! CPE last modification start date. Maximum 120 day range. A start and end date is required. All times are in UTC 00:00. A datetime object or string can be passed as a date. NVDLib will automatically parse the datetime object into the correct format. String Example: ‘2020-06-28 00:00’
    lastModEndDate (str) – Include the time!! CPE last modification end date. Maximum 120 day range. Must be included with lastModStartDate. String Example: ‘2020-06-28 00:00’.
    limit (int) – Limits the number of results of the search.
    key (str) – NVD API Key. Allows for a request every 0.6 seconds instead of 6 seconds.
    delay – Can only be used if an API key is provided. The amount of time to sleep in between requests. Must be a value above 0.6 seconds if an API key is present. delay is set to 6 seconds if no API key is passed.
    verbose (bool) – Prints the URL request for debugging purposes.
    """


searchCVE_json = {
    "name": "searchCVE",
    "description": """Build and send GET request then return list of objects containing a collection of CVEs. For more information on the parameters available, please visit https://nvd.nist.gov/developers/vulnerabilities\n\nWhen providing ANY date time strings, please also specify the time. Such as: "00:00" suffix to the end of every datetime string. So, if you're generating a date, make sure to say '2023-03-01 00:00'.""",
    "parameters": {
        "type": "object",
        "properties": {
            "cpeName": {
                "type": "string",
                "description": """Please do not confuse this with keywordSearch; this requires the argument to start with "cpe", whereas the keywordSearch argument allows for arbitrary keywords. This value will be compared agains the CPE Match Criteria within a CVE applicability statement. (i.e. find the vulnerabilities attached to that CPE). Partial match strings are allowed.""",
            },
            "cveId": {
                "type": "string",
                "description": """Please pass in a string integer, like "1" or "30". Returns a single CVE that already exists in the NVD.""",
            },
            "cvssV2Metrics": {
                "type": "string",
                "description": """This parameter returns only the CVEs that match the provided CVSSv2 vector string. Either full or partial vector strings may be used. This parameter cannot be used in requests that include cvssV3Metrics.""",
            },
            "cvssV2Severity": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH"],
                "description": """Find vulnerabilities having a LOW, MEDIUM, or HIGH version 2 severity.""",
            },
            "cvssV3Metrics": {
                "type": "string",
                "description": """This parameter returns only the CVEs that match the provided CVSSv3 vector string. Either full or partial vector strings may be used. This parameter cannot be used in requests that include cvssV2Metrics.""",
            },
            "cvssV3Severity": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
                "description": """Find vulnerabilities having a LOW, MEDIUM, HIGH, or CRITICAL version 3 severity.""",
            },
            "cweId": {
                "type": "string",
                "description": """Filter collection by CWE (Common Weakness Enumeration) ID. You can find a list at https://cwe.mitre.org/. A CVE can have multiple CWE IDs assigned to it. Examples include "CVE-34".""",
            },
            "hasCertAlerts": {
                "type": "boolean",
                "description": """Returns CVE that contain a Technical Alert from US-CERT.""",
            },
            "hasCertNotes": {
                "type": "boolean",
                "description": """Returns CVE that contain a Vulnerability Note from CERT/CC.""",
            },
            "hasOval": {
                "type": "boolean",
                "description": """Returns CVE that contain information from MITRE's Open Vulnerability and Assessment Language (OVAL) before this transitioned to the Center for Internet Security (CIS).""",
            },
            "isVulnerable": {
                "type": "boolean",
                "description": """Returns CVE associated with a specific CPE, where the CPE is also considered vulnerable. REQUIRES cpeName parameter. isVulnerable is not compatible with virtualMatchString parameter.""",
            },
            "keywordExactMatch": {
                "type": "boolean",
                "description": """When keywordSearch is used along with keywordExactmatch, it will search the NVD for CVEs containing exactly what was passed to keywordSearch. REQUIRES keywordSearch.""",
            },
            "keywordSearch": {
                "type": "string",
                "description": """Searches CVEs where a word or phrase is found in the current description. If passing multiple keywords with a space character in between then each word must exist somewhere in the description, not necessarily together unless keywordExactMatch=True is passedto searchCVE.""",
            },
            "lastModStartDate": {
                "type": "string",
                "description": """Include the time, such as "2023-03-01 00:00". These parameters return only the CVEs that were last modified during the specified period. If a CVE has been modified more recently than the specified period, it will not be included in the response. If filtering by the last modified date, both lastModStartDate and lastModEndDate are REQUIRED. The maximum allowable range when using any date range parameters is 120 consecutive days. Example includes "2023-03-01 00:00".""",
            },
            "lastModEndDate": {
                "type": "string",
                "description": """Include the time, such as "2023-03-01 00:00". Required if using lastModStartDate. Example includes "2023-03-01 00:00".""",
            },
            "noRejected": {
                "type": "boolean",
                "description": """Filters out all CVEs that are in a reject or rejected status. Searches without this parameter include rejected CVEs.""",
            },
            "pubStartDate": {
                "type": "string",
                "description": """Include the time, such as "2023-03-01 00:00". These parameters return only the CVEs that were added to the NVD (i.e., published) during the specified period. If filtering by the published date, both pubStartDate and pubEndDate are REQUIRED. The maximum allowable range when using any date range parameters is 120 consecutive days. Example includes "2023-03-01 00:00".""",
            },
            "pubEndDate": {
                "type": "string",
                "description": """Include the time, such as "2023-03-01 00:00". Required if using pubStartDate. Examples include "2023-03-01 00:00".""",
            },
            "sourceIdentifier": {
                "type": "string",
                "description": """Returns CVE where the data source of the CVE is the value that is passed to sourceIdentifier.""",
            },
            "versionEnd": {
                "type": "string",
                "description": """Must be combined with versionEndType and virtualMatchString. Returns only the CVEs associated with CPEs in specific version ranges.""",
            },
            "versionEndType": {
                "type": "string",
                "enum": ["including", "excluding"],
                "description": """Must be combined with versionEnd and virtualMatchString. Valid values are including or excluding. Denotes to include the specified version in versionEnd, or exclude it.""",
            },
            "versionStart": {
                "type": "string",
                "description": """Must be combined with versionStartType and virtualMatchString. Returns only CVEs with specific versions. Requests that include versionStart cannot include a version component in the virtualMatchString.""",
            },
            "versionStartType": {
                "type": "string",
                "enum": ["including", "excluding"],
                "description": """Must be combined with versionStart and virtualMatchString. Valid values are including or excluding. Denotes to include the specified version in versionStart, or exclude it.""",
            },
            "virtualMatchString": {
                "type": "string",
                "description": """A more broad filter compared to cpeName. The cpe match string that is passed to virtualMatchString is compared against the CPE Match Criteria present on CVE applicability statements.""",
            },
            "limit": {
                "type": "integer",
                "description": """Custom argument to limit the number of results of the search. Allowed any number between 1 and 2000.""",
            },
            "delay": {
                "type": "integer",
                "description": """Can only be used if an API key is provided. This allows the user to define a delay. The delay must be greater than 0.6 seconds. The NVD API recommends scripts sleep for atleast 6 seconds in between requests.""",
            },
            "key": {
                "type": "string",
                "description": """NVD API Key. Allows for the user to define a delay. NVD recommends scripts sleep 6 seconds in between requests. If no valid API key is provided, requests are sent with a 6 second delay.""",
            },
            "verbose": {
                "type": "boolean",
                "description": """Prints the URL request for debugging purposes.""",
            },
        },
        "required": [],
    },
}
searchCPE_json = {
    "name": "searchCPE",
    "description": """Build and send GET request then return list of objects containing a collection of CPEs.\n\nWhen providing ANY date time strings, please also specify the time. Such as: "00:00" suffix to the end of every datetime string. So, if you're generating a date, make sure to say "2023-03-01 00:00".""",
    "parameters": {
        "type": "object",
        "properties": {
            "cpeNameId": {
                "type": "string",
                "description": "Returns a specific CPE record using its UUID. If a correctly formatted UUID is passed but it does not exist, it will return empty results. The UUID is the cpeNameId value when searching CPE.",
            },
            "cpeMatchString": {
                "type": "string",
                "description": "Use a partial CPE name to search for other CPE names.",
            },
            "keywordExactMatch": {
                "type": "boolean",
                "description": "Searches metadata within CPE title and reference links for an exact match of the phrase or word passed to it. Must be included with keywordSearch.",
            },
            "keywordSearch": {
                "type": "string",
                "description": "Returns CPE records where a word or phrase is found in the metadata title or reference links. Space characters act as an AND statement.",
            },
            "lastModStartDate": {
                "type": "string",
                "description": """Include the time!! CPE last modification start date. Maximum 120 day range. A start and end date is required. All times are in UTC 00:00. A datetime object or string can be passed as a date. NVDLib will automatically parse the datetime object into the correct format. String Example: ‘2020-06-28 00:00’""",
            },
            "lastModEndDate": {
                "type": "string",
                "description": """Include the time!! CPE last modification end date. Maximum 120 day range. Must be included with lastModStartDate. String Example: ‘2020-06-28 00:00’.""",
            },
            "limit": {
                "type": "integer",
                "description": """Limits the number of results of the search.""",
            },
            "key": {
                "type": "string",
                "description": """NVD API Key. Allows for a request every 0.6 seconds instead of 6 seconds.""",
            },
            "delay": {
                "type": "integer",
                "description": """Can only be used if an API key is provided. The amount of time to sleep in between requests. Must be a value above 0.6 seconds if an API key is present. delay is set to 6 seconds if no API key is passed.""",
            },
            "verbose": {
                "type": "boolean",
                "description": """Prints the URL request for debugging purposes.""",
            },
        },
        "required": [],
    },
}
