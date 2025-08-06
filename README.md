# WordXploitBD - Custom Wordlist Generator for BD
Developed by **Shoaib Bin Rashid (R3D_XplOiT)**

## 🚀 What is WordXploitBD?

WordXploitBD is a powerful, customizable Bangladeshi wordlist generator for red teamers, CTFers, penetration testers, and security researchers.

-   🇧🇩 BD-focused, real-world password patterns
-   🔥 Smart, Extreme, and Batch modes
-   🧑‍💻 CLI and interactive support
-   📦 Ready for GitHub and real-world use
----------

## 🛠️ Features

-   **Smart, Extreme, and Super Extreme modes**  for single target.
-   **Batch mode**: Generate wordlists for multiple names at once (all in one file).
-   **BD-style, real-world, and advanced password patterns**  for each name.
-   **Lowercase, realistic email combos**  (e.g.  `shoaib@gmail.com`,  `mridul123@gmail.com`).
-   **No sandwich, no case/leet, no special char around emails.**
-   **Common passwords**  (from leaks and BD usage) always added at the end.
-   **Always adds  `name@gmail.com`  for every name**  (for completeness).
-   **All passwords are 8-20 characters.**
-   **CLI and interactive menu**: Use as a script or as a command-line tool.
-   **Colorful, user-friendly output**.

----------

## 🖥️ Usage

### **Interactive Menu (Recommended for Beginners)**

```bash
python wordxploitbd.py
```

-   Choose Target or Batch mode from the menu.
-   Follow the prompts.

----------

### **CLI Mode (For Automation/Advanced Use)**

#### **Single Target (Smart Mode)**


```bash
python wordxploitbd.py --mode smart --target shoaib
```

➡️  _Smart wordlist for "shoaib" (output:  `shoaib_smart.txt`)_

#### **Single Target (Extreme Mode)**

```
python wordxploitbd.py --mode extreme --target mridul
```

➡️  _Extreme wordlist for "mridul" (output:  `mridul_extreme.txt`)_

#### **Single Target (Super Extreme Mode)**

```
python wordxploitbd.py --mode superextream --target oly
```

➡️  _Super extreme (huge) wordlist for "oly" (output:  `oly_super_extreme.txt`)_

#### **Batch Mode (Smart)**
```
python wordxploitbd.py --mode batch --batchfile names.txt --wordlistmode smart
```

➡️  _Smart wordlists for all names in  `names.txt`  (output:  `batch_Xploit.txt`)_

#### **Batch Mode (Extreme)**

----------

```
python wordxploitbd.py --mode batch --batchfile names.txt --wordlistmode extreme
```

➡️  _Extreme wordlists for all names in  `names.txt`  (output:  `batch_Xploit.txt`)_

#### **Custom Output File**

```
python wordxploitbd.py --mode smart --target arittro --output mylist.txt
```

➡️  _Saves the wordlist to  `mylist.txt`_

----------

## 📝 What You Get in the Output

-   All common BD-style, real-world, and advanced password patterns for each name.
-   Lowercase, realistic combos (e.g.  `shoaib123`,  `mridulbd2023`,  `arittro@bd`,  `olycr72025`).
-   Lowercase, real email combos (e.g.  `shoaib@gmail.com`,  `mridul123@gmail.com`).
-   No sandwich, no case/leet, no special char around emails.
-   Common passwords always added at the end.
-   Always adds  `name@gmail.com`  for every name.
-   All passwords are 8-20 characters.

----------

## 🧑‍💻 Sample Output Passwords [Batch Mode]

text

```
shoaib123 
shoaib2023 
shoaibbd2023 
shoaib007 
shoaibcr7 
shoaibadmin 
olybd2023 
olycr7bd 
oly007bd 
olyadmin 
oly123456 
olybd71 
arittro1a 
arittrobd 
arittro23 
arittrocr7 
arittro007 
arittrobd71 
mridul23 
mridulbd 
mridul007 
mridulcr7 
mridulbd71 
mridul123
...
```
----------

## 🏁 Quick Reference Table

| Command | What it does | Output file |
| --- | --- | --- |
| `python wordxploitbd.py --mode smart --target shoaib` | Smart wordlist for "shoaib" | `shoaib_smart.txt` |
| `python wordxploitbd.py --mode extreme --target arittro` | Extreme wordlist for "arittro" | `arittro_extreme.txt` |
| `python wordxploitbd.py --mode superextream --target oly` | Super extreme wordlist for "oly" | `oly_super_extreme.txt` |
| `python wordxploitbd.py --mode batch --batchfile names.txt --wordlistmode smart` | Smart wordlists for all names in file | `batch_Xploit.txt` |
| `python wordxploitbd.py --mode batch --batchfile names.txt --wordlistmode extreme` | Extreme wordlists for all names in file | `batch_Xploit.txt` |

----------

## 🛠️ Add Your Own Patterns

You can easily make WordXploitBD even more powerful and customized for your target by editing the data lists at the top of the script:

- **Add to `common_passwords`**  
  For static or leaked passwords you want to always include (e.g. `"bismillah123"`, `"boss2023"`, `"passwordbd"`).

- **Add to `app_endings`**  
  For more email domains or username endings (e.g. `@protonmail.com`, `@bkash.com`, `.xyz`, `.shop`).

- **Add to `magic_numbers`**  
  For more years, phone endings, lucky numbers, or batch/roll numbers (e.g. `"2010"`, `"017"`, `"2026"`, `"555"`).

- **Add to `prefixes` and `suffixes`**  
  For more BD nicknames, family words, company names, or any custom word (e.g. `"bossman"`, `"mama"`, `"tiger"`, `"ctg"`, `"pro"`).

- **Add to `locations`, `departments`, `institutes`, `sports_keywords`, `keyboard_patterns`**  
  To cover more real-world, BD, or target-specific patterns.

**Example:**  
If you want to add `"pro"`, `"tiger"`, and `"ctg"` as extra suffixes and prefixes, just add them to both lists:
```python
prefixes = [..., 'pro', 'tiger', 'ctg']
suffixes = [..., 'pro', 'tiger', 'ctg']
```
----------
## 🧪 Test Your Output

```bash
cat batch_Xploit.txt | grep "shoaib123"
cat batch_Xploit.txt | grep "mridulbd2023"
cat batch_Xploit.txt | grep "arittro@bd"
cat batch_Xploit.txt | grep "olycr7"
cat batch_Xploit.txt | grep "shoaibadmin"
cat batch_Xploit.txt | grep "mridul007"
cat batch_Xploit.txt | grep "arittrobd71"
```

----------

## 🏆 Tips

-   **Batch mode:**  Only Smart/Extreme, all passwords go to  `batch_Xploit.txt`.
-   **Target mode:**  All three modes, output per target.
-   **Common passwords always added at the end.**
-   **Always adds  `name@gmail.com`  for every name (for completeness).**
-   **All passwords are 8-20 characters.**

----------

## 👨‍💻 Contact

Developed by **Shoaib Bin Rashid (R3D_XplOiT)**

- **LinkedIn:** [Shoaib Bin Rashid](https://www.linkedin.com/in/shoaib-bin-rashid/)
- **Email:** shoaibbinrashid11@gmail.com
- **GitHub:** [Shoaib Bin Rashid](https://github.com/Shoaib-Bin-Rashid)
- **Twitter:** [@ShoaibBinRashi1](https://x.com/ShoaibBinRashi1)

## 📄 License

MIT License © 2025 Shoaib Bin Rashid (R3D_XplOiT)
