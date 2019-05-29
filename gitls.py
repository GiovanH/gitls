import os
import glob
import git
import traceback

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

        status = "".join([
            colorama.Fore.RED + "d" if dirty else colorama.Fore.GREEN + "c"
        ])
    except git.exc.InvalidGitRepositoryError as e:
        status = colorama.Fore.RESET + " " * flaglen
    except git.exc.GitCommandError:
        # traceback.print_exc()
        # print(d)
        status = colorama.Fore.CYAN + "x" * flaglen

    print(" ", status, d)
