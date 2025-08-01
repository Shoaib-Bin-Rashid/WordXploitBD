# WordXploitBD - Custom Wordlist Generator for BD
# Copyright (c) 2024 Shoaib Bin Rashid (R3D_XplOiT)
# Licensed under the MIT License

import os
import sys
import argparse


DEBUG = True
CHUNK_SIZE = 100000
password_counter = [0]

# Color functions for CLI
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def cyan(text): return color(text, '36')
def green(text): return color(text, '32')
def yellow(text): return color(text, '33')
def red(text): return color(text, '31')
def magenta(text): return color(text, '35')
def bold(text): return color(text, '1')
def gray(text): return color(text, '90')

def debug_print(msg):
    if DEBUG:
        print(msg)

# Data lists (BD context)
institutes = [
    'buet', 'du', 'ru', 'cu', 'ju', 'jnu', 'sust', 'kuet', 'cuet', 'ruet', 'ku', 'bup',
    'bracu', 'aiub', 'nsu', 'uiu', 'bubt', 'ulab', 'iub', 'eastwest', 'seu', 'uap',
    'iut', 'aust', 'dmc', 'cmc', 'rmc', 'mmc', 'smc',
    'notredame', 'viqarunnisa', 'rajuk', 'holycross', 'dhakacollege', 'citycollege', 'adamjee'
]
departments = [
    'cse', 'eee', 'bba', 'ict', 'law', 'mbbs', 'english', 'maths', 'physics', 'chemistry', 'pharmacy', 'civil', 'me', 'arch', 'textile', 'genetics', 'biotech', 'finance', 'marketing', 'hrm'
]
mobile_prefixes = ['017', '018', '019', '016', '015']
number_suffixes = [
    '123456', '654321', '111111', '222222', '333333', '444444', '555555', '666666', '777777', '888888', '999999',
    '112233', '223344', '334455', '445566', '556677', '667788', '778899', '889900', '121212', '232323', '343434',
    '565656', '787878', '909090', '123123', '321321', '456456', '789789', '147258', '258369', '369147', '101010',
    '202020', '303030', '404040', '505050', '606060', '707070', '808080', '909090'
]
prefixes = [
    'noob','not', 'pass', 'user', 'admin', 'login', 'welcome', 'test', 'guest', 'root', 'default', 'secret',
    'wifi', 'home', 'office', 'mobile', 'gmail', 'facebook', 'fb', 'insta', 'instagram', 'twitter', 'mail', 'email',
    'bd', 'bd71', 'boss', 'sir', 'madam', 'apu', 'vai', 'bhai', 'apa','gamer' ,'hacker'
]
common_suffixes = [
    'apu', 'vai', 'bhai', 'apa', 'boss', 'sir', 'madam',  'love',
    'bd', 'bd71', 'wifi', 'home', 'office', 'cricket', 'football','noob', 'not' ,'router' ,'com' ,'wifi', 
    'password', 'pass', 'user', 'admin', 'login', 'welcome', 'test', 'guest', 'root', 'default', 'secret',
    'mobile', 'gmail', 'facebook', 'fb', 'insta', 'instagram', 'twitter', 'mail', 'email' , 'net' , 'discord'
]
locations = [
    'dhaka', 'chittagong', 'ctg', 'khulna', 'rajshahi', 'sylhet', 'barisal', 'rangpur', 'mymensingh',
    'comilla', 'noakhali', 'gazipur', 'narayanganj', 'tangail', 'dinajpur', 'bogura', 'jessore', 'kushtia',
    'feni', 'coxbazar', 
    'mirpur', 'gulshan', 'uttara', 'banani', 'dhanmondi', 'motijheel', 'badda', 'mohammadpur', 'tejgaon', 'shyamoli', 'farmgate', 'lalbagh', 'paltan', 'ramna',
]
suffixes = common_suffixes + locations
special_chars = ['@', '_', '-', '.', '#', '!', '$', '&',]
sports_keywords  = [ 'messi10', 'ronaldo7', 'barca123', 'neymarjr', 'cr7', 'mbappe', 'haaland', 'bayern', 'realmadrid', 'barcelona', 'psg', 'liverpool', 'manutd', 'chelsea',]
keyboard_patterns = ['qwerty', 'asdf', 'zxcvbn', 'qazwsx', '1q2w3e', '1qaz2wsx', '1234qwer', '4321rewq']
common_passwords = [
     "12345678", "123456789", "1234567890", "987654321", "11223344", "password123",
    "admin1234", "qwerty123", "guest1234", "welcome123", "default123", "pass@1234",
    "bangladesh", "bangladesh71", "amarbangla", "deshpremi", "amardesh123",
    "khulnaghor", "ctglovers", "rajuk1234", "notredame1", "viqarunnisa1",
    "friend123", "loveyou12", "iloveyou1", "crush2023", "sadboy007", "lonelygal", 
    "eidmubarak", "ramadan23", "alhamdulillah", "bismillah1", "iftar2023", "iftar1234",
    "baba12345", "ma1234567", "apu123456", "vai123456", "boss12345",
    "sakibking", "cr7bd2023", "messi10bd", "pubgkingg", "freefire1",
    "wifi12345", "modem1234", "router1234", "netflixbd", "discord007",
    "youtube123", "gmail2023", "facebook1", "instagrm1", "test@1234",
    "adminadmin", "rootadmin", "superuser1", "coaching1", "student01",
    "ssc2020bd", "hsc2022bd", "examresult", "education1", "passward1","thispasswordisunique001",
    '12345678', '87654321', '123456789', '987654321', '1234567890', '0987654321',
    '11223344', '44332211', '11112222', '22221111', '12344321', '43211234',
    '12341234', '43214321', '11221122', '22112211', '123123123', '321321321',
    '1234567891', '123456780', '123456700', '1234567899', '11111111', '22222222', '33333333', '44444444', '55555555', '66666666', '77777777', '88888888', '99999999',
    '123456', '654321', '123123', '321321', '123321', '321123', '147258369', '963852741', '12369874', '98741236', '12344321', '43211234', '12341234', '43214321',
    '10101010', '20202020', '30303030', '40404040', '50505050', '60606060', '70707070', '80808080', '90909090',
    '12121212', '23232323', '34343434', '56565656', '78787878', '90909090', '1234123412', '9876987698', '11235813', '31415926'
]

