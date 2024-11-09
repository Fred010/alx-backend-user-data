#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']+'
    return re.sub(
            pattern, lambda match: match.group(1) + '=' + redaction, message)
