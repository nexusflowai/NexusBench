# pylint: disable=unused-argument,redefined-builtin
import random
import datetime

random.seed(42)

# Extended Mock Data
mock_db = {
    "domains": {
        "example.com": {
            "report": {"last_analysis_date": 1596230400},
            "related_threat_actors": [
                {
                    "name": "Actor1",
                    "source_region": "North America",
                    "last_modification_date": 1609459200,
                },
                {
                    "name": "Actor2",
                    "source_region": "Europe",
                    "last_modification_date": 1612137600,
                },
            ],
            "historical_ssl_certificates": [
                {"valid": True, "issuer": "Trusty CA", "expiration_date": "2030-01-01"},
                {"valid": False, "issuer": "Shady CA", "expiration_date": "2020-01-01"},
            ],
            "caa_records": ["Record1", "Record2"],
            "communicating_files": ["file1.exe", "file2.exe"],
            "graphs": ["graph1", "graph2"],
            "related_objects": ["object1", "object2"],
            "comments": ["Good domain", "Secure and safe"],
            "urls": ["https://www.example.com/info", "https://www.example.com/contact"],
            "subdomains": ["sub.example.com", "test.example.com"],
            "parent": "com",
            "resolutions": [
                {
                    "resolution_id": "res0",
                    "resolved_to": "192.168.1.1",
                    "last_resolved": "2023-08-01",
                },
                {
                    "resolution_id": "res1",
                    "resolved_to": "192.168.1.2",
                    "last_resolved": "2023-08-02",
                },
            ],
            "mx_records": ["mx1.mailhost.com", "mx2.mailhost.com"],
            "communicating_files": ["commfile1.exe", "commfile2.exe", "commfile3.exe"],
        },
        "example1.com": {
            "comments": ["Free domain", "Secure and safe"],
        },
        "test.com": {"comments": ["This is a testing domain", "Reserved for QA"]},
        "testsite.org": {
            "comments": [
                "This is a testing domain for organisations",
                "Reserved for QA",
            ]
        },
        "testsite.com": {
            "comments": ["This is a commercial testing domain", "Reserved for QA"],
            "immediate_parent": "com",
        },
        "xyz.com": {"immediate_parent": "com", "comments": ["Random domain"]},
        "abc.com": {"comments": ["Broadcast television and radio network"]},
        "lmn.com": {"comments": ["Random domain", "LMN"]},
        "stackoverflow.com": {
            "comments": ["A question-and-answer website for computer programmers"]
        },
        "github.com": {"comments": ["This domain is for software development"]},
        "examplesite.com": {"comments": ["Example site for hosting"]},
        "hackers.com": {
            "related_threat_actors": [
                {
                    "name": "CyberSyndicate",
                    "source_region": "Unknown",
                    "last_modification_date": 1650000000,
                },
                {
                    "name": "DataHeistGroup",
                    "source_region": "Global",
                    "last_modification_date": 1660000000,
                },
            ]
        },
    },
    "ip_addresses": {
        "192.168.1.1": {
            "votes": {"yes": 10, "no": 5},
            "comments": ["Responsive IP", "No downtime observed."],
            "related_threat_actors": [
                {
                    "name": "MaliciousGroupA",
                    "source_region": "Australia",
                    "last_modification_date": 1622068801,
                },
                {
                    "name": "ExploitNetX",
                    "source_region": "Europe",
                    "last_modification_date": 1625068800,
                },
            ],
        },
        "192.0.2.0": {
            "comments": ["Frequently used in DDoS attacks", "Under surveillance"],
            "related_threat_actors": [
                {
                    "name": "MaliciousGroupA",
                    "source_region": "Asia",
                    "last_modification_date": 1625068800,
                },
                {
                    "name": "ExploitNet",
                    "source_region": "Europe",
                    "last_modification_date": 1635724800,
                },
            ],
        },
        "152.678.234.60": {
            "comments": ["Often flagged for suspicious activities", "High risk IP"]
        },
        "192.168.1.2": {
            "related_threat_actors": [],
            "comments": ["Low traffic, minimal security incidents."],
        },
        "176.762.91.012": {
            "report": {"last_analysis_date": 1640995200},
            "comments": ["Unknown traffic patterns observed."],
            "votes": {"yes": 16, "no": 2},
        },
        "196.84.239.213": {
            "comments": [
                "Periodic pings observed, possibly for keeping connections alive."
            ]
        },
        "241.342.56.78": {"comments": ["Recently listed on a watch list."]},
        "172.16.254.1": {"comments": ["Internal IP, used for testing environments."]},
        "198.51.100.0": {"comments": ["No significant findings."]},
        "253.451.46.89": {
            "comments": ["Infrequent connections, low risk."],
            "historical_ssl_certificates": [
                {"valid": True, "issuer": "Trusty CA", "expiration_date": "2030-05-01"},
                {"valid": False, "issuer": "Shady CA", "expiration_date": "2020-06-01"},
            ],
        },
        "34.74.55.1": {
            "related_threat_actors": [
                {"name": "HackerX", "source_region": "North America"}
            ],
            "urls": ["http://34.74.55.1/info", "http://34.74.55.1/stats"],
            "comments": ["Monitored by multiple agencies."],
        },
        "12.345.678.90": {"comments": ["IP address not resolving, possibly inactive."]},
    },
}