tech_keywords = ['android', 'windows', 'iphone', 'samsung', 'realme', 'router', 'wifi', 'bluetooth', 'pubg', 'freefire']
cultural_keywords = ['allah', 'islam', 'quran', 'eidmubarak', 'bismillah', 'krishna', 'ramadan', 'shiv', 'masjid']
app_endings = ['.com', '.bd', '.mail.com', '.gmail.com', '.fb', '.insta', '.apk','.net', '.org', '.edu', '.gov', '.info', '.xyz', '.io','@gmial.com']


# Local slang, trending, and festival words
slang = [
    'bondhu', 'valobashi', 'shundor', 'boss', 'vai', 'apu', 'dost', 'pagol', 'bhalobasha', 'mon', 'shopno', 'shanti', 'baba', 'ma', 'bhai', 'apu', 'dada', 'didi', 'uncle', 'aunty'
]
festivals = [
    'eid', 'eidmubarak', 'ramadan', 'puja', 'durga', 'pohela', 'boishakh', 'bijoy', 'bijoydibosh', 'shadhinota', 'shadhinotadibosh', '1612', '2603', '1971'
]
brands = [
    'bkash', 'nagad', 'pathao', 'daraz', 'chaldal', 'evaly', 'shohoz', 'bikroy', 'rokomari', 'bproperty', 'pran', 'bata', 'priyoshop', 'grameenphone', 'robi', 'airtel', 'teletalk', 'banglalink'
]
magic_numbers = [
    '123', '007', '786', '111', '666', '999', '420',
    '1122', '1212', '2023', '2024', '2025', '69',
    '10', '11', '22', '33', '44', '55','1243','5678'
]

def smart_leetify(word):
    leet_map = {'a': '@', 'i': '1', 'e': '3', 'o': '0', 's': '$'}
    result = []
    replaced = set()
    for c in word:
        if c in leet_map and c not in replaced:
            result.append(leet_map[c])
            replaced.add(c)
        else:
            result.append(c)
    return ''.join(result)

