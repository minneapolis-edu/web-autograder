from git import Repo, GitCommandError
import os

# token = os.environ['GITHUB_AUTOGRADER_ACCESS_TOKEN']

def clone_or_pull_latest(repo_url, target_dir, repo_dir):

    """ Clone the given repo to location target_dir/repo_dir.
    If the dir already exists, attempt to git pull to get latest code.
    Error if directory already exists and it's remote origin is not the same URL as repo_url
    Error if repo not found. """

    repo_target_dir = os.path.join(target_dir, repo_dir)

    try:
        repo = Repo.clone_from(repo_url, os.path.join(target_dir, repo_dir))
    except GitCommandError as e:
        if 'remote: Repository not found.' in e.stderr:
            # The URL isn't a repo
            return f'The URL {repo_url} was not found or not a git repository.'

        elif 'already exists and is not an empty directory' in e.stderr:
            # repo already exists. Is it the one we wanted to download? If so, pull latest
            # print('something already exists at location', target_dir, repo_dir)
            repo = Repo(repo_target_dir)

            try:
                origin = repo.remote('origin')
            except ValueError:
                return f'There is no origin remote for the contents of {repo_target_dir} to pull. Is this directory a git repository?'
                # this directory has something in it, but it's not a git repo

            if origin.url == repo_url:
                # this is the repo and it's already downloaded. Pull any changes
                origin.pull()

            else:
                #this is another repo
                return f'This directory {repo_target_dir} was cloned from a different repo URL from {repo_url}.'
        else:
            # Some other error
            return f'error cloning {repo_url} into {repo_target_dir} because {e.stderr}'


if __name__ == '__main__':
    ex_repo_url = 'https://github.com/minneapolis-edu/temp'
    ex_dir = '/Users/admin/TEMP/repos/'
    err = clone_or_pull_latest(ex_repo_url, ex_dir, 'tempsdfsdf')
    print('is there an error?', err)
