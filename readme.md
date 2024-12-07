# ASTRONEER Folder Swap Script
This script is designed for the **Steam version of ASTRONEER** to help users easily switch between the current game version and another version stored locally. It also ensures the corresponding save data is swapped to maintain consistency.

### Installation
1. Go to Releases
2. Download executive file

### Setup
1. Place the script or executable file in the directory where the game is installed. The way to the directory should look something like this `.../SteamLibrary/steamapps/common`.
2. Ensure the `ASTRONEER_temp` folder exists in the game directory.
3. Optionally, create a shortcut to the executable and move it to your desktop for easier access.

## Notes
- The script automatically checks if the target folder exists before renaming.
- Temporary names are used to avoid overwriting folders during the swap.
- Ensure both `ASTRONEER_temp` and `Astro_temp` folders exist before running the script.

## Folder Paths
- **Game Folder**: `ASTRONEER` and `ASTRONEER_temp` in the current working directory.
- **AppData Folder**: `Astro` and `Astro_temp` in: `%LOCALAPPDATA%\Astro`