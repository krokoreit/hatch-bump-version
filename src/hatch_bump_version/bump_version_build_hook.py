import subprocess
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from .utils import get_git_tag, get_hatch_version, read_published_version


PRINT_DEBUG_ALLOWED = False
PRINT_DEBUG_TAG = "[BumpVersionBuildHook]"

def print_debug(*args, **kwargs):
    """Prints messages if PRINT_DEBUG_ALLOWED is True."""
    if PRINT_DEBUG_ALLOWED:
        print(PRINT_DEBUG_TAG + ": " + " ".join(map(str,args)), **kwargs)


class BumpVersionBuildHook(BuildHookInterface):
    PLUGIN_NAME = "bump_version" # use in [tool.hatch.build.hooks.bump_version]

    def initialize(self, version, build_data):
        """Compares build and published versions and bumps version if needed."""

        git_tag = get_git_tag()
        print_debug(f"git tag         = {git_tag}")

        # ToDo: may want to use hatch version later
        #hatch_version = get_hatch_version()
        #print_debug(f"hatch version   = {hatch_version}")

        published = read_published_version()
        print_debug(f"published       = {published}")

        # Only run git bump-version if git tag == last published
        if git_tag and published and git_tag == published:
            print("[BumpVersionBuildHook] Version already published → bumping version…")
            self._run_git_bump_version()
            # update metadata._version with hatch version reading git tag
            hatch_version = get_hatch_version()
            self.metadata._version = hatch_version
        else:
            print("[BumpVersionBuildHook] No version bump needed.")


    def _run_git_bump_version(self):
        """Tries to run git bump-version."""
        try:
            subprocess.run(
                ["git", "bump-version", "-Y"],
                check=True,
            )
            print_debug("git bump-version executed successfully.")
        except subprocess.CalledProcessError as e:
            # do not raise as the bump-version script has echo'ed the error message already
            print("--- Error: stopped build process ---")
            exit(1)