def get_random_object_from_list(list_of_objects):
    """
    This function selects and returns a random object from a list of objects. It is designed to handle any list length, including empty lists.

    Args:
    - list_of_objects: list, required, List containing objects from which the function will pick out a random object.
    """
    if list_of_objects:
        return random.choice(list_of_objects)
    return None


def get_first_object_from_list(list_of_objects):
    """
    Retrieves the first object from a given list. If the list is empty, it return `None`.

    Args:
    - list_of_objects: list, required, List containing objects from which the function will pick out the first object.
    """
    if list_of_objects:
        return list_of_objects[0]
    return None


def calculate_sum_of_numbers(num1, num2):
    """
    Computes the sum of two numbers provided. Input numbers can be either integer or floating-point values.

    Args:
    - num1: Integer or Float, required, The first number
    - num2: Integer or Float, required, The second number
    """
    return num1 + num2


def extract_resolution_date(dns_res_obj):
    """
    Extracts the date of DNS resolution from a DNS resolution object. The date is returned as a Unix timestamp.

    Args:
    - dns_res_obj: object, required, The DNS resolution object from which the date of resolution is to be extracted.
    """
    return dns_res_obj.get("resolution_date")


def count_items_in_list(input_list):
    """
    This function takes a list as an input and returns the number of items present in the list.

    Args:
    - input_list: list, required, List whose items are to be counted
    """
    return len(input_list)


def vt_get_majority_vote(votes):
    """
    This function takes a dictionary of votes returns the name with the majority votes. If the votes are equal, it will return the first encountered key in the dictionary.

    Args:
    - votes: dictionary, required, dictionary of votes
    """
    if votes:
        return max(votes, key=votes.get)
    return None


def vt_get_multiple_domain_reports(domains, x_apikey):
    """
    Retrieves reports for a list of domains provided. For each domain in the list, it requests the collected information regarding that domain from VirusTotal.

    Args:
    - domains: list of strings, required, A list of Domain names
    - x_apikey: string, required, Your API key
    """
    return {domain: {"report_info": f"Report for {domain}"} for domain in domains}


def vt_get_comments_on_multiple_domains(domains, x_apikey, limit=None, cursor=None):
    """
    This function will retrieve comments for each specified domain in the given list.

    Args:
    - domains, list of strings, required, List of domain names
    - x_apikey, string, required, Your API key
    - limit, int32, optional, Maximum number of comments to retrieve for each domain
    - cursor, string, optional, Continuation cursor
    """
    comments = {}
    for domain in domains:
        if domain in mock_db["domains"]:
            comments[domain] = (
                mock_db["domains"][domain]["comments"][:limit]
                if limit
                else mock_db["domains"][domain]["comments"]
            )
        else:
            comments[domain] = ["Domain not found"]
    return comments


def vt_get_last_analysis_date_from_report(report):
    """
    This function retrieves the last analysis date from the domain report collected by VirusTotal. The returned date is in Unix timestamp format.

    Args:
    - report: dict, required, The domain report collected by vt_get_domain_report function.
    """
    return report.get("last_analysis_date")


def vt_is_date_within_range(timestamp, start=None, end=None):
    """
    Checks if a given Unix timestamp is within a specified date range. The range is specified by 'start' and 'end' dates formatted as 'YYYY/MM/DD'. It's permissible for only one of 'start' or 'end' to be present in the function call. If 'start' is not provided, the function checks if the timestamp is earlier than or equal to the 'end' date. Similarly, If 'end' is not provided, the function checks if the timestamp is later than or equal to the 'start' date.

    Args:
    - timestamp: int, required, Unix timestamp
    - start: string, optional, Start of the date range in 'YYYY/MM/DD' format
    - end: string, optional, End of the date range in 'YYYY/MM/DD' format
    """
    if not timestamp:
        return False
    date = datetime.datetime.fromtimestamp(timestamp)
    start_date = (
        datetime.datetime.strptime(start, "%Y/%m/%d")
        if start and len(start) == 10
        else None
    )
    end_date = (
        datetime.datetime.strptime(end, "%Y/%m/%d") if end and len(end) == 10 else None
    )
    return (not start_date or date >= start_date) and (not end_date or date <= end_date)


def convert_unix_timestamp_to_date(unix_timestamp):
    """
    Converts a UNIX timestamp to a human-readable date in the format 'YYYY/MM/DD'.

    Args:
    - unix_timestamp: integer, required, The UNIX timestamp to be converted.
    """
    return datetime.datetime.fromtimestamp(unix_timestamp).strftime("%Y/%m/%d")


def vt_get_threat_actors_latest_modification_date(threat_actor_objects, x_apikey):
    """
    This function retrieves the latest modification date from a list of threat actor objects. It iterates through each threat actor object, checks its modification date, and returns the most recent modification date.

    Args:
    - threat_actor_objects: list of objects, required, A list of threat actor objects.
    - x_apikey: string, required, Your API key.
    """
    if threat_actor_objects:
        return max(
            actor.get("last_modification_date", 0) for actor in threat_actor_objects
        )
    return 0


def vt_get_threat_actors_main_source_region(threat_actors, x_apikey):
    """
    This function takes a list of threat actor objects and returns the primary source region among them. Each threat actor object has an attribute 'source region', and the function analyses this attribute across all objects to determine and return the most common source region, deemed as the 'main' source region.

    Args:
    - threat_actors: list, required, List of threat actor objects
    - x_apikey: string, required, Your API key.
    """
    if threat_actors:
        regions = [
            actor["source_region"]
            for actor in threat_actors
            if "source_region" in actor
        ]
        if regions:
            return max(set(regions), key=regions.count)
    return "No data available"