def partial_leet_variants(word):
    variants = set()
    variants.add(word)
    if len(word) >= 4:
        variants.add(word[:2] + smart_leetify(word[2:]))
        variants.add(smart_leetify(word[:2]) + word[2:])
        variants.add(word.capitalize())
        variants.add(smart_leetify(word).capitalize())
    if len(word) >= 5:
        variants.add(smart_leetify(word))
    return variants

def case_variations(word):
    return {word, word.lower(), word.upper(), word.capitalize()}

def add(pw, buffer, seen, out_file):
    if 8 <= len(pw) <= 20 and pw not in seen:
        buffer.append(pw)
        seen.add(pw)
        password_counter[0] += 1
        if password_counter[0] % 1000000 == 0:
            print(magenta(f"🟣 Progress: {password_counter[0]:,} passwords generated..."))
        if len(buffer) >= CHUNK_SIZE:
            write_buffer(buffer, out_file)

def write_buffer(buffer, out_file):
    with open(out_file, "a", encoding="utf-8") as f:
        for pw in buffer:
            f.write(pw + "\n")
    buffer.clear()

def add_common_passwords(out_file):
    for pw in common_passwords:
        if 8 <= len(pw) <= 20:
            with open(out_file, "a", encoding="utf-8") as f:
                f.write(pw + "\n")

def save_final(buffer, out_file):
    if buffer:
        write_buffer(buffer, out_file)

def force_write_basic_emails(name_list, out_file):
    for name in name_list:
        with open(out_file, "a", encoding="utf-8") as f:
            f.write(f"{name.lower()}@gmail.com\n")

def smart_generate(name_list, buffer, seen, out_file):
    for idx, name in enumerate(name_list):
        for var in [name, name.capitalize()]:
            for pre in prefixes:
                add(pre + var, buffer, seen, out_file)
            for suf in suffixes:
                add(var + suf, buffer, seen, out_file)
            for pre in mobile_prefixes:
                for suf in number_suffixes:
                    add(var + pre + suf, buffer, seen, out_file)
            for d in range(1, 10):
                add(var + str(d), buffer, seen, out_file)
            for d in range(0, 100):
                add(var + str(d).zfill(2), buffer, seen, out_file)
            for d in range(0, 1000):
                add(var + str(d).zfill(3), buffer, seen, out_file)
            for d in range(0, 10000):
                add(var + str(d).zfill(4), buffer, seen, out_file)
            for suf in suffixes:
                for d in range(1, 10):
                    add(var + suf + str(d), buffer, seen, out_file)
                for d in range(0, 100):
                    add(var + suf + str(d).zfill(2), buffer, seen, out_file)
                for d in range(0, 1000):
                    add(var + suf + str(d).zfill(3), buffer, seen, out_file)
                for d in range(0, 10000):
                    add(var + suf + str(d).zfill(4), buffer, seen, out_file)
            for foot in sports_keywords:
                add(var + foot, buffer, seen, out_file)
            for ch in special_chars:
                add(var + ch, buffer, seen, out_file)
            for ch in special_chars:
                for d in range(1, 10):
                    add(var + ch + str(d), buffer, seen, out_file)
                for d in range(0, 100):
                    add(var + ch + str(d).zfill(2), buffer, seen, out_file)
                for d in range(0, 1000):
                    add(var + ch + str(d).zfill(3), buffer, seen, out_file)
                for d in range(0, 10000):
                    add(var + ch + str(d).zfill(4), buffer, seen, out_file)
            for ch in special_chars:
                for suf in suffixes:
                    add(var + ch + suf, buffer, seen, out_file)
            for ch in special_chars:
                for inst in institutes:
                    add(var + ch + inst, buffer, seen, out_file)
            for inst in institutes:
                add(var + inst, buffer, seen, out_file)
            for dept in departments:
                add(var + dept, buffer, seen, out_file)
            for ch in special_chars:
                for dept in departments:
                    add(var + ch + dept, buffer, seen, out_file)
            for pat in keyboard_patterns:
                add(var + pat, buffer, seen, out_file)
            for ch in special_chars:
                add(ch + var + ch, buffer, seen, out_file)

