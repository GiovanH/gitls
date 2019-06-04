# import os
import glob
import git
# import traceback

import colorama

colorama.init()


dirs = ""
print(dirs)

flaglen = 1

for d in glob.glob("**/"):
    status = "." * flaglen

    try:
        repo = git.Repo(d)

        dirty = repo.is_dirty()

        remote = True
        try:
            rremote = repo.remote()
        except ValueError:
            remote = False

        status = "".join([
            # colorama.Fore.RED + "l" if dirty else colorama.Fore.GREEN + "r",
            colorama.Fore.RED + "d" if dirty else colorama.Fore.GREEN + "c"
        ])
    except git.exc.InvalidGitRepositoryError as e:
        status = colorama.Fore.LIGHTBLACK_EX + " " * flaglen
    except git.exc.GitCommandError:
        # traceback.print_exc()
        # print(d)
        status = colorama.Fore.YELLOW + "x" * flaglen

    print(" ", status, d)
print(colorama.Fore.RESET)
