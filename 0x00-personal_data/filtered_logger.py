#!/usr/bin/env python3
"""
Update the class to accept a list of strings fields constructor argument.
"""

import logging
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str) -> str:
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']+'
    return re.sub(
            pattern, lambda match: match.group(1) + '=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        # Use filter_datum to replace sensitive data in the message
        record.msg = filter_datum(
                self.fields,
                self.REDACTION,
                record.getMessage(), self.SEPARATOR)
        return super().format(record)