def extreme_generate(name_list, buffer, seen, out_file):
    numbers = [str(d) for d in range(1, 10)]
    numbers += [str(d).zfill(2) for d in range(0, 100)]
    numbers += [str(d).zfill(3) for d in range(0, 1000)]
    numbers += [str(d).zfill(4) for d in range(0, 10000)]
    for name in name_list:
        for variant in case_variations(name):
            leet_variants = partial_leet_variants(variant)
            for var in leet_variants:
                for num in numbers:
                    add(var + num, buffer, seen, out_file)
                    for ch in special_chars:
                        add(var + ch + num, buffer, seen, out_file)
                        add(var + num + ch, buffer, seen, out_file)
                        add(ch + var + num + ch, buffer, seen, out_file)
                for suf in suffixes:
                    add(var + suf, buffer, seen, out_file)
                    for num in numbers:
                        add(var + suf + num, buffer, seen, out_file)
                for dept in departments:
                    add(var + dept, buffer, seen, out_file)
                for inst in institutes:
                    add(var + inst, buffer, seen, out_file)
                for loc in locations:
                    add(var + loc, buffer, seen, out_file)
                for sport in sports_keywords:
                    add(var + sport, buffer, seen, out_file)
                for pat in keyboard_patterns:
                    add(var + pat, buffer, seen, out_file)
                for ch in special_chars:
                    add(ch + var + ch, buffer, seen, out_file)
                    for suf in (suffixes + tech_keywords + cultural_keywords):
                        add(var + ch + suf, buffer, seen, out_file)
                    for dept in departments:
                        add(var + ch + dept, buffer, seen, out_file)
                    for inst in institutes:
                        add(var + ch + inst, buffer, seen, out_file)
                    for sport in sports_keywords:
                        add(var + ch + sport, buffer, seen, out_file)
                # App-style: name.mail.com, name.fb, etc.
                for app in app_endings:
                    add(var.lower() + app, buffer, seen, out_file)
                    for num in magic_numbers:
                        add(var.lower() + num + app, buffer, seen, out_file)
                # Merged name combos from 2 names
                for n2 in name_list:
                    if n2 != name:
                        for combo in [
                            var + n2, n2 + var,
                            var.capitalize() + n2,
                            n2.capitalize() + var,
                            var + n2.capitalize(),
                            n2 + var.capitalize(),
                            var.capitalize() + n2.capitalize(),
                            n2.capitalize() + var.capitalize()
                        ]:
                            add(combo, buffer, seen, out_file)
                            for num in numbers:
                                add(combo + num, buffer, seen, out_file)
                            for ch in special_chars:
                                add(ch + combo + ch, buffer, seen, out_file)

