# 🎨 ANSI Escape Codes for Terminal Formatting

ANSI escape codes are sequences of characters used to control text formatting, color, and cursor movement in terminal displays. These codes are widely supported on **Linux**, **macOS**, and some **Windows** terminals.

---

## 🚀 Why Use ANSI Escape Codes?

- ✅ Change text color  
- ✅ Apply styles like **bold**, *italic*, and __underline__  
- ✅ Reset formatting to avoid style carryover  
- ✅ Improve terminal output readability

---

## 🔤 Basic ANSI Escape Codes

| Code         | Effect            |
|--------------|-------------------|
| `\033[0m`     | Reset formatting  |
| `\033[1m`     | Bold text         |
| `\033[3m`     | Italic text       |
| `\033[4m`     | Underline text    |
| `\033[31m`    | Red text          |
| `\033[32m`    | Green text        |
| `\033[33m`    | Yellow text       |
| `\033[34m`    | Blue text         |
| `\033[1;33m`  | Bold + Yellow     |
| `\033[1;34m`  | Bold + Blue       |

---

## 🧪 Example Usage in Python

```python
print("\033[1;34mBold Blue Text\033[0m")      # Bold Blue
print("\033[3;31mItalic Red Text\033[0m")     # Italic Red
print("\033[4;32mUnderlined Green Text\033[0m")  # Underlined Green
📤 Output:
🔵 Bold Blue Text

🔴 Italic Red Text

🟢 Underlined Green Text

❓ Why Use \033[0m?
If you don't reset the formatting, the applied style may affect all subsequent terminal text.

❌ Without Reset:
python
Copy
Edit
print("\033[1mBold Text!")
print("Normal Text")  # This will also appear bold!
✅ With Reset:
python
Copy
Edit
print("\033[1mBold Text!\033[0m")
print("Normal Text")  # Back to normal
🎨 More Color Codes
Code	Color
\033[30m	Black
\033[31m	Red
\033[32m	Green
\033[33m	Yellow
\033[34m	Blue
\033[35m	Magenta
\033[36m	Cyan
\033[37m	White
✅ Conclusion
ANSI escape codes offer a simple, powerful way to enhance your terminal output:

Highlight important logs

Improve user experience in CLI apps

Make debugging easier with color-coded messages

📌 Tip: Windows Command Prompt may not support ANSI codes by default. For best results, use Windows Terminal or enable ANSI support in PowerShell.
