import subprocess
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from .utils import get_git_tag, get_hatch_version, read_published_version


class BumpVersionBuildHook(BuildHookInterface):
    PLUGIN_NAME = "bump_version" # use in [tool.hatch.build.hooks.bump_version]

    def initialize(self, version, build_data):
        """Compares build and published versions and bumps version if needed."""

        git_tag = get_git_tag()
        hatch_version = get_hatch_version()
        published = read_published_version()

        show_versions = False
        if show_versions:
            print(f"[BumpVersionBuildHook] git tag         = {git_tag}")
            print(f"[BumpVersionBuildHook] hatch version   = {hatch_version}")
            print(f"[BumpVersionBuildHook] published       = {published}")

        # Only run git bump-version if git tag == last published
        if git_tag and published and git_tag == published:
            print("[BumpVersionBuildHook] Version already published → bumping version…")
            self._run_git_bump_version()
        else:
            print("[BumpVersionBuildHook] No version bump needed.")


    def _run_git_bump_version(self):
        """Tries to run git bump-version."""
        try:
            subprocess.run(
                ["git", "bump-version", "-Y"],
                check=True,
            )
            print("[BumpVersionBuildHook] git bump-version executed successfully.")
        except subprocess.CalledProcessError as e:
            # do not raise as the bump-version script has echo'ed the error message already
            print("--- Error: stopped build process ---")
            exit(1)