def super_extreme_generate(name_list, buffer, seen, out_file):
    numbers = [str(d) for d in range(1, 10)]
    numbers += [str(d).zfill(2) for d in range(0, 100)]
    numbers += [str(d).zfill(3) for d in range(0, 1000)]
    numbers += [str(d).zfill(4) for d in range(0, 10000)]
    magic_numbers = [
        '123', '007', '786', '111', '666', '999', '420',
        '1122', '1212', '2023', '2024', '2025', '69',
        '10', '11', '22', '33', '44', '55','1243','5678'
    ]
    all_suffixes = list(set(suffixes + slang + festivals + brands))
    all_fields = all_suffixes + departments + institutes + locations + sports_keywords + keyboard_patterns + app_endings
    all_fields = list(set(all_fields))  # 🧼 CLEAN AND UNIQUE
    for name in name_list:
        for var in case_variations(name):
            for v in partial_leet_variants(var):
                lvar = smart_leetify(v)
                # 1. Basic patterns
                for num in numbers:
                    for ch in special_chars:
                        add(v + num, buffer, seen, out_file)
                        add(num + v, buffer, seen, out_file)
                        add(v + ch + num, buffer, seen, out_file)
                        add(v + num + ch, buffer, seen, out_file)
                        add(lvar + num, buffer, seen, out_file)
                        add(lvar + ch + num, buffer, seen, out_file)
                        if len(v) >= 7:
                            add(v + ch, buffer, seen, out_file)
                            add(ch + v, buffer, seen, out_file)
                        if len(lvar) >= 6:
                            add(ch + lvar + ch, buffer, seen, out_file)
                # 2. Field-based combos (heavy) — full numbers in realistic places
                for field in all_fields:
                    add(v + field, buffer, seen, out_file)
                    for num in numbers:
                        add(v + field + num, buffer, seen, out_file)
                    for num in magic_numbers:
                        for ch in special_chars:
                            add(v + ch + field + num, buffer, seen, out_file)
                            add(v + field + ch + num, buffer, seen, out_file)
                            add(field + v + ch + num, buffer, seen, out_file)
                # 3. Email combos — only lowercase, no sandwich, no case/leet
                for app in app_endings:
                    add(v.lower() + app, buffer, seen, out_file)
                    for num in magic_numbers:
                        add(v.lower() + num + app, buffer, seen, out_file)
                # 4. Prefix + name + number (e.g. gamershoaib11)
                for pre in prefixes:
                    for pre_var in case_variations(pre):
                        add(pre_var + v, buffer, seen, out_file)
                        for num in magic_numbers:
                            add(pre_var + v + num, buffer, seen, out_file)
                # 5. name + prefix (e.g. shoaibgamer)
                for pre in prefixes:
                    for pre_var in case_variations(pre):
                        add(v + pre_var, buffer, seen, out_file)
                        for num in magic_numbers:
                            add(v + pre_var + num, buffer, seen, out_file)
                # 6. Sandwich patterns
                if len(v) >= 6:
                    for ch1 in special_chars:
                        for ch2 in special_chars:
                            add(ch1 + v + ch2, buffer, seen, out_file)
                            for num in magic_numbers:
                                add(ch1 + v + num + ch2, buffer, seen, out_file)
                # 7. Leetify + suffix
                for suf in all_suffixes:
                    add(lvar + suf, buffer, seen, out_file)
                    for num in magic_numbers:
                        add(lvar + suf + num, buffer, seen, out_file)

def merge_names(name_list, buffer, seen, out_file, extreme_mode=False):
    for n1 in name_list:
        for n2 in name_list:
            if n1.lower() != n2.lower():
                combos = set()
                combos.add(n1 + n2)
                combos.add(n2 + n1)
                combos.add(n1.capitalize() + n2)
                combos.add(n2.capitalize() + n1)
                combos.add(n1 + n2.capitalize())
                combos.add(n2 + n1.capitalize())
                combos.add(n1.capitalize() + n2.capitalize())
                combos.add(n2.capitalize() + n1.capitalize())
                for suf in suffixes:
                    combos.add(n1 + n2 + suf)
                    combos.add(n2 + n1 + suf)
                for d in range(1, 10):
                    combos.add(n1 + n2 + str(d))
                    combos.add(n2 + n1 + str(d))
                for d in range(0, 100):
                    combos.add(n1 + n2 + str(d).zfill(2))
                    combos.add(n2 + n1 + str(d).zfill(2))
                for d in range(0, 1000):
                    combos.add(n1 + n2 + str(d).zfill(3))
                    combos.add(n2 + n1 + str(d).zfill(3))
                for d in range(0, 10000):
                    combos.add(n1 + n2 + str(d).zfill(4))
                    combos.add(n2 + n1 + str(d).zfill(4))
                for ch in special_chars:
                    combos.add(ch + n1 + n2 + ch)
                    combos.add(ch + n2 + n1 + ch)
                for combo in combos:
                    if extreme_mode:
                        for cased in case_variations(combo):
                            add(cased, buffer, seen, out_file)
                    else:
                        add(combo, buffer, seen, out_file)

def cupp_prompt():
    print(yellow("🔎 Enter as much info as you know (leave blank if unknown):"))
    name = input("Target's name: ").strip().lower()
    nickname = input("Nickname: ").strip().lower()
    birthdate = input("Birthdate (DDMMYYYY or YYYY): ").strip()
    partner = input("Partner's name: ").strip().lower()
    partner_nick = input("Partner's nickname: ").strip().lower()
    child = input("Child's name: ").strip().lower()
    pet = input("Pet's name: ").strip().lower()
    company = input("Company/School: ").strip().lower()
    team = input("Favorite team/player: ").strip().lower()
    extra = input("Any extra word (comma separated): ").strip().lower()
    name_list = [n for n in [name, nickname, partner, partner_nick, child, pet, company, team] if n]
    if extra:
        name_list += [e.strip() for e in extra.split(",") if e.strip()]
    return name, name_list

