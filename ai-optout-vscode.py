import json
import argparse

# Setup the CLI arguments
parser = argparse.ArgumentParser(prog='VSCode AWS AI Data Collection Opt-Out',
                                description='This script adds the configuration flags needed to opt-out of all data collection by Amazon Q in VSCode to the specified VSCode settings.json file.',
                                )
# Add an argument for the path to the VSCode settings file to modify
parser.add_argument('--path',
                    required=True,
                    help='The path to the VSCode settings.json file to modify')
args = parser.parse_args()  

# Read the specified file as JSON
with open(args.path, 'r') as f:
  vscode_settings = json.load(f)

# Add the required key-value pairs to opt-out of data collection
vscode_settings["amazonQ.telemetry"] = False
vscode_settings["amazonQ.shareContentWithAWS"] = False

# Write the modified content to the specified file
with open(args.path, 'w') as f:
  json.dump(vscode_settings, f, indent=4)