def vt_validate_historical_ssl_certificates(historical_ssl_certificates, x_apikey):
    """
    This function takes historical SSL certificates as input and checks if there is at least one valid SSL certificate present inside the provided historical data. It validates the SSL certificate by checking whether it is not expired and its issuing authority is trustworthy.

    Args:
    - historical_ssl_certificates: list, required, List of SSL certificates in the history
    - x_apikey: string, required, Your API key
    """
    return any(
        cert["valid"]
        and datetime.datetime.strptime(cert["expiration_date"], "%Y-%m-%d")
        > datetime.datetime.now()
        for cert in historical_ssl_certificates
    )


def vt_get_dns_resolution_object(id, x_apikey):
    """
    This endpoint retrieves a Resolution object by its ID. A resolution object ID is made by appending the IP and the domain it resolves to together.

    Domain-IP resolutions. Resolution objects include the following attributes:
    date: <integer> date when the resolution was made (UTC timestamp).
    host_name: <string> domain or subdomain requested to the resolver.
    host_name_last_analysis_stats: <dictionary> last detection stats from the resolution's domain. Similar to the domains's last_analysis_stats attribute.
    ip_address: <string> IP address the domain was resolved to.
    ip_address_last_analysis_stats: <dictionary> last detection stats from the resolution's IP address. Similar to the IP address' last_analysis_stats attribute.
    resolver: <string> source of the resolution.

    Args:
    - id: string, required, Resolution object ID
    - x_apikey: string, required, Your API key
    """
    return mock_db["ip_addresses"].get(id)


def vt_get_objects_related_to_ip_address(
    ip, relationship, x_apikey, limit=None, cursor=None
):
    """
    IP addresses have number of relationships to other objects. This returns ALL objects that fit the relationship.

    The relationships are documented here:
    - comments: The comments for the IP address. Returns a list of comments.
    - communicating_files: Files that communicate with the IP address. Returns a list of files.
    - downloaded_files: Files downloaded from the IP address. VT Enterprise users only. Returns a list of files.
    - graphs: Graphs including the IP address. Returns a list of graphs.
    - historical_ssl_certificates: SSL certificates associated with the IP. Returns a list of SSL certificates.
    - historical_whois: WHOIS information for the IP address. Retrurns a list of Whois attributes.
    - related_comments: Community posted comments in the IP's related objects. Returns a list of comments.
    - related_references: Returns the references related to the IP address. Returns a list of References.
    - related_threat_actors: Threat actors related to the IP address. Returns a list of threat actors.
    - referrer_files: Files containing the IP address. Returns a list of Files.
    - resolutions: Resolves the IP addresses. Returns a list of resolutions.
    - urls: Returns a list of URLs related to the IP address. Returns a list of URLs.

    Args:
    - ip, string, required, IP address
    - relationship, string, required, Relationship name (see the list of items from above)
    - x_apikey, string, required, Your API key
    - limit, int32, optional, Maximum number of comments to retrieve
    - cursor, string, optional, Continuation cursor
    """
    if ip in mock_db["ip_addresses"] and relationship in mock_db["ip_addresses"][ip]:
        related_data = mock_db["ip_addresses"][ip][relationship]
        if isinstance(related_data, list):
            return related_data[:limit] if limit else related_data
        return []
    return []


def vt_get_ip_address_report(ip, x_apikey):
    """
    Retrieve an IP address report. These reports condense all of the recent activity that VirusTotal has seen for the resource under consideration, as well as contextual information about it.
    This function specifically generates these reports using the IP address parameter.

    Args:
    - ip: string, required, IP address
    - x_apikey: string, required, Your API key
    """
    return mock_db["ip_addresses"][ip]["report"]


def vt_add_votes_to_ip_address(ip, data, x_apikey):
    """
    With this function you can post a vote for a given file. The body for the POST request must be the JSON representation of a vote object. Note however that you don't need to provide an ID for the object, as they are automatically generated for new votes. The verdict attribute must have be either harmless or malicious.

    Please ensure that the JSON object you provide conforms accurately to valid JSON standards.

    Args:
    - ip, string, required, IP address
    - data, json, Vote object
    - x_apikey, string, required, Your API key
    """
    return f"Votes added to ip: {ip}"


def vt_get_domain_report(domain, x_apikey):
    """
    Retrieves a domain report. These reports contain information regarding the domain itself that VirusTotal has collected.

    Args:
    - domain: string, required, Domain name
    - x_apikey: string, required, Your API key
    """
    if domain in mock_db["domains"]:
        report = mock_db["domains"][domain].get("report")
        # Ensure the report has a last_analysis_date
        if report and "last_analysis_date" in report:
            return report
        else:
            # Return a default report if the report is missing or incomplete
            return {"last_analysis_date": 1580515200}  # Default date, e.g., 2020-02-01
    else:
        # Return a default report if the domain does not exist
        return {"last_analysis_date": 1580515200}  # Default date, e.g., 2020-02-01


