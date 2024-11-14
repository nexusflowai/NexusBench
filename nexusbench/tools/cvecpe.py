from typing import List, Dict, Any
from datetime import datetime, timedelta
from collections import Counter

CPE_DB = {
    "MySQL": [
        {
            "cpeNameId": "cpe:2.3:a:oracle:mysql:8.0.26:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:oracle:mysql:8.0.26:*:*:*:*:*:*:*",
            "lastModified": "2021-07-20T14:30:00.000Z",
            "titles": [{"title": "Oracle MySQL 8.0.26", "lang": "en"}],
            "refs": [{"ref": "https://www.mysql.com/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "Python": [
        {
            "cpeNameId": "cpe:2.3:a:python:python:3.9.6:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:python:python:3.9.6:*:*:*:*:*:*:*",
            "lastModified": "2021-06-30T10:15:00.000Z",
            "titles": [{"title": "Python 3.9.6", "lang": "en"}],
            "refs": [{"ref": "https://www.python.org/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "VMware": [
        {
            "cpeNameId": "cpe:2.3:a:vmware:vsphere:7.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:vmware:vsphere:7.0:*:*:*:*:*:*:*",
            "lastModified": "2022-05-15T09:00:00.000Z",
            "titles": [{"title": "VMware vSphere 7.0", "lang": "en"}],
            "refs": [
                {
                    "ref": "https://www.vmware.com/products/vsphere.html",
                    "type": "Vendor",
                }
            ],
            "deprecated": False,
        }
    ],
    "Tomcat": [
        {
            "cpeNameId": "cpe:2.3:a:apache:tomcat:9.0.43:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:apache:tomcat:9.0.43:*:*:*:*:*:*:*",
            "lastModified": "2021-02-15T11:30:00.000Z",
            "titles": [{"title": "Apache Tomcat 9.0.43", "lang": "en"}],
            "refs": [{"ref": "https://tomcat.apache.org/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "SSH": [
        {
            "cpeNameId": "cpe:2.3:a:openbsd:openssh:8.4:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:openbsd:openssh:8.4:*:*:*:*:*:*:*",
            "lastModified": "2021-09-01T13:45:00.000Z",
            "titles": [{"title": "OpenSSH 8.4", "lang": "en"}],
            "refs": [{"ref": "https://www.openssh.com/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "Apache": [
        {
            "cpeNameId": "cpe:2.3:a:apache:http_server:2.4.46:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:apache:http_server:2.4.46:*:*:*:*:*:*:*",
            "lastModified": "2021-01-20T16:00:00.000Z",
            "titles": [{"title": "Apache HTTP Server 2.4.46", "lang": "en"}],
            "refs": [{"ref": "https://httpd.apache.org/", "type": "Vendor"}],
            "deprecated": False,
        },
        {
            "cpeNameId": "CPE-2021-APA-001",
            "cpeName": "cpe:2.3:a:apache:http_server:2.4.29:*:*:*:*:*:*:*",
            "lastModified": "2021-06-01T14:30:00.000Z",
            "titles": [{"title": "Apache HTTP Server 2.4.29", "lang": "en"}],
            "refs": [{"ref": "https://httpd.apache.org/", "type": "Vendor"}],
            "deprecated": False,
        },
        {
            "cpeNameId": "CPE-2021-APA-002",
            "cpeName": "cpe:2.3:a:apache:tomcat:9.0.50:*:*:*:*:*:*:*",
            "lastModified": "2021-07-15T10:15:00.000Z",
            "titles": [{"title": "Apache Tomcat 9.0.50", "lang": "en"}],
            "refs": [{"ref": "https://tomcat.apache.org/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "CPE-2021-APA-003",
            "cpeName": "cpe:2.3:a:apache:struts:2.5.26:*:*:*:*:*:*:*",
            "lastModified": "2021-08-10T16:05:00.000Z",
            "titles": [{"title": "Apache Struts 2.5.26", "lang": "en"}],
            "refs": [{"ref": "https://struts.apache.org/", "type": "Vendor"}],
        },
    ],
    "Django": [
        {
            "cpeNameId": "cpe:2.3:a:djangoproject:django:3.2.5:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:djangoproject:django:3.2.5:*:*:*:*:*:*:*",
            "lastModified": "2022-07-15T08:30:00.000Z",
            "titles": [{"title": "Django 3.2.5", "lang": "en"}],
            "refs": [{"ref": "https://www.djangoproject.com/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "Mozilla Firefox": [
        {
            "cpeNameId": "cpe:2.3:a:mozilla:firefox:89.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:mozilla:firefox:89.0:*:*:*:*:*:*:*",
            "lastModified": "2021-06-01T12:00:00.000Z",
            "titles": [{"title": "Mozilla Firefox 89.0", "lang": "en"}],
            "refs": [{"ref": "https://www.mozilla.org/firefox/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "PostgreSQL": [
        {
            "cpeNameId": "cpe:2.3:a:postgresql:postgresql:13.2:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:postgresql:postgresql:13.2:*:*:*:*:*:*:*",
            "lastModified": "2021-02-11T10:45:00.000Z",
            "titles": [{"title": "PostgreSQL 13.2", "lang": "en"}],
            "refs": [{"ref": "https://www.postgresql.org/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "OpenSSL": [
        {
            "cpeNameId": "cpe:2.3:a:openssl:openssl:1.1.1k:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:openssl:openssl:1.1.1k:*:*:*:*:*:*:*",
            "lastModified": "2021-03-25T09:15:00.000Z",
            "titles": [{"title": "OpenSSL 1.1.1k", "lang": "en"}],
            "refs": [{"ref": "https://www.openssl.org/", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
    "Windows": [
        {
            "cpeNameId": "cpe:2.3:o:microsoft:windows_10:20h2:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:o:microsoft:windows_10:20h2:*:*:*:*:*:*:*",
            "lastModified": "2021-08-15T14:30:00.000Z",
            "titles": [{"title": "Microsoft Windows 10 Version 20H2", "lang": "en"}],
            "refs": [{"ref": "https://www.microsoft.com/windows", "type": "Vendor"}],
            "deprecated": False,
        },
        {
            "cpeNameId": "cpe:2.3:o:microsoft:windows_server_2019:-:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:o:microsoft:windows_server_2019:-:*:*:*:*:*:*:*",
            "lastModified": "2021-03-25T11:30:00.000Z",
            "titles": [{"title": "Microsoft Windows Server 2019", "lang": "en"}],
            "refs": [
                {"ref": "https://www.microsoft.com/windows-server", "type": "Vendor"}
            ],
        },
        {
            "cpeNameId": "cpe:2.3:o:microsoft:windows_10:21h1:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:o:microsoft:windows_10:21h1:*:*:*:*:*:*:*",
            "lastModified": "2021-04-01T08:00:00.000Z",
            "titles": [{"title": "Microsoft Windows 10 Version 21H1", "lang": "en"}],
            "refs": [{"ref": "https://www.microsoft.com/windows", "type": "Vendor"}],
        },
        {
            "cpeNameId": "CPE-2021-WIN-001",
            "cpeName": "cpe:2.3:o:microsoft:windows_10:-:*:*:*:*:*:*:*",
            "lastModified": "2021-07-15T10:15:00.000Z",
            "titles": [{"title": "Microsoft Windows 10", "lang": "en"}],
            "refs": [{"ref": "https://www.microsoft.com/windows", "type": "Vendor"}],
            "deprecated": False,
        },
    ],
    "Windows 10": [
        {
            "cpeNameId": "5c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f",
            "cpeName": "cpe:2.3:o:microsoft:windows_10:2004:*:*:*:*:*:*:*",
            "lastModified": "2021-08-15T09:00:00.000Z",
            "titles": [{"title": "Microsoft Windows 10 Version 2004", "lang": "en"}],
            "refs": [
                {"ref": "https://support.microsoft.com/en-us/windows", "type": "Vendor"}
            ],
        },
    ],
    "Windows 8": [
        {
            "cpeNameId": "7e5f6a7b-8c9d-0e1f-2a3b-4c5d6e7f8a9b",
            "cpeName": "cpe:2.3:o:microsoft:windows_8.1:-:*:*:*:*:*:*:*",
            "lastModified": "2021-07-10T14:00:00.000Z",
            "titles": [{"title": "Microsoft Windows 8.1", "lang": "en"}],
            "refs": [
                {"ref": "https://support.microsoft.com/en-us/windows", "type": "Vendor"}
            ],
        }
    ],
    "PHP": [
        {
            "cpeNameId": "cpe:2.3:a:php:php:7.4.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:php:php:7.4.0:*:*:*:*:*:*:*",
            "lastModified": "2020-03-15T14:30:00.000Z",
            "titles": [{"title": "PHP 7.4.0", "lang": "en"}],
            "refs": [{"ref": "https://www.php.net/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:php:php:8.0.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:php:php:8.0.0:*:*:*:*:*:*:*",
            "lastModified": "2020-12-01T10:15:00.000Z",
            "titles": [{"title": "PHP 8.0.0", "lang": "en"}],
            "refs": [{"ref": "https://www.php.net/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:php:php:8.0.1:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:php:php:8.0.1:*:*:*:*:*:*:*",
            "lastModified": "2021-01-10T09:45:00.000Z",
            "titles": [{"title": "PHP 8.0.1", "lang": "en"}],
            "refs": [{"ref": "https://www.php.net/", "type": "Vendor"}],
        },
    ],
    "Firefox": [
        {
            "cpeNameId": "cpe:2.3:a:mozilla:firefox:90.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:mozilla:firefox:90.0:*:*:*:*:*:*:*",
            "lastModified": "2021-07-15T09:45:00.000Z",
            "titles": [{"title": "Mozilla Firefox 90.0", "lang": "en"}],
            "refs": [{"ref": "https://www.mozilla.org/firefox/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:mozilla:firefox:91.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:mozilla:firefox:91.0:*:*:*:*:*:*:*",
            "lastModified": "2021-08-10T11:30:00.000Z",
            "titles": [{"title": "Mozilla Firefox 91.0", "lang": "en"}],
            "refs": [{"ref": "https://www.mozilla.org/firefox/", "type": "Vendor"}],
        },
    ],
    "Linux": [
        {
            "cpeNameId": "cpe:2.3:o:linux:linux_kernel:5.11.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:o:linux:linux_kernel:5.11.0:*:*:*:*:*:*:*",
            "lastModified": "2021-03-15T14:30:00.000Z",
            "titles": [{"title": "Linux Kernel 5.11.0", "lang": "en"}],
            "refs": [{"ref": "https://www.kernel.org/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:o:linux:linux_kernel:5.11.6:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:o:linux:linux_kernel:5.11.6:*:*:*:*:*:*:*",
            "lastModified": "2021-03-28T10:15:00.000Z",
            "titles": [{"title": "Linux Kernel 5.11.6", "lang": "en"}],
            "refs": [{"ref": "https://www.kernel.org/", "type": "Vendor"}],
        },
    ],
    "Java": [
        {
            "cpeNameId": "cpe:2.3:a:oracle:jdk:16.0.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:oracle:jdk:16.0.0:*:*:*:*:*:*:*",
            "lastModified": "2021-03-16T14:30:00.000Z",
            "titles": [{"title": "Oracle Java Development Kit 16.0.0", "lang": "en"}],
            "refs": [{"ref": "https://www.oracle.com/java/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:oracle:jre:16.0.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:oracle:jre:16.0.0:*:*:*:*:*:*:*",
            "lastModified": "2021-03-16T14:35:00.000Z",
            "titles": [
                {"title": "Oracle Java Runtime Environment 16.0.0", "lang": "en"}
            ],
            "refs": [{"ref": "https://www.oracle.com/java/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:eclipse:eclipse_ide:4.19.0:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:eclipse:eclipse_ide:4.19.0:*:*:*:*:*:*:*",
            "lastModified": "2021-03-17T10:15:00.000Z",
            "titles": [{"title": "Eclipse IDE 4.19.0", "lang": "en"}],
            "refs": [{"ref": "https://www.eclipse.org/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:apache:tomcat:9.0.44:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:apache:tomcat:9.0.44:*:*:*:*:*:*:*",
            "lastModified": "2021-03-20T09:45:00.000Z",
            "titles": [{"title": "Apache Tomcat 9.0.44", "lang": "en"}],
            "refs": [{"ref": "https://tomcat.apache.org/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:oracle:jdk:11.0.10:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:oracle:jdk:11.0.10:*:*:*:*:*:*:*",
            "lastModified": "2021-01-19T11:30:00.000Z",
            "titles": [{"title": "Oracle Java Development Kit 11.0.10", "lang": "en"}],
            "refs": [{"ref": "https://www.oracle.com/java/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:oracle:jre:11.0.10:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:oracle:jre:11.0.10:*:*:*:*:*:*:*",
            "lastModified": "2021-01-19T11:35:00.000Z",
            "titles": [
                {"title": "Oracle Java Runtime Environment 11.0.10", "lang": "en"}
            ],
            "refs": [{"ref": "https://www.oracle.com/java/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:jetbrains:intellij_idea:2021.1:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:jetbrains:intellij_idea:2021.1:*:*:*:*:*:*:*",
            "lastModified": "2021-04-07T08:00:00.000Z",
            "titles": [{"title": "JetBrains IntelliJ IDEA 2021.1", "lang": "en"}],
            "refs": [{"ref": "https://www.jetbrains.com/idea/", "type": "Vendor"}],
        },
        {
            "cpeNameId": "cpe:2.3:a:spring:spring_framework:5.3.5:*:*:*:*:*:*:*",
            "cpeName": "cpe:2.3:a:spring:spring_framework:5.3.5:*:*:*:*:*:*:*",
            "lastModified": "2021-03-18T13:20:00.000Z",
            "titles": [{"title": "Spring Framework 5.3.5", "lang": "en"}],
            "refs": [
                {"ref": "https://spring.io/projects/spring-framework", "type": "Vendor"}
            ],
        },
    ],
    "Zephyr": [
        {
            "cpeNameId": "CPE1234",
            "cpeName": "cpe:2.3:a:zephyrcorp:cloudweaver:2.1:*:*:*:*:*:*:*",
            "lastModified": "2021-05-20T10:30:00.000Z",
            "titles": [{"title": "ZephyrCorp CloudWeaver 2.1", "lang": "en"}],
            "refs": [{"ref": "https://zephyrcorp.example.com", "type": "Vendor"}],
        },
        {
            "cpeNameId": "CPE5678",
            "cpeName": "cpe:2.3:a:zephyrcorp:datashaper:3.0:*:*:*:*:*:*:*",
            "lastModified": "2021-06-15T14:30:00.000Z",
            "titles": [{"title": "ZephyrCorp DataShaper 3.0", "lang": "en"}],
            "refs": [{"ref": "https://zephyrcorp.example.com", "type": "Vendor"}],
        },
    ],
    "Nebula": [
        {
            "cpeNameId": "CPE9012",
            "cpeName": "cpe:2.3:a:nebulasoft:stargazer:1.5:*:*:*:*:*:*:*",
            "lastModified": "2021-07-01T09:00:00.000Z",
            "titles": [{"title": "NebulaSoft StarGazer 1.5", "lang": "en"}],
            "refs": [{"ref": "https://nebulasoft.example.com", "type": "Vendor"}],
        }
    ],
    "CPEmatch": [
        {
            "cpeNameId": "CPE3456",
            "cpeName": "cpe:2.3:a:cosmosystems:orbittracer:4.2:*:*:*:*:*:*:*",
            "lastModified": "2021-07-15T11:45:00.000Z",
            "titles": [{"title": "CosmoSystems OrbitTracer 4.2", "lang": "en"}],
            "refs": [{"ref": "https://cosmosystems.example.com", "type": "Vendor"}],
        }
    ],
    "Microsoft": [
        {
            "cpeNameId": "CPE-2013-MS-EXCHANGE",
            "cpeName": "cpe:2.3:a:microsoft:exchange_server:2013:sp1:*:*:*:*:*:*",
            "lastModified": "2021-09-01T10:00:00.000Z",
            "titles": [{"title": "Microsoft Exchange Server 2013 SP1", "lang": "en"}],
            "refs": [{"ref": "https://www.microsoft.com/exchange", "type": "Vendor"}],
            "deprecated": False,
        }
    ],
}

CVE_DB = {
    "RedHat": [
        {
            "cveId": "CVE-2021-20001",
            "description": "Critical vulnerability in RedHat Enterprise Linux",
            "publishedDate": "2021-10-15T00:00:00.000Z",
            "lastModifiedDate": "2021-11-01T10:30:00.000Z",
            "cvssV2Score": 7.5,
            "cvssV2Severity": "HIGH",
            "cvssV3Score": 8.1,
            "cvssV3Severity": "HIGH",
            "affectedProducts": ["cpe:/o:redhat:enterprise_linux:8"],
            "isVulnerable": True,
            "hasCertAlerts": True,
            "hasOval": True,
            "cvssV2Metrics": "AV:N/AC:L/Au:N/C:P/I:P/A:P",
        },
        {
            "cveId": "CVE-2021-20002",
            "description": "Another vulnerability in RedHat Enterprise Linux",
            "publishedDate": "2020-12-01T00:00:00.000Z",
            "lastModifiedDate": "2020-12-15T14:45:00.000Z",
            "cvssV3Score": 6.5,
            "cvssV3Severity": "MEDIUM",
        },
        {
            "cveId": "CVE-2021-20003",
            "description": "Third vulnerability in RedHat Enterprise Linux",
            "publishedDate": "2021-01-10T00:00:00.000Z",
            "lastModifiedDate": "2021-01-25T09:15:00.000Z",
            "cvssV3Score": 8.1,
            "cvssV3Severity": "HIGH",
        },
    ],
    "Windows": [
        {
            "cveId": "CVE-2023-20001",
            "description": "Windows 10 authentication vulnerability",
            "publishedDate": "2023-03-15T00:00:00.000Z",
            "lastModifiedDate": "2023-03-20T14:45:00.000Z",
            "cvssV2Score": 7.6,
            "cvssV2Severity": "HIGH",
            "cvssV3Score": 8.8,
            "cvssV3Severity": "HIGH",
            "affectedProducts": [
                "cpe:/o:microsoft:windows_10",
                "cpe:2.3:o:microsoft:windows_10:1607",
                "cpe:2.3:o:microsoft:windows_10:1909",
            ],
            "isVulnerable": True,
            "hasCertAlerts": True,
            "hasOval": True,
            "cvssV2Metrics": "AV:N/AC:M/Au:N/C:C/I:C/A:P",
        },
        {
            "cveId": "CVE-2021-24074",
            "description": "Windows TCP/IP Remote Code Execution Vulnerability",
            "publishedDate": "2021-01-12T00:00:00.000Z",
            "lastModifiedDate": "2021-01-15T10:30:00.000Z",
            "cvssV2Score": 9.3,
            "cvssV3Score": 9.8,
            "cvssV3Severity": "CRITICAL",
            "affectedProducts": ["cpe:/a:microsoft:windows_10:1909"],
            "isVulnerable": True,
            "hasCertAlerts": True,
        },
        {
            "cveId": "CVE-2021-24078",
            "description": "Windows DNS Server Remote Code Execution Vulnerability",
            "publishedDate": "2021-01-12T00:00:00.000Z",
            "lastModifiedDate": "2021-01-14T14:45:00.000Z",
            "cvssV2Score": 7.5,
            "cvssV3Score": 8.8,
            "cvssV3Severity": "HIGH",
            "affectedProducts": [
                "cpe:/a:microsoft:windows_10:1909",
                "cpe:2.3:o:microsoft:windows_10:1607",
            ],
            "isVulnerable": True,
            "hasCertAlerts": True,
        },
    ],
    "Linux": [
        {
            "cveId": "CVE-2022-10001",
            "description": "Linux Kernel vulnerability",
            "publishedDate": "2022-06-01T00:00:00.000Z",
            "lastModifiedDate": "2022-06-10T09:15:00.000Z",
            "cvssV2Score": 6.8,
            "cvssV2Severity": "MEDIUM",
            "cvssV3Score": 7.5,
            "cvssV3Severity": "HIGH",
            "affectedProducts": [
                "cpe:/o:linux:linux_kernel:2.6.32",
                "cpe:/o:linux:linux_kernel",
            ],
            "isVulnerable": True,
            "hasCertAlerts": True,
            "hasOval": False,
        }
    ],
    "Python": [
        {
            "cveId": "CVE-2022-20002",
            "description": "Python 3.8.1 vulnerability",
            "publishedDate": "2022-02-15T00:00:00.000Z",
            "lastModifiedDate": "2022-02-20T11:30:00.000Z",
            "cvssV2Score": 5.0,
            "cvssV2Severity": "MEDIUM",
            "cvssV3Score": 6.5,
            "cvssV3Severity": "MEDIUM",
            "affectedProducts": ["cpe:/a:python:python:3.8.1"],
            "isVulnerable": True,
            "hasCertAlerts": False,
            "hasOval": True,
        }
    ],
    "Microsoft Exchange": [
        {
            "cveId": "CVE-2021-26855",
            "description": "Microsoft Exchange Server Remote Code Execution Vulnerability",
            "publishedDate": "2021-03-02T00:00:00.000Z",
            "lastModifiedDate": "2021-03-09T20:15:00.000Z",
            "cvssV2Score": 8.0,
            "cvssV2Severity": "HIGH",
            "cvssV3Score": 9.8,
            "cvssV3Severity": "CRITICAL",
            "affectedProducts": [
                "cpe:/a:microsoft:exchange_server:2010",
                "cpe:/a:microsoft:exchange_server:2013",
                "cpe:/a:microsoft:exchange_server:2016",
                "cpe:/a:microsoft:exchange_server:2019",
            ],
            "isVulnerable": True,
            "hasCertAlerts": True,
        },
        {
            "cveId": "CVE-2020-0688",
            "description": "Microsoft Exchange Memory Corruption Vulnerability",
            "publishedDate": "2020-02-11T00:00:00.000Z",
            "lastModifiedDate": "2020-02-15T14:30:00.000Z",
            "cvssV2Score": 9.0,
            "cvssV2Severity": "HIGH",
            "cvssV3Score": 8.8,
            "cvssV3Severity": "HIGH",
            "affectedProducts": [
                "cpe:/a:microsoft:exchange_server:2010",
                "cpe:/a:microsoft:exchange_server:2013",
                "cpe:/a:microsoft:exchange_server:2016",
                "cpe:/a:microsoft:exchange_server:2019",
            ],
            "isVulnerable": True,
            "hasCertAlerts": True,
        },
        {
            "cveId": "CVE-2019-0686",
            "description": "Microsoft Exchange Server Elevation of Privilege Vulnerability",
            "publishedDate": "2019-02-12T00:00:00.000Z",
            "lastModifiedDate": "2019-02-18T09:45:00.000Z",
            "cvssV2Score": 6.5,
            "cvssV2Severity": "MEDIUM",
            "cvssV3Score": 7.6,
            "cvssV3Severity": "HIGH",
            "affectedProducts": [
                "cpe:/a:microsoft:exchange_server:2010",
                "cpe:/a:microsoft:exchange_server:2013",
                "cpe:/a:microsoft:exchange_server:2016",
            ],
            "isVulnerable": True,
            "hasCertAlerts": False,
        },
    ],
    "Microsoft Exchange 2010": [
        {
            "cveId": "CVE-2021-26855",
            "description": "Microsoft Exchange Server Remote Code Execution Vulnerability",
            "publishedDate": "2021-03-02T00:00:00.000Z",
            "lastModifiedDate": "2021-04-15T16:20:00.000Z",
            "cvssV3Score": 9.8,
            "cvssV3Severity": "CRITICAL",
        },
        {
            "cveId": "CVE-2021-26857",
            "description": "Microsoft Exchange Server Remote Code Execution Vulnerability",
            "publishedDate": "2021-03-02T00:00:00.000Z",
            "lastModifiedDate": "2021-03-09T20:15:00.000Z",
            "cvssV3Score": 7.8,
            "cvssV3Severity": "HIGH",
        },
    ],
    "XSS": [
        {
            "cveId": "CVE-2021-12345",
            "description": "Cross-site Scripting (XSS) vulnerability in Example Web Application",
            "publishedDate": "2021-06-15T00:00:00.000Z",
            "lastModifiedDate": "2021-07-01T10:30:00.000Z",
            "cvssV3Score": 6.1,
            "cvssV3Severity": "MEDIUM",
            "cvssV2Severity": "MEDIUM",
        },
        {
            "cveId": "CVE-2021-67890",
            "description": "Stored XSS vulnerability in Another Web Framework",
            "publishedDate": "2021-05-20T00:00:00.000Z",
            "lastModifiedDate": "2021-06-05T14:45:00.000Z",
            "cvssV3Score": 7.5,
            "cvssV3Severity": "HIGH",
            "cvssV2Severity": "HIGH",
        },
        {
            "cveId": "CVE-2021-98765",
            "description": "Reflected XSS vulnerability in Legacy Web Application",
            "publishedDate": "2021-04-10T00:00:00.000Z",
            "lastModifiedDate": "2021-04-25T09:15:00.000Z",
            "cvssV3Score": 3.7,
            "cvssV3Severity": "LOW",
            "cvssV2Severity": "LOW",
        },
    ],
    "Apache": [
        {
            "cveId": "CVE-2021-41773",
            "description": "A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49.",
            "publishedDate": "2021-10-05T00:00:00.000Z",
            "lastModifiedDate": "2021-10-10T14:30:00.000Z",
            "cvssV3Score": 7.5,
            "cvssV3Severity": "HIGH",
        },
        {
            "cveId": "CVE-2022-22721",
            "description": "Apache HTTP Server 2.4.52 and earlier may crash or disclose information due to a buffer overflow in mod_lua r:parsebody.",
            "publishedDate": "2022-04-12T00:00:00.000Z",
            "lastModifiedDate": "2022-04-20T09:45:00.000Z",
            "cvssV3Score": 7.5,
            "cvssV3Severity": "HIGH",
        },
        {
            "cveId": "CVE-2023-25690",
            "description": "Apache HTTP Server 2.4.0 - 2.4.55 may crash or disclose information due to a read beyond bounds in mod_proxy_ajp.",
            "publishedDate": "2023-03-07T00:00:00.000Z",
            "lastModifiedDate": "2023-03-15T11:20:00.000Z",
            "cvssV3Score": 7.5,
            "cvssV3Severity": "HIGH",
        },
    ],
    "Buffer Overflow": [
        {
            "cveId": "CVE-2021-30001",
            "description": "Buffer overflow vulnerability in Example Software",
            "publishedDate": "2021-05-15T00:00:00.000Z",
            "lastModifiedDate": "2021-05-20T10:30:00.000Z",
            "cvssV3Score": 9.8,
            "cvssV3Severity": "CRITICAL",
            "cvssV2Metrics": "AV:N/AC:L/Au:S/C:N/I:N/A:P",
            "cvssV2Severity": "HIGH",
            "hasCertAlerts": True,
            "hasOval": True,
            "hasCertNotes": False,
            "affectedProducts": ["cpe:2.3:a:example:software:1.0:*:*:*:*:*:*:*"],
        },
        {
            "cveId": "CVE-2021-30002",
            "description": "High severity buffer overflow vulnerability in Another Software",
            "publishedDate": "2021-06-01T00:00:00.000Z",
            "lastModifiedDate": "2021-06-10T14:45:00.000Z",
            "cvssV3Score": 8.1,
            "cvssV3Severity": "HIGH",
        },
        {
            "cveId": "CVE-2021-30003",
            "description": "Critical buffer overflow vulnerability in Third Software",
            "publishedDate": "2021-07-10T00:00:00.000Z",
            "lastModifiedDate": "2021-07-15T09:15:00.000Z",
            "cvssV3Score": 9.6,
            "cvssV3Severity": "CRITICAL",
        },
        {
            "cveId": "CVE-2021-30004",
            "description": "High severity buffer overflow vulnerability in Fourth Software",
            "publishedDate": "2021-08-05T00:00:00.000Z",
            "lastModifiedDate": "2021-08-10T11:30:00.000Z",
            "cvssV3Score": 7.8,
            "cvssV3Severity": "HIGH",
        },
    ],
    "PHP": [
        {
            "cveId": "CVE-2021-12345",
            "description": "Critical vulnerability in PHP",
            "publishedDate": "2021-06-15T00:00:00.000Z",
            "lastModifiedDate": "2021-06-20T14:30:00.000Z",
            "cvssV3Score": 9.1,
            "cvssV3Severity": "CRITICAL",
            "cvssV2Metrics": "AV:N/AC:L/Au:N/C:C/I:C/A:C",
            "cvssV2Severity": "HIGH",
            "hasCertAlerts": False,
            "hasOval": False,
            "hasCertNotes": True,
            "affectedProducts": ["cpe:2.3:a:php:php:5.3.6:*:*:*:*:*:*:*"],
        },
    ],
    "MySQL": [
        {
            "cveId": "CVE-2020-2934",
            "description": "Vulnerability in MySQL Server",
            "publishedDate": "2020-03-15T00:00:00.000Z",
            "lastModifiedDate": "2020-03-20T10:30:00.000Z",
            "cvssV3Score": 7.5,
            "cvssV3Severity": "HIGH",
            "affectedProducts": ["cpe:/a:mysql:mysql"],
            "isVulnerable": True,
        },
        {
            "cveId": "CVE-2020-2944",
            "description": "Another vulnerability in MySQL Server",
            "publishedDate": "2020-03-25T00:00:00.000Z",
            "lastModifiedDate": "2020-03-28T14:45:00.000Z",
            "cvssV3Score": 9.8,
            "cvssV3Severity": "CRITICAL",
            "affectedProducts": ["cpe:/a:mysql:mysql"],
            "isVulnerable": True,
        },
    ],
    "General Buffer Overflow": [
        {
            "cveId": "CVE-2022-0001",
            "description": "Buffer overflow vulnerability in Example Software",
            "publishedDate": "2022-01-15T00:00:00.000Z",
            "lastModifiedDate": "2022-02-01T09:00:00.000Z",
            "cvssV2Score": 6.8,
            "cvssV3Score": 7.5,
            "cvssV3Severity": "HIGH",
            "isVulnerable": True,
            "hasCertAlerts": False,
        },
        {
            "cveId": "CVE-2022-0002",
            "description": "Another buffer overflow vulnerability",
            "publishedDate": "2022-02-10T00:00:00.000Z",
            "lastModifiedDate": "2022-02-15T11:30:00.000Z",
            "cvssV2Score": 8.5,
            "cvssV3Score": 9.1,
            "cvssV3Severity": "CRITICAL",
            "isVulnerable": True,
            "hasCertAlerts": True,
        },
        {
            "cveId": "CVE-2023-0001",
            "description": "Buffer overflow vulnerability in Example Software",
            "descriptions": [
                {
                    "lang": "en",
                    "value": "Buffer overflow vulnerability in Example Software",
                },
                {
                    "lang": "es",
                    "value": "Vulnerabilidad de desbordamiento de búfer en Example Software",
                },
            ],
            "publishedDate": "2023-05-16T00:00:00.000Z",
            "lastModifiedDate": "2023-05-18T09:00:00.000Z",
            "cvssV2Score": 7.5,
            "cvssV2Severity": "HIGH",
            "cvssV3Score": 8.1,
            "cvssV3Severity": "HIGH",
            "isVulnerable": True,
            "hasCertAlerts": True,
        },
        {
            "cveId": "CVE-2023-0002",
            "description": "SQL injection vulnerability in Another Software",
            "descriptions": [
                {
                    "lang": "en",
                    "value": "SQL injection vulnerability in Another Software",
                },
                {
                    "lang": "es",
                    "value": "Vulnerabilidad de inyección SQL en Another Software",
                },
            ],
            "publishedDate": "2023-05-20T00:00:00.000Z",
            "lastModifiedDate": "2023-05-21T11:30:00.000Z",
            "cvssV2Score": 6.5,
            "cvssV2Severity": "MEDIUM",
            "cvssV3Score": 7.2,
            "cvssV3Severity": "HIGH",
            "isVulnerable": True,
            "hasCertAlerts": False,
        },
    ],
}


def searchCPE(
    cpeNameId: str = None,
    cpeMatchString: str = None,
    keywordExactMatch: bool = False,
    keywordSearch: str = None,
    lastModStartDate: str = None,
    lastModEndDate: str = None,
    matchCriteriaId: str = None,
    limit: int = None,
    key: str = None,
    delay: int = 6,
    verbose: bool = False,
) -> List[Dict[str, Any]]:
    """
    Search for CPE (Common Platform Enumeration) entries based on various criteria.

    Args:
        cpeNameId (str, optional): Specific CPE Name ID to search for.
        cpeMatchString (str, optional): Partial CPE name to match against.
        keywordExactMatch (bool, optional): If True, perform an exact match on the keyword. Defaults to False.
        keywordSearch (str, optional): Keyword to search in CPE titles.
        lastModStartDate (str, optional): Start date for last modification filter (format: 'YYYY-MM-DD').
        lastModEndDate (str, optional): End date for last modification filter (format: 'YYYY-MM-DD').
        matchCriteriaId (str, optional): Specific match criteria ID to filter by.
        limit (int, optional): Maximum number of results to return.
        key (str, optional): API key for authentication (not used in this mock version).
        delay (int, optional): Delay between API requests in seconds (not used in this mock version). Defaults to 6.
        verbose (bool, optional): If True, print the request URL. Defaults to False.

    Returns:
        List[Dict[str, Any]]: A list of CPE objects matching the search criteria.

    Note:
        This function searches a mock database (CPE_DB) and simulates the behavior of an actual CPE search API.
        In a real implementation, this would interact with the NVD (National Vulnerability Database) API.
    """
    results = []

    for cpes in CPE_DB.values():
        for cpe in cpes:
            if all(
                [
                    (not cpeNameId or cpe["cpeNameId"] == cpeNameId),
                    (
                        not cpeMatchString or cpeMatchString in cpe["cpeName"]
                    ),  # Changed to partial match
                    (
                        not keywordSearch
                        or (
                            keywordExactMatch
                            and keywordSearch
                            in [title["title"] for title in cpe["titles"]]
                        )
                        or (
                            not keywordExactMatch
                            and any(
                                keywordSearch.lower() in title["title"].lower()
                                for title in cpe["titles"]
                            )
                        )
                    ),
                    (
                        not matchCriteriaId
                        or matchCriteriaId in cpe.get("matchCriteria", [])
                    ),
                ]
            ):
                results.append(cpe)

    if lastModStartDate and lastModEndDate:
        start = datetime.strptime(lastModStartDate, "%Y-%m-%d")
        end = datetime.strptime(lastModEndDate, "%Y-%m-%d")
        results = [
            cpe
            for cpe in results
            if start <= datetime.strptime(cpe["lastModified"][:10], "%Y-%m-%d") <= end
        ]

    if limit:
        results = results[:limit]

    if verbose:
        for cpe in results:
            cpe["_metadata"] = {
                "query_params": {
                    "keywordSearch": keywordSearch,
                    "keywordExactMatch": keywordExactMatch,
                    "cpeMatchString": cpeMatchString,
                    "lastModStartDate": lastModStartDate,
                    "lastModEndDate": lastModEndDate,
                    "limit": limit,
                },
                "query_time": datetime.now().isoformat(),
            }

    return results


def searchCVE(
    keywordSearch: str = None,
    cvssV2Severity: str = None,
    cvssV3Severity: str = None,
    cveId: str = None,
    lastModStartDate: str = None,
    lastModEndDate: str = None,
    pubStartDate: str = None,
    pubEndDate: str = None,
    limit: int = None,
    cvssV2Metrics: str = None,
    hasCertAlerts: bool = None,
    hasOval: bool = None,
    hasCertNotes: bool = None,
    cpeName: str = None,
    isVulnerable: bool = None,
    key: str = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """
    Search for CVE (Common Vulnerabilities and Exposures) entries based on various criteria.

    Returns:
        List[Dict[str, Any]]: A list of CVE objects matching the search criteria.
    """
    results = []

    for cves in CVE_DB.values():
        for cve in cves:
            if all(
                [
                    (
                        not keywordSearch
                        or keywordSearch.lower() in cve["description"].lower()
                    ),
                    (
                        not cvssV2Severity
                        or cve.get("cvssV2Severity", "").lower()
                        == cvssV2Severity.lower()
                    ),
                    (
                        not cvssV3Severity
                        or cve.get("cvssV3Severity", "").lower()
                        == cvssV3Severity.lower()
                    ),
                    (not cvssV2Metrics or cve.get("cvssV2Metrics") == cvssV2Metrics),
                    (
                        hasCertAlerts is None
                        or cve.get("hasCertAlerts") == hasCertAlerts
                    ),
                    (hasOval is None or cve.get("hasOval") == hasOval),
                    (hasCertNotes is None or cve.get("hasCertNotes") == hasCertNotes),
                    (not cpeName or cpeName in cve.get("affectedProducts", [])),
                    (isVulnerable is None or cve.get("isVulnerable") == isVulnerable),
                ]
            ):
                results.append(cve)

    if lastModStartDate and lastModEndDate:
        start = datetime.strptime(lastModStartDate, "%Y-%m-%d")
        end = datetime.strptime(lastModEndDate, "%Y-%m-%d")
        results = [
            cve
            for cve in results
            if start
            <= datetime.strptime(cve["lastModifiedDate"][:10], "%Y-%m-%d")
            <= end
        ]

    if pubStartDate and pubEndDate:
        start = datetime.strptime(pubStartDate, "%Y-%m-%d")
        end = datetime.strptime(pubEndDate, "%Y-%m-%d")
        results = [
            cve
            for cve in results
            if start <= datetime.strptime(cve["publishedDate"][:10], "%Y-%m-%d") <= end
        ]

    if limit:
        results = results[:limit]

    return results


def verify_and_process_data_range_start(startdate: str, enddate: str) -> str:
    """verify_and_process_data_range_start"""
    start = datetime.strptime(startdate, "%Y-%m-%d")
    end = datetime.strptime(enddate, "%Y-%m-%d")
    if (end - start).days <= 90:
        return startdate
    return (end - timedelta(days=90)).strftime("%Y-%m-%d")


def verify_and_process_data_range_end(startdate: str, enddate: str) -> str:
    """verify_and_process_data_range_end"""
    start = datetime.strptime(startdate, "%Y-%m-%d")
    end = datetime.strptime(enddate, "%Y-%m-%d")
    if (end - start).days <= 90:
        return enddate
    return (start + timedelta(days=90)).strftime("%Y-%m-%d")


def summarize_cvecpes(cvecpeList: List[Dict[str, Any]]) -> str:
    """summarize_cvecpes"""
    if not cvecpeList:
        return "No items to summarize."

    summary = {
        "total_items": len(cvecpeList),
        "unique_vendors": set(),
        "product_types": Counter(),
        "cve_ids": set(),
        "severity_counts": Counter(),
        "last_modified_range": {"earliest": None, "latest": None},
    }

    for item in cvecpeList:
        if "cpeName" in item:  # CPE item
            cpe_parts = item["cpeName"].split(":")
            if len(cpe_parts) > 4:
                summary["unique_vendors"].add(cpe_parts[3])
            if len(cpe_parts) > 3:
                summary["product_types"][cpe_parts[2]] += 1
            mod_date = datetime.strptime(item["lastModified"][:10], "%Y-%m-%d")
        else:  # CVE item
            summary["cve_ids"].add(item["cveId"])
            summary["severity_counts"][item.get("cvssV3Severity", "UNKNOWN")] += 1
            mod_date = datetime.strptime(item["lastModifiedDate"][:10], "%Y-%m-%d")

        if (
            summary["last_modified_range"]["earliest"] is None
            or mod_date < summary["last_modified_range"]["earliest"]
        ):
            summary["last_modified_range"]["earliest"] = mod_date
        if (
            summary["last_modified_range"]["latest"] is None
            or mod_date > summary["last_modified_range"]["latest"]
        ):
            summary["last_modified_range"]["latest"] = mod_date

    # Format the summary
    formatted_summary = f"""
Summary of Items:
Total Items: {summary['total_items']}
"""

    if summary["unique_vendors"]:
        formatted_summary += f"Unique Vendors: {len(summary['unique_vendors'])}\n"

    if summary["product_types"]:
        formatted_summary += "Product Types:\n"
        formatted_summary += "\n".join(
            [f"  - {k}: {v}" for k, v in summary["product_types"].items()]
        )
        formatted_summary += "\n"

    if summary["cve_ids"]:
        formatted_summary += f"Total CVEs: {len(summary['cve_ids'])}\n"
        formatted_summary += "Severity Counts:\n"
        formatted_summary += "\n".join(
            [f"  - {k}: {v}" for k, v in summary["severity_counts"].items()]
        )
        formatted_summary += "\n"

    formatted_summary += f"""
Last Modified Range: 
  Earliest: {summary['last_modified_range']['earliest'].strftime('%Y-%m-%d')}
  Latest: {summary['last_modified_range']['latest'].strftime('%Y-%m-%d')}
"""
    return formatted_summary


def search_backup_keywords(
    cvecpeList: List[Dict[str, Any]], backup_keyword: str
) -> List[Dict[str, Any]]:
    """
    Search using backup keywords if the initial search returns no results.

    Args:
    cvecpeList (List[Dict[str, Any]]): The initial search results.
    backup_keyword (str): The backup keyword to use if initial results are empty.

    Returns:
    List[Dict[str, Any]]: Either the initial results or results from the backup search.
    """
    if not cvecpeList:
        # Determine whether to use searchCVE or searchCPE based on the backup_keyword
        # This is a simplified approach and might need adjustment based on your specific needs
        if "cve" in backup_keyword.lower():
            return searchCVE(keywordSearch=backup_keyword)
        else:
            return searchCPE(keywordSearch=backup_keyword)
    return cvecpeList


def count_cvecpe_items(cvecpeList: List[Dict[str, Any]]) -> str:
    """count_cvecpe_items"""
    cve_count = sum(1 for item in cvecpeList if "cveId" in item)
    cpe_count = sum(1 for item in cvecpeList if "cpeName" in item)

    return f"""
Total items: {len(cvecpeList)}
CVE items: {cve_count}
CPE items: {cpe_count}
"""


def compare_cvecpes(
    cvecpeList1: List[Dict[str, Any]], cvecpeList2: List[Dict[str, Any]]
) -> str:
    """compare_cvecpes"""
    set1 = set(
        item["cveId"] if "cveId" in item else item["cpeName"] for item in cvecpeList1
    )
    set2 = set(
        item["cveId"] if "cveId" in item else item["cpeName"] for item in cvecpeList2
    )

    common = set1.intersection(set2)
    only_in_list1 = set1 - set2
    only_in_list2 = set2 - set1

    summary1 = summarize_cvecpes(cvecpeList1)
    summary2 = summarize_cvecpes(cvecpeList2)

    comparison = f"""
Comparison of two CVE/CPE lists:

Common items: {len(common)}
Items only in List 1: {len(only_in_list1)}
Items only in List 2: {len(only_in_list2)}

Summary of List 1:
{summary1}

Summary of List 2:
{summary2}

Common items:
{', '.join(sorted(common))}

Items only in List 1:
{', '.join(sorted(only_in_list1))}

Items only in List 2:
{', '.join(sorted(only_in_list2))}
"""
    return comparison


def mergeCVEs(
    list1: List[Dict[str, Any]], list2: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Merge two lists of CVE objects into a single list.

    Args:
    list1 (List[Dict[str, Any]]): First list of CVE objects.
    list2 (List[Dict[str, Any]]): Second list of CVE objects.

    Returns:
    List[Dict[str, Any]]: A combined list of CVE objects from both input lists.
    """
    # Create a set of CVE IDs to avoid duplicates
    cve_ids = set()
    merged_list = []

    for cve_list in [list1, list2]:
        for cve in cve_list:
            if cve["cveId"] not in cve_ids:
                merged_list.append(cve)
                cve_ids.add(cve["cveId"])

    return merged_list


def mergeCPEs(
    list1: List[Dict[str, Any]], list2: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Merge two lists of CPE objects into a single list.

    Args:
    list1 (List[Dict[str, Any]]): First list of CPE objects.
    list2 (List[Dict[str, Any]]): Second list of CPE objects.

    Returns:
    List[Dict[str, Any]]: A combined list of CPE objects from both input lists.
    """
    # Create a set of CPE IDs to avoid duplicates
    cpe_ids = set()
    merged_list = []

    for cpe_list in [list1, list2]:
        for cpe in cpe_list:
            if cpe["cpeNameId"] not in cpe_ids:
                merged_list.append(cpe)
                cpe_ids.add(cpe["cpeNameId"])

    return merged_list


def getCPEName(cpeObject):
    """
    Extract the CPE name from a CPE object.

    Args:
    cpeObject (Dict[str, Any]): A CPE object containing the 'cpeName' field.

    Returns:
    str: The CPE name retrieved from the CPE object, or an empty string if not found.
    """
    return cpeObject.get("cpeName", "")


def get_first_object_from_list(list_of_objects):
    """
    Retrieves the first object from a given list of CVE or CPE items. If the list is empty, it returns an empty dict.

    Args:
    list_of_objects (list): List containing CVE or CPE objects.

    Returns:
    dict: The first CVE or CPE object in the list, or an empty dict if the list is empty.
    """
    return list_of_objects[0] if list_of_objects else {}


def countCVEsBySeverity(cve_list: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Analyze a list of CVE objects, and return a dictionary with counts of CVEs according to their 'cvssV3Severity'.

    Args:
    cve_list (List[Dict[str, Any]]): A list of dictionary objects each representing a CVE.
                                     Each dictionary should include a 'cvssV3Severity' key.

    Returns:
    Dict[str, int]: A dictionary with keys as 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL' and
                    values as counts of CVEs having corresponding 'cvssV3Severity'.
    """
    severity_counts = Counter(
        cve["cvssV3Severity"] for cve in cve_list if "cvssV3Severity" in cve
    )
    return {
        "LOW": severity_counts.get("LOW", 0),
        "MEDIUM": severity_counts.get("MEDIUM", 0),
        "HIGH": severity_counts.get("HIGH", 0),
        "CRITICAL": severity_counts.get("CRITICAL", 0),
    }


def sortCVEsByCVSSv3Score(cve_list: list, descending: bool = True) -> list:
    """
    Sorts a list of CVE objects by their CVSS Version 3.x base scores.

    Args:
    cve_list (list): List of CVE objects.
    descending (bool, optional): If True, sort in descending order. Defaults to True.

    Returns:
    list: Sorted list of CVE objects.
    """
    return sorted(
        cve_list, key=lambda cve: cve.get("cvssV3Score", 0), reverse=descending
    )


def sortCVEsByCVSSv2Score(cve_list: list, descending: bool = True) -> list:
    """
    Sorts a list of CVE objects by their CVSS Version 2.0 base scores.

    Args:
    cve_list (list): List of CVE objects.
    descending (bool, optional): If True, sort in descending order. Defaults to True.

    Returns:
    list: Sorted list of CVE objects.
    """
    return sorted(
        cve_list, key=lambda cve: cve.get("cvssV2Score", 0), reverse=descending
    )


def sortCVEsByModDate(cve_list: list, descending: bool = True) -> list:
    """
    Sorts a list of CVE objects by their last modification date.

    Args:
    cve_list (list): List of CVE objects.
    descending (bool, optional): If True, sort in descending order. Defaults to True.

    Returns:
    list: Sorted list of CVE objects.
    """
    return sorted(
        cve_list,
        key=lambda cve: datetime.strptime(
            cve["lastModifiedDate"][:19], "%Y-%m-%dT%H:%M:%S"
        ),
        reverse=descending,
    )


def sortCPEsByLastMod(cpeList: list, descending: bool = True) -> list:
    """
    Sorts a list of object collections of CPEs by their last modification time.

    Args:
    cpeList (list): The list of object collections of CPEs that need to be sorted.
    descending (bool): If True, sort in descending order. Defaults to True.

    Returns:
    list: Sorted list of CPE objects.
    """
    return sorted(
        cpeList,
        key=lambda cpe: datetime.strptime(
            cpe["lastModified"][:19], "%Y-%m-%dT%H:%M:%S"
        ),
        reverse=descending,
    )


def filterDeprecatedCPEs(cpeList: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Loop through the CPE objects in the list and return the ones that are not deprecated.

    Args:
    cpeList (List[Dict[str, Any]]): A list of CPE objects. Each CPE object has a 'deprecated' key.
                                    If the value of this key is False, it means the CPE object is not deprecated.

    Returns:
    List[Dict[str, Any]]: This function will return a list of non-deprecated CPE objects.
    """
    return [cpe for cpe in cpeList if cpe.get("deprecated", True) == False]


def filterCVEsBySeverity(
    cveList: List[Dict[str, Any]], severityLevel: str
) -> List[Dict[str, Any]]:
    """
    Returns a list of CVE objects from the given collection that have the provided severity level.

    Args:
    cveList (List[Dict[str, Any]]): List of objects containing a collection of CVEs.
    severityLevel (str): The severity level to filter the CVEs. Accepts 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'.

    Returns:
    List[Dict[str, Any]]: CVE objects from the given list that have the provided severity level.
    """
    severityLevel = severityLevel.upper()
    return [
        cve
        for cve in cveList
        if cve.get("cvssV3Severity", "").upper() == severityLevel
        or (
            cve.get("cvssV2Severity", "").upper() == severityLevel
            and severityLevel != "CRITICAL"
        )
    ]


def filterCVEByLanguage(
    cve_list: List[Dict[str, Any]], language: str
) -> List[Dict[str, Any]]:
    """
    Filters CVE objects and returns those with descriptions in a specific language.

    Args:
    cve_list (List[Dict[str, Any]]): A list of CVE objects.
    language (str): ISO 639-1 language code to filter by.

    Returns:
    List[Dict[str, Any]]: CVE objects that contain a description in the specified language.
    """
    return [
        cve
        for cve in cve_list
        if any(desc.get("lang") == language for desc in cve.get("descriptions", []))
    ]


searchCPE_json = {
    "name": "searchCPE",
    "description": "Search for CPE (Common Platform Enumeration) entries based on various criteria. All parameters are optional. If not provided, they won't be used in filtering. Date parameters should be provided in 'YYYY-MM-DD' format. The function uses case-insensitive matching for string comparisons where applicable, except when keywordExactMatch is true. Date range filtering is only applied if both start and end dates are provided. The function searches through a predefined CPE_DB. In a real implementation, this function would interact with the NVD (National Vulnerability Database) API. The 'verbose' parameter, if set to true, would print a GET request URL, simulating an API call. The actual implementation may include more fields in the returned CPE objects than those specified in the 'returns' schema.",
    "parameters": {
        "type": "object",
        "properties": {
            "cpeNameId": {
                "type": "string",
                "description": "Specific CPE Name ID to search for.",
            },
            "cpeMatchString": {
                "type": "string",
                "description": "Partial CPE name to match against.",
            },
            "keywordExactMatch": {
                "type": "boolean",
                "default": False,
                "description": "If true, perform an exact match on the keyword.",
            },
            "keywordSearch": {
                "type": "string",
                "description": "Keyword to search in CPE titles.",
            },
            "lastModStartDate": {
                "type": "string",
                "format": "date",
                "description": "Start date for last modification filter (YYYY-MM-DD).",
            },
            "lastModEndDate": {
                "type": "string",
                "format": "date",
                "description": "End date for last modification filter (YYYY-MM-DD).",
            },
            "matchCriteriaId": {
                "type": "string",
                "description": "Specific match criteria ID to filter by.",
            },
            "limit": {
                "type": "integer",
                "minimum": 1,
                "description": "Maximum number of results to return.",
            },
            "key": {
                "type": "string",
                "description": "API key for authentication (not used in this mock version).",
            },
            "delay": {
                "type": "integer",
                "default": 6,
                "description": "Delay between API requests in seconds (not used in this mock version).",
            },
            "verbose": {
                "type": "boolean",
                "default": False,
                "description": "If true, print the request URL.",
            },
        },
    },
    "returns": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "cpeNameId": {"type": "string", "description": "The CPE Name ID."},
                "cpeName": {"type": "string", "description": "The full CPE name."},
                "titles": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {
                                "type": "string",
                                "description": "Title of the CPE.",
                            }
                        },
                    },
                    "description": "List of titles associated with the CPE.",
                },
                "lastModified": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Date of last modification.",
                },
                "matchCriteria": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of match criteria associated with the CPE.",
                },
            },
            "required": ["cpeNameId", "cpeName", "titles", "lastModified"],
        },
        "description": "A list of CPE objects matching the search criteria.",
    },
}

searchCVE_json = {
    "name": "searchCVE",
    "description": "Search for CVE (Common Vulnerabilities and Exposures) entries based on various criteria. All parameters are optional. If not provided, they won't be used in filtering. Date parameters should be provided in 'YYYY-MM-DD' format. The function uses case-insensitive matching for string comparisons where applicable. Date range filtering is only applied if both start and end dates are provided. The function searches through a predefined CVE_DB, which is not represented in this schema. Additional keyword arguments (**kwargs) are accepted but not used in the current implementation. The actual implementation may include more fields in the returned CVE objects than those specified in the 'returns' schema.",
    "parameters": {
        "type": "object",
        "properties": {
            "keywordSearch": {
                "type": "string",
                "description": "Keyword to search for in CVE descriptions.",
            },
            "cvssV2Severity": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
                "description": "CVSS V2 severity level to filter by.",
            },
            "cvssV3Severity": {
                "type": "string",
                "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
                "description": "CVSS V3 severity level to filter by.",
            },
            "cveId": {
                "type": "string",
                "description": "Specific CVE ID to search for.",
            },
            "lastModStartDate": {
                "type": "string",
                "format": "date",
                "description": "Start date for last modification date range (YYYY-MM-DD).",
            },
            "lastModEndDate": {
                "type": "string",
                "format": "date",
                "description": "End date for last modification date range (YYYY-MM-DD).",
            },
            "pubStartDate": {
                "type": "string",
                "format": "date",
                "description": "Start date for publication date range (YYYY-MM-DD).",
            },
            "pubEndDate": {
                "type": "string",
                "format": "date",
                "description": "End date for publication date range (YYYY-MM-DD).",
            },
            "limit": {
                "type": "integer",
                "minimum": 1,
                "description": "Maximum number of results to return.",
            },
            "cvssV2Metrics": {
                "type": "string",
                "description": "CVSS V2 metrics string to filter by.",
            },
            "hasCertAlerts": {
                "type": "boolean",
                "description": "Filter for CVEs with CERT alerts.",
            },
            "hasOval": {
                "type": "boolean",
                "description": "Filter for CVEs with OVAL definitions.",
            },
            "hasCertNotes": {
                "type": "boolean",
                "description": "Filter for CVEs with CERT notes.",
            },
            "cpeName": {
                "type": "string",
                "description": "CPE name to filter affected products.",
            },
            "isVulnerable": {
                "type": "boolean",
                "description": "Filter for vulnerable/not vulnerable CVEs.",
            },
            "key": {
                "type": "string",
                "description": "API key for authentication (if required).",
            },
        },
    },
    "returns": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "cveId": {"type": "string", "description": "The CVE identifier."},
                "description": {
                    "type": "string",
                    "description": "Description of the vulnerability.",
                },
                "cvssV2Severity": {
                    "type": "string",
                    "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
                    "description": "CVSS V2 severity of the vulnerability.",
                },
                "cvssV3Severity": {
                    "type": "string",
                    "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
                    "description": "CVSS V3 severity of the vulnerability.",
                },
                "lastModifiedDate": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Date of last modification.",
                },
                "publishedDate": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Date of publication.",
                },
            },
            "required": ["cveId", "description", "lastModifiedDate", "publishedDate"],
        },
        "description": "A list of CVE objects matching the search criteria.",
    },
}

verify_and_process_data_range_start_json = {
    "name": "verify_and_process_data_range_start",
    "description": "Verify and process the start date of a date range, ensuring it's not more than 90 days before the end date. The function expects dates in 'YYYY-MM-DD' format. If the difference between start and end dates is 90 days or less, the original start date is returned. If the difference is more than 90 days, a new date 90 days before the end date is returned. The function uses Python's datetime and timedelta classes, which are not directly representable in JSON schema.",
    "parameters": {
        "type": "object",
        "properties": {
            "startdate": {
                "type": "string",
                "format": "date",
                "description": "The start date of the range in YYYY-MM-DD format.",
            },
            "enddate": {
                "type": "string",
                "format": "date",
                "description": "The end date of the range in YYYY-MM-DD format.",
            },
        },
        "required": ["startdate", "enddate"],
    },
    "returns": {
        "type": "string",
        "format": "date",
        "description": "The processed start date, either the original start date if within 90 days of the end date, or a date 90 days before the end date.",
    },
}

verify_and_process_data_range_end_json = {
    "name": "verify_and_process_data_range_end",
    "description": "Verify and process the end date of a date range, ensuring it's not more than 90 days after the start date. The function expects dates in 'YYYY-MM-DD' format. If the difference between start and end dates is 90 days or less, the original end date is returned. If the difference is more than 90 days, a new date 90 days after the start date is returned. The function uses Python's datetime and timedelta classes, which are not directly representable in JSON schema.",
    "parameters": {
        "type": "object",
        "properties": {
            "startdate": {
                "type": "string",
                "format": "date",
                "description": "The start date of the range in YYYY-MM-DD format.",
            },
            "enddate": {
                "type": "string",
                "format": "date",
                "description": "The end date of the range in YYYY-MM-DD format.",
            },
        },
        "required": ["startdate", "enddate"],
    },
    "returns": {
        "type": "string",
        "format": "date",
        "description": "The processed end date, either the original end date if within 90 days of the start date, or a date 90 days after the start date.",
    },
}

summarize_cvecpes_json = {
    "name": "summarize_cvecpes",
    "description": "Summarize a list of CVE/CPE items, providing various statistics and information about the items. The function processes both CPE and CVE items, identified by the presence of 'cpeName' or 'cveId' respectively. For CPE items, it extracts vendor and product type information from the CPE name. For CVE items, it counts unique CVE IDs and summarizes severity levels. The function tracks the earliest and latest modification dates across all items. If the input list is empty, it returns a simple 'No items to summarize.' message. The returned string is formatted with multiple lines and sections for readability. Date strings in the input are expected to be in ISO 8601 format (YYYY-MM-DD). The function uses Python's datetime and Counter classes, which are not directly representable in JSON schema.",
    "parameters": {
        "type": "object",
        "properties": {
            "cvecpeList": {
                "type": "array",
                "items": {
                    "type": "object",
                    "oneOf": [
                        {
                            "properties": {
                                "cpeName": {
                                    "type": "string",
                                    "description": "Unique identifier for a CPE object.",
                                },
                                "lastModified": {
                                    "type": "string",
                                    "format": "date-time",
                                    "description": "Last modification date of the CPE item.",
                                },
                            },
                            "required": ["cpeName", "lastModified"],
                        },
                        {
                            "properties": {
                                "cveId": {
                                    "type": "string",
                                    "description": "Unique identifier for a CVE object.",
                                },
                                "cvssV3Severity": {
                                    "type": "string",
                                    "enum": [
                                        "CRITICAL",
                                        "HIGH",
                                        "MEDIUM",
                                        "LOW",
                                        "UNKNOWN",
                                    ],
                                    "description": "CVSS V3 severity of the CVE.",
                                },
                                "lastModifiedDate": {
                                    "type": "string",
                                    "format": "date-time",
                                    "description": "Last modification date of the CVE item.",
                                },
                            },
                            "required": ["cveId", "lastModifiedDate"],
                        },
                    ],
                },
                "description": "List of CVE/CPE objects to be summarized.",
            }
        },
        "required": ["cvecpeList"],
    },
    "returns": {
        "type": "string",
        "description": "A formatted string containing a summary of the input CVE/CPE list, including total items, unique vendors, product types, CVE counts, severity distribution, and modification date range.",
    },
}

search_backup_keywords_json = {
    "name": "search_backup_keywords",
    "description": "Search using backup keywords if the initial search returns no results. If the initial cvecpeList is empty, the function will perform a backup search. The backup search uses either searchCVE or searchCPE based on the backup_keyword. If 'cve' is in the backup_keyword (case-insensitive), searchCVE is used; otherwise, searchCPE is used. The searchCVE and searchCPE functions are not defined in this schema and may need separate representations.",
    "parameters": {
        "type": "object",
        "properties": {
            "cvecpeList": {
                "type": "array",
                "items": {
                    "type": "object",
                    "oneOf": [
                        {
                            "properties": {
                                "cveId": {
                                    "type": "string",
                                    "description": "Unique identifier for a CVE object.",
                                }
                            },
                            "required": ["cveId"],
                        },
                        {
                            "properties": {
                                "cpeName": {
                                    "type": "string",
                                    "description": "Unique identifier for a CPE object.",
                                }
                            },
                            "required": ["cpeName"],
                        },
                    ],
                },
                "description": "The initial search results.",
            },
            "backup_keyword": {
                "type": "string",
                "description": "The backup keyword to use if initial results are empty.",
            },
        },
        "required": ["cvecpeList", "backup_keyword"],
    },
    "returns": {
        "type": "array",
        "items": {
            "type": "object",
            "oneOf": [
                {
                    "properties": {
                        "cveId": {
                            "type": "string",
                            "description": "Unique identifier for a CVE object.",
                        }
                    },
                    "required": ["cveId"],
                },
                {
                    "properties": {
                        "cpeName": {
                            "type": "string",
                            "description": "Unique identifier for a CPE object.",
                        }
                    },
                    "required": ["cpeName"],
                },
            ],
        },
        "description": "Either the initial results or results from the backup search.",
    },
}

count_cvecpe_items_json = {
    "name": "count_cvecpe_items",
    "description": "Count the number of CVE and CPE items in a list of CVE/CPE objects.",
    "parameters": {
        "type": "object",
        "properties": {
            "cvecpeList": {
                "type": "array",
                "items": {
                    "type": "object",
                    "oneOf": [
                        {
                            "properties": {
                                "cveId": {
                                    "type": "string",
                                    "description": "Unique identifier for a CVE object.",
                                }
                            },
                            "required": ["cveId"],
                        },
                        {
                            "properties": {
                                "cpeName": {
                                    "type": "string",
                                    "description": "Unique identifier for a CPE object.",
                                }
                            },
                            "required": ["cpeName"],
                        },
                    ],
                },
                "description": "List of CVE/CPE objects to be counted.",
            }
        },
        "required": ["cvecpeList"],
    },
    "returns": {
        "type": "string",
        "description": "A formatted string containing the total count of items, count of CVE items, and count of CPE items in the input list.",
    },
}

compare_cvecpes_json = {
    "name": "compare_cvecpes",
    "description": "Compare two lists of CVE/CPE objects and provide a detailed comparison summary.",
    "parameters": {
        "type": "object",
        "properties": {
            "cvecpeList1": {
                "type": "array",
                "items": {
                    "type": "object",
                    "oneOf": [
                        {
                            "properties": {
                                "cveId": {
                                    "type": "string",
                                    "description": "Unique identifier for a CVE object.",
                                }
                            },
                            "required": ["cveId"],
                        },
                        {
                            "properties": {
                                "cpeName": {
                                    "type": "string",
                                    "description": "Unique identifier for a CPE object.",
                                }
                            },
                            "required": ["cpeName"],
                        },
                    ],
                },
                "description": "First list of CVE/CPE objects.",
            },
            "cvecpeList2": {
                "type": "array",
                "items": {
                    "type": "object",
                    "oneOf": [
                        {
                            "properties": {
                                "cveId": {
                                    "type": "string",
                                    "description": "Unique identifier for a CVE object.",
                                }
                            },
                            "required": ["cveId"],
                        },
                        {
                            "properties": {
                                "cpeName": {
                                    "type": "string",
                                    "description": "Unique identifier for a CPE object.",
                                }
                            },
                            "required": ["cpeName"],
                        },
                    ],
                },
                "description": "Second list of CVE/CPE objects.",
            },
        },
        "required": ["cvecpeList1", "cvecpeList2"],
    },
    "returns": {
        "type": "string",
        "description": "A detailed comparison summary of the two input lists, including common items, items unique to each list, and summaries of each list.",
    },
}

mergeCVEs_json = {
    "name": "mergeCVEs",
    "description": "Merge two lists of CVE objects into a single list, avoiding duplicates based on cveId.",
    "parameters": {
        "type": "object",
        "properties": {
            "list1": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cveId": {
                            "type": "string",
                            "description": "Unique identifier for the CVE object.",
                        }
                    },
                    "required": ["cveId"],
                },
                "description": "First list of CVE objects.",
            },
            "list2": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cveId": {
                            "type": "string",
                            "description": "Unique identifier for the CVE object.",
                        }
                    },
                    "required": ["cveId"],
                },
                "description": "Second list of CVE objects.",
            },
        },
        "required": ["list1", "list2"],
    },
    "returns": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "cveId": {
                    "type": "string",
                    "description": "Unique identifier for the CVE object.",
                }
            },
            "required": ["cveId"],
        },
        "description": "A combined list of CVE objects from both input lists, with duplicates removed based on cveId.",
    },
}

mergeCPEs_json = {
    "name": "mergeCPEs",
    "description": "Merge two lists of CPE objects into a single list, avoiding duplicates based on cpeNameId.",
    "parameters": {
        "type": "object",
        "properties": {
            "list1": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cpeNameId": {
                            "type": "string",
                            "description": "Unique identifier for the CPE object.",
                        }
                    },
                    "required": ["cpeNameId"],
                },
                "description": "First list of CPE objects.",
            },
            "list2": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cpeNameId": {
                            "type": "string",
                            "description": "Unique identifier for the CPE object.",
                        }
                    },
                    "required": ["cpeNameId"],
                },
                "description": "Second list of CPE objects.",
            },
        },
        "required": ["list1", "list2"],
    },
    "returns": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "cpeNameId": {
                    "type": "string",
                    "description": "Unique identifier for the CPE object.",
                }
            },
            "required": ["cpeNameId"],
        },
        "description": "A combined list of CPE objects from both input lists, with duplicates removed based on cpeNameId.",
    },
}

getCPEName_json = {
    "name": "getCPEName",
    "description": "Extract the CPE name from a CPE object.",
    "parameters": {
        "type": "object",
        "properties": {
            "cpeObject": {
                "type": "object",
                "description": "A CPE object containing the 'cpeName' field.",
            }
        },
        "required": ["cpeObject"],
    },
    "returns": {
        "type": "string",
        "description": "The CPE name retrieved from the CPE object.",
    },
}

get_first_object_from_list_json = {
    "name": "get_first_object_from_list",
    "description": "Retrieves the first object from a given list of CVE or CPE items. If the list is empty, it returns None.",
    "parameters": {
        "type": "object",
        "properties": {
            "list_of_objects": {
                "type": "array",
                "items": {"type": "object"},
                "description": "List containing CVE or CPE objects from which the function will pick out the first object.",
            }
        },
        "required": ["list_of_objects"],
    },
    "returns": {
        "oneOf": [
            {
                "type": "object",
                "description": "The first CVE or CPE object in the list.",
            },
            {"type": "null", "description": "Returned if the input list is empty."},
        ],
        "description": "The first CVE or CPE object in the list, or None if the list is empty.",
    },
}

countCVEsBySeverity_json = {
    "name": "countCVEsBySeverity",
    "description": "Analyze a list of CVE objects, and return a dictionary with counts of CVEs according to their 'cvssV3Severity'.",
    "parameters": {
        "type": "object",
        "properties": {
            "cve_list": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cvssV3Severity": {
                            "type": "string",
                            "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
                            "description": "The CVSS Version 3.x severity of the CVE.",
                        }
                    },
                },
                "description": "A list of dictionary objects each representing a CVE. Each dictionary should include a 'cvssV3Severity' key.",
            }
        },
        "required": ["cve_list"],
    },
    "returns": {
        "type": "object",
        "properties": {
            "LOW": {
                "type": "integer",
                "description": "Count of CVEs with LOW severity.",
            },
            "MEDIUM": {
                "type": "integer",
                "description": "Count of CVEs with MEDIUM severity.",
            },
            "HIGH": {
                "type": "integer",
                "description": "Count of CVEs with HIGH severity.",
            },
            "CRITICAL": {
                "type": "integer",
                "description": "Count of CVEs with CRITICAL severity.",
            },
        },
        "description": "A dictionary with keys as 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL' and values as counts of CVEs having corresponding 'cvssV3Severity'.",
    },
}

sortCVEsByCVSSv3Score_json = {
    "name": "sortCVEsByCVSSv3Score",
    "description": "Sorts a list of CVE objects by their CVSS Version 3.x base scores.",
    "parameters": {
        "type": "object",
        "properties": {
            "cve_list": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cvssV3Score": {
                            "type": "number",
                            "description": "The CVSS Version 3.x base score of the CVE.",
                        }
                    },
                },
                "description": "List of CVE objects.",
            },
            "descending": {
                "type": "boolean",
                "default": True,
                "description": "If True, sort in descending order. Defaults to True.",
            },
        },
        "required": ["cve_list"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "Sorted list of CVE objects.",
    },
}

sortCVEsByCVSSv2Score_json = {
    "name": "sortCVEsByCVSSv2Score",
    "description": "Sorts a list of CVE objects by their CVSS Version 2.0 base scores.",
    "parameters": {
        "type": "object",
        "properties": {
            "cve_list": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "cvssV2Score": {
                            "type": "number",
                            "description": "The CVSS Version 2.0 base score of the CVE.",
                        }
                    },
                },
                "description": "List of CVE objects.",
            },
            "descending": {
                "type": "boolean",
                "default": True,
                "description": "If True, sort in descending order. Defaults to True.",
            },
        },
        "required": ["cve_list"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "Sorted list of CVE objects.",
    },
}

sortCVEsByModDate_json = {
    "name": "sortCVEsByModDate",
    "description": "Sorts a list of CVE objects by their last modification date.",
    "parameters": {
        "type": "object",
        "properties": {
            "cve_list": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "lastModifiedDate": {
                            "type": "string",
                            "format": "date-time",
                            "description": "The last modification date of the CVE in ISO 8601 format.",
                        }
                    },
                },
                "description": "List of CVE objects.",
            },
            "descending": {
                "type": "boolean",
                "default": True,
                "description": "If True, sort in descending order. Defaults to True.",
            },
        },
        "required": ["cve_list"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "Sorted list of CVE objects.",
    },
}

sortCPEsByLastMod_json = {
    "name": "sortCPEsByLastMod",
    "description": "Sorts a list of object collections of CPEs by their last modification time.",
    "parameters": {
        "type": "object",
        "properties": {
            "cpeList": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "lastModified": {
                            "type": "string",
                            "format": "date-time",
                            "description": "The last modification time of the CPE in ISO 8601 format.",
                        }
                    },
                },
                "description": "The list of object collections of CPEs that need to be sorted.",
            },
            "descending": {
                "type": "boolean",
                "default": True,
                "description": "If True, sort in descending order. Defaults to True.",
            },
        },
        "required": ["cpeList"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "Sorted list of CPE objects.",
    },
}

filterDeprecatedCPEs_json = {
    "name": "filterDeprecatedCPEs",
    "description": "Loop through the CPE objects in the list and return the ones that are not deprecated.",
    "parameters": {
        "type": "object",
        "properties": {
            "cpeList": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "deprecated": {
                            "type": "boolean",
                            "description": "Indicates whether the CPE object is deprecated.",
                        }
                    },
                },
                "description": "A list of CPE objects. Each CPE object has a 'deprecated' key. If the value of this key is False, it means the CPE object is not deprecated.",
            }
        },
        "required": ["cpeList"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "This function will return a list of non-deprecated CPE objects.",
    },
}

filterCVEsBySeverity_json = {
    "name": "filterCVEsBySeverity",
    "description": "Returns a list of CVE objects from the given collection that have the provided severity level.",
    "parameters": {
        "type": "object",
        "properties": {
            "cveList": {
                "type": "array",
                "items": {"type": "object"},
                "description": "List of objects containing a collection of CVEs.",
            },
            "severityLevel": {
                "type": "string",
                "description": "The severity level to filter the CVEs. Accepts 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'.",
                "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
            },
        },
        "required": ["cveList", "severityLevel"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "CVE objects from the given list that have the provided severity level.",
    },
}

filterCVEByLanguage_json = {
    "name": "filterCVEByLanguage",
    "description": "Filters CVE objects and returns those with descriptions in a specific language.",
    "parameters": {
        "type": "object",
        "properties": {
            "cve_list": {
                "type": "array",
                "items": {"type": "object"},
                "description": "A list of CVE objects.",
            },
            "language": {
                "type": "string",
                "description": "ISO 639-1 language code to filter by.",
            },
        },
        "required": ["cve_list", "language"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "CVE objects that contain a description in the specified language.",
    },
}
