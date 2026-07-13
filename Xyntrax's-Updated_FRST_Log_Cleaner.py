import os
import sys
import datetime

# clean and important
CLEAN_STRINGS = {
    "14EC5FE4-5B1E-42B9-9EDA-F281C1506E7A",
    "89B4C1CD-B018-4511-B0A1-5476DBF70820",
    "8203C095-FB62-4005-807D-7C9A3775D1EA",
    "Edge DefaultProfile: Default",
    "Edge Extension: (uBlock Origin)",
    "Edge Extension: (HTTPS Everywhere)",
    "Edge Extension: (Kaspersky Protection)",
    "Edge Extension: (Malwarebytes Browser Guard)",
    "Edge Extension: (Outlook)",
    "Edge Extension: (Word)",
    "Edge Extension: (Excel)",
    "Edge Extension: (PowerPoint)",
    "Edge Extension: (IDM Integration Module)",
    "Edge Extension: (Bitdefender Anti-tracker)",
    "FF Extension: (Avast Online Security)",
    "FF Extension: (Avast SafePrice | Comparison, deals, coupons)",
    "FF Extension: (Adblock Plus - free ad blocker)",
    "FF Extension: (uBlock Origin)",
    "FF Extension: (Adobe Acrobat)",
    "FF Extension: (Bitdefender Wallet)",
    "FF Extension: (Bitdefender Anti-tracker)",
    "FF Extension: (Bitdefender Antispam Toolbar)",
    "FF Extension: (IDM integration)",
    "FF Extension: (IDM CC)",
    "BRA Extension: (Malwarebytes Browser Guard)",
    "BRA Extension: (IDM Integration Module)",
    "BRA Extension: (Brave Local Data Files Updater)",
    "BRA Extension: (Brave Ad Block Updater (Default))",
    "BRA Extension: (Brave NTP sponsored images)",
    "BRA Extension: (Brave SpeedReader Updater)",
    "BRA Extension: (Brave HTTPS Everywhere Updater)",
    "OPR Extension: (Rich Hints Agent)",
    "OPR Extension: (Amazon Assistant Promotion)",
    "CHR Extension: (Google Drive)",
    "CHR Extension: (YouTube)",
    "CHR Extension: (uBlock Origin)",
    "CHR Extension: (HTTPS Everywhere)",
    "CHR Extension: (Chrome Web Store Payments)",
    "CHR Extension: (Gmail)",
    "CHR Extension: (Chrome Media Router)",
    "CHR Extension: (Slides)",
    "CHR Extension: (Docs)",
    "CHR Extension: (Sheets)",
    "CHR Extension: (Google Docs Offline)",
    "CHR Extension: (Kaspersky Protection)",
    "CHR Extension: (Grammarly for Chrome)",
    "CHR Extension: (Duolingo on the Web)",
    "CHR Extension: (Avast Online Security)",
    "CHR Extension: (Avast SafePrice | Comparison, deals, coupons)",
    "CHR Extension: (Adobe Acrobat)",
    "CHR Extension: (Malwarebytes Browser Guard)",
    "CHR Extension: (Emsisoft Browser Security)",
    "CHR Extension: (Decentraleyes)",
    "CHR Extension: (LocalCDN)",
    "CHR Extension: (User-Agent Switcher for Chrome)",
    "CHR Extension: (Quick source viewer)",
    "CHR Extension: (Decentraleyes)",
    "CHR Extension: (Tampermonkey)",
    "CHR Extension: (Dark Reader)",
    "CHR Extension: (IDM Integration Module)",
    "CHR Extension: (EditThisCookie)",
    "CHR Extension: (Cookie-Editor)",
    "CHR Extension: (BetterTTV)",
    "CHR Extension: (ColorPick Eyedropper)",
    "CHR Extension: (Proxy SwitchyOmega)",
    "CHR Extension: (Sci-Hub X Now!)",
    "CHR Extension: (Bypass Paywalls Clean)",
    "CHR Extension: (Untrusted Types for DevTools)",
    "CHR Extension: (Adblock Plus - free ad blocker)",
    "CHR Extension: (Privacy Badger)",
    "CHR Extension: (Google Translate)",
    "CHR Extension: (Adobe Acrobat: PDF edit, convert, sign tools)",
    "BRA Extension: (Wallet Data Files Updater)",
    "bojobppfploabceghnmlahpoonbcbacn", # Malwarebytes Browser Guard (edge)
    "jmjflgjpcpepeafmmgdpfkogkghcpiha", # Edge relevant text changes (edge)
    "aeblfdkhhhdcdjpifhhbdiojplfjncoa", # 1Password – Password Manager (chromium)
    "ihcjicgdanjaechkgeegckofjjedodee", # Malwarebytes Browser Guard (chromium)
    "ghbmnnjooekpmoecnnnilnnbdlolhkhi", # Google Docs Offline (chromium)
    "gighmmpiobklfepjocnamgkkbiglidom", # AdBlock — block ads across the web (chromium)
    "mmioliijnhnoblpgimnlajmefafdfilb", # Shazam: Find song names from your browser (chromium)
    "ponfpcnoihfmfllpaingbgckeeldkhle", # Enhancer for YouTube™ (chromium)
    "nkbihfbeogaeaoehlefnkodbefgpgknn", # MetaMask (chromium)
    "amaaokahonnfjjemodnpmeenfpnnbkco", # Grepper (chromium)
    "bcjindcccaagfpapjjmafapmmgkkhgoa", # JSON Formatter (chromium)
    "fbgcedjacmlbgleddnoacbnijgmiolem", # Microsoft Bing Search with Rewards (chromium)
    "gngocbkfmikdgphklgmmehbjjlfgdemm", # SwagButton (chromium)
    "pocpnlppkickgojjlmhdmidojbmbodfm", # Chromebook Recovery Utility (chromium)
    "R2 NVDisplay.ContainerLocalSystem;",
    "(2BrightSparks Pte Ltd )",
    "(Adobe Systems)",
    "(Audyssey Labs)",
    "(Broadcom)",
    "(Conexant Systems Inc.)",
    "(DTS)",
    "(DTS, Inc.)",
    "(Digimarc)",
    "(Discord Inc.)",
    "(Dolby Laboratories)",
    "(Dolby Laboratories, Inc.)",
    "(EldoS Corporation)",
    "(Farbar)",
    "(General Workings, Inc.)",
    "(Harman)",
    "(ICEpower a/s)",
    "(Igor Pavlov)",
    "(Initex)",
    "(Intel)",
    "(Khronos Group)",
    "(Mente Binária)",
    "(MicroWorld Technologies Inc.)",
    "(Mozilla Foundation)",
    "(Mozilla)",
    "(Oracle Corporation)",
    "(Other World Computing, Inc.)",
    "(Pango Inc)",
    "(Razer Inc)",
    "(Real Sound Lab SIA)",
    "(Realtek semiconductor)",
    "(SRS Labs, Inc.)",
    "(Seiko Epson Corporation)",
    "(Skype)",
    "(Sony Corporation)",
    "(Sound Research, Corp.)",
    "(Synopsys, Inc.)",
    "(Sysinternals - www.sysinternals.com)",
    "(TOSHIBA CORPORATION.)",
    "(TOSHIBA Corporation)",
    "(The ICU Project)",
    "(Tonec Inc.)",
    "(Toshiba Client Solutions Co., Ltd.)",
    "(VSO Software)",
    "(Virage Logic Corporation / Sonic Focus)",
    "(VoodooSoft, LLC)",
    "(Windows (R) Win 7 DDK provider)",
    "(Yamaha Corporation)",
    "(curl, hxxps://curl.se/)",
    "(Electronic Arts)",
    "(On2.com)",
    "(Logitech)",
    "(Tonec Inc.)",
    "2BrightSparks Pte. Ltd.",
    "A-Volute SAS",
    "A-Volute",
    "ARCAI",
    "ASROCK Incorporation",
    "ASUSTEK COMPUTER INC.",
    "ASUSTeK Computer Inc.",
    "AVB Disc Soft, SIA",
    "Acer Incorporated",
    "Acro Software Inc.",
    "Adobe Inc.",
    "Adobe Systems Incorporated",
    "Adobe Systems, Incorporated",
    "Advanced Micro Devices Inc.",
    "Advanced Micro Devices, Inc",
    "Advanced Micro Devices, Inc.",
    "Amazon.com Services LLC",
    "AnchorFree Inc",
    "Apple Inc.",
    "Autodesk, Inc.",
    "Avid Technology, Inc.",
    "BattlEye Innovations e.K.",
    "Beijing NormalSoft technology Co.,Ltd.",
    "Blizzard Entertainment, Inc.",
    "Bluestack Systems, Inc",
    "CPUID S.A.R.L.U.",
    "Canon Inc.",
    "Citrix Systems, Inc.",
    "Code Sector",
    "Conexant Systems, Inc.",
    "Corel Corporation",
    "Corsair Memory, Inc.",
    "Dell Inc",
    "Digiarty Software, Inc.",
    "Disc Soft Ltd",
    "Discord Inc.",
    "Dolby Laboratories, Inc.",
    "Dropbox, Inc",
    "ELAN Microelectronics Corp.",
    "EVGA Co., Ltd.",
    "EVGA Corp.",
    "EasyAntiCheat Oy",
    "EldoS Corporation",
    "Electronic Arts, Inc.",
    "Epic Games Inc.",
    "Even Balance, Inc.",
    "Figma, Inc.",
    "Flexera Software LLC",
    "Fortemedia Inc",
    "GIGA-BYTE TECHNOLOGY CO., LTD.",
    "Gaijin Network LTD",
    "Gemalto, Inc.",
    "Glarysoft LTD",
    "Global Media (Thailand) Co., Ltd",
    "GoTrustID Inc.",
    "Google Inc.",
    "Google LLC",
    "Guillaume Ryder (hxxp://utilfr42.free.fr)",
    "HP Inc.",
    "Hewlett Packard",
    "Hewlett-Packard Co.",
    "Hewlett-Packard Company",
    "Huawei Technologies Co., Ltd.",
    "INTEL CORP",
    "Initeks, OOO",
    "Initex",
    "Insecure.Com LLC",
    "Intel Corporation",
    "Intel(R) Corporation",
    "Intel(R) pGFX",
    "Ivaylo Beltchev",
    "Kilonova LLC",
    "Kristjan Skutta",
    "Lenovo (Beijing) Limited",
    "Lenovo",
    "Lenovo.",
    "LogMeIn, Inc.",
    "Logitech, Inc.",
    "MICRO-STAR INTERNATIONAL CO., LTD",
    "MICRO-STAR INTERNATIONAL CO., LTD.",
    "MICSYS Technology Co., Ltd.",
    "Mediafour Corporation",
    "Micro-Star International CO., LTD.",
    "Microsemi Corporation.",
    "Microsemi Storage Solutions Inc.",
    "Microsoft Corp.",
    "Microsoft Corporation",
    "Microsoft Windows",
    "MiniTool Solution Ltd",
    "Mozilla Corporation",
    "NVIDIA Corporation",
    "Node.js Foundation",
    "Notepad++",
    "Nuance Communications, Inc.",
    "OOO Lightshot",
    "Open Source Developer, Dominik Reichl",
    "OpenJS Foundation",
    "Oracle America, Inc.",
    "Other World Computing, Inc",
    "PACE Anti-Piracy, Inc.",
    "PC Micro Systems Inc.",
    "Pango Inc.",
    "Parsec Cloud, Inc.",
    "Piriform Software Ltd",
    "Primera Technology, Inc.",
    "QFX Software Corporation",
    "Qualcomm Atheros",
    "RealNetworks, Inc.",
    "Realtek Semiconductor Corp",
    "Realtek Semiconductor Corp.",
    "Red Giant Software LLC",
    "Riot Games, Inc.",
    "Riverbed Technology, Inc.",
    "Rivet Networks LLC",
    "Rockstar Games, Inc.",
    "SCREENOVATE TECHNOLOGIES LTD.",
    "SEIKO EPSON CORPORATION",
    "SEIKO EPSON Corporation",
    "Samsung Electronics CO., LTD.",
    "Samsung Electronics Co., Ltd.",
    "SanDisk Corporation",
    "Shaul Eizikovich",
    "Skype Software Sarl",
    "Smart Sound Technology",
    "SonicWall Inc.",
    "Sony Imaging Products & Solutions Inc.",
    "Sound Research Corporation",
    "Spotify AB",
    "SteelSeries ApS",
    "Sublime HQ Pty Ltd",
    "SurfRight B.V.",
    "Swift Media Entertainment, Inc.",
    "Symantec Corporation",
    "Synaptics Incorporated",
    "TEFINCOM S.A.",
    "TeamViewer Germany GmbH",
    "Threatstar B.V.",
    "Tonalio GmbH",
    "Tonec Inc.",
    "Travis Lee Robinson",
    "Valve Corp.",
    "Valve Corporation",
    "VideoLAN",
    "Wacom Co., Ltd.",
    "Wacom Technology Corp.",
    "Wacom Technology, Corp.",
    "Waves Inc",
    "Western Digital Technologies, Inc.",
    "Wondershare Technology Co.,Ltd",
    "X-Rite Incorporated",
    "magicJack, L.P.",
    "voidtools",
    "Mega Limited",
    "Shenzhen Evision Semiconductor Technology Co., Ltd",
    "Shenzhen Evision Semiconductor Technology Co.,Ltd.",
    "Shanghai Yitu Information Technology Co.,Ltd.",
    "e2eSoft",
    "PUBG CORPORATION",
    "Int3 Software AB",
    "Giga-Byte Technology",
    "Windows (R) Server 2003 DDK provider",
    "VMware, Inc.",
    "Firebit OU",
    "Rainmeter",
    "kernel-panik",
    "Razer USA Ltd.",
    "The CefSharp Authors",
    "Razer Inc.",
    "ASUSTeK COMPUTER INC.",
    "ASUSTek Computer Inc.",
    "Plex, Inc.",
    "DTS, Inc.",
    "Logitech Inc",
    "Logitech Inc.",
    "Gaijin Network Ltd",
    "Nefarius Software Solutions e.U.",
    "Riot Games, Inc",
    "Roblox Corporation",
    "Rockstar Games",
    "ROBLOX Corporation",
    "win.rar GmbH",
    "Microsoft Studios",
    "WHIRLWIND VIRTUAL REALITIES INC.",
    "Noriyuki MIYAZAKI",
    "Blizzard Entertainment",
    "BeamMP",
    "VoodooSoft, LLC",
    "(NVIDIA Corp.)",
    "Reincubate Ltd",
    "(Team Cherry)",
    "LunarG, Inc.",
    "Python Software Foundation",
    "Parsec Cloud Inc.",
    "Microsoft Corporation",
    "Oracle Corporation",
    "Epic Games, Inc.",
    "AutoHotkey Foundation LLC",
    "Igor Pavlov",
    "FOXIT SOFTWARE INC.",
    "philandro Software GmbH",
    "AnyDesk Software GmbH",
    "Foxit Software Inc.",
    "The Git Development Community",
    "Skutta, Kristjan",
    "Proton Technologies AG",
    "Jagex Limited",
    "Activision Publishing Inc",
    "Activision Blizzard, Inc.",
    "Micro-Star Int'l Co. Ltd.",
    "VS Revo Group Ltd.",
    "VS Revo Group",
    "Jagex Ltd",
    "Mozilla",
    "Nicholas H.Tollervey",
    "Newgrounds",
    "OBS Project",
    "Proton AG",
    "TeamViewer",
    "RuneLite",
    "Realtek",
    "PROXIMA BETA PTE. LIMITED",
    "KRAFTON, Inc.",
    "Advanced Micro Devices INC.",
    "Advanced Micro Devices",
    "LG Electronics Inc.",
    "Snap Inc.",
    "GOG  sp. z o.o",
    "GOG.com",
    "FACE IT LIMITED",
    "tinyBuild Games",
    "Wellbia.com Co., Ltd.",
    "Audacity Team",
    "CPUID, Inc.",
    "Bethesda Softworks",
    "BANDAI NAMCO Entertainment Inc.",
    "WhatsApp Inc.",
    "TechPowerUp LLC",
    "Ubisoft Entertainment Sweden AB",
    "Ring.com",
    "NZXT, Inc.",
    "Wondershare Technology Group Co.,Ltd",
    "Wondershare",
    "Voyetra Turtle Beach, Inc.",
    "ROCCAT",
    "Ferox Games B.V.",
    "Spotify Ltd",
    "Medal B.V.",
    "Logitech",
    "Lexikos",
    "Voicemod Sociedad Limitada",
    "Voicemod",
    "GoPro Inc.",
    "Twitch Interactive, Inc.",
    "Facebook, Inc.",
    "Chris Andriessen",
    "Moonsworth, LLC",
    "Now.gg, INC",
    "Vincent Burel",
    "Windows (R) Win 7 DDK provider",
    "(AMD)",
    "Disney",
    "Charles Milette",
    "Bandicam Company",
    "Conexant Systems LLC.",
    "The Qt Company Ltd.",
    "F.lux Software LLC",
    "f.lux Software LLC",
    ": %windir%\system32\compattelrunner.exe",
    "Synaptics Hong Kong Limited, Taiwan Branch (H.K.)",
    "TRACKER SOFTWARE PRODUCTS (CANADA) LIMITED",
    "Tracker Software Products (Canada) Ltd.",
    "Electronic Arts",
    "TranslucentTB Open Source Developers",
    "MSI Co., LTD",
    "Axiw Software",
    "Signify Netherlands B.V.",
    "rocksdanister",
    "Oculus VR, LLC",
    "Facebook Technologies, LLC",
    "Zoom Video Communications, Inc.",
    "Unity Technologies ApS",
    "Unity Technologies Inc.",
    "Ubisoft",
    "Chrome\\User Data\System Profile [",
    "ManyCam (VISICOM MÉDIA INC.)",
    "Visicom Media Inc.",
    "WindowsLiveWallpaper",
    "Chan Software Solutions",
    "Instagram",
    "Amazon Development Centre (London) Ltd",
    "Rémi Mercier",
    "Whirlwind FX (Whirlwind Virtual Realities Inc.)",
    "(Microsoft)",
    "ppy Pty Ltd",
    "Crystal Dew World",
    "(Meta)",
    "TranslucentTB",
    "CyberLink Corp.",
    "CyberLink",
    "GoPro Media, Inc.",
    "Hewlett-Packard Development Company, L.P.",
    "Virtual Desktop, Inc.",
    "BUREL VINCENT",
    "VB-AUDIO Software",
    "Silicon Motion, Inc.",
    "(Facebook Inc.)",
    "VB-Audio Software",
    "Red Giant   LLC",
    "Red Giant LLC",
    "Focusrite Audio Engineering Ltd.",
    "Focusrite Audio Engineering Ltd",
    "Focusrite Audio Engineering, Ltd.",
    "Psyonix, LLC",
    "(BetterDiscord)",
    "Bytedance Pte. Ltd.",
    "Mojang AB",
    "Mojang",
    "DISPLAYLINK (UK) LIMITED",
    "DisplayLink Corp.",
    "ASUSTek COMPUTER INC.",
    "(AMD Inc.)",
    "Docker Inc",
    "(ELAN Microelectronic Corp.)",
    "LIAN LI INDUSTRIAL CO., LTD.",
    "Lian-Li",
    "MUSIC Tribe Brands DE GmbH",
    "TC-Helicon Vocal Technologies Inc.",
    "Alexey Nicolaychuk",
    "Florian Höch",
    "Duet, Inc.",
    "Hugh Bailey",
    "Shenzhen Huion Animation Technology Co.,LTD",
    "ICEpower a/s",
    "ICEpower A/S",
    "COGNOSPHERE PTE. LTD.",
    "HoYoverse",
    "Corsair Components, Inc.",
    "Dell Technologies",
    "Monect (Suzhou) Co., Ltd.",
    "Monect, Inc.",
    "KRAFTON, Inc",
    "Stardock Corporation",
    "Stardock Software, Inc",
    "STARDOCK SYSTEMS, INC.",
    "Micro-Star INT'L CO., LTD.",
    "Sony Corporation",
    "ASUS",
    "ASUSTeK Computer Inc.",
    "ASUSTeK COMPUTER INC.",
    "KINGSTON COMPONENTS INC.",
    "Adobe Inc.",
    "Adobe Systems",
    "Voicemod Sociedad Limitada",
    "Voicemod",
    "win.rar GmbH",
    "Alexander Roshal",
}