def cli_main():

    parser = argparse.ArgumentParser(
        description="WordXploitBD - Custom Wordlist Generator for BD"
    )
    parser.add_argument('--mode', choices=['smart', 'extreme', 'superextreme', 'batch'], required=True, help='Mode to use')
    parser.add_argument('--target', help='Target name (for single mode)')
    parser.add_argument('--batchfile', help='File with list of names (for batch mode)')
    parser.add_argument('--wordlistmode', choices=['smart', 'extreme'], help='Wordlist mode for batch (smart or extreme)')
    parser.add_argument('--output', help='Output file name (default: auto)')
    args = parser.parse_args()

    if args.mode == "batch":
        if not args.batchfile:
            print("❌ Please provide --batchfile for batch mode.")
            return
        if not args.wordlistmode:
            print("❌ Please provide --wordlistmode (smart or extreme) for batch mode.")
            return
        out_file = args.output if args.output else "batch_Xploit.txt"
        buffer = []
        seen = set()
        with open(args.batchfile, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]
        for name in names:
            print(gray("-" * 50))
            print(cyan(f"🔎 Generating wordlist for: {name} in {args.wordlistmode.upper()} mode"))
            name_list = [name]
            if args.wordlistmode == "smart":
                smart_generate(name_list, buffer, seen, out_file)
                merge_names(name_list, buffer, seen, out_file, extreme_mode=False)
            elif args.wordlistmode == "extreme":
                extreme_generate(name_list, buffer, seen, out_file)
                merge_names(name_list, buffer, seen, out_file, extreme_mode=True)
            force_write_basic_emails(name_list, out_file)
        add_common_passwords(out_file)
        save_final(buffer, out_file)
        print(green(f"✅ Batch wordlist generation complete! Saved to {bold(out_file)}"))
        print(bold(green(f"✅ Total unique passwords: {len(seen):,}")))
        file_size = os.path.getsize(out_file) / (1024 * 1024)
        print(cyan(f"🗂️  Final file size: {file_size:.2f} MB [Approx]"))
    else:
        if not args.target:
            print("❌ Please provide --target for single mode.")
            return
        name_list = [args.target]
        if args.output:
            out_file = args.output
        else:
            if args.mode == "smart":
                out_file = f"{args.target}_smart.txt"
            elif args.mode == "extreme":
                out_file = f"{args.target}_extreme.txt"
            else:
                out_file = f"{args.target}_super_extreme.txt"
        buffer = []
        seen = set()
        print(gray("-" * 50))
        print(cyan(f"🔎 Generating wordlist for: {args.target} in {args.mode.upper()} mode"))
        if args.mode == "smart":
            smart_generate(name_list, buffer, seen, out_file)
            merge_names(name_list, buffer, seen, out_file, extreme_mode=False)
        elif args.mode == "extreme":
            extreme_generate(name_list, buffer, seen, out_file)
            merge_names(name_list, buffer, seen, out_file, extreme_mode=True)
        elif args.mode == "superextreme":
            super_extreme_generate(name_list, buffer, seen, out_file)
        force_write_basic_emails(name_list, out_file)
        add_common_passwords(out_file)
        save_final(buffer, out_file)
        print(gray("-" * 50))
        print(green(f"✅ Wordlist generation complete! Saved to {bold(out_file)}"))
        print(bold(green(f"✅ Total unique passwords: {len(seen):,}")))
        file_size = os.path.getsize(out_file) / (1024 * 1024)
        print(cyan(f"🗂️  Final file size: {file_size:.2f} MB [Approx]"))