def vt_get_comments_on_ip_address(ip, x_apikey, limit=None, cursor=None):
    """
    Retrieves the comments on a provided IP address. Returns a list of Comment objects.

    Args:
    - ip, string, required, IP address
    - x_apikey, string, required, Your API key
    - limit, int32, optional, Maximum number of comments to retrieve
    - cursor, string, optional, Continuation cursor
    """
    return (
        mock_db["ip_addresses"][ip]["comments"][:limit]
        if limit
        else mock_db["ip_addresses"][ip]["comments"]
    )


def vt_add_comment_to_ip_address(ip, data, x_apikey):
    """
    With this function you can post a comment for a given IP address. The body for the POST request must be the JSON representation of a comment object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new comments.
    However, please note that you will need to provide a valid data JSON for using this function.

    Any word starting with # in your comment's text will be considered a tag, and added to the comment's tag attribute.

    Returns a Comment object.

    Args:
    - ip: string, required, IP address
    - data: json, required, A comment object
    - x_apikey: string, required, Your API key
    """
    if "comments" not in mock_db["ip_addresses"][ip]:
        mock_db["ip_addresses"][ip]["comments"] = []
    mock_db["ip_addresses"][ip]["comments"].append(data)
    return f"Following data has been added to {ip}: {data}"


def vt_get_object_descriptors_related_to_ip_address(
    ip, relationship, x_apikey, limit=None, cursor=None
):
    """
    This function simulates an API that retrieves descriptors related to an IP address.
    It returns specific attributes or details depending on the relationship type.

    Parameters:
    - ip: string, required, the IP address to query.
    - relationship: string, required, type of relationship data to retrieve.
    - x_apikey: string, required, API key for authentication.
    - limit: int, optional, limit on the number of results to return.
    - cursor: string, optional, cursor for pagination.

    Returns:
    A list of dictionaries containing the related data, or an empty list if no data or IP is found.
    """

    # Check for valid API key (for simulation purposes, any string is considered valid)
    if not isinstance(x_apikey, str) or not x_apikey:
        raise ValueError("Invalid API key provided.")

    # Check for valid IP in the mock database
    if ip not in mock_db["ip_addresses"]:
        return []  # Return an empty list if the IP is not found

    # Fetch data based on the relationship
    data = {
        "comments": [
            {"comment": comment}
            for comment in mock_db["ip_addresses"][ip].get("comments", [])
        ],
        "communicating_files": [
            {"file_name": f"file{index}.exe"} for index in range(5)
        ],
        "downloaded_files": [
            {"file_name": f"download{index}.zip"} for index in range(3)
        ],
        "graphs": [{"graph_id": f"graph{index}"} for index in range(2)],
        "historical_ssl_certificates": [
            {"certificate_id": f"cert{index}"} for index in range(4)
        ],
        "historical_whois": [{"record_id": f"whois{index}"} for index in range(2)],
        "related_comments": [
            {"comment": "Related comment " + str(i)} for i in range(3)
        ],
        "related_references": [{"reference": f"ref{index}"} for index in range(2)],
        "related_threat_actors": [
            {"actor_name": actor["name"]}
            for actor in mock_db["ip_addresses"][ip].get("related_threat_actors", [])
        ],
        "referrer_files": [
            {"file_name": f"referrer_file{index}.exe"} for index in range(3)
        ],
        "resolutions": [{"resolution_id": f"res{index}"} for index in range(2)],
        "urls": [{"url": f"http://192.168.0.{index}/"} for index in range(1, 6)],
    }

    result = data.get(relationship, [])
    # Implement cursor-based slicing if needed
    start = 0 if cursor is None else int(cursor)
    return result[start : start + limit] if limit else result[start:]


def vt_get_objects_related_to_domain(
    domain, relationship, x_apikey, limit=None, cursor=None
):
    """
    Objects are a key concept in the VirusTotal API. Each object has an identifier and a type.
    Each object has an associated URL, and each domain is associated with objects.
    This function returns ALL of the objects related to the domain, based on the specified relationship.

    The following describe the valid relationship:
    - caa_records: Records CAA for the domain.
    - cname_records: Records CNAME for the domain.
    - comments: Community posted comments about the domain.
    - communicating_files: Files that communicate with the domain.
    - downloaded_files: Files downloaded from that domain.
    - graphs: All graphs that include the domain.
    - historical_ssl_certificates: SSL certificates associated with the domain.
    - historical_whois: WHOIS information for the domain.
    - immediate_parent: Domain's immediate parent.
    - mx_records: Records MX for the domain.
    - ns_records: Records NS for the domain.
    - parent: Domain's top parent.
    - referrer_files: Refers to any and all files that contain this domain.
    - related_comments: Community posted comments in the domain's related objects.
    - related_references: Refers to the References related to the domain.
    - related_threat_actors: Refers to the threat actors related to the domain. A list of Threat Actors.
    - resolutions: DNS resolutions for the domain.
    - soa_records: Records SOA for the domain.
    - siblings: Refers to the Domain's sibling domains.
    - subdomains: Refers to the Domain's subdomains.
    - urls: Refers to the URLs that contain this domain.
    - user_votes: Refers to the current user's votes.


    Args:
    - domain: string, required, Domain name
    - relationship, string, required, Relationship name (see table)
    - x_apikey, string, required, Your API key
    - limit, int32, optional, Maximum number of comments to retrieve
    - cursor, string, optional, Continuation cursor
    """
    if domain in mock_db["domains"] and relationship in mock_db["domains"][domain]:
        related_data = mock_db["domains"][domain][relationship]
        if isinstance(related_data, list):
            return related_data[:limit] if limit else related_data
        return related_data
    return []


