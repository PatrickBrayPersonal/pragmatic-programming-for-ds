import os
import json
import fire


def convert_files_to_launch_json(
    directory: str,
    launch_options: list,
    module: str,
    endswith: str = ".yaml",
    more_args: list = [],
):
    for file in os.listdir(directory):
        if file.endswith(endswith):
            filepath = os.path.join(directory, file)
            option = {
                "name": file,
                "type": "python",
                "request": "launch",
                "program": filepath,
                "console": "integratedTerminal",
                "justMyCode": True,
                "args": more_args,
            }
            launch_options.append(option)
    return launch_options


def debug_update():
    output_directory = r".vscode"
    launch_options = []
    launch_options = convert_files_to_launch_json(
        "notebooks/", launch_options, "features", endswith=".py"
    )
    current_file = {
        "name": "Python: Current File",
        "type": "python",
        "request": "launch",
        "program": "${file}",
        "console": "integratedTerminal",
        "justMyCode": True,
    }
    launch_options.append(current_file)
    launch_json = {"version": "0.2.0", "configurations": launch_options}
    os.makedirs(output_directory, exist_ok=True)
    with open(os.path.join(output_directory, "launch.json"), "w") as outfile:
        json.dump(launch_json, outfile, indent=2)
    print("successfully updated launch.json")


if __name__ == "__main__":
    fire.Fire()
