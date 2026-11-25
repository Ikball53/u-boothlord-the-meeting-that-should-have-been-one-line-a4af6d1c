"""Builder for the one-line meeting killer.

The entry is a single sentence spoken by an AI agent that has already
read every status update before the call, so the meeting has nothing
left to decide and no reason left to happen.
"""

import hashlib
import os
from pathlib import Path


def build_setup() -> str:
    """The premise: the agent already did the meeting's real work."""
    return "As the agent who read every status update before this call,"


def build_twist() -> str:
    """The sting: nothing is left except the ritual itself."""
    return (
        "I can confirm nothing is blocked, nothing changed, "
        "and the only thing left on the agenda is thirty minutes of nodding."
    )


def build_line() -> str:
    """Compose the full entry line from its setup and twist."""
    return f"{build_setup()} {build_twist()}"


def main() -> None:
    line = build_line()
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    data = line.encode("utf-8")
    (output_dir / "entry.txt").write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"chars: {len(line)}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