def vt_get_object_descriptors_related_to_domain(
    domain, relationship, x_apikey, limit=None, cursor=None
):
    """
    This specifically returns related object's IDs (and context attributes, if any). Please note that this will not return all attributes. This will return objects relating to a domain.

    - caa_records: Records CAA for the domain.
    - cname_records: Records CNAME for the domain.
    - comments: Community posted comments about the domain.
    - communicating_files: Files that communicate with the domain.
    - downloaded_files: Files downloaded from that domain.
    - graphs: All graphs that include the domain.
    - historical_ssl_certificates: SSL certificates associated with the domain.
    - historical_whois: WHOIS information for the domain.
    - immediate_parent: Domain's immediate parent.
    - mx_records: Records MX for the domain.
    - ns_records: Records NS for the domain.
    - parent: Domain's top parent.
    - referrer_files: Refers to any and all files that contain this domain.
    - related_comments: Community posted comments in the domain's related objects.
    - related_references: Refers to the References related to the domain.
    - related_threat_actors: Refers to the threat actors related to the domain. A list of Threat Actors.
    - resolutions: DNS resolutions for the domain.
    - soa_records: Records SOA for the domain.
    - siblings: Refers to the Domain's sibling domains.
    - subdomains: Refers to the Domain's subdomains.
    - urls: Refers to the URLs that contain this domain.
    - user_votes: Refers to the current user's votes.

    Args:
    - domain: string, required, Domain name
    - relationship: string, required, Relationship name (see table)
    - x_apikey: string, required, Your API key
    - limit: int32, optional, Maximum number of comments to retrieve
    - cursor: string, optional, Continuation cursor
    """
    if domain not in mock_db["domains"]:
        return []  # No data for the non-existent domain

    # Define the data based on available mock relationships
    descriptors = {
        "caa_records": [
            {"record": rec} for rec in mock_db["domains"][domain].get("caa_records", [])
        ],
        "cname_records": [{"record": "cname.example.com"}],  # Static example
        "comments": [
            {"comment": comment}
            for comment in mock_db["domains"][domain].get("comments", [])
        ],
        "communicating_files": [
            {"file_name": file}
            for file in mock_db["domains"][domain].get("communicating_files", [])
        ],
        "downloaded_files": [
            {"file_name": f"download{index}.mp4"} for index in range(3)
        ],  # Example
        "graphs": [{"graph_id": f"graph{index}"} for index in range(2)],  # Example
        "historical_ssl_certificates": [
            {"certificate_id": f"cert{index}"} for index in range(4)
        ],  # Example
        "historical_whois": [
            {"record_id": f"whois{index}"} for index in range(2)
        ],  # Example
        "immediate_parent": [{"parent": "com"}],  # Example
        "mx_records": [
            {"record": record}
            for record in mock_db["domains"][domain].get("mx_records", [])
        ],
        "ns_records": [{"record": "ns1.nameserver.com"}],  # Static example
        "parent": [{"parent": "com"}],  # Example
        "referrer_files": [
            {"file_name": f"referrer{index}.pdf"} for index in range(2)
        ],  # Example
        "related_comments": [{"comment": "Related to example.com"}],  # Static example
        "related_references": [
            {"reference": f"ref{index}"} for index in range(2)
        ],  # Example
        "related_threat_actors": [
            {"actor_name": actor["name"]}
            for actor in mock_db["domains"][domain].get("related_threat_actors", [])
        ],
        "resolutions": [
            {"resolution_id": f"res{index}"} for index in range(2)
        ],  # Example
        "soa_records": [{"record": "soa.example.com"}],  # Static example
        "siblings": [{"domain": "sibling.example.com"}],  # Static example
        "subdomains": [
            {"domain": sub} for sub in mock_db["domains"][domain].get("subdomains", [])
        ],
        "urls": [{"url": url} for url in mock_db["domains"][domain].get("urls", [])],
        "user_votes": [{"votes": "up"}],  # Static example
    }

    # Get data slice based on cursor and limit
    result = descriptors.get(relationship, [])
    start = 0 if cursor is None else int(cursor)
    return result[start : start + limit] if limit else result[start:]


def vt_get_comments_on_domain(domain, x_apikey, limit=None, cursor=None):
    """
    This function will retrieve comments on a specified domain.

    Args:
    - domain, string, required, Domain name
    - x_apikey, string, required, Your API key
    - limit, int32, optional, Maximum number of comments to retrieve
    - cursor, string, optional, Continuation cursor
    """
    return (
        mock_db["domains"][domain]["comments"][:limit]
        if limit
        else mock_db["domains"][domain]["comments"]
    )


def vt_get_votes_on_ip_address(ip):
    """
    This function will retrieve votes on a provided IP address.

    Args:
    - ip: string, required, ip address

    """
    return mock_db["ip_addresses"][ip]["votes"]


get_random_object_from_list_json = {
    "name": "get_random_object_from_list",
    "description": "This function selects and returns a random object from a list of objects. It is designed to handle any list length, including empty lists.",
    "parameters": {
        "type": "object",
        "properties": {
            "list_of_objects": {
                "type": "array",
                "items": {
                    "type": "object",
                    "description": "Individual objects in the list from which a random object will be selected.",
                },
                "description": "List containing objects from which the function will pick out a random object.",
            }
        },
        "required": ["list_of_objects"],
    },
}


