# Week 7 Assignment: Shopping List Manager

Hands-on lab practising Python lists: indexing, `.append()`, `.remove()`, membership checks with `in`, and looping.

## Files

- `list_warmup.py` - creates a fruits list and demonstrates index access, append, remove and `len()`.
- `shopping_list.py` - a menu-driven shopping list manager (add / remove / show / done) that never crashes.
- `list_report.py` - prints a numbered list, counts names longer than 4 letters, and finds the longest name with a loop.
- `screenshots/` - screenshots of each program running.

## Why check `in` before `.remove()`?

Calling `.remove()` on an item that is not in the list raises a `ValueError` and crashes the program. Checking with `in` first lets the program handle a missing item gracefully by printing a friendly message instead. This makes the manager safe for users who mistype or forget what they added.
