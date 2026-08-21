"""Human-readable size parsing."""

UNITS = {"B": 1, "KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}


def parse_size(text):
    """Turn a string like "10MB" into a byte count."""
    trimmed = text.strip()
    digits = "".join(char for char in trimmed if char.isdigit())
    unit = trimmed[len(digits):].upper()
    return int(digits) * UNITS[unit]


def format_size(count):
    """Turn a byte count into the largest whole unit that fits."""
    for name in ("GB", "MB", "KB"):
        if count >= UNITS[name]:
            return f"{count // UNITS[name]}{name}"
    return f"{count}B"