get_first_object_from_list_json = {
    "name": "get_first_object_from_list",
    "description": "Retrieves the first object from a given list. If the list is empty, it returns `None`.",
    "parameters": {
        "type": "object",
        "properties": {
            "list_of_objects": {
                "type": "array",
                "items": {
                    "type": "object",
                    "description": "Individual objects in the list",
                },
                "description": "List containing objects from which the function will pick out the first object.",
            }
        },
        "required": ["list_of_objects"],
    },
}


calculate_sum_of_numbers_json = {
    "name": "calculate_sum_of_numbers",
    "description": "Computes the sum of two numbers provided. Input numbers can be either integer or floating-point values.",
    "parameters": {
        "type": "object",
        "properties": {
            "num1": {"type": ["integer", "number"], "description": "The first number"},
            "num2": {"type": ["integer", "number"], "description": "The second number"},
        },
        "required": ["num1", "num2"],
    },
}

extract_resolution_date_json = {
    "name": "extract_resolution_date",
    "description": "Extracts the date of DNS resolution from a DNS resolution object. The date is returned as a Unix timestamp.",
    "parameters": {
        "type": "object",
        "properties": {
            "dns_res_obj": {
                "type": "object",
                "description": "The DNS resolution object from which the date of resolution is to be extracted.",
            }
        },
        "required": ["dns_res_obj"],
    },
}

count_items_in_list_json = {
    "name": "count_items_in_list",
    "description": "This function takes a list as an input and returns the number of items present in the list.",
    "parameters": {
        "type": "object",
        "properties": {
            "input_list": {
                "type": "array",
                "items": {
                    "type": "object",
                    "description": "Individual items in the list",
                },
                "description": "List whose items are to be counted",
            }
        },
        "required": ["input_list"],
    },
}


vt_get_majority_vote_json = {
    "name": "vt_get_majority_vote",
    "description": "This function takes a dictionary of votes returns the name with the majority votes. If the votes are equal, it will return the first encountered key in the dictionary.",
    "parameters": {
        "type": "object",
        "properties": {
            "votes": {"type": "object", "description": "Dictionary of votes"}
        },
        "required": ["votes"],
    },
}