if __name__ == "__main__":
    print(bold(cyan("""
==================================================
||   WordXploitBD - Custom Wordlist Generator   ||
||       By Shoaib Bin Rashid (R3D_XplOiT)      ||
==================================================
""")))
    if len(sys.argv) > 1 and sys.argv[1].startswith('--'):
        cli_main()
    else:
    # interactive menu
        print(yellow("Which mode do you want to use?"))
        print(f"{green('[1]')} Target Mode (single name, as before)")
        print(f"{green('[2]')} Batch Mode (read names from file)")
        mode_type = input(cyan("Enter 1 or 2: ")).strip()
        if mode_type == "2":
            filename = input(yellow("Enter filename (e.g. names.txt): ")).strip()
            print(yellow("Which wordlist mode?"))
            print(f"{green('[1]')} Smart Xploit Mode")
            print(f"{green('[2]')} Extream Xploit Mode")
            mode = input(cyan("Enter 1 or 2: ")).strip()
            if mode == "2":
                mode = "extreme"
            else:
                mode = "smart"
            # Batch mode: all passwords go to one file
            out_file = "batch_Xploit.txt"
            buffer = []
            seen = set()
            with open(filename, "r", encoding="utf-8") as f:
                names = [line.strip() for line in f if line.strip()]
            for name in names:
                print(gray("-" * 50))
                print(cyan(f"🔎 Generating wordlist for: {name} in {mode.upper()} mode"))
                name_list = [name]
                if mode == "smart":
                    smart_generate(name_list, buffer, seen, out_file)
                    merge_names(name_list, buffer, seen, out_file, extreme_mode=False)
                elif mode == "extreme":
                    extreme_generate(name_list, buffer, seen, out_file)
                    merge_names(name_list, buffer, seen, out_file, extreme_mode=True)
                force_write_basic_emails(name_list, out_file)
            add_common_passwords(out_file)
            save_final(buffer, out_file)
            print(green(f"✅ Batch wordlist generation complete! Saved to {bold(out_file)}"))
            print(bold(green(f"✅ Total unique passwords: {len(seen):,}")))
            file_size = os.path.getsize(out_file) / (1024 * 1024)
            print(cyan(f"🗂️  Final file size: {file_size:.2f} MB [Approx]"))
        else:
            target_name, name_list = cupp_prompt()
            if not target_name:
                print(red("🚫 ERROR: No name entered."))
            else:
                print(gray("-" * 50))
                print(yellow("Which wordlist mode? [Press Enter for 1]"))
                print(f"{green('[1]')} Smart Xploit Mode (recommended)")
                print(f"{green('[2]')} Extream Xploit Mode (all combos, up to 3 fields)")
                print(f"{green('[3]')} Super Extream Xploit Mode (all possible deadly patterns, huge file!)")
                mode = input(cyan("Enter 1, 2, or 3: ")).strip()
                if mode == "3":
                    print(red("⚠️  This will generate a HUGE file and may take a long time!"))
                    print(red("⚠️  Using all deadly patterns, not all permutations, for efficiency."))
                    mode = "superextreme"
                    out_file = f"{target_name}_super_extreme.txt"
                elif mode == "2":
                    mode = "extreme"
                    out_file = f"{target_name}_extreme.txt"
                else:
                    mode = "smart"
                    out_file = f"{target_name}_smart.txt"
                buffer = []
                seen = set()
                print(gray("-" * 50))
                print(cyan(f"🔎 Generating wordlist for: {target_name} in {mode.upper()} mode"))
                if mode == "smart":
                    smart_generate(name_list, buffer, seen, out_file)
                    merge_names(name_list, buffer, seen, out_file, extreme_mode=False)
                elif mode == "extreme":
                    extreme_generate(name_list, buffer, seen, out_file)
                    merge_names(name_list, buffer, seen, out_file, extreme_mode=True)
                elif mode == "superextreme":
                    super_extreme_generate(name_list, buffer, seen, out_file)
                force_write_basic_emails(name_list, out_file)
                add_common_passwords(out_file)
                save_final(buffer, out_file)
                print(gray("-" * 50))
                print(green(f"✅ Wordlist generation complete! Saved to {bold(out_file)}"))
                print(bold(green(f"✅ Total unique passwords: {len(seen):,}")))
                file_size = os.path.getsize(out_file) / (1024 * 1024)
                print(cyan(f"🗂️  Final file size: {file_size:.2f} MB [Approx]"))