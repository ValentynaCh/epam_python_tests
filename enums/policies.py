from enum import Enum


class Policies(Enum):
    investors = "INVESTORS",
    open_source = "OPEN SOURCE",
    privacy_policy = "PRIVACY POLICY",
    cookie_policy = "COOKIE POLICY",
    applicant_privacy_notice = "APPLICANT PRIVACY NOTICE",
    web_accessibility = "WEB ACCESSIBILITY",

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