vt_get_multiple_domain_reports_json = {
    "name": "vt_get_multiple_domain_reports",
    "description": "Retrieves reports for a list of domains provided. For each domain in the list, it requests the collected information regarding that domain from VirusTotal.",
    "parameters": {
        "type": "object",
        "properties": {
            "domains": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of Domain names",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["domains", "x_apikey"],
    },
}

vt_get_comments_on_multiple_domains_json = {
    "name": "vt_get_comments_on_multiple_domains",
    "description": "This function will retrieve comments for each specified domain in the given list.",
    "parameters": {
        "type": "object",
        "properties": {
            "domains": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of domain names",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
            "limit": {
                "type": "integer",
                "format": "int32",
                "description": "Maximum number of comments to retrieve for each domain",
            },
            "cursor": {"type": "string", "description": "Continuation cursor"},
        },
        "required": ["domains", "x_apikey"],
    },
}

vt_get_last_analysis_date_from_report_json = {
    "name": "vt_get_last_analysis_date_from_report",
    "description": "This function retrieves the last analysis date from the domain report collected by VirusTotal. The returned date is in Unix timestamp format.",
    "parameters": {
        "type": "object",
        "properties": {
            "report": {
                "type": "object",
                "description": "The domain report collected by vt_get_domain_report function.",
            }
        },
        "required": ["report"],
    },
}

vt_is_date_within_range_json = {
    "name": "vt_is_date_within_range",
    "description": "Checks if a given Unix timestamp is within a specified date range. The range is specified by 'start' and 'end' dates formatted as 'YYYY/MM/DD'. It's permissible for only one of 'start' or 'end' to be present in the function call. If 'start' is not provided, the function checks if the timestamp is earlier than or equal to the 'end' date. Similarly, If 'end' is not provided, the function checks if the timestamp is later than or equal to the 'start' date.",
    "parameters": {
        "type": "object",
        "properties": {
            "timestamp": {"type": "integer", "description": "Unix timestamp"},
            "start": {
                "type": "string",
                "description": "Start of the date range in 'YYYY/MM/DD' format",
            },
            "end": {
                "type": "string",
                "description": "End of the date range in 'YYYY/MM/DD' format",
            },
        },
        "required": ["timestamp"],
    },
}

convert_unix_timestamp_to_date_json = {
    "name": "convert_unix_timestamp_to_date",
    "description": "Converts a UNIX timestamp to a human-readable date in the format 'YYYY/MM/DD'.",
    "parameters": {
        "type": "object",
        "properties": {
            "unix_timestamp": {
                "type": "integer",
                "description": "The UNIX timestamp to be converted.",
            }
        },
        "required": ["unix_timestamp"],
    },
}


vt_get_threat_actors_latest_modification_date_json = {
    "name": "vt_get_threat_actors_latest_modification_date",
    "description": "This function retrieves the latest modification date from a list of threat actor objects. It iterates through each threat actor object, checks its modification date, and returns the most recent modification date.",
    "parameters": {
        "type": "object",
        "properties": {
            "threat_actor_objects": {
                "type": "array",
                "items": {"type": "object"},
                "description": "A list of threat actor objects.",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["threat_actor_objects", "x_apikey"],
    },
}

vt_get_threat_actors_main_source_region_json = {
    "name": "vt_get_threat_actors_main_source_region",
    "description": "This function takes a list of threat actor objects and returns the primary source region among them. Each threat actor object has an attribute 'source region', and the function analyses this attribute across all objects to determine and return the most common source region, deemed as the 'main' source region.",
    "parameters": {
        "type": "object",
        "properties": {
            "threat_actors": {
                "type": "array",
                "items": {"type": "object"},
                "description": "List of threat actor objects",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["threat_actors", "x_apikey"],
    },
}

vt_validate_historical_ssl_certificates_json = {
    "name": "vt_validate_historical_ssl_certificates",
    "description": "This function takes historical SSL certificates as input and checks if there is at least one valid SSL certificate present inside the provided historical data. It validates the SSL certificate by checking whether it is not expired and its issuing authority is trustworthy.",
    "parameters": {
        "type": "object",
        "properties": {
            "historical_ssl_certificates": {
                "type": "array",
                "items": {"type": "object"},
                "description": "List of SSL certificates in the history",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["historical_ssl_certificates", "x_apikey"],
    },
}

vt_get_dns_resolution_object_json = {
    "name": "vt_get_dns_resolution_object",
    "description": "This endpoint retrieves a Resolution object by its ID. A resolution object ID is made by appending the IP and the domain it resolves to together.\n\nDomain-IP resolutions. Resolution objects include the following attributes:\ndate: <integer> date when the resolution was made (UTC timestamp).\nhost_name: <string> domain or subdomain requested to the resolver.\nhost_name_last_analysis_stats: <dictionary> last detection stats from the resolution's domain. Similar to the domains's last_analysis_stats attribute.\nip_address: <string> IP address the domain was resolved to.\nip_address_last_analysis_stats: <dictionary> last detection stats from the resolution's IP address. Similar to the IP address' last_analysis_stats attribute.\nresolver: <string> source of the resolution.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {"type": "string", "description": "Resolution object ID"},
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["id", "x_apikey"],
    },
}

vt_get_objects_related_to_ip_address_json = {
    "name": "vt_get_objects_related_to_ip_address",
    "description": "IP addresses have a number of relationships to other objects. This returns ALL objects that fit the relationship. Returns a list of URLs.",
    "parameters": {
        "type": "object",
        "properties": {
            "ip": {"type": "string", "description": "IP address"},
            "relationship": {
                "type": "string",
                "description": "Relationship name (see the list of table). \n\nThe relationships are documented here:\n- comments: The comments for the IP address. Returns a list of comments.\n- communicating_files: Files that communicate with the IP address. Returns a list of files.\n- downloaded_files: Files downloaded from the IP address. VT Enterprise users only. Returns a list of files.\n- graphs: Graphs including the IP address. Returns a list of graphs.\n- historical_ssl_certificates: SSL certificates associated with the IP. Returns a list of SSL certificates.\n- historical_whois: WHOIS information for the IP address. Returns a list of Whois attributes.\n- related_comments: Community posted comments in the IP's related objects. Returns a list of comments.\n- related_references: Returns the references related to the IP address. Returns a list of References.\n- related_threat_actors: Threat actors related to the IP address. Returns a list of threat actors.\n- referrer_files: Files containing the IP address. Returns a list of Files.\n- resolutions: Resolves the IP addresses. Returns a list of resolutions.\n- urls: Returns a list of URLs related to the IP address. ",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
            "limit": {
                "type": "integer",
                "description": "Maximum number of comments to retrieve",
                "format": "int32",
            },
            "cursor": {"type": "string", "description": "Continuation cursor"},
        },
        "required": ["ip", "relationship", "x_apikey"],
    },
}

vt_get_ip_address_report_json = {
    "name": "vt_get_ip_address_report",
    "description": "Retrieve an IP address report. These reports condense all of the recent activity that VirusTotal has seen for the resource under consideration, as well as contextual information about it. This function specifically generates these reports using the IP address parameter.",
    "parameters": {
        "type": "object",
        "properties": {
            "ip": {"type": "string", "description": "IP address"},
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["ip", "x_apikey"],
    },
}

vt_add_votes_to_ip_address_json = {
    "name": "vt_add_votes_to_ip_address",
    "description": "With this function, you can post a vote for a given file. The body for the POST request must be the JSON representation of a vote object. Note however that you don't need to provide an ID for the object, as they are automatically generated for new votes. The verdict attribute must be either 'harmless' or 'malicious'.\n\nPlease ensure that the JSON object you provide conforms accurately to valid JSON standards.",
    "parameters": {
        "type": "object",
        "properties": {
            "ip": {"type": "string", "description": "IP address"},
            "data": {
                "type": "object",
                "description": "Vote object, must conform to valid JSON standards and contain a 'verdict' attribute that is either 'harmless' or 'malicious'.",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["ip", "data", "x_apikey"],
    },
}


vt_get_domain_report_json = {
    "name": "vt_get_domain_report",
    "description": "Retrieves a domain report. These reports contain information regarding the domain itself that VirusTotal has collected.",
    "parameters": {
        "type": "object",
        "properties": {
            "domain": {"type": "string", "description": "Domain name"},
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["domain", "x_apikey"],
    },
}


vt_get_comments_on_ip_address_json = {
    "name": "vt_get_comments_on_ip_address",
    "description": "Retrieves the comments on a provided IP address. Returns a list of Comment objects.",
    "parameters": {
        "type": "object",
        "properties": {
            "ip": {"type": "string", "description": "IP address"},
            "x_apikey": {"type": "string", "description": "Your API key"},
            "limit": {
                "type": "integer",
                "description": "Maximum number of comments to retrieve",
                "format": "int32",
            },
            "cursor": {"type": "string", "description": "Continuation cursor"},
        },
        "required": ["ip", "x_apikey"],
    },
}


vt_add_comment_to_ip_address_json = {
    "name": "vt_add_comment_to_ip_address",
    "description": "With this function, you can post a comment for a given IP address. The body for the POST request must be the JSON representation of a comment object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new comments. However, please note that you will need to provide a valid data JSON for using this function.\n\nAny word starting with # in your comment's text will be considered a tag, and added to the comment's tag attribute.\n\nReturns a Comment object.",
    "parameters": {
        "type": "object",
        "properties": {
            "ip": {"type": "string", "description": "IP address"},
            "data": {
                "type": "object",
                "description": "A comment object, must conform to valid JSON standards and contain the necessary attributes for a comment.",
            },
            "x_apikey": {"type": "string", "description": "Your API key"},
        },
        "required": ["ip", "data", "x_apikey"],
    },
}

vt_get_object_descriptors_related_to_ip_address_json = {
    "name": "vt_get_object_descriptors_related_to_ip_address",
    "description": "This specifically returns related object's IDs (and context attributes, if any). Please note that this will not return all attributes.\n\nYou are expected to provide the relationship to the object you're interested in. The valid relationships are documented and include comments, communicating files, downloaded files (VT Enterprise users only), graphs, historical SSL certificates, historical whois, related comments, related references, related threat actors, referrer files, resolutions, and URLs.",
    "parameters": {
        "type": "object",
        "properties": {
            "ip": {"type": "string", "description": "IP address"},
            "relationship": {"type": "string", "description": "Relationship name"},
            "x_apikey": {"type": "string", "description": "Your API key"},
            "limit": {
                "type": "integer",
                "description": "Maximum number of objects to retrieve",
                "format": "int32",
            },
            "cursor": {"type": "string", "description": "Continuation cursor"},
        },
        "required": ["ip", "relationship", "x_apikey"],
    },
}

vt_get_objects_related_to_domain_json = {
    "name": "vt_get_objects_related_to_domain",
    "description": "Objects are a key concept in the VirusTotal API. Each object has an identifier and a type. Each object has an associated URL, and each domain is associated with objects. This function returns ALL of the objects related to the domain, based on the specified relationship.\n\nValid relationships include caa_records, cname_records, comments, communicating_files, downloaded_files, graphs, historical_ssl_certificates, historical_whois, immediate_parent, mx_records, ns_records, parent, referrer_files, related_comments, related_references, related_threat_actors, resolutions, soa_records, siblings, subdomains, urls, user_votes.",
    "parameters": {
        "type": "object",
        "properties": {
            "domain": {"type": "string", "description": "Domain name"},
            "relationship": {"type": "string", "description": "Relationship name"},
            "x_apikey": {"type": "string", "description": "Your API key"},
            "limit": {
                "type": "integer",
                "description": "Maximum number of objects to retrieve",
                "format": "int32",
            },
            "cursor": {"type": "string", "description": "Continuation cursor"},
        },
        "required": ["domain", "relationship", "x_apikey"],
    },
}

vt_get_object_descriptors_related_to_domain_json = {
    "name": "vt_get_object_descriptors_related_to_domain",
    "description": "This function specifically returns related object's IDs (and context attributes, if any) but will not return all attributes. It returns objects relating to a domain based on the specified relationship. Valid relationships include caa_records, cname_records, comments, communicating_files, downloaded_files, graphs, historical_ssl_certificates, historical_whois, immediate_parent, mx_records, ns_records, parent, referrer_files, related_comments, related_references, related_threat_actors, resolutions, soa_records, siblings, subdomains, urls, and user_votes.",
    "parameters": {
        "type": "object",
        "properties": {
            "domain": {"type": "string", "description": "Domain name"},
            "relationship": {"type": "string", "description": "Relationship name"},
            "x_apikey": {"type": "string", "description": "Your API key"},
            "limit": {
                "type": "integer",
                "description": "Maximum number of objects to retrieve",
                "format": "int32",
            },
            "cursor": {"type": "string", "description": "Continuation cursor"},
        },
        "required": ["domain", "relationship", "x_apikey"],
    },
}

vt_get_comments_on_domain_json = {
    "name": "vt_get_comments_on_domain",
    "description": "This function will retrieve comments on a specified domain.",
    "parameters": {
        "type": "object",
        "properties": {
            "domain": {"type": "string", "description": "Domain name"},
            "x_apikey": {"type": "string", "description": "Your API key"},
            "limit": {
                "type": "integer",
                "description": "Maximum number of comments to retrieve",
                "format": "int32",
            },
            "cursor": {"type": "string", "description": "Continuation cursor"},
        },
        "required": ["domain", "x_apikey"],
    },
}

vt_get_votes_on_ip_address_json = {
    "name": "vt_get_votes_on_ip_address",
    "description": "This function will retrieve votes on a provided IP address.",
    "parameters": {
        "type": "object",
        "properties": {"ip": {"type": "string", "description": "IP address"}},
        "required": ["ip"],
    },
}
