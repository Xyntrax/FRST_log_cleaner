# FRST Log Cleaner

An updated version of [SkeletalDemise's](https://github.com/SkeletalDemise/FRST_log_cleaner) FRST Log Cleaner with improved and added **Functionalities**.

## How It Works

1. Provide **FRST.txt** and **Addition.txt**
2. The tool removes lines containing known clean strings (*browser extensions, legitimate software vendors, etc.*)
3. Matching lines are removed from the cleaned logs and saved into a separate file so they can still be reviewed

## Output Files

The script creates a timestamped folder containing:

- **FRST_Cleaned.txt** and **Addition_Cleaned.txt** - Cleaned logs ready for triage
- **Whitelisted_Strings.txt** - Contains all of the removed clean entries

## Usage

### Automated Scan Mode

Automatically searches the *current directory* for **FRST.txt** and **Addition.txt**:

```
python Xyntrax-Updated_FRST_Log_Cleaner.py scan
```

### Manual File Input

```
python Xyntrax-Updated_FRST_Log_Cleaner.py FRST.txt Addition.txt
```