IMPORTANT_STRINGS = {
    "<==== ATTENTION",
    "No File",
    "File not signed",
    "[not found]",
    "[X]",
    "Hidden",
    "no ImagePath",
    "detected!",
    "powershell",
}

WHITE_LIST = set()


def print_banner():
    # ANSI color codes
    DARK_BLUE = "\033[34m"
    DARK_ORANGE = "\033[38;5;208m"
    DARK_RED = "\033[31m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    banner = f"""
{WHITE}+----------------------------------------------------------------------+
{WHITE}|                                                                      |
|        {DARK_BLUE}          ███████╗██████╗ ███████╗████████╗{WHITE}                   |
|        {DARK_BLUE}          ██╔════╝██╔══██╗██╔════╝╚══██╔══╝{WHITE}                   |
|        {DARK_BLUE}          █████╗  ██████╔╝███████╗   ██║{WHITE}                      |
|        {DARK_BLUE}          ██╔══╝  ██╔══██╗╚════██║   ██║{WHITE}                      |
|        {DARK_BLUE}          ██║     ██║  ██║███████║   ██║{WHITE}                      |
|        {DARK_BLUE}          ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝{WHITE}                      |
|                                                                      |
|══════════════════════ {DARK_BLUE}FRST{WHITE} {DARK_ORANGE}Log Cleaner{WHITE} ══════════════════════════════|
|                                                                      |
|              {DARK_RED}► Forked and improved by Xyntrax{WHITE}                        |
|              {DARK_RED}► Originally made by SkeletalDemise{WHITE}                     |
|                                                                      |
{WHITE}+----------------------------------------------------------------------+{RESET}
"""
    print(banner)


def should_remove_line(line):
    contains_clean_string = any(clean_string in line for clean_string in CLEAN_STRINGS)
    contains_important_string = any(important_string in line for important_string in IMPORTANT_STRINGS)
    contains_white_list_string = any(white_string in line for white_string in WHITE_LIST)
    return contains_clean_string and not contains_important_string and not contains_white_list_string


def create_output_folder():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"FRST_Logs_Cleaned_{timestamp}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name


def clean_log(input_path, output_folder):
    cleaned_lines = []
    removed_lines = []
    original_lines = 0

    with open(input_path, encoding="utf-8") as oldfile:
        for line in oldfile:
            original_lines += 1
            line = line.replace("\u00AE", "(R)").replace("Ã‚", "")
            if should_remove_line(line):
                removed_lines.append(line)
            else:
                cleaned_lines.append(line)

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_folder, f"{base_name}_Cleaned.txt")
    with open(output_path, "w", encoding="utf-8") as newfile:
        newfile.writelines(cleaned_lines)

    return output_path, cleaned_lines, removed_lines, original_lines


def calculate_reduction(input_path, output_path, removed_count):
    original_log_size = os.path.getsize(input_path)
    cleaned_log_size = os.path.getsize(os.path.realpath(output_path))
    percent_reduction = (original_log_size - cleaned_log_size) / original_log_size * 100 if original_log_size > 0 else 0

    return {
        'original_size': original_log_size,
        'cleaned_size': cleaned_log_size,
        'reduction_percent': percent_reduction,
        'removed_count': removed_count
    }


def write_whitelist(output_folder, results):
    whitelist_path = os.path.join(output_folder, "Whitelisted_Strings.txt")
    with open(whitelist_path, "w", encoding="utf-8") as f:
        for file_name, data in results.items():
            f.write(f"============================={file_name} Removed Entries=============================\n")
            if data['removed_lines']:
                f.writelines(data['removed_lines'])
            else:
                f.write("(No entries removed)\n")
            f.write("\n")
    return whitelist_path


def print_summary(results, output_folder):
    print("\n" + "=" * 40)
    print("SUMMARY")
    print("=" * 40)

    total_original = 0
    total_cleaned = 0
    total_removed = 0

    for file_name, data in results.items():
        total_original += data['original_lines']
        total_cleaned += len(data['cleaned_lines'])
        total_removed += data['removed_count']

    for file_name, data in results.items():
        reduction = data['reduction_percent']
        print(f"\n{file_name}:")
        print(f"  - Original lines: {data['original_lines']:,}")
        print(f"  - Cleaned lines: {len(data['cleaned_lines']):,}")
        print(f"  - Lines removed: {data['removed_count']:,}")
        print(f"  - Size reduction: {int(reduction)}%")

    print(f"\nTotal:")
    print(f"  - Files processed: {len(results)}")
    print(f"  - Total original lines: {total_original:,}")
    print(f"  - Total cleaned lines: {total_cleaned:,}")
    print(f"  - Total lines removed: {total_removed:,}")

    print(f"\nOutput folder: {os.path.abspath(output_folder)}/")
    print("  - FRST_Cleaned.txt")
    print("  - Addition_Cleaned.txt")
    print("  - Whitelisted_Strings.txt")
    print("\nCleaning Complete")


def process_files(file_paths, output_folder):
    results = {}

    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        print(f"\nProcessing: {base_name}.txt")

        output_path, cleaned_lines, removed_lines, original_lines = clean_log(file_path, output_folder)
        stats = calculate_reduction(file_path, output_path, len(removed_lines))

        results[base_name] = {
            'cleaned_lines': cleaned_lines,
            'removed_lines': removed_lines,
            'original_lines': original_lines,
            'removed_count': len(removed_lines),
            'reduction_percent': stats['reduction_percent']
        }

        print(f"  - Original lines: {original_lines:,}")
        print(f"  - Cleaned lines: {len(cleaned_lines):,}")
        print(f"  - Lines removed: {len(removed_lines):,}")
        print(f"  - Size reduction: {int(stats['reduction_percent'])}%")

    return results


def scan_mode():
    files_found = []
    for filename in ["FRST.txt", "Addition.txt"]:
        if os.path.exists(filename):
            files_found.append(filename)

    if not files_found:
        print("\nFRST.txt & Addition.txt not found. Please check if they are on the same directory.")
        return None

    return files_found


def validate_files(file_list):

    ALLOWED_FILES = {"frst.txt", "addition.txt"}
    valid_files = []
    missing_files = []
    wrong_name_files = []

    for f in file_list:
        base_name = os.path.basename(f).lower()

        if not os.path.exists(f):
            missing_files.append(f)
        elif base_name not in ALLOWED_FILES:
            wrong_name_files.append(f)
        else:
            valid_files.append(f)

    return valid_files, missing_files, wrong_name_files


def main():
    print_banner()

    # Get raw input files from whatever source
    raw_files = None

    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "scan":
            raw_files = scan_mode()
        else:
            raw_files = sys.argv[1:]
    else:
        user_input = input("\nEnter file path(s) separated by space, or type 'scan' to auto-detect: ").strip()

        if user_input.lower() == "scan":
            raw_files = scan_mode()
        elif user_input:
            raw_files = user_input.split()
        else:
            print("No input provided.")
            return

    # If scan_mode returned None (no files found), exit
    if raw_files is None:
        return

    # Validate ALL files through the same pipeline
    valid_files, missing_files, wrong_name_files = validate_files(raw_files)

    # Report errors
    if missing_files:
        print(f"\nThese files do not exist: {', '.join(missing_files)}")
    if wrong_name_files:
        print(f"\nThese files are not supported (must be FRST.txt or Addition.txt): {', '.join(wrong_name_files)}")

    if not valid_files:
        print("No valid files found. Please check the file paths and try again.")
        return

    print(f"\nProcessing valid files: {', '.join(valid_files)}")
    files_to_process = valid_files

    output_folder = create_output_folder()
    print(f"\nOutput folder: {output_folder}/")

    results = process_files(files_to_process, output_folder)

    if not results:
        print("No files were processed.")
        return

    write_whitelist(output_folder, results)
    print_summary(results, output_folder)


if __name__ == "__main__":
    main()