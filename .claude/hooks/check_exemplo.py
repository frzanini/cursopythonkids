"""PostToolUse hook: valida sintaxe de exemplo.py editado (ver CLAUDE.md § Invariantes)."""
import json
import py_compile
import sys

payload = json.load(sys.stdin)
file_path = payload.get("tool_input", {}).get("file_path", "")

if not file_path.endswith("exemplo.py"):
    sys.exit(0)

try:
    py_compile.compile(file_path, doraise=True)
except py_compile.PyCompileError as exc:
    print(f"exemplo.py com erro de sintaxe:\n{exc}", file=sys.stderr)
    sys.exit(2)
