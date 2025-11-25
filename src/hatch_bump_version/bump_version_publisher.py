from hatch.publish.index import IndexPublisher
from .utils import read_published_version, write_published_version, get_git_tag, get_hatch_version


class BumpVersionPublisher(IndexPublisher):
    PLUGIN_NAME = "bump_version" # use in [tool.hatch.publish.bump_version]

    def publish(self, artifacts, options):
        # Determine what we are publishing
        git_tag = get_git_tag()
        hatch_version = get_hatch_version()
        published = read_published_version()
        print(f"[BumpVersionPublisher] git tag         = {git_tag}")
        print(f"[BumpVersionPublisher] hatch version   = {hatch_version}")
        print(f"[BumpVersionPublisher] published       = {published}")

        if git_tag:
            print(f"[BumpVersionPublisher] Writing published version: {git_tag} and {hatch_version}")
            write_published_version(git_tag)

        # Continue with standard index publishing
        print("We have disabled index publisher at the moment.")
        #return super().publish(artifacts, options)